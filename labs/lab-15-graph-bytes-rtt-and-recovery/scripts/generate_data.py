"""Synthetic offline packet fixtures. No network traffic is sent."""
from pathlib import Path
import json, struct, argparse, ssl, tempfile, subprocess
from scapy.all import Ether,IP,TCP,UDP,ARP,ICMP,DNS,DNSQR,DNSRR,Raw,wrpcap
BASE=1790899200
CLIENT='192.0.2.10'; SERVER='192.0.2.20'; RESOLVER='192.0.2.53'
def make_packets():
 p=[]; clock=0
 def add(x,t=None):
  nonlocal clock
  clock=clock+0.01 if t is None else t
  x.time=BASE+clock; p.append(x)
 def e(x,rev=False): return Ether(src='02:00:00:00:00:20' if rev else '02:00:00:00:00:10',dst='02:00:00:00:00:10' if rev else '02:00:00:00:00:20')/x
 add(Ether(src='02:00:00:00:00:10',dst='ff:ff:ff:ff:ff:ff')/ARP(op=1,psrc=CLIENT,pdst=SERVER,hwsrc='02:00:00:00:00:10'))
 add(e(ARP(op=2,psrc=SERVER,pdst=CLIENT,hwsrc='02:00:00:00:00:20',hwdst='02:00:00:00:00:10'),True))
 for ident,name,rcode,delay in [(101,'portal.example.test',0,.02),(102,'missing.example.test',3,.02),(103,'slow.example.test',0,.8)]:
  add(e(IP(src=CLIENT,dst=RESOLVER)/UDP(sport=53000+ident,dport=53)/DNS(id=ident,qd=DNSQR(qname=name))))
  add(e(IP(src=RESOLVER,dst=CLIENT)/UDP(sport=53,dport=53000+ident)/DNS(id=ident,qr=1,ra=1,rcode=rcode,qd=DNSQR(qname=name),an=DNSRR(rrname=name,rdata=SERVER) if not rcode else None),True),clock+delay)
 for i in range(3):
  add(e(IP(src=CLIENT,dst=SERVER,ttl=64)/ICMP(type=8,id=7,seq=i)/Raw(b'LAB-PING')))
  add(e(IP(src=SERVER,dst=CLIENT,ttl=64)/ICMP(type=0,id=7,seq=i)/Raw(b'LAB-PING'),True),clock+.03)
 add(e(IP(src=CLIENT,dst=SERVER)/UDP(sport=55000,dport=9999)/Raw(b'LAB-UDP')))
 add(e(IP(src=SERVER,dst=CLIENT)/ICMP(type=3,code=3)/IP(src=CLIENT,dst=SERVER)/UDP(sport=55000,dport=9999),True))
 add(Ether(src='02:00:00:00:00:10',dst='01:00:5e:00:00:01')/IP(src=CLIENT,dst='224.0.0.1',ttl=1)/UDP(sport=55001,dport=5000)/Raw(b'LAB-MULTICAST'))
 def conn(port,dport=80,delay=.04,path='/health',status=200,body=b'LAB-OK',fault=False):
  c=IP(src=CLIENT,dst=SERVER); s=IP(src=SERVER,dst=CLIENT); sq=1000; aq=7000
  add(e(c/TCP(sport=port,dport=dport,flags='S',seq=sq,window=64240,options=[('MSS',1460),('WScale',7),('SAckOK',b'')])))
  add(e(s/TCP(sport=dport,dport=port,flags='SA',seq=aq,ack=sq+1,window=64240,options=[('MSS',1460),('WScale',7),('SAckOK',b'')]),True),clock+.03)
  add(e(c/TCP(sport=port,dport=dport,flags='A',seq=sq+1,ack=aq+1)))
  req=f'GET {path} HTTP/1.1\r\nHost: portal.example.test\r\nConnection: close\r\n\r\n'.encode()
  add(e(c/TCP(sport=port,dport=dport,flags='PA',seq=sq+1,ack=aq+1)/Raw(req)))
  add(e(s/TCP(sport=dport,dport=port,flags='A',seq=aq+1,ack=sq+1+len(req)),True))
  reason={200:'OK',404:'Not Found',500:'Internal Server Error'}[status]
  resp=f'HTTP/1.1 {status} {reason}\r\nContent-Type: text/plain\r\nContent-Length: {len(body)}\r\n\r\n'.encode()+body
  segment=e(s/TCP(sport=dport,dport=port,flags='PA',seq=aq+1,ack=sq+1+len(req))/Raw(resp),True)
  add(segment,clock+delay)
  if fault:
   # Unacknowledged identical segment after 1s => detectable retransmission.
   add(segment.copy(),clock+1)
  add(e(c/TCP(sport=port,dport=dport,flags='A',seq=sq+1+len(req),ack=aq+1+len(resp),window=0 if fault else 64240)))
  add(e(s/TCP(sport=dport,dport=port,flags='FA',seq=aq+1+len(resp),ack=sq+1+len(req)),True))
  add(e(c/TCP(sport=port,dport=dport,flags='A',seq=sq+1+len(req),ack=aq+2+len(resp))))
 conn(51001);conn(51002,delay=.75,path='/slow');conn(51003,path='/missing',status=404,body=b'LAB-MISSING');conn(51004,path='/fault',status=500,body=b'LAB-ERROR',fault=True)
 add(e(IP(src=CLIENT,dst=SERVER)/TCP(sport=52000,dport=81,flags='S',seq=1)))
 add(e(IP(src=SERVER,dst=CLIENT)/TCP(sport=81,dport=52000,flags='RA',seq=0,ack=2),True))
 # SIP signalling plus RTP with a deliberate sequence gap.
 for text,rev in [('INVITE sip:desk@192.0.2.20 SIP/2.0\r\nVia: SIP/2.0/UDP 192.0.2.10:5060;branch=z9hG4bKlab\r\nFrom: <sip:analyst@192.0.2.10>;tag=1\r\nTo: <sip:desk@192.0.2.20>\r\nCall-ID: lab-001@example.test\r\nCSeq: 1 INVITE\r\nContent-Length: 0\r\n\r\n',False),('SIP/2.0 200 OK\r\nVia: SIP/2.0/UDP 192.0.2.10:5060;branch=z9hG4bKlab\r\nFrom: <sip:analyst@192.0.2.10>;tag=1\r\nTo: <sip:desk@192.0.2.20>;tag=2\r\nCall-ID: lab-001@example.test\r\nCSeq: 1 INVITE\r\nContent-Length: 0\r\n\r\n',True)]:
  add(e(IP(src=SERVER if rev else CLIENT,dst=CLIENT if rev else SERVER)/UDP(sport=5060,dport=5060)/Raw(text.encode()),rev))
 for seq in [100,101,103,104]:
  add(e(IP(src=CLIENT,dst=SERVER)/UDP(sport=4000,dport=4002)/Raw(struct.pack('!BBHII',0x80,0,seq,seq*160,0x11223344)+b'\xff'*160)),clock+.02)
 # Cleartext HTTP/2 prior-knowledge fixture, no TLS implied.
 preface=b'PRI * HTTP/2.0\r\n\r\nSM\r\n\r\n'+b'\x00\x00\x00\x04\x00\x00\x00\x00\x00'
 add(e(IP(src=CLIENT,dst=SERVER)/TCP(sport=54000,dport=8080,flags='S',seq=1)))
 add(e(IP(src=SERVER,dst=CLIENT)/TCP(sport=8080,dport=54000,flags='SA',seq=1,ack=2),True))
 add(e(IP(src=CLIENT,dst=SERVER)/TCP(sport=54000,dport=8080,flags='A',seq=2,ack=2)))
 add(e(IP(src=CLIENT,dst=SERVER)/TCP(sport=54000,dport=8080,flags='PA',seq=2,ack=2)/Raw(preface)))
 return p

def tls_packets(folder):
 """Perform a real TLS 1.2 MemoryBIO exchange and wrap records in synthetic TCP."""
 c_in,c_out,s_in,s_out=[ssl.MemoryBIO() for _ in range(4)]
 with tempfile.TemporaryDirectory() as td:
  cert=Path(td)/'cert.pem'; key=Path(td)/'key.pem'
  subprocess.run(['openssl','req','-x509','-newkey','rsa:2048','-nodes','-keyout',str(key),'-out',str(cert),'-days','1','-subj','/CN=portal.example.test'],check=True,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
  sc=ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER);sc.load_cert_chain(cert,key)
  cc=ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT);cc.check_hostname=False;cc.verify_mode=ssl.CERT_NONE
  for ctx in [sc,cc]:ctx.minimum_version=ctx.maximum_version=ssl.TLSVersion.TLSv1_2
  cc.keylog_filename=str(folder/'data'/'lab-tls.keys')
  c=cc.wrap_bio(c_in,c_out,server_hostname='portal.example.test'); s=sc.wrap_bio(s_in,s_out,server_side=True)
  wire=[]
  for _ in range(12):
   for obj in [c,s]:
    try:obj.do_handshake()
    except ssl.SSLWantReadError:pass
   for out,inp,rev in [(c_out,s_in,False),(s_out,c_in,True)]:
    b=out.read()
    if b:wire.append((b,rev));inp.write(b)
  c.write(b'GET /health HTTP/1.1\r\nHost: portal.example.test\r\n\r\n');b=c_out.read();wire.append((b,False));s_in.write(b);s.read(4096)
  s.write(b'HTTP/1.1 200 OK\r\nContent-Length: 6\r\n\r\nLAB-OK');b=s_out.read();wire.append((b,True));c_in.write(b);c.read(4096)
 p=[]; cs=100;ss=500
 def pack(rev,flags,seq,ack,payload=b''):
  x=Ether(src='02:00:00:00:00:20' if rev else '02:00:00:00:00:10',dst='02:00:00:00:00:10' if rev else '02:00:00:00:00:20')/IP(src=SERVER if rev else CLIENT,dst=CLIENT if rev else SERVER)/TCP(sport=443 if rev else 56000,dport=56000 if rev else 443,flags=flags,seq=seq,ack=ack)
  if payload:x=x/Raw(payload)
  x.time=BASE+10+len(p)*.02;p.append(x)
 pack(False,'S',cs,0);cs+=1;pack(True,'SA',ss,cs);ss+=1;pack(False,'A',cs,ss)
 for b,rev in wire:
  pack(rev,'PA',ss if rev else cs,cs if rev else ss,b)
  if rev:ss+=len(b)
  else:cs+=len(b)
  pack(not rev,'A',cs if rev else ss,ss if rev else cs)
 return p

def generate(folder):
 folder=Path(folder);(folder/'data').mkdir(exist_ok=True)
 wrpcap(str(folder/'data'/'branch-office.pcap'),make_packets())
 wrpcap(str(folder/'data'/'tls-session.pcap'),tls_packets(folder))
 print('Generated offline synthetic captures in',folder/'data')
if __name__=='__main__':
 parser=argparse.ArgumentParser();parser.add_argument('--folder',default=str(Path(__file__).resolve().parent.parent));a=parser.parse_args();generate(a.folder)
