"""Draw the concept visuals used on the C1123 slides and in the Learner Guide.

Most visuals are drawn from the labs' own synthetic captures through TShark,
so every ladder diagram, timing and chart matches what learners will see in
the labs. A few concept diagrams (encapsulation, filter pipeline, DHCP DORA, NAT,
capture placement) are drawn schematically.

Output: courseware/assets/visuals/*.png   (house palette, 16:9-friendly)
"""
from pathlib import Path
import shutil, subprocess
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "courseware/assets/visuals"
LAB = ROOT / "labs/lab-17-compare-encrypted-and-decrypted-views/data"
PCAP, TLS, KEYS = LAB / "branch-office.pcap", LAB / "tls-session.pcap", LAB / "lab-tls.keys"
TSHARK = shutil.which("tshark") or "/Applications/Wireshark.app/Contents/MacOS/tshark"

BLUE, TEAL, VIOLET, AMBER, RED, INK, GREY, LIGHT, LINE = (
    "#1F6FEB", "#10B981", "#7C3AED", "#F59E0B", "#DC2626", "#161B26", "#5B6372", "#F5F8FC", "#E2E8F0")
plt.rcParams.update({"font.family": "Arial", "font.size": 13, "axes.edgecolor": LINE,
                     "axes.labelcolor": INK, "xtick.color": GREY, "ytick.color": GREY})


def ts(pcap, display_filter, fields, extra=()):
    cmd = [TSHARK, "-n", "-r", str(pcap), "-Y", display_filter, "-T", "fields", "-E", "separator=/t"]
    for f in fields:
        cmd += ["-e", f]
    cmd += list(extra)
    out = subprocess.run(cmd, capture_output=True, text=True, check=True).stdout
    return [line.split("\t") for line in out.splitlines() if line.strip()]


def save(fig, name):
    OUT.mkdir(parents=True, exist_ok=True)
    fig.savefig(OUT / name, dpi=160, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print("Saved", name)


# ------------------------------------------------------------------ ladder diagrams
def ladder(name, hosts, msgs, title_note="", notes=(), height=None):
    """hosts: [(ip, label)] left→right. msgs: [(time, src, dst, text, colour)].
    notes: [(t0, t1, text, colour)] — braces on the right showing a measured interval."""
    n = len(msgs)
    h = height or max(4.2, 0.62 * n + 1.6)
    fig, ax = plt.subplots(figsize=(12, h))
    xs = {ip: i * (10.0 / max(1, len(hosts) - 1)) for i, (ip, _) in enumerate(hosts)}
    y0, step = 0.0, 1.0
    for ip, label in hosts:
        x = xs[ip]
        ax.add_patch(FancyBboxPatch((x - 1.45, -1.25), 2.9, 0.8, boxstyle="round,pad=0.02",
                                    fc=LIGHT, ec=BLUE, lw=1.5))
        ax.text(x, -0.85, label, ha="center", va="center", fontsize=12.5, color=INK, weight="bold")
        ax.plot([x, x], [-0.45, n * step + 0.2], color=LINE, lw=2, zorder=0)
    ys = []
    for i, (t, src, dst, text, col) in enumerate(msgs):
        y = y0 + (i + 0.6) * step
        ys.append(y)
        ax.annotate("", xy=(xs[dst], y + 0.25), xytext=(xs[src], y),
                    arrowprops=dict(arrowstyle="-|>", color=col, lw=2.2, mutation_scale=16))
        mid = (xs[src] + xs[dst]) / 2
        ax.text(mid, y + 0.02, text, ha="center", va="bottom", fontsize=11.5, color=INK,
                bbox=dict(fc="white", ec="none", pad=1.2))
        ax.text(-1.6, y + 0.12, f"{t:.3f} s", ha="right", va="center", fontsize=10.5, color=GREY, family="Menlo")
    right = max(xs.values())
    for i0, i1, text, col in notes:
        ya, yb = ys[i0], ys[i1] + 0.25
        ax.plot([right + 0.55] * 2, [ya, yb], color=col, lw=3)
        ax.text(right + 0.75, (ya + yb) / 2, text, va="center", fontsize=11.5, color=col, weight="bold")
    ax.set_xlim(-2.9, right + 4.4)
    ax.set_ylim(n * step + 0.6, -1.5)
    ax.axis("off")
    if title_note:
        ax.text(-2.9, n * step + 0.55, title_note, fontsize=10, color=GREY, va="top")
    save(fig, name)


def short(info, limit=46):
    info = " ".join(info.replace("Standard query response", "response").replace("Standard query", "query").split())
    return info if len(info) <= limit else info[:limit - 1] + "…"


def frames(filter_, pcap=PCAP, extra=()):
    rows = ts(pcap, filter_, ["frame.number", "frame.time_relative", "ip.src", "arp.src.proto_ipv4",
                              "ip.dst", "arp.dst.proto_ipv4", "_ws.col.info"], extra)
    out = []
    for r in rows:
        src = (r[2] or r[3]).split(",")[0]     # outer header first (ICMP errors quote an inner IP header)
        dst = (r[4] or r[5]).split(",")[0]
        out.append((int(r[0]), float(r[1]), src, dst, r[6]))
    return out


C, S, R = "192.0.2.10", "192.0.2.20", "192.0.2.53"
SRC = "Synthetic lab capture branch-office.pcap · times are frame.time_relative"


def build_ladders():
    # ARP + DNS
    fr = frames("arp || dns")
    msgs = []
    for n, t, s, d, info in fr:
        if "Who has" in info: msgs.append((t, C, S, "ARP: Who has 192.0.2.20? (broadcast)", AMBER))
        elif "is at" in info: msgs.append((t, S, C, "ARP reply: 192.0.2.20 is at 02:00:…:20", AMBER))
        else:
            col = RED if "No such name" in info else (VIOLET if "slow" in info and "response" in info else BLUE)
            msgs.append((t, s, d, short(info), col))
    ladder("ladder-arp-dns.png", [(C, "Client 192.0.2.10"), (S, "Server 192.0.2.20"), (R, "Resolver 192.0.2.53")],
           msgs, SRC, notes=[(6, 7, "0.800 s\nslow answer", VIOLET), (4, 5, "NXDOMAIN", RED)])
    # TCP + HTTP stream 0
    fr = frames("tcp.stream == 0")
    msgs = [(t, s, d, short(info.replace("51001 → 80 ", "").replace("80 → 51001 ", "")), TEAL if "HTTP" in info or "GET" in info else BLUE)
            for n, t, s, d, info in fr]
    ladder("ladder-tcp-http.png", [(C, "Client :51001"), (S, "Server :80")], msgs, SRC,
           notes=[(0, 1, "SYN→SYN/ACK\n30 ms", BLUE), (0, 2, "iRTT 40 ms", TEAL), (3, 5, "server\n50 ms", VIOLET)])
    # Slow stream 1
    fr = frames("tcp.stream == 1")
    msgs = [(t, s, d, short(info.replace("51002 → 80 ", "").replace("80 → 51002 ", "")),
             VIOLET if "200 OK" in info else BLUE) for n, t, s, d, info in fr]
    ladder("ladder-slow.png", [(C, "Client :51002"), (S, "Server :80")], msgs, SRC,
           notes=[(0, 1, "path\n30 ms", BLUE), (4, 5, "server think\n750 ms", VIOLET)])
    # Stream 3: 500, retransmission, zero window
    fr = frames("tcp.stream == 3")
    def col(info):
        return RED if ("Retransmission" in info or "ZeroWindow" in info) else (AMBER if "500" in info else BLUE)
    msgs = [(t, s, d, short(info.replace("51004 → 80 ", "").replace("80 → 51004 ", "").replace("[PSH, ACK] ", ""), 50), col(info))
            for n, t, s, d, info in fr]
    ladder("ladder-retrans.png", [(C, "Client :51004"), (S, "Server :80")], msgs, SRC,
           notes=[(5, 6, "repeat after\n1.000 s", RED)])
    # ICMP + UDP refusal + TCP RST
    fr = frames("icmp || udp.dstport == 9999 || tcp.stream == 4")
    msgs = []
    for n, t, s, d, info in fr:
        if "Echo (ping) reply" in info: msgs.append((t, s, d, "ICMP Echo reply seq=" + info.split("seq=")[1].split("/")[0], TEAL))
        elif "Echo (ping) request" in info: msgs.append((t, s, d, "ICMP Echo request seq=" + info.split("seq=")[1].split("/")[0], BLUE))
        elif "9999" in info: msgs.append((t, s, d, "UDP 55000 → 9999 (LAB-UDP)", VIOLET))
        elif "unreachable" in info: msgs.append((t, s, d, "ICMP Type 3 Code 3: port unreachable", RED))
        elif "RST" in info: msgs.append((t, s, d, "TCP RST, ACK — port 81 refused", RED))
        else: msgs.append((t, s, d, "TCP SYN → port 81", BLUE))
    ladder("ladder-icmp-udp.png", [(C, "Client 192.0.2.10"), (S, "Server 192.0.2.20")], msgs, SRC,
           notes=[(0, 1, "30 ms", TEAL), (6, 7, "service\nrefused", RED)])
    # SIP + RTP
    rows = ts(PCAP, "sip || udp.port == 4002", ["frame.time_relative", "ip.src", "ip.dst", "_ws.col.info", "rtp.seq"],
              ["-d", "udp.port==4002,rtp"])
    msgs = []
    for t, s, d, info, seq in rows:
        s, d = s.split(",")[0], d.split(",")[0]
        if "INVITE" in info and "Request" in info: msgs.append((float(t), s, d, "SIP INVITE sip:desk@192.0.2.20", BLUE))
        elif "200 OK" in info: msgs.append((float(t), s, d, "SIP 200 OK (INVITE)", TEAL))
        else: msgs.append((float(t), s, d, f"RTP seq {seq}", VIOLET))
    msgs.insert(4, (msgs[3][0] + 0.010, C, S, "RTP seq 102 — not in capture", RED))
    ladder("ladder-sip-rtp.png", [(C, "Phone A 192.0.2.10"), (S, "Desk 192.0.2.20")], msgs,
           SRC + " · RTP decoded with Decode As", notes=[(4, 4, "gap in\nsequence", RED)])
    # TLS 1.2 handshake (decrypted view)
    fr = frames("tcp || tls || http", TLS, ["-o", f"tls.keylog_file:{KEYS}"])
    msgs = []
    for n, t, s, d, info in fr:
        if "[ACK]" in info and "SYN" not in info and len(msgs) > 2:
            continue                                   # hide bare ACKs after the handshake
        colr = VIOLET if ("Hello" in info or "Key Exchange" in info or "Finished" in info) else (TEAL if "HTTP" in info or "GET" in info else BLUE)
        text = info.replace("56000 → 443 ", "").replace("443 → 56000 ", "")
        text = text.replace("Server Hello, Certificate, Server Key Exchange, Server Hello Done", "Server Hello, Certificate, Key Exch., Done")
        text = text.replace("Client Key Exchange, Change Cipher Spec, Finished", "Client Key Exch., Change Cipher Spec, Finished")
        text = text.replace("New Session Ticket, Change Cipher Spec, Finished", "Session Ticket, Change Cipher Spec, Finished")
        msgs.append((t, s, d, short(text, 52), colr))
    ladder("ladder-tls.png", [(C, "Client :56000"), (S, "Server :443")], msgs,
           "Synthetic lab capture tls-session.pcap with lab-tls.keys loaded — HTTP is visible only with the key log",
           notes=[(3, 6, "TLS 1.2\nhandshake", VIOLET), (7, 8, "decrypted\nHTTP", TEAL)])


# ------------------------------------------------------------------ charts from the capture
def build_charts():
    rows = ts(PCAP, "frame", ["frame.time_relative", "_ws.col.protocol", "frame.len", "tcp.analysis.retransmission",
                              "tcp.analysis.zero_window"])
    # I/O graph
    fig, ax = plt.subplots(figsize=(12, 4.6))
    bins = [i * 0.1 for i in range(36)]
    import collections
    cnt, by = collections.Counter(), collections.defaultdict(collections.Counter)
    for t, proto, ln, rt, zw in rows:
        b = int(float(t) / 0.1); cnt[b] += 1
        by[b]["Bad TCP"] += bool(rt or zw)
    xs = [i * 0.1 for i in range(36)]
    ax.bar(xs, [cnt[i] for i in range(36)], width=0.09, align="edge", color=BLUE, label="All packets")
    ax.bar(xs, [by[i]["Bad TCP"] for i in range(36)], width=0.09, align="edge", color=RED, label="tcp.analysis.retransmission || zero_window")
    ax.annotate("DNS 0.8 s gap", xy=(0.45, 0.4), xytext=(0.35, 6.2), color=VIOLET, fontsize=12, arrowprops=dict(arrowstyle="->", color=VIOLET))
    ax.annotate("/slow: 0.75 s idle", xy=(1.6, 0.3), xytext=(1.35, 7.2), color=VIOLET, fontsize=12, arrowprops=dict(arrowstyle="->", color=VIOLET))
    ax.annotate("1 s stall → retransmission", xy=(3.25, 1.2), xytext=(2.35, 8.2), color=RED, fontsize=12, arrowprops=dict(arrowstyle="->", color=RED))
    ax.set_xlabel("Seconds since start of capture (100 ms intervals)"); ax.set_ylabel("Packets per interval")
    ax.spines[["top", "right"]].set_visible(False)
    ax.legend(frameon=False, loc="upper center", bbox_to_anchor=(0.5, -0.18), ncol=2)
    save(fig, "chart-io-graph.png")
    # Protocol mix (packets vs bytes)
    pk, by_ = collections.Counter(), collections.Counter()
    for t, proto, ln, rt, zw in rows:
        p = "TLS" if proto.startswith("TLS") else proto
        pk[p] += 1; by_[p] += int(ln)
    order = sorted(pk, key=lambda p: -pk[p])
    fig, ax = plt.subplots(figsize=(12, 4.6))
    import numpy as np
    x = np.arange(len(order))
    ax.bar(x - 0.2, [100 * pk[p] / sum(pk.values()) for p in order], 0.4, color=BLUE, label="% of packets")
    ax.bar(x + 0.2, [100 * by_[p] / sum(by_.values()) for p in order], 0.4, color=TEAL, label="% of bytes")
    ax.set_xticks(x, order); ax.set_ylabel("Share of capture (%)")
    ax.spines[["top", "right"]].set_visible(False); ax.legend(frameon=False)
    save(fig, "chart-protocol-mix.png")
    # Stevens graph for stream 3
    st = ts(PCAP, "tcp.stream == 3 && ip.src == 192.0.2.20 && tcp.len > 0", ["frame.time_relative", "tcp.seq", "tcp.len", "tcp.analysis.retransmission"])
    zw = ts(PCAP, "tcp.analysis.zero_window", ["frame.time_relative"])
    fig, ax = plt.subplots(figsize=(12, 4.6))
    for t, seq, ln, rt in st:
        t, seq, ln = float(t), int(seq), int(ln)
        ax.plot([t, t], [seq, seq + ln], color=RED if rt else BLUE, lw=5, solid_capstyle="butt")
        ax.text(t + 0.03, seq + ln / 2, ("Retransmission (same bytes 1–92)" if rt else "Original segment: HTTP 500, bytes 1–92"),
                color=RED if rt else BLUE, va="center", fontsize=12)
    for (t,) in zw:
        ax.axvline(float(t), color=AMBER, ls="--"); ax.text(float(t) + 0.02, 15, "Zero Window\nadvertised", color=AMBER, fontsize=11.5)
    ax.set_xlim(2.1, 3.9); ax.set_ylim(-5, 110)
    ax.set_xlabel("Seconds since start of capture"); ax.set_ylabel("Server sequence number (relative)")
    ax.spines[["top", "right"]].set_visible(False)
    save(fig, "chart-stevens.png")
    # DNS response times
    dn = ts(PCAP, "dns.flags.response == 1", ["dns.qry.name", "dns.time", "dns.flags.rcode"])
    fig, ax = plt.subplots(figsize=(12, 3.8))
    names = [n for n, _, _ in dn]; vals = [float(v) * 1000 for _, v, _ in dn]
    cols = [RED if rc == "3" else (VIOLET if v > 500 else TEAL) for (_, _, rc), v in zip(dn, vals)]
    ax.barh(names, vals, color=cols)
    for i, ((_, _, rc), v) in enumerate(zip(dn, vals)):
        ax.text(v + 10, i, f"{v:.0f} ms" + ("  · NXDOMAIN (rcode 3)" if rc == "3" else ""), va="center", fontsize=12)
    ax.invert_yaxis(); ax.set_xlabel("dns.time (ms)"); ax.set_xlim(0, 1050)
    ax.spines[["top", "right"]].set_visible(False)
    save(fig, "chart-dns-time.png")
    # Delay breakdown for /slow
    fig, ax = plt.subplots(figsize=(12, 3.6))
    parts = [("SYN→SYN/ACK (path)", 30, BLUE), ("ACK (handshake done)", 10, TEAL), ("Request → server ACK", 10, AMBER), ("Server processing", 750, VIOLET)]
    left, k = 0, 0
    for label, w, c in parts:
        ax.barh([0], [w], left=left, color=c, edgecolor="white", height=0.5)
        if w > 60:
            ax.text(left + w / 2, 0, f"{label}: {w} ms", ha="center", va="center", fontsize=12.5, color="white", weight="bold")
        else:
            ty = 1.59 - 0.42 * k; k += 1          # first (leftmost) segment gets the highest label: leaders never cross
            ax.annotate(f"{label}: {w} ms", xy=(left + w / 2, 0.25), xytext=(110, ty), color=c, fontsize=12, weight="bold",
                        va="center", ha="left", arrowprops=dict(arrowstyle="-", color=c, relpos=(0, 0.5)))
        left += w
    ax.set_ylim(-0.4, 2.0)
    ax.set_xlim(0, 820); ax.set_yticks([]); ax.set_xlabel("Milliseconds within TCP stream 1 (GET /slow)")
    ax.spines[["top", "right", "left"]].set_visible(False)
    save(fig, "chart-delay-breakdown.png")


# ------------------------------------------------------------------ schematic diagrams
def box(ax, x, y, w, h, text, fc, tc="white", fs=12.5, bold=True):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.02", fc=fc, ec="white", lw=2))
    ax.text(x + w / 2, y + h / 2, text, ha="center", va="center", color=tc, fontsize=fs, weight="bold" if bold else "normal")


def arrow(ax, x0, y0, x1, y1, col=GREY):
    ax.annotate("", xy=(x1, y1), xytext=(x0, y0), arrowprops=dict(arrowstyle="-|>", color=col, lw=2, mutation_scale=16))


def build_diagrams():
    # Encapsulation — real byte counts from frame 21 (GET /health, 124 bytes)
    fig, ax = plt.subplots(figsize=(12, 4.2)); ax.axis("off"); ax.set_xlim(0, 12); ax.set_ylim(0, 5)
    segs = [("Ethernet II\n14 B", 1.6, AMBER), ("IPv4\n20 B", 1.6, BLUE), ("TCP\n20 B", 1.6, TEAL), ("HTTP: GET /health …\n70 B payload", 6.0, VIOLET)]
    x = 0.4
    for t, w, c in segs:
        box(ax, x, 2.4, w, 1.2, t, c); x += w
    ax.text(0.4, 4.15, "Frame 21 in branch-office.pcap — 124 bytes on the wire", fontsize=13, color=INK, weight="bold")
    for i, (lbl, c) in enumerate([("Layer 2 · MAC addresses change per hop", AMBER), ("Layer 3 · IP addresses end-to-end", BLUE),
                                  ("Layer 4 · ports identify the conversation", TEAL), ("Layer 7 · the application message", VIOLET)]):
        lx, ly = 0.4 + (i % 2) * 5.8, 1.6 - (i // 2) * 0.55
        ax.add_patch(plt.Rectangle((lx, ly), 0.3, 0.3, color=c)); ax.text(lx + 0.45, ly + 0.15, lbl, va="center", fontsize=12, color=INK)
    ax.text(0.4, 0.15, "Packet Details shows the same order top-to-bottom: Frame › Ethernet II › Internet Protocol › TCP › HTTP", fontsize=11.5, color=GREY)
    save(fig, "diagram-encapsulation.png")
    # Capture → display filter pipeline
    fig, ax = plt.subplots(figsize=(12, 3.6)); ax.axis("off"); ax.set_xlim(0, 12.4); ax.set_ylim(0, 3.6)
    stages = [("Network\ninterface", GREY), ("Capture filter\nBPF syntax", AMBER), ("Saved file\npcapng", BLUE),
              ("Dissectors\ndecode fields", VIOLET), ("Display filter\nfield syntax", TEAL), ("Packet list\nyou see", INK)]
    for i, (t, c) in enumerate(stages):
        box(ax, 0.2 + i * 2.05, 1.5, 1.75, 1.3, t, c, fs=11.5)
        if i: arrow(ax, 0.2 + i * 2.05 - 0.3, 2.15, 0.2 + i * 2.05 - 0.02, 2.15)
    ax.text(2.25, 3.2, "tcp port 80", ha="center", color=AMBER, fontsize=12, family="Menlo")
    ax.text(10.45, 3.2, "tcp.port == 80", ha="center", color=TEAL, fontsize=12, family="Menlo")
    ax.text(2.6, 0.9, "Discarded packets are gone for good", ha="center", color=AMBER, fontsize=11.5, weight="bold")
    ax.text(8.75, 0.9, "Hidden packets return when you clear the filter", ha="center", color=TEAL, fontsize=11.5, weight="bold")
    save(fig, "diagram-filter-pipeline.png")
    # Capture placement
    fig, ax = plt.subplots(figsize=(12, 4.4)); ax.axis("off"); ax.set_xlim(0, 12); ax.set_ylim(0, 4.6)
    box(ax, 0.3, 2.6, 2.0, 1.0, "Client\n192.0.2.10", BLUE); box(ax, 4.0, 2.6, 2.0, 1.0, "Access\nswitch", GREY)
    box(ax, 7.6, 2.6, 1.8, 1.0, "Uplink /\nrouter", GREY); box(ax, 10.0, 2.6, 1.8, 1.0, "Server\n192.0.2.20", TEAL)
    for x0, x1 in [(2.3, 4.0), (6.0, 7.6), (9.4, 10.0)]:
        ax.plot([x0, x1], [3.1, 3.1], color=INK, lw=2)
    for x, lbl, c, sees in [(1.3, "A", BLUE, "Sensor on client:\nall of its own traffic"),
                            (5.0, "B", AMBER, "SPAN on switch:\ncopied frames; may drop under load"),
                            (8.5, "C", VIOLET, "TAP on uplink:\nboth directions incl. errors"),
                            (10.9, "D", TEAL, "Sensor at server:\nserver-side timing")]:
        ax.add_patch(plt.Circle((x, 1.75), 0.32, color=c)); ax.text(x, 1.75, lbl, ha="center", va="center", color="white", weight="bold")
        ax.text(x, 0.95, sees, ha="center", va="top", fontsize=10.5, color=INK)
        ax.plot([x, x], [2.07, 2.6], color=c, ls="--")
    save(fig, "diagram-capture-points.png")
    # DHCP DORA
    ladder_static("diagram-dhcp-dora.png", ["Client (0.0.0.0)", "DHCP server"],
                  [(0, 1, "DHCP Discover — broadcast, UDP 68 → 67", BLUE), (1, 0, "DHCP Offer — proposed IP, lease, gateway, DNS", TEAL),
                   (0, 1, "DHCP Request — broadcast: accepts the offer", BLUE), (1, 0, "DHCP ACK — lease confirmed", TEAL)],
                  "Filter: dhcp  (bootp in Wireshark versions before 3.0)")
    # NAT
    fig, ax = plt.subplots(figsize=(12, 3.8)); ax.axis("off"); ax.set_xlim(0, 12); ax.set_ylim(0, 4)
    box(ax, 0.3, 2.2, 2.4, 1.1, "Inside host\n10.0.0.5:51001", BLUE); box(ax, 4.8, 2.2, 2.4, 1.1, "NAT router", GREY)
    box(ax, 9.3, 2.2, 2.4, 1.1, "Web server\n198.51.100.7:443", TEAL)
    arrow(ax, 2.7, 2.75, 4.8, 2.75, BLUE); arrow(ax, 7.2, 2.75, 9.3, 2.75, BLUE)
    ax.text(3.75, 3.0, "src 10.0.0.5:51001", ha="center", fontsize=11); ax.text(8.25, 3.0, "src 203.0.113.9:62001", ha="center", fontsize=11)
    ax.text(6.0, 1.4, "Translation table: 10.0.0.5:51001 ↔ 203.0.113.9:62001", ha="center", fontsize=12, color=VIOLET, weight="bold")
    ax.text(6.0, 0.6, "Capture on BOTH sides and match on timing, sequence numbers or payload to correlate the flows", ha="center", fontsize=11, color=GREY)
    save(fig, "diagram-nat.png")


def ladder_static(name, hosts, msgs, note):
    fig, ax = plt.subplots(figsize=(12, 0.62 * len(msgs) + 1.9)); ax.axis("off")
    xs = [i * 10.0 / (len(hosts) - 1) for i in range(len(hosts))]
    n = len(msgs)
    for x, h in zip(xs, hosts):
        ax.add_patch(FancyBboxPatch((x - 1.3, -1.25), 2.6, 0.8, boxstyle="round,pad=0.02", fc=LIGHT, ec=BLUE, lw=1.5))
        ax.text(x, -0.85, h, ha="center", va="center", weight="bold", fontsize=12.5)
        ax.plot([x, x], [-0.45, n + 0.2], color=LINE, lw=2, zorder=0)
    for i, (s, d, t, c) in enumerate(msgs):
        y = i + 0.6
        ax.annotate("", xy=(xs[d], y + 0.25), xytext=(xs[s], y), arrowprops=dict(arrowstyle="-|>", color=c, lw=2.2, mutation_scale=16))
        ax.text(5, y + 0.02, t, ha="center", va="bottom", fontsize=11.5, bbox=dict(fc="white", ec="none", pad=1.2))
    ax.text(-1.3, n + 0.55, note, fontsize=10.5, color=GREY, va="top")
    ax.set_xlim(-1.6, 11.6); ax.set_ylim(n + 0.7, -1.5)
    save(fig, name)


if __name__ == "__main__":
    build_ladders()
    build_charts()
    build_diagrams()
