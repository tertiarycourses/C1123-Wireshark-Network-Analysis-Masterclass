from pathlib import Path
import subprocess,shutil
root=Path(__file__).resolve().parent.parent
exe=shutil.which('tshark') or '/Applications/Wireshark.app/Contents/MacOS/tshark'
cmd=[exe,'-n','-r',str(root/'data/branch-office.pcap'),'-T','fields','-E','header=y','-E','separator=,','-E','quote=d']
for field in ['frame.number','frame.time_relative','frame.len','ip.src','ip.dst','tcp.stream','http.request.uri','http.response.code']:cmd+=['-e',field]
r=subprocess.run(cmd,capture_output=True,text=True,check=True)
(root/'outputs').mkdir(exist_ok=True)
(root/'outputs/evidence.csv').write_text(r.stdout)
print('Wrote outputs/evidence.csv')
