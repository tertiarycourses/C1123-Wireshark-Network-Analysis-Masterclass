from pathlib import Path
import shutil,json,sys,re
from course_content import *
from generate_traces import generate
ROOT=Path(__file__).resolve().parent.parent
BUILD=ROOT/'.claude/skills/non-wsq-courseware-build/build'
slugs={i:re.sub('[^a-z0-9]+','-',t[2].lower()).strip('-') for i,t in enumerate(TOPICS,1)}
base=ROOT/'courseware/assets/fixture';base.mkdir(exist_ok=True); generate(base)
all_labs=[]
for i,(title,concepts,lab,fil,count,tasks) in enumerate(TOPICS,1):
 folder=ROOT/'labs'/f'lab-{i:02d}-{slugs[i]}'
 for d in ['data','scripts','assets','checkpoints','outputs']:(folder/d).mkdir(parents=True,exist_ok=True)
 shutil.copytree(base/'data',folder/'data',dirs_exist_ok=True)
 shutil.copy(ROOT/'scripts/generate_traces.py',folder/'scripts/generate_data.py')
 (folder/'requirements.txt').write_text('scapy>=2.6,<3\n')
 checks=[{'filter':fil,'count':count}]
 if i==14:checks += [{'filter':'tcp.analysis.zero_window','count':1},{'filter':'tcp.flags.reset == 1','count':1}]
 if i==16:checks += [{'filter':'http2.type == 4','count':1,'decode':['-d','tcp.port==8080,http2']}]
 if i==17:checks += [{'filter':'http.request','count':0},{'filter':'http.request','count':1,'keylog':True},{'filter':'http.response.code == 200','count':1,'keylog':True}]
 (folder/'assets/checks.json').write_text(json.dumps({'capture':'tls-session.pcap' if i==17 else 'branch-office.pcap','checks':checks},indent=2)+'\n')
 verify='''"""Check observable fixture facts with TShark. Does not inspect learner answers."""
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
'''
 (folder/'scripts/verify.py').write_text(verify)
 (folder/'scripts/export_evidence.py').write_text('''from pathlib import Path
import subprocess,shutil
root=Path(__file__).resolve().parent.parent
exe=shutil.which('tshark') or '/Applications/Wireshark.app/Contents/MacOS/tshark'
cmd=[exe,'-n','-r',str(root/'data/branch-office.pcap'),'-T','fields','-E','header=y','-E','separator=,','-E','quote=d']
for field in ['frame.number','frame.time_relative','frame.len','ip.src','ip.dst','tcp.stream','http.request.uri','http.response.code']:cmd+=['-e',field]
r=subprocess.run(cmd,capture_output=True,text=True,check=True)
(root/'outputs').mkdir(exist_ok=True)
(root/'outputs/evidence.csv').write_text(r.stdout)
print('Wrote outputs/evidence.csv')
''')
 (folder/'assets/topology.md').write_text('# Fictional branch office\n\nClient 192.0.2.10 (02:00:00:00:00:10) → switched LAN → server 192.0.2.20 (02:00:00:00:00:20). Resolver 192.0.2.53 is on the LAN. All IPs are documentation addresses; example.test names are synthetic.\n\nThe generated trace assumes both traffic directions are visible at a logical LAN observation point. For a routed comparison, add gateway 192.0.2.1, a router and a remote server. Identify what changes at Ethernet and IP layers.\n')
 templates={
 'capture-plan.md':'# Capture plan\n\nQuestion:\nPermission owner:\nSensor interface and placement:\nDirections visible:\nCapture filter: tcp port 80\nDuration: 60 seconds\nRing-buffer limit: 3 files of 10 MB\nDropped packet check:\nPrivacy and retention:\n',
 'dependency-map.md':'# Dependency chain\n\nARP request/reply frames:\nDNS query/response frames:\nTCP handshake frames:\nHTTP request/response frames:\nLocal next hop:\nRemote routed comparison:\n',
 'dns-observations.csv':'name,transaction_id,rcode,elapsed_seconds,next_investigation\n',
 'arp-table.csv':'ip,mac,request_frame,reply_frame\n',
 'arp-hypotheses.md':'# Competing explanations\n\nA missing reply could reflect an unavailable peer, VLAN mismatch or capture loss. A changed MAC could reflect a legitimate move, duplicate address or spoofing. Identify which extra observation would distinguish each pair.\n',
 'ip-header.csv':'frame,version,ihl,total_length,ttl,protocol,more_fragments,offset,scope\n',
 'icmp-events.csv':'frame,type,code,quoted_protocol,quoted_port,conclusion\n',
 'tcp-evidence.csv':'stream,frame,event,interval_seconds,limitation\n',
 'incident-ticket.md':'# Ticket BR-104\n\nUsers report intermittent portal errors, slow name lookups and a refused diagnostic service. Analyse the fictional trace; do not assume all symptoms share a root cause. Deliver a short incident report that another analyst can reproduce.\n',
 'report-template.md':'# Branch-office incident report\n\n## Scope and observation point\n\n## Timeline and affected flows\n\n## Observed facts with frame numbers and measurements\n\n## Hypotheses and competing explanations\n\n## Impact and recommended next action\n\n## Next capture placement and limitations\n',
 'ten-step-checklist.md':'# Ten troubleshooting steps\n\n1. Define scope and baseline.\n2. Check capture completeness.\n3. Use color.\n4. Inspect endpoints and conversations.\n5. Focus with filters.\n6. Build basic I/O graphs.\n7. Compare time values.\n8. Inspect Expert Information.\n9. Follow streams and compare TCP graphs.\n10. Check refusals/redirections and report evidence with uncertainty.\n'}
 for name,body in templates.items():(folder/'assets'/name).write_text(body)
 (folder/'outputs/.gitkeep').write_text('')
 (folder/'data/README.md').write_text('# Synthetic fixture provenance\n\nCreated entirely offline for C1123. No traffic is sent by the generator. Branch-office packets are authored with Scapy; TLS uses a real Python ssl MemoryBIO handshake with a temporary self-signed certificate, wrapped in synthetic TCP. The private certificate key is discarded. lab-tls.keys contains deliberately shareable secrets for this fictional session only. TLS capture and key log must be regenerated together. Packet timings are constructed for learning; they are not production measurements.\n')
 extra=[('Prepare your lab workspace. Open this lab folder in a terminal. Windows uses py -3 in place of python3. Wireshark GUI alone is sufficient for the investigation; CLI scripts require TShark on PATH. Run the fixture verification first.','python3 scripts/verify.py')]
 steps=extra+tasks+[('Export a reproducible packet table. Record the filter, frame numbers, measurement, explanation and limitation in outputs/findings.md.','python3 scripts/export_evidence.py')]
 trouble='TShark not found: install Wireshark CLI tools and add the installation folder to PATH; on Windows use the Wireshark install directory. A filter returns zero: clear other filters, use the specified capture, and check the expression is in the display toolbar. TLS remains opaque: select the matching lab-tls.keys file by absolute path, reload, and remove a key-log preference from another lab.'
 test=f'The supplied {fil} expression matches {count} frame(s) in the specified capture. Run scripts/verify.py and compare the listed frame numbers. Keep your findings and exported table in outputs/. Explain the observed result rather than only copying a count.'
 duration=60 if i in [16,17] else 75 if i==18 else 45
 md=f'# Lab {i:02d} — {lab}\n\nC1123 | {VERSION} | {duration} minutes\n\n## Goal\n\n{concepts[0]}\n\n## What you will build\n\nA packet evidence table and written findings for {lab.lower()}.\n\n## Prerequisites\n\nWireshark 4.6 or later, Python 3 for optional scripts, TShark CLI tools. '+('Complete earlier navigation/filter labs; all data is included here so you can rejoin independently.' if i>1 else 'No earlier lab required.')+'\n\n## Files\n\n- data/: offline captures and synthetic TLS session secrets\n- scripts/: generation, fixture verification and CSV export\n- assets/: topology, observation templates and checks\n- checkpoints/: rejoin instructions\n- outputs/: your saved evidence\n\n## Steps\n\n'
 for n,(inst,cmd) in enumerate(steps,1):md+=f'### {n}. {inst}\n\n'+(f'```bash\n{cmd}\n```\n\n' if cmd else '')
 md+=f'## Test it\n\n{test}\n\n## Troubleshooting\n\n{trouble}\n\n## Challenge\n\nCreate a second filter that answers the same question, then identify one packet it includes or excludes differently. Support your explanation with a frame number.\n\n## Reflection\n\nWhat additional observation would turn your leading hypothesis into a stronger conclusion?\n\n## Reset and regeneration\n\nKeep the supplied captures for the core lab. Optional regeneration requires `python3 -m pip install -r requirements.txt` and OpenSSL, then `python3 scripts/generate_data.py`. Do not send packets or capture an unauthorised interface. Clear TLS key-log preferences after the exercise.\n'
 (folder/'README.md').write_text(md)
 (folder/'checkpoints/README.md').write_text(f'# Rejoin checkpoint — Lab {i:02d}\n\nStart with the supplied data capture; no output from a previous lab is required. Reset to the C1123-Analyst profile or Default, clear all display filters, then follow this folder README. Run `python3 scripts/verify.py` to verify the fixture before continuing. Expected core filter: `{fil}`; expected frames: {count}.\n')
 all_labs.append(dict(num=i,topic=i,title=lab,objective=f'LO{1 if i<=4 else 2 if i<=8 else 3 if i<=13 else 4 if i<=17 else 5}',desc=concepts[0],build='Evidence CSV and packet findings',services='Wireshark, TShark, Python',steps=steps,test=test,troubleshooting=trouble,reflection='Which second observation point would strengthen your conclusion?',challenge='Develop and explain an alternative filter.',duration=duration))
 (BUILD/f'data_domain{i}.py').write_text(f'DOMAIN{i} = '+repr([all_labs[-1]])+'\n')
index='# C1123 lab activities\n\nEach folder is self-contained and uses the same fictional branch-office scenario. Open its README first.\n\n'
for i,t in enumerate(TOPICS,1): index+=f'- [Lab {i:02d}: {t[2]}](lab-{i:02d}-{slugs[i]}/README.md)\n'
(ROOT/'labs/README.md').write_text(index)
meta=f'''TITLE={TITLE!r}
SHORT_TITLE='Wireshark Network Analysis Masterclass (C1123)'
COURSE_CODE='C1123'
VERSION='v4.0'
VERSION_DATE='2 October 2026'
ORG='Tertiary Infotech Academy Pte Ltd'
UEN='UEN: 201200696W'
TRAINER='Dr. Alfred Ang'
DAYS=4
MODE='Instructor-led demonstrations and practical labs; 30 instructional hours'
COMPANY='Fictional Branch Office'
LAB_SLUGS={slugs!r}
LEARNING_OUTCOMES=['LO1: Plan scoped captures and configure a reproducible analyst profile.','LO2: Navigate, filter, summarize and time network exchanges.','LO3: Interpret DNS, ARP, IPv4, ICMP and UDP evidence.','LO4: Diagnose TCP and application behaviour, including HTTP and authorised TLS inspection.','LO5: Report observed facts, hypotheses and next actions with defensible evidence.']
TOPICS={ [dict(num=i,code=f'{i:02d}',title=t[0],subtitle=t[2],concepts=t[1]) for i,t in enumerate(TOPICS,1)]!r}
DAY_THEMES={{1:'Capture and analyst workflow',2:'Time, statistics, filters and DNS',3:'IP and transport diagnostics',4:'Graphs, applications and reporting'}}
LG_INTRO='This guide supports C1123, a four-day, 30-hour commercial short course. It includes detailed instructions for 18 self-contained labs using supplied synthetic packet captures.'
LG_INTRO2='The revised v4.0 deck starts from the supplied v3 reference presentation. Current lab instructions, data and scripts are supplied here; the legacy external trace names are not required for the new activities.'
LG_SETUP={{'needs':['Windows or macOS laptop; Wireshark 4.6 or later from https://www.wireshark.org/download.html.','TShark CLI tools for automated fixture checks; Python 3 for scripts. Scapy and OpenSSL only if regenerating data.','Download the whole labs folder so captures, templates and scripts stay together.'], 'verify_text':'Confirm Wireshark opens branch-office.pcap. For command-line checks use:', 'verify_code':'tshark --version\\npython3 --version','conventions':['Windows: use py -3 instead of python3. If tshark is not on PATH, use the Wireshark installation directory.','All packet addresses and names are synthetic. The generator sends no packets.','Steps assume you are inside the current lab folder. Clear filters between investigations.','4 days include 450 instructional minutes and 30 minutes of tea breaks each day; lunch is separate.']}}
LAB_NOTE='Use the README in the matching labs/lab-NN-title/ folder. Capture only with permission.'
LG_NEXT_STEPS=['Repeat a lab with a fresh analyst profile.','Use the ten-step checklist on a new authorised capture.','Preserve packet numbers, filters and limitations in every report.']
LG_GLOSSARY=[('Capture filter','libpcap expression limiting packets stored during capture.'),('Display filter','Wireshark expression selecting stored packets for viewing.'),('iRTT','Initial TCP round-trip sample from the handshake.'),('Retransmission','Repeated TCP byte range; interpretation depends on capture completeness.'),('Zero window','A receiver advertisement that no receive-buffer space is available.'),('TLS key log','Per-session secrets permitting authorised decryption of the matching session.'),('SPAN','Switch mirroring of selected traffic to a sensor port.'),('TAP','An inline observation device supplying link traffic to a sensor.')]
VERSION_HISTORY=[('4.0','2 October 2026','Revised from the supplied v3 deck; current guidance, visuals and 18 self-contained labs.','Dr. Alfred Ang')]
def SCHEDULE(lab_titles):
 result={{}}
 groups={{1:[1,2,3,4],2:[5,6,7,8,9],3:[10,11,12,13,14],4:[15,16,17,18]}}
 labmins={{1:180,2:225,3:225,4:240}}
 for day,nums in groups.items():
  demo=420-labmins[day]
  blocks=[(90,'topic','Concepts and demonstrations: topics '+', '.join(map(str,nums))),(15,'break','Tea break'),(60,'lab',lab_titles(nums)),(45,'topic','Evidence interpretation and worked examples'),(60,'lunch','Lunch'),(90,'lab','Continue labs: '+lab_titles(nums)),(15,'break','Tea break'),(demo-135,'topic','Worked examples and topic synthesis'),(labmins[day]-150,'lab','Complete lab investigations and findings'),(30,'recap','Learning reinforcement, topic recap and reflection')]
  now=9*60+30; rows=[]
  for minutes,kind,text in blocks:
   end=now+minutes;fmt=lambda x:f'{{x//60:02d}}:{{x%60:02d}}'
   rows.append((fmt(now),fmt(end),minutes,kind,text));now=end
  result[day]=(DAY_THEMES[day],rows)
 return result
'''
(BUILD/'course_data.py').write_text(meta)
(ROOT/'scripts/manifest.json').write_text(json.dumps({'title':TITLE,'code':CODE,'version':VERSION,'labs':all_labs,'topics':TOPICS,'slugs':slugs},indent=2))
shutil.rmtree(base)
print('Prepared 18 self-contained labs and aligned source data')
