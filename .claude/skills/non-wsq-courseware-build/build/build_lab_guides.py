#!/usr/bin/env python3
"""Generate the C1123 lab folders' instructions and mock data from the single source.

For every lab (course_data.LAB_BRIEFS + data_domainN.py) this writes, inside
labs/lab-NN-<slug>/:

  LAB-NN-Instructions.md      full step-by-step instructions (the PDF twin is
                              rendered by build_lab_pdfs.py from the same blocks)
  README.md                   short landing page pointing at the instructions
  assets/scenario.md          mock help-desk ticket that sets the lab scenario
  assets/expected-evidence.png the packet list the lab filter should produce
  assets/<lab templates>      lab-specific mock templates (filter matrix, HTTP summary, …)
  outputs/findings.md         pre-structured findings sheet the learner completes
  scripts/export_evidence.py  exports THIS lab's capture + filter to outputs/evidence.csv

and refreshes labs/README.md. The deck carries only each lab's scenario and a
four-task summary; the detailed steps live here and in the Learner Guide.
Nothing is deleted.
"""
import glob, importlib, os, re, shutil, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import course_data as C


def repo_root(start):
    d = start
    for _ in range(8):
        d = os.path.dirname(d)
        if os.path.isdir(os.path.join(d, "courseware")) and os.path.isdir(os.path.join(d, "labs")):
            return d
    raise RuntimeError("Course repository not found")


def load_activities():
    acts = []
    for path in sorted(glob.glob(os.path.join(HERE, "data_domain[0-9]*.py"))):
        name = os.path.basename(path)[:-3]
        if not re.fullmatch(r"data_domain\d+", name):
            continue
        n = re.search(r"\d+", name).group()
        acts.extend(getattr(importlib.import_module(name), f"DOMAIN{n}"))
    return sorted(acts, key=lambda a: a["num"])


REPO = repo_root(HERE)
LABS = os.path.join(REPO, "labs")
SHOTS = os.path.join(REPO, "courseware", "assets", "screenshots")
ACTS = load_activities()
TOPICS = {t["num"]: t for t in C.TOPICS}
LO = {lo.split(":", 1)[0]: lo.split(":", 1)[1].strip() for lo in C.LEARNING_OUTCOMES}


def folder_name(a):
    return f"lab-{a['num']:02d}-{C.LAB_SLUGS[a['num']]}"


def lab_minutes():
    """Hands-on minutes per lab, read from the Lesson Plan schedule so they agree."""
    mins = {}
    sched = C.SCHEDULE(lambda nums: " ".join(f"Lab {n}:" for n in nums))
    for _day, (_theme, rows) in sched.items():
        for row in rows:
            m = re.fullmatch(r"Hands-on: Lab (\d+):", row[4].strip())
            if m:
                mins[int(m.group(1))] = mins.get(int(m.group(1)), 0) + row[2]
    return mins


MINUTES = lab_minutes()

BASE_FILES = [
    ("data/branch-office.pcap", "Synthetic branch-office capture used by the lab"),
    ("assets/scenario.md", "The help-desk ticket that sets the scenario"),
    ("assets/checks.json", "Filters and frame counts the fixture must satisfy"),
    ("assets/expected-evidence.png", "The packet list your filter should produce"),
    ("scripts/verify.py", "Checks the capture facts with TShark"),
    ("scripts/export_evidence.py", "Exports this lab's evidence rows to outputs/evidence.csv"),
    ("outputs/findings.md", "Findings sheet you complete"),
]

TROUBLE_KEYS = ("TShark not found:", "A filter returns zero:", "TLS remains opaque:")


def troubleshooting(a):
    text = a.get("troubleshooting", "")
    parts = []
    for i, key in enumerate(TROUBLE_KEYS):
        start = text.find(key)
        if start < 0:
            continue
        ends = [text.find(k) for k in TROUBLE_KEYS[i + 1:] if text.find(k) > start]
        end = min(ends) if ends else len(text)
        parts.append((key.rstrip(":"), text[start + len(key):end].strip()))
    return parts or [("Problem", text)]


def lab_files(a):
    files = list(BASE_FILES)
    if a["num"] == 17:
        files[0] = ("data/tls-session.pcap", "Synthetic TLS capture used by the lab")
    files += C.LAB_BRIEFS[a["num"]]["files"]
    seen, out = set(), []
    for p, d in files:
        if p not in seen:
            seen.add(p); out.append((p, d))
    return out


def lab_blocks(a):
    """One ordered content stream per lab, rendered to Markdown here and to PDF
    by build_lab_pdfs.py. Block kinds: h1, meta, h2, p, bullets, numbered,
    steps, table, img, note."""
    b = C.LAB_BRIEFS[a["num"]]
    t = TOPICS[a["topic"]]
    lo = a["objective"]
    blocks = [
        ("h1", f"Lab {a['num']:02d} — {a['title']}"),
        ("meta", [("Course", f"{C.TITLE} ({C.COURSE_CODE})"), ("Topic", f"{t['code']} — {t['title']}"),
                  ("Learning outcome", f"{lo} — {LO.get(lo, '')}"),
                  ("Time", f"about {MINUTES.get(a['num'], a.get('duration', 45))} minutes"),
                  ("Version", f"{C.VERSION} · {C.VERSION_DATE}")]),
        ("h2", "Scenario"), ("p", b["scenario"]),
        ("h2", "Goal"), ("p", a["desc"]),
        ("h2", "What you will produce"), ("p", b["produce"] + "."),
        ("h2", "Before you start"),
        ("bullets", ["Wireshark 4.6 or later, with the TShark command-line tools on PATH.",
                     "Python 3 for the verification and export scripts (Windows: use py -3 in place of python3).",
                     "Open this lab folder in a terminal; every file the lab needs is inside it.",
                     "Use only the supplied synthetic captures — do not capture on a network you are not authorised to monitor."]),
        ("h2", "Files for this lab"),
        ("table", ["File", "What it is for"], lab_files(a)),
        ("h2", "Lab at a glance"), ("numbered", b["tasks"]),
        ("h2", "Step-by-step"), ("steps", a["steps"]),
        ("h2", "Expected evidence"),
        ("p", "With the lab filter applied, your packet list should match the frames below "
              "(produced by TShark from this lab's own capture)."),
        ("img", "assets/expected-evidence.png", f"Lab {a['num']:02d} expected evidence"),
        ("h2", "Test it"), ("p", a["test"]),
        ("h2", "Troubleshooting"), ("bullets", [f"{k}: {v}" for k, v in troubleshooting(a)]),
        ("h2", "Try it with TShark"),
        ("p", "The same evidence from the command line — run it from this lab folder:"),
        ("code", C.LAB_EXTENSIONS[a["num"]][0]),
        ("h2", "Challenge"), ("p", a.get("challenge", "")),
        ("h2", "Reflection"), ("p", a.get("reflection", "")),
        ("h2", "Extension (optional)"), ("p", C.LAB_EXTENSIONS[a["num"]][1]),
        ("h2", "Reset"),
        ("p", "Clear all display filters and return to the C1123-Analyst or Default profile. "
              "If you loaded a TLS key log, remove it from Preferences > Protocols > TLS. "
              "The supplied captures never need regenerating for the core lab."),
        ("note", "The same steps appear in the Learner Guide. The slides show only the scenario and a summary."),
    ]
    return blocks


def to_markdown(blocks):
    out = []
    for blk in blocks:
        k = blk[0]
        if k == "h1": out += [f"# {blk[1]}", ""]
        elif k == "meta": out += [" | ".join(f"**{a}:** {b}" for a, b in blk[1]), ""]
        elif k == "h2": out += [f"## {blk[1]}", ""]
        elif k == "p": out += [blk[1], ""]
        elif k == "bullets": out += [f"- {x}" for x in blk[1]] + [""]
        elif k == "numbered": out += [f"{i}. {x}" for i, x in enumerate(blk[1], 1)] + [""]
        elif k == "steps":
            for i, (text, cmd) in enumerate(blk[1], 1):
                out += [f"{i}. {text}", ""]
                if cmd:
                    out += ["   ```bash", f"   {cmd}", "   ```", ""]
        elif k == "table":
            out += ["| " + " | ".join(blk[1]) + " |", "|" + "---|" * len(blk[1])]
            out += [f"| `{p}` | {d} |" for p, d in blk[2]] + [""]
        elif k == "img": out += [f"![{blk[2]}]({blk[1]})", ""]
        elif k == "code": out += ["```bash", blk[1], "```", ""]
        elif k == "note": out += [f"> **Note:** {blk[1]}", ""]
    out += ["---", "", f"*{C.TITLE} · {C.COURSE_CODE} · Version {C.VERSION} · © 2026 Tertiary Infotech Academy Pte Ltd*", ""]
    return "\n".join(out)


# ------------------------------------------------------------------ mock data
EXPORT_SCRIPT = '''"""Export this lab's evidence rows to outputs/evidence.csv.

Uses the capture and filter(s) defined in assets/checks.json, so the exported
table always matches the frames the lab asks about.
"""
from pathlib import Path
import json, shutil, subprocess, sys

root = Path(__file__).resolve().parent.parent
exe = shutil.which("tshark")
if not exe and sys.platform == "darwin":
    candidate = Path("/Applications/Wireshark.app/Contents/MacOS/tshark")
    if candidate.exists():
        exe = str(candidate)
if not exe:
    raise SystemExit("TShark not found. Install Wireshark with CLI tools, or add its folder to PATH.")
cfg = json.loads((root / "assets/checks.json").read_text())
checks = [c for c in cfg["checks"] if c.get("count")]
display_filter = " || ".join(f"({c['filter']})" for c in checks)
cmd = [exe, "-n", "-r", str(root / "data" / cfg["capture"]), "-Y", display_filter,
       "-T", "fields", "-E", "header=y", "-E", "separator=,", "-E", "quote=d"]
for field in ["frame.number", "frame.time_relative", "_ws.col.def_src", "_ws.col.def_dst",
              "_ws.col.protocol", "frame.len", "_ws.col.info"]:
    cmd += ["-e", field]
for c in checks:
    for arg in c.get("decode", []):
        if arg not in cmd:
            cmd.append(arg)
keylog = any(c.get("keylog") for c in checks)
cmd += ["-o", "tls.keylog_file:" + (str(root / "data/lab-tls.keys") if keylog else "")]
r = subprocess.run(cmd, capture_output=True, text=True)
if r.returncode:
    raise SystemExit(r.stderr)
(root / "outputs").mkdir(exist_ok=True)
(root / "outputs/evidence.csv").write_text(r.stdout)
print(f"Wrote outputs/evidence.csv ({max(0, len(r.stdout.splitlines()) - 1)} rows) for: {display_filter}")
'''

LAB_TEMPLATES = {
    7: {"assets/filter-matrix.csv":
        "question,display_filter,matching_frames,count,notes\n"
        "Which DNS responses report a missing name?,dns.flags.rcode == 3,,,\n"
        "Which packets open TCP connections?,tcp.flags.syn == 1,,,\n"
        ",,,,\n,,,,\n,,,,\n"},
    15: {"assets/graph-notes-template.md":
         "# Graph notes — Lab 15\n\n| Graph | Stream / filter | Interval | Unit | Visible pattern | Limitation |\n"
         "|---|---|---|---|---|---|\n| Time/Sequence (Stevens) | tcp.stream == 3 | — | sequence number | | |\n"
         "| I/O — retransmissions | tcp.analysis.retransmission | 1 s | packets | | |\n"
         "| I/O — zero window | tcp.analysis.zero_window | 1 s | packets | | |\n"
         "| Round Trip Time | tcp.stream == 3 | — | seconds | | |\n"},
    16: {"assets/http-summary.csv":
         "uri,status_code,request_frame,response_frame,response_interval_s,proposed_next_step\n"
         "/health,,,,,\n/slow,,,,,\n/missing,,,,,\n/fault,,,,,\n"},
}


def scenario_ticket(a):
    b = C.LAB_BRIEFS[a["num"]]
    lines = [
        f"# Help-desk ticket HD-20{a['num']:02d}", "",
        "| Field | Value |", "|---|---|",
        f"| Site | {C.COMPANY} (fictional) |",
        "| Reported by | Branch help desk |",
        "| Client | 192.0.2.10 (02:00:00:00:00:10) |",
        "| Server | 192.0.2.20 (02:00:00:00:00:20) — portal.example.test |",
        "| Resolver | 192.0.2.53 |",
        f"| Evidence supplied | data/{'tls-session.pcap' if a['num'] == 17 else 'branch-office.pcap'} |", "",
        "## What was reported", "", b["scenario"], "",
        "## What you are asked to deliver", "", b["produce"] + ".", "",
        "All names and addresses are documentation values; the capture is synthetic.", "",
    ]
    if a["num"] == 18:
        lines += ["See also `assets/incident-ticket.md` (ticket BR-104).", ""]
    return "\n".join(lines)


def findings_template(a):
    b = C.LAB_BRIEFS[a["num"]]
    lines = [f"# Findings — Lab {a['num']:02d}: {a['title']}", "",
             "Analyst:            Date:", "",
             "## Capture and observation point", "", "- Capture file:", "- Profile used:", "- Display filter(s):", "",
             "## Evidence by task", ""]
    for i, task in enumerate(b["tasks"], 1):
        lines += [f"### {i}. {task}", "", "- Frame number(s):", "- Measurement / value:", "- What it shows:", ""]
    lines += ["## Conclusion", "", "- Observed facts:", "- Hypothesis (if any):",
              "- Limitation of this capture:", "- Next observation that would strengthen the conclusion:", ""]
    return "\n".join(lines)


def write(path, text, overwrite=True):
    if not overwrite and os.path.exists(path):
        return
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(text)


def readme(a):
    stem = f"LAB-{a['num']:02d}-Instructions"
    b = C.LAB_BRIEFS[a["num"]]
    return "\n".join([
        f"# Lab {a['num']:02d} — {a['title']}", "",
        b["scenario"], "",
        "## Instructions", "",
        f"- [{stem}.md]({stem}.md) — full step-by-step instructions",
        f"- [{stem}.pdf]({stem}.pdf) — the same instructions, printable", "",
        "## Quick start", "", "```bash", "python3 scripts/verify.py", "```", "",
        "## Folder contents", "",
        "- `data/` — synthetic captures (and, for the TLS lab, synthetic session secrets)",
        "- `assets/` — scenario ticket, expected evidence, templates and fixture checks",
        "- `scripts/` — verification, evidence export and optional data regeneration",
        "- `checkpoints/` — how to rejoin if you missed an earlier lab",
        "- `outputs/` — your findings and exported evidence", "",
        f"*{C.TITLE} · {C.COURSE_CODE} · Version {C.VERSION}*", ""])


def main():
    for a in ACTS:
        folder = os.path.join(LABS, folder_name(a))
        if not os.path.isdir(folder):
            print("Skipped (folder missing)", folder); continue
        shot = os.path.join(SHOTS, f"lab-{a['num']:02d}-evidence.png")
        if os.path.exists(shot):
            shutil.copyfile(shot, os.path.join(folder, "assets", "expected-evidence.png"))
        write(os.path.join(folder, "assets", "scenario.md"), scenario_ticket(a))
        write(os.path.join(folder, "outputs", "findings.md"), findings_template(a))
        for rel, body in LAB_TEMPLATES.get(a["num"], {}).items():
            write(os.path.join(folder, rel), body)
        write(os.path.join(folder, "scripts", "export_evidence.py"), EXPORT_SCRIPT)
        write(os.path.join(folder, f"LAB-{a['num']:02d}-Instructions.md"), to_markdown(lab_blocks(a)))
        write(os.path.join(folder, "README.md"), readme(a))
        print("Saved", folder_name(a))

    rows = [f"# Labs — {C.TITLE}", "",
            f"**Course code:** {C.COURSE_CODE}  |  **Version {C.VERSION} · {C.VERSION_DATE}**", "",
            f"All {len(ACTS)} labs use the same fictional branch office and supplied synthetic captures — "
            "no live network access is needed. Each lab folder is self-contained.", "",
            "Every folder holds `LAB-NN-Instructions.md` and `LAB-NN-Instructions.pdf` (full steps), "
            "a scenario ticket, the expected evidence, templates, a findings sheet and the verification scripts.", "",
            "| Topic | Lab | Activity | Instructions | You produce |", "|---|---:|---|---|---|"]
    for a in ACTS:
        f = folder_name(a); stem = f"LAB-{a['num']:02d}-Instructions"
        rows.append(f"| {TOPICS[a['topic']]['code']} | {a['num']:02d} | [{a['title']}]({f}/README.md) | "
                    f"[MD]({f}/{stem}.md) · [PDF]({f}/{stem}.pdf) | {C.LAB_BRIEFS[a['num']]['produce']} |")
    rows += ["", "## Further learning", "", "These sources informed the v5.1 labs and are recommended for extra practice. "
             "Kurose & Ross material is used with acknowledgement, as its terms require; no lab text is copied.", ""]
    rows += [f"- [{n}]({u})" for n, u in C.SOURCES]
    rows += ["", "Use only authorised data. The TLS key log in Lab 17 is synthetic session material for the supplied capture only.", "",
             "---", "", f"*{C.TITLE} · {C.COURSE_CODE} · Version {C.VERSION} · © 2026 Tertiary Infotech Academy Pte Ltd*", ""]
    write(os.path.join(LABS, "README.md"), "\n".join(rows))
    print("Saved labs/README.md")


if __name__ == "__main__":
    main()
