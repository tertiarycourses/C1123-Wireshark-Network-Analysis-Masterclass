"""Refresh static contents numbers against the final rendered PDF, excluding contents pages."""
import sys,re
from pathlib import Path
import fitz
from docx import Document
norm=lambda s:re.sub('[^a-z0-9]','',s.lower())
for filename in sys.argv[1:]:
 p=Path(filename);doc=Document(p);pdf=fitz.open(p.with_suffix('.pdf'));pages=[norm(pg.get_text()) for pg in pdf]
 start=next(i for i,t in enumerate(pages) if ('thisguidesupportsc1123' if p.name.startswith('LG') else 'courseinformation') in t and i>=3)
 updates=0
 for para in doc.paragraphs:
  if '\t' not in para.text:continue
  title=para.text.rsplit('\t',1)[0];key=norm(title)
  page=next((i+1 for i in range(start,len(pages)) if key in pages[i]),None)
  if page:
   para.runs[0].text=title+'\t'+str(page)
   for run in para.runs[1:]:run.text=''
   updates+=1
 doc.save(p);print(p.name,updates,'TOC entries refreshed')
