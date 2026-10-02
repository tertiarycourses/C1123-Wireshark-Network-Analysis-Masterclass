"""Check observable fixture facts with TShark. Does not inspect learner answers."""
from pathlib import Path
import subprocess,json,shutil,sys
root=Path(__file__).resolve().parent.parent
exe=shutil.which('tshark')
if not exe and sys.platform=='darwin':
 candidate=Path('/Applications/Wireshark.app/Contents/MacOS/tshark')
 if candidate.exists():exe=str(candidate)
if not exe: raise SystemExit('TShark not found. Install Wireshark with CLI tools, or add its folder to PATH.')
cfg=json.loads((root/'assets/checks.json').read_text())
for check in cfg['checks']:
 cmd=[exe,'-n','-r',str(root/'data'/cfg['capture']),'-Y',check['filter'],'-T','fields','-e','frame.number']
 cmd+=check.get('decode',[])
 cmd+=['-o','tls.keylog_file:'+str(root/'data/lab-tls.keys')] if check.get('keylog') else ['-o','tls.keylog_file:']
 r=subprocess.run(cmd,capture_output=True,text=True)
 if r.returncode:raise SystemExit(r.stderr)
 frames=r.stdout.strip().splitlines() if r.stdout.strip() else []
 if len(frames)!=check['count']:raise SystemExit(f"Expected {check['count']} frames for {check['filter']}; got {len(frames)}: {frames}")
 print(check['filter'], '=>', len(frames), 'frames:', ', '.join(frames))
print('Fixture checks complete.')
