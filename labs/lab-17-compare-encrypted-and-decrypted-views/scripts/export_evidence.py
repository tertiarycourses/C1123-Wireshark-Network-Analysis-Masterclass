"""Export this lab's evidence rows to outputs/evidence.csv.

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
