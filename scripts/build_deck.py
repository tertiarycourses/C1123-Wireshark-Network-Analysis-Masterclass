"""Copy the user reference deck, refresh it and add editable evidence visuals."""
from pathlib import Path
import shutil,json,re
from pptx import Presentation
from pptx.util import Inches,Pt
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import PP_ALIGN
from pptx.opc.packuri import PackURI
from course_content import *
ROOT=Path(__file__).resolve().parent.parent
out=ROOT/'courseware'/f'{TITLE} (C1123)-{VERSION}.pptx'
reference=next((ROOT/'reference').glob('*.pptx'))
shutil.copy2(reference,out)
p=Presentation(out)
for layout in list(p.slide_layouts)+list(p.slide_masters):
 for sh in list(layout.shapes):
  if sh.top/914400>=5.1 or (sh.has_text_frame and ('This material belongs' in sh.text or '‹#›' in sh.text)):
   sh._element.getparent().remove(sh._element)
W=p.slide_width/914400;H=p.slide_height/914400
NAVY='17314D';TEAL='008C95';AMBER='D99830';GREY='506070';LIGHT='EEF5F7';WHITE='FFFFFF'
def rect(s,x,y,w,h,color,line=None):
 sh=s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE,Inches(x),Inches(y),Inches(w),Inches(h));sh.fill.solid();sh.fill.fore_color.rgb=RGBColor.from_string(color);sh.line.fill.background();return sh
def text(s,t,x,y,w,h,size=20,color=NAVY,bold=False):
 sh=s.shapes.add_textbox(Inches(x),Inches(y),Inches(w),Inches(h));tf=sh.text_frame;tf.word_wrap=True;tf.margin_left=tf.margin_right=Inches(.04)
 for i,line in enumerate(t.split('\n')):
  q=tf.paragraphs[0] if i==0 else tf.add_paragraph();q.text=line;q.font.name='Arial';q.font.size=Pt(size);q.font.bold=bold;q.font.color.rgb=RGBColor.from_string(color)
 return sh
def clear(s):
 for sh in list(s.shapes):sh._element.getparent().remove(sh._element)
 s.background.fill.solid();s.background.fill.fore_color.rgb=RGBColor.from_string(WHITE)
def footer(s):
 for sh in list(s.shapes):
  if sh.top/914400>=5.25:sh._element.getparent().remove(sh._element)
 text(s,'C1123  |  v4.0  |  Tertiary Infotech Academy',.35,5.27,8,.22,9,GREY)
def base(s,title,kicker='NETWORK ANALYSIS'):
 clear(s);text(s,kicker,.4,.22,9,.3,10,TEAL,True);text(s,title,.4,.65,9.1,.8,25,NAVY,True);footer(s)
def cards(s,title,labels,bodies,kicker='EVIDENCE → INTERPRETATION'):
 base(s,title,kicker)
 for k,(label,body) in enumerate(zip(labels,bodies)):
  x=.4+k*3.13;rect(s,x,1.8,2.98,2.95,LIGHT);text(s,f'{k+1:02d}',x+.16,2,2.6,.4,24,TEAL,True);text(s,label,x+.16,2.58,2.6,.55,17,NAVY,True);text(s,body,x+.16,3.22,2.6,1.32,14,GREY)
def flow(s,title,labels,bodies):
 base(s,title)
 for k,(label,body) in enumerate(zip(labels,bodies)):
  y=1.62+k*1.03;rect(s,.55,y,2.0,.77,TEAL);text(s,label,.68,y+.12,1.73,.45,16,WHITE,True);text(s,body,2.82,y+.02,6.5,.8,17,GREY)
def cover(s):
 clear(s);s.shapes.add_picture(str(ROOT/'courseware/assets/network-analysis.png'),0,0,width=p.slide_width,height=p.slide_height)
 rect(s,.35,.55,5.1,3.9,WHITE);text(s,'PACKET EVIDENCE • PRACTICAL DIAGNOSTICS',.6,.82,4.65,.5,11,TEAL,True)
 text(s,TITLE,.6,1.5,4.5,1.75,30,NAVY,True);text(s,'C1123 | 4 days | 30 instructional hours\nv4.0 • 2 October 2026\nTrainer: Dr. Alfred Ang',.6,3.32,4.6,1.1,14,GREY);footer(s)
ranges=[(1,62,1),(63,110,2),(111,113,3),(114,174,4),(175,201,5),(202,237,6),(238,246,16),(247,249,18),(250,289,15),(290,292,6),(293,297,18)]
updates=[]
original_ids={}
source_numbers={}
for n,s in enumerate(list(p.slides),1):
 original_ids[id(s)]=n
 source_numbers[s.part]=n
 old=' | '.join(sh.text for sh in s.shapes if sh.has_text_frame)
 topic=next((t for a,b,t in ranges if a<=n<=b),1)
 ti,concepts,lab,fil,count,tasks=TOPICS[topic-1]
 if n==1:cover(s);updates.append(n);continue
 if n in range(3,15):
  t=TOPICS[(n-3)%18];cards(s,f'Topic {(n-3)%18+1:02d} • {t[0]}',['Observe','Interpret','Verify'],t[1],'COURSE ROADMAP');updates.append(n);continue
 # Replace procedural/legacy external-file exercises with current concept/evidence visuals.
 procedural= n in [90,91,92,93,94,107,245,246] or bool(re.search(r'\b(solution|lab|step\s*\d|WinPcap|!=|RSA keys|certificate delivery|feedback)\b|[→⇒]|File\s*\||Edit\s*\||Select Statistics|Right click|Right-Click|www\.chappell|No Key No Data|SUM\(tcp.seq\)',old,re.I))
 if procedural:
  labels=['Observed fact','Interpretation','Boundary']
  if topic==5:
   bodies=['30 ms synthetic SYN → SYN/ACK sample.','760 ms request → response for /slow.','One-sided timings cannot locate the delaying device.']
  elif topic==15:
   bodies=['Repeated sequence range in stream 3.','A repeated segment and receive-window zero are distinct events.','Graph units and bins must be stated; sequence-number sums are not throughput.']
  elif topic==6:
   bodies=['SIP INVITE and 200 OK; RTP sequences 100, 101, 103, 104.','One synthetic media sequence is missing.','Call quality requires timing and capture-completeness context.']
  elif topic==16:
   bodies=['/health: 200; /missing: 404; /fault: 500.','Application errors can coexist with a working TCP connection.','TLS payload is visible only with matching authorised session secrets.']
  else:bodies=concepts
  cards(s,ti,labels,bodies,f'CURRENT CONCEPTS • LAB {topic:02d}');updates.append(n)
 elif n in [79,153,159,161,165,166,173] or '????' in old:
  current=14 if 136<=n<=174 else 2
  cards(s,TOPICS[current-1][0],['Observe','Explain','Limit'],TOPICS[current-1][1],'CURRENT PROTOCOL GUIDANCE')
 else:
  # Keep copied technical diagrams/screenshots and concept text.
  for sh in s.shapes:
   if not sh.has_text_frame:continue
   sh.text_frame.word_wrap=True
   if sh.left+sh.width>p.slide_width:sh.width=p.slide_width-sh.left-Inches(.1)
   for par in sh.text_frame.paragraphs:
    for run in par.runs:
     run.text=run.text.replace('4 Days Wireshark Network Analysis Specialization',TITLE).replace('Follow SSL Stream','Follow TLS Stream').replace('SSL communication','TLS communication').replace('WireShark','Wireshark').replace('Wire Shark','Wireshark').replace('‹#›','').replace('www.Wiki.wireshark.org','wiki.wireshark.org').replace('www.ask.wireshark.org','ask.wireshark.org')
  footer(s)
# Remove superseded external-file procedures and repeated solutions from the teaching run.
removed=[]
for idx in range(296,-1,-1):
 if idx+1 in updates and idx+1 != 1 or idx+1 in [16,17,293,294,295,296,297]:
  sid=p.slides._sldIdLst[idx];p.part.drop_rel(sid.rId);p.slides._sldIdLst.remove(sid);removed.append(idx+1)
for k,slide in enumerate(p.slides,1):
 slide.part._partname=PackURI(f'/ppt/slides/slide{k}.xml')
# Appended current companion curriculum: concept overview + visual evidence + lab brief, not instructions.
for i,(title,concepts,lab,fil,count,tasks) in enumerate(TOPICS,1):
 s=p.slides.add_slide(p.slide_layouts[6]);base(s,f'{i:02d}  {title}','CURRENT TEACHING COMPANION')
 rect(s,.4,1.65,4.45,3.25,LIGHT);text(s,concepts[0],.65,1.95,3.9,1.8,23,NAVY,True)
 if i in [2,8,14,17]:
  s.shapes.add_picture(str(ROOT/'courseware/assets/packet-investigation.png'),Inches(5.0),Inches(1.75),width=Inches(4.5),height=Inches(2.5))
  text(s,f'Lab {i:02d} • {lab}',5.1,4.3,4.2,.65,16,TEAL,True)
 else:
  text(s,f'Lab {i:02d}\n{lab}',5.2,1.8,4.1,1.1,22,TEAL,True);text(s,'Use the self-contained lab folder and Learner Guide. Observe → explain → verify → discuss.',5.2,3.05,4.1,1.5,18,GREY)
 s=p.slides.add_slide(p.slide_layouts[6]);flow(s,title,['Observe','Interpret','Corroborate'],concepts)
 s=p.slides.add_slide(p.slide_layouts[6]);cards(s,f'Lab {i:02d} • {lab}',['Build','Evidence','Reflect'],['A reproducible packet table and written findings.',f'{count} frame(s) match the core question in the supplied synthetic fixture.','Which second observation would strengthen your conclusion?'],'PRACTICAL ACTIVITY • FULL STEPS IN LG / LAB README')
# Add purpose and appropriate closing.
s=p.slides.add_slide(p.slide_layouts[6]);flow(s,"How You'll Learn",['Demonstrate','Investigate','Verify'],['Watch an evidence-led example.','Work with the supplied synthetic captures and templates.','Reproduce the observation, then discuss its limitations.'])
s=p.slides.add_slide(p.slide_layouts[6]);cards(s,'What You Achieved',['Capture','Diagnose','Report'],['Planned scope and a repeatable analyst workflow.','Interpreted protocol, timing and application evidence.','Separated facts, hypotheses and next actions.'])
s=p.slides.add_slide(p.slide_layouts[6]);flow(s,'Keep Practising',['Repeat','Apply','Review'],['Redo a lab with a fresh profile.','Use the checklist with an authorised new capture.','Check that every conclusion cites a packet or measurement.'])
s=p.slides.add_slide(p.slide_layouts[6]);base(s,'Thank You','WIRESHARK NETWORK ANALYSIS MASTERCLASS');text(s,'Keep the evidence.\nExplain the uncertainty.',.7,2,8.5,1.8,34,TEAL,True)
# Put the copied concept material inside the matching current topic sequence.
slides=list(p.slides);ids=list(p.slides._sldIdLst);retained=len(slides)-58
mapping={}
for j,slide in enumerate(slides[:retained]):
 n=source_numbers.get(slide.part,1)
 topic=(8 if 18<=n<=33 else 1 if n<=62 else 7 if 85<=n<=110 else 2 if n<=110 else 3 if n<=113 else 4 if n<=133 else 14 if n<=174 else 5 if n<=201 else 6 if n<=237 else 17 if n in [241,242] else 16 if n<=246 else 18 if n<=249 else 15 if n<=289 else 6)
 mapping[j]=topic
order=[0,1,len(slides)-4]
for i in range(1,19):
 order.append(retained+3*(i-1))
 order.extend(j for j in range(2,retained) if mapping[j]==i)
 order.extend([retained+3*(i-1)+1,retained+3*(i-1)+2])
order.extend([len(slides)-3,len(slides)-2,len(slides)-1])
assert len(order)==len(slides) and len(set(order))==len(slides)
for el in ids:p.slides._sldIdLst.remove(el)
for j in order:p.slides._sldIdLst.append(ids[j])
p.save(out)
(ROOT/'scripts/deck-provenance.json').write_text(json.dumps({'reference':reference.name,'reference_slides':297,'output_slides':len(p.slides),'refreshed_original_slide_numbers':updates,'superseded_procedural_slides_removed_from_teaching_run':sorted(removed),'method':'Copy original PPT, retain original slide order and non-procedural diagrams, retain concept diagrams; move procedural teaching to LG and replace external-file exercises with 18 self-contained lab briefs.'},indent=2))
print(out,len(p.slides),'slides;',len(updates),'reference slides refreshed')
