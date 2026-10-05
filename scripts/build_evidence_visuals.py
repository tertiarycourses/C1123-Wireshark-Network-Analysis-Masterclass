"""Render a Wireshark-style 'expected evidence' packet list for every lab.

Runs TShark against each lab's own synthetic capture with the filters in its
assets/checks.json, and draws the result as a filter bar + coloured packet list
(Wireshark default colouring rules, simplified). Output:
courseware/assets/screenshots/lab-NN-evidence.png  (used by course_data.LAB_SHOTS
and the Learner Guide).
"""
from pathlib import Path
import json, shutil, subprocess
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT/'courseware/assets/screenshots'
TSHARK = shutil.which('tshark') or '/Applications/Wireshark.app/Contents/MacOS/tshark'
MONO = ImageFont.truetype('/System/Library/Fonts/Menlo.ttc', 20)
MONO_B = ImageFont.truetype('/System/Library/Fonts/Menlo.ttc', 20, index=1)
SANS = ImageFont.truetype('/System/Library/Fonts/Supplemental/Arial Bold.ttf', 19)
COLS = [('No.', 60), ('Time', 130), ('Source', 215), ('Destination', 215), ('Protocol', 110), ('Info', 610)]
WIDTH = sum(w for _, w in COLS) + 20
ROW_H, MAX_ROWS = 32, 10
FIELDS = ['frame.number', 'frame.time_relative', '_ws.col.def_src', '_ws.col.def_dst', '_ws.col.protocol',
          'frame.len', '_ws.col.info', 'tcp.analysis.flags', 'tcp.flags.reset', 'tcp.flags.syn', 'tcp.flags.fin', 'icmp.type']

def colour(row):
    proto, flags, rst, syn, fin, icmp = row[4], row[7], row[8], row[9], row[10], row[11]
    if flags or rst in ('1', 'True'):       return ('#000000', '#ff5f5f')   # Bad TCP
    if icmp and icmp.split(',')[0] in ('3', '11'): return ('#000000', '#b7f774')  # ICMP errors
    if syn in ('1', 'True') or fin in ('1', 'True'): return ('#a0a0a0', '#12272e')  # TCP SYN/FIN
    p = proto.upper()
    if p.startswith('HTTP'):  return ('#e4ffc7', '#12272e')
    if p in ('ARP',):         return ('#faf0d7', '#12272e')
    if p.startswith('ICMP'):  return ('#fce0ff', '#12272e')
    if p.startswith('TLS'): return ('#e7e6ff', '#12272e')
    if p in ('TCP',):         return ('#e7e6ff', '#12272e')
    if p in ('SIP', 'RTP', 'DNS', 'UDP', 'IGMPV2', 'IGMP') : return ('#daeeff', '#12272e')
    return ('#ffffff', '#12272e')

def run(lab, check, capture):
    cmd = [TSHARK, '-n', '-r', str(lab/'data'/capture), '-Y', check['filter'], '-T', 'fields', '-E', 'separator=/t']
    for f in FIELDS: cmd += ['-e', f]
    cmd += check.get('decode') or []
    cmd += ['-o', 'tls.keylog_file:' + (str(lab/'data/lab-tls.keys') if check.get('keylog') else '')]
    out = subprocess.run(cmd, capture_output=True, text=True, check=True).stdout
    return [l.split('\t') + [''] * (len(FIELDS) - len(l.split('\t'))) for l in out.splitlines() if l.strip()]

def fit(d, text, font, w):
    if d.textlength(text, font=font) <= w: return text
    while text and d.textlength(text + '…', font=font) > w: text = text[:-1]
    return text + '…'

def panel(check, rows, capture):
    n = min(len(rows), MAX_ROWS); extra = len(rows) - n
    h = 50 + 36 + ROW_H * max(n, 1) + (ROW_H if extra else 0) + 34
    im = Image.new('RGB', (WIDTH, h), 'white'); d = ImageDraw.Draw(im)
    # display-filter bar (green = valid expression)
    d.rectangle([10, 8, WIDTH - 10, 44], fill='#afffaf', outline='#7a9a7a')
    label = check['filter'] + ('    [TLS key log loaded]' if check.get('keylog') else '') + ('    [Decode As: ' + check['decode'][1] + ']' if check.get('decode') else '')
    d.text((18, 14), fit(d, label, MONO_B, WIDTH - 40), font=MONO_B, fill='#12272e')
    y = 50; x = 10
    d.rectangle([10, y, WIDTH - 10, y + 34], fill='#eceff1', outline='#c4ccd0')
    for name, w in COLS:
        d.text((x + 6, y + 6), name, font=SANS, fill='#263238'); x += w
    y += 36
    if not rows:
        d.text((16, y + 5), '(no packets match — expected for this view)', font=MONO, fill='#6b7780'); y += ROW_H
    for r in rows[:n]:
        bg, fg = colour(r); d.rectangle([10, y, WIDTH - 10, y + ROW_H - 1], fill=bg)
        vals = [r[0], f"{float(r[1]):.6f}", r[2], r[3], r[4], r[6]]
        x = 10
        for (name, w), v in zip(COLS, vals):
            d.text((x + 6, y + 6), fit(d, v, MONO, w - 10), font=MONO, fill=fg); x += w
        y += ROW_H
    if extra:
        d.text((16, y + 5), f'… {extra} more matching packets', font=MONO, fill='#6b7780'); y += ROW_H
    d.rectangle([10, y + 4, WIDTH - 10, y + 36], fill='#f5f7f8', outline='#d5dbde')
    d.text((16, y + 9), f'{capture}    Displayed: {len(rows)}', font=MONO, fill='#455a64')
    return im

def main():
    OUT.mkdir(parents=True, exist_ok=True)
    for lab in sorted((ROOT/'labs').glob('lab-[0-9][0-9]-*')):
        cfg = json.loads((lab/'assets/checks.json').read_text())
        panels = [panel(c, run(lab, c, cfg['capture']), cfg['capture']) for c in cfg['checks']]
        H = sum(p.height for p in panels) + 12 * (len(panels) - 1)
        im = Image.new('RGB', (WIDTH, H), 'white'); y = 0
        for p in panels: im.paste(p, (0, y)); y += p.height + 12
        num = int(lab.name[4:6]); im.save(OUT/f'lab-{num:02d}-evidence.png'); print(lab.name, im.size)

if __name__ == '__main__':
    main()
