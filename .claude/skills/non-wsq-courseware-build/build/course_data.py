TITLE='Wireshark Network Analysis Masterclass'
SHORT_TITLE='Wireshark Network Analysis Masterclass (C1123)'
COURSE_CODE='C1123'
VERSION='v5.1'
VERSION_DATE='5 October 2026'
ORG='Tertiary Infotech Academy Pte Ltd'
UEN='UEN: 201200696W'
TRAINER='Dr. Alfred Ang'
DAYS=4
MODE='Instructor-led demonstrations and practical labs; 30 instructional hours'
COMPANY='Fictional Branch Office'
LAB_SLUGS={1: 'establish-a-trace-baseline', 2: 'plan-capture-placement', 3: 'create-an-analyst-profile', 4: 'color-and-annotate-evidence', 5: 'separate-path-and-server-delay', 6: 'summarize-traffic-and-a-voice-stream', 7: 'build-a-filter-evidence-matrix', 8: 'reconstruct-an-application-dependency-chain', 9: 'diagnose-dns-failure-and-delay', 10: 'verify-link-local-resolution', 11: 'classify-ipv4-scope-and-headers', 12: 'interpret-echo-and-unreachable-messages', 13: 'follow-datagrams-and-service-refusal', 14: 'investigate-retransmission-and-zero-window', 15: 'graph-bytes-rtt-and-recovery', 16: 'inspect-http-outcomes-and-http-2-frames', 17: 'compare-encrypted-and-decrypted-views', 18: 'produce-an-evidence-led-incident-report'}
LEARNING_OUTCOMES=['LO1: Plan scoped captures and configure a reproducible analyst profile.','LO2: Navigate, filter, summarize and time network exchanges.','LO3: Interpret DNS, ARP, IPv4, ICMP and UDP evidence.','LO4: Diagnose TCP and application behaviour, including HTTP and authorised TLS inspection.','LO5: Report observed facts, hypotheses and next actions with defensible evidence.']
TOPICS=[{'num': 1, 'code': '01', 'title': 'Introduction to Network Analysis and Wireshark', 'subtitle': 'Establish a trace baseline', 'concepts': ['A capture is a measurement at one observation point, not a complete network history.', 'Packet list, protocol details and bytes connect a summary to the underlying evidence.', 'Record interface, timestamp precision, dropped packets and capture scope before interpreting a trace.']}, {'num': 2, 'code': '02', 'title': 'Capture Methods and Capture Filters', 'subtitle': 'Plan capture placement', 'concepts': ['A switched access port normally observes its own traffic and broadcasts; SPAN or TAP placement changes visibility.', 'Capture filters use libpcap syntax before packets are stored; display filters hide or show stored packets.', 'Bound file size and duration; check capture drops before attributing missing packets to network loss.']}, {'num': 3, 'code': '03', 'title': 'Global Preferences and Troubleshooting Profiles', 'subtitle': 'Create an analyst profile', 'concepts': ['A profile bundles reproducible columns, coloring rules and protocol settings.', 'Name resolution can obscure numeric evidence and generate additional traffic; document the setting.', 'Protocol heuristics and TCP analysis preferences change interpretation, not the stored bytes.']}, {'num': 4, 'code': '04', 'title': 'Navigation and Coloring Techniques', 'subtitle': 'Color and annotate evidence', 'concepts': ['Color rules are applied in order; the first matching rule wins.', 'Temporary coloring is useful for a conversation; permanent rules support repeated triage.', 'Bookmarks and comments preserve the analyst path without changing the captured payload.']}, {'num': 5, 'code': '05', 'title': 'Time Values and Delay Types', 'subtitle': 'Separate path and server delay', 'concepts': ['Displayed delta depends on the current filter; capture delta does not.', 'SYN to SYN/ACK gives an initial path-related sample; request to response includes application processing.', 'One-sided timestamps cannot identify exactly which intermediate device delayed or dropped a packet.']}, {'num': 6, 'code': '06', 'title': 'Trace Statistics and VoIP Overview', 'subtitle': 'Summarize traffic and a voice stream', 'concepts': ['Protocol Hierarchy shows captured composition; byte share differs from packet share.', 'Conversations and Endpoints identify concentration; they do not alone prove malicious activity.', 'SIP signals a call while RTP carries media; jitter, loss and codec interpretation need stream context.']}, {'num': 7, 'code': '07', 'title': 'Display Filters', 'subtitle': 'Build a filter evidence matrix', 'concepts': ['Parentheses make mixed and/or expressions explicit.', 'Field existence and Boolean equality differ: tcp.flags.syn == 1 tests the bit.', 'Since Wireshark 3.6, != uses all-not-equal semantics; historical slides describing any-not-equal are obsolete.']}, {'num': 8, 'code': '08', 'title': 'TCP/IP Communications and Resolution', 'subtitle': 'Reconstruct an application dependency chain', 'concepts': ['ARP resolves a local next-hop MAC; DNS resolves a name to an address.', 'The destination IP stays end-to-end across routing while link-layer addresses change per hop.', 'Resolution, connection establishment and application exchange form a dependency chain.']}, {'num': 9, 'code': '09', 'title': 'DNS Traffic Analysis', 'subtitle': 'Diagnose DNS failure and delay', 'concepts': ['Transaction ID plus addresses and ports pair a query with its response.', 'NXDOMAIN reports that a name does not exist; it differs from silence or timeout.', 'DNS response time is a measured exchange, influenced by resolver and path behaviour.']}, {'num': 10, 'code': '10', 'title': 'ARP Traffic Analysis', 'subtitle': 'Verify link-local resolution', 'concepts': ['ARP requests are link-local broadcasts; replies usually return to the requester.', 'A repeated unresolved request suggests a local resolution problem, but a single trace may miss the reply.', 'MAC changes require corroboration before claiming duplicate IP or spoofing.']}, {'num': 11, 'code': '11', 'title': 'IPv4 Traffic Analysis', 'subtitle': 'Classify IPv4 scope and headers', 'concepts': ['TTL limits forwarding hops; it is not a latency measurement.', 'Broadcast and multicast use different addressing scopes and delivery rules.', 'Fragmentation fields describe packet handling; missing fragments can reflect capture limitations.']}, {'num': 12, 'code': '12', 'title': 'ICMP Traffic Analysis', 'subtitle': 'Interpret echo and unreachable messages', 'concepts': ['Echo requests/replies show an IP exchange; they do not guarantee an application works.', 'Destination unreachable messages quote the offending datagram.', 'ICMP may be filtered or rate-limited, so absence of a reply needs cautious interpretation.']}, {'num': 13, 'code': '13', 'title': 'UDP Traffic Analysis', 'subtitle': 'Follow datagrams and service refusal', 'concepts': ['UDP has no transport handshake or retransmission; the application may provide reliability.', 'A port number is a decoding hint; payload and context identify the application.', 'Following a UDP stream collects datagrams and does not invent missing data.']}, {'num': 14, 'code': '14', 'title': 'TCP Protocol Analysis', 'subtitle': 'Investigate retransmission and zero window', 'concepts': ['Sequence numbers count bytes; ACK numbers indicate the next expected byte.', 'Retransmission and duplicate ACK labels are heuristics sensitive to capture placement and completeness.', 'Zero window indicates receive-side flow control; it is distinct from network congestion.']}, {'num': 15, 'code': '15', 'title': 'Traffic Graphs', 'subtitle': 'Graph bytes, RTT and recovery', 'concepts': ['An I/O graph bins observed events; units and interval determine what it means.', 'TCP time-sequence graphs show byte progress, stalls and repeated sequence ranges.', 'RTT samples, application response time and throughput answer different questions.']}, {'num': 16, 'code': '16', 'title': 'HTTP and HTTP/2 Analysis', 'subtitle': 'Inspect HTTP outcomes and HTTP/2 frames', 'concepts': ['HTTP response codes describe application outcomes after transport delivery.', 'A response time contains more than network latency; pair the correct request and response.', 'HTTP/2 multiplexes frames; encrypted HTTP/2 needs authorised TLS secrets to inspect payload.']}, {'num': 17, 'code': '17', 'title': 'TLS-Encrypted Traffic Analysis', 'subtitle': 'Compare encrypted and decrypted views', 'concepts': ['Without session secrets, encrypted application records do not disclose HTTP payload.', 'A controlled key log enables authorised inspection of this synthetic TLS exchange.', 'A server RSA private key alone cannot decrypt modern ECDHE or TLS 1.3 sessions.']}, {'num': 18, 'code': '18', 'title': 'Ten Troubleshooting Steps and Reporting', 'subtitle': 'Produce an evidence-led incident report', 'concepts': ['Begin with scope and a baseline, then focus with endpoints, filters, time and graphs.', 'Separate observed facts from hypotheses and specify what new evidence would test them.', 'A useful report states affected flow, measurement, impact, recommended action and uncertainty.']}]
DAY_THEMES={1:'Capture and analyst workflow',2:'Time, statistics, filters and DNS',3:'IP and transport diagnostics',4:'Graphs, applications and reporting'}
LG_INTRO='This guide supports C1123, a four-day, 30-hour commercial short course. It includes detailed instructions for 18 self-contained labs using supplied synthetic packet captures.'
LG_INTRO2='Version 5.0 aligns the slides, this guide and the lesson plan with the Tertiary Infotech house design. Every lab ships with its own synthetic capture, templates and verification script; the Expected Evidence figure in each lab shows the packet list you should reproduce.'
LG_SETUP={'needs':['Windows or macOS laptop; Wireshark 4.6 or later from https://www.wireshark.org/download.html.','TShark CLI tools for automated fixture checks; Python 3 for scripts. Scapy and OpenSSL only if regenerating data.','Download the whole labs folder so captures, templates and scripts stay together.'], 'verify_text':'Confirm Wireshark opens branch-office.pcap. For command-line checks use:', 'verify_code':'tshark --version\npython3 --version','conventions':['Windows: use py -3 instead of python3. If tshark is not on PATH, use the Wireshark installation directory.','All packet addresses and names are synthetic. The generator sends no packets.','Steps assume you are inside the current lab folder. Clear filters between investigations.','4 days include 450 instructional minutes and 30 minutes of tea breaks each day; lunch is separate.']}
LAB_NOTE='Use the README in the matching labs/lab-NN-title/ folder. Capture only with permission.'
LG_NEXT_STEPS=['Repeat a lab with a fresh analyst profile.','Use the ten-step checklist on a new authorised capture.','Preserve packet numbers, filters and limitations in every report.']
LG_GLOSSARY=[('Capture filter','libpcap expression limiting packets stored during capture.'),('Display filter','Wireshark expression selecting stored packets for viewing.'),('iRTT','Initial TCP round-trip sample from the handshake.'),('Retransmission','Repeated TCP byte range; interpretation depends on capture completeness.'),('Zero window','A receiver advertisement that no receive-buffer space is available.'),('TLS key log','Per-session secrets permitting authorised decryption of the matching session.'),('SPAN','Switch mirroring of selected traffic to a sensor port.'),('TAP','An inline observation device supplying link traffic to a sensor.')]
VERSION_HISTORY=[('4.0','2 October 2026','Revised from the supplied v3 deck; current guidance, visuals and 18 self-contained labs.','Dr. Alfred Ang'),
 ('5.0','5 October 2026','Deck rebuilt on the house non-WSQ engine (C735 design system): full admin opener, core-concepts section, reference diagrams re-presented as captioned visuals, TShark evidence visuals per lab, per-topic schedule with day dividers and breaks.','Dr. Alfred Ang'),
 ('5.1','5 October 2026','Lab step slides replaced by scenario + summary slides (full steps in the LG and new per-lab instruction MD/PDF). About 40 new concept slides with visuals drawn from the lab captures; DHCP, NAT, IPv6, TShark, security patterns and baselining added from external sources. Per-lab scenario tickets, findings templates, TShark equivalents and optional extensions.','Dr. Alfred Ang')]

# ------------------------------------------------------------------ schedule (per-topic, 480 training min/day incl. tea; lunch excluded)
def SCHEDULE(lab_titles):
 T={t['num']:t['title'] for t in TOPICS}
 def topic(n): return 'Topic %d — %s (concepts + demonstration)'%(n,T[n])
 def lab(n): return 'Hands-on: '+lab_titles([n])
 plan={
  1:[(20,'admin','Welcome, trainer and learner introductions, ground rules, course objectives and lab setup check'),
     (30,'topic',topic(1)),(40,'lab',lab(1)),(15,'break','Tea break'),
     (30,'topic',topic(2)),(75,'lab',lab(2)),(60,'lunch','Lunch break'),
     (30,'topic',topic(3)),(60,'lab',lab(3)),(15,'break','Tea break'),
     (30,'topic',topic(4)),(75,'lab',lab(4)),
     (30,'lab','Guided practice: re-run Labs 1–4 with your own analyst profile; worked examples'),
     (30,'recap','Day 1 recap, learning reinforcement and Q&A')],
  2:[(15,'recap','Day 1 review and Day 2 objectives'),
     (25,'topic',topic(5)),(50,'lab',lab(5)),(15,'break','Tea break'),
     (25,'topic',topic(6)),(50,'lab',lab(6)),
     (30,'lab','Guided practice: timing and statistics worked examples (Labs 5–6)'),(60,'lunch','Lunch break'),
     (15,'topic',topic(7)),(30,'lab',lab(7)),(15,'topic',topic(8)),(30,'lab',lab(8)),(15,'break','Tea break'),
     (30,'topic',topic(9)),(60,'lab',lab(9)),
     (45,'lab','Guided practice: filter, resolution and DNS worked examples (Labs 7–9)'),
     (30,'recap','Day 2 recap, learning reinforcement and Q&A')],
  3:[(15,'recap','Day 2 review and Day 3 objectives'),
     (25,'topic',topic(10)),(50,'lab',lab(10)),(15,'break','Tea break'),
     (25,'topic',topic(11)),(50,'lab',lab(11)),
     (30,'lab','Guided practice: ARP and IPv4 worked examples (Labs 10–11)'),(60,'lunch','Lunch break'),
     (15,'topic',topic(12)),(30,'lab',lab(12)),(15,'topic',topic(13)),(30,'lab',lab(13)),(15,'break','Tea break'),
     (30,'topic',topic(14)),(60,'lab',lab(14)),
     (45,'lab','Guided practice: transport-layer worked examples (Labs 12–14)'),
     (30,'recap','Day 3 recap, learning reinforcement and Q&A')],
  4:[(15,'recap','Day 3 review and Day 4 objectives'),
     (25,'topic',topic(15)),(50,'lab',lab(15)),(15,'break','Tea break'),
     (30,'topic',topic(16)),(75,'lab',lab(16)),(60,'lunch','Lunch break'),
     (30,'topic',topic(17)),(60,'lab',lab(17)),(15,'break','Tea break'),
     (30,'topic',topic(18)),(75,'lab',lab(18)),
     (30,'lab','Synthesis: present your evidence-led incident report findings'),
     (30,'recap','Course recap, next steps and Q&A')],
 }
 fmt=lambda x:f'{x//60}:{x%60:02d}'
 out={}
 for day,blocks in plan.items():
  now=9*60+30; rows=[]
  assert sum(m for m,k,_ in blocks if k!='lunch')==480, day
  for m,k,text in blocks:
   rows.append((fmt(now),fmt(now+m),m,k,text)); now+=m
  out[day]=(DAY_THEMES[day],rows)
 return out

# Deck markers that mirror the schedule above
DAY_START_TOPIC={5:2,10:3,15:4}
BREAK_AFTER_TOPIC={1:('Tea Break','15 minutes'),2:('Lunch Break','1 hour'),3:('Tea Break','15 minutes'),
 4:('End of Day 1','See you tomorrow'),
 5:('Tea Break','15 minutes'),6:('Lunch Break','1 hour'),8:('Tea Break','15 minutes'),9:('End of Day 2','See you tomorrow'),
 10:('Tea Break','15 minutes'),11:('Lunch Break','1 hour'),13:('Tea Break','15 minutes'),14:('End of Day 3','See you tomorrow'),
 15:('Tea Break','15 minutes'),16:('Lunch Break','1 hour'),17:('Tea Break','15 minutes')}

# ------------------------------------------------------------------ admin / opener
TRAINER_CERT='PhD — specialises in networking, cyber security, cloud and AI.'
TRAINER_DELIVERS='Courses on network analysis, cyber security, cloud and AI for Tertiary Infotech Academy.'
ICE_BREAKER=['Your name and organisation / role.',
 'Your experience with Wireshark or network troubleshooting (if any).',
 'A slow or broken network problem you would like to be able to explain with packets.']
LO_TITLES=['Capture & profile','Navigate & time','Core protocols','TCP & applications','Evidence reporting']
PORTAL_SHOT='lms-portal.png'
LAB_SHOT_KICKER='EXPECTED EVIDENCE'
LAB_SHOTS={n:[(f'lab-{n:02d}-evidence.png','Expected Evidence — '+t,
  'Produced by TShark 4.6 from this lab\'s own synthetic capture with the lab filter(s) applied — your packet list should match.')]
  for n,t in LAB_SLUGS.items()}
LAB_SHOTS={n:[(f,'Expected Evidence — Lab %d'%n,c)] for n,[(f,_,c)] in LAB_SHOTS.items()}

COURSE_OVERVIEW=dict(
 section_title='Network Analysis Fundamentals',
 concepts_title='What is Wireshark?',
 concepts=[('Packet analyzer','Captures packets and presents every field it can decode — a measuring device for the network.'),
  ('Free and open source','Cross-platform (Windows, macOS, Linux) with TShark as its command-line twin.'),
  ('3,000+ protocols','Dissectors decode Ethernet to HTTP/2, DNS, TLS, SIP/RTP and more.'),
  ('Evidence, not opinion','Every claim cites a frame number, a filter and a measurement.')],
 framework_title='Who Uses Wireshark — and Why',
 framework=[('Network administrators','Troubleshoot slow and failing connections.'),
  ('Security analysts','Examine suspicious conversations and indicators.'),
  ('QA and developers','Verify and debug protocol implementations.'),
  ('Support engineers','Prove where a delay or failure actually occurs.'),
  ('Learners','See how network protocols really behave on the wire.'),
  ('Incident responders','Preserve packet evidence for a report.')],
 statement=dict(headline='Capture the evidence. Explain the uncertainty.',
  body='A trace is a measurement at one observation point — this course teaches you to say exactly what it proves and what it does not.',kicker='THE ANALYST MINDSET'),
 pillars_title='The Four Days at a Glance',
 pillars=[('Capture & navigate',['Place the capture point correctly','Build a reproducible analyst profile','Colour, time and filter efficiently']),
  ('Protocols & transport',['DNS, ARP, IPv4, ICMP, UDP evidence','TCP handshake, loss, retransmission','Zero window and recovery']),
  ('Applications & reporting',['I/O, RTT and Stevens graphs','HTTP outcomes, HTTP/2 and TLS','An evidence-led incident report'])],
 arc_title='How Every Lab Progresses',
 arc=['Open the lab\'s own synthetic capture — no live network traffic is needed.',
  'Apply the lab filter and locate the frames that answer the question.',
  'Record frame numbers, measurements and one limitation in outputs/findings.md.',
  'Run scripts/verify.py — it confirms the capture facts your findings rely on.'],
)

NEXT_STEPS=dict(title='Continue Your Learning',items=[
 'All course material stays on the LMS at https://lms-tms.tertiaryinfotech.com.',
 'The 18 labs and their captures are in the course GitHub repository — re-run them any time.',
 'Apply the ten-step troubleshooting checklist to an authorised capture at work.',
 'Explore networking and cyber-security courses at www.tertiarycourses.com.sg.'])
THANK_YOU=dict(kicker='THANK YOU FOR ATTENDING',
 body='Keep the evidence, explain the uncertainty — and keep practising with the 18 labs on your own machine.')

# ------------------------------------------------------------------ per-topic visual slides (images under courseware/assets/)
D='reference-diagrams/'
TOPIC_SLIDES={
 1:[('text_image','The TCP/IP and OSI Models',['The OSI model has seven layers; TCP/IP folds them into four.','Wireshark\'s Packet Details pane is ordered the same way — frame, Ethernet, IP, TCP/UDP, application.','Locate each fault at a layer before you choose a filter.'],D+'ref-020.png','OSI layers mapped to the TCP/IP model','REFRESHER'),
    ('text_image','Building a Packet',['Each layer wraps the one above: an application payload gains TCP, IP and Ethernet headers.','MAC addresses change at every hop; IP addresses stay end-to-end (unless NAT rewrites them).','Ports identify the conversation on each host.'],D+'ref-024.png','Encapsulation of an FTP request from client A to server A','ENCAPSULATION'),
    ('text_image','Data Flow Through the Network',['Data passes down the sender\'s stack, across switches and routers, and up the receiver\'s stack.','Switches forward on MAC; routers forward on IP.','Where you capture decides which hops you can see.'],D+'ref-023.png','Process-to-process, host-to-host and hop-by-hop delivery','DATA FLOW'),
    ('text_image','Inside Wireshark',['The capture engine collects packets through libpcap / Npcap.','Wiretap reads and writes trace formats: pcap, pcapng, snoop and more.','Dissectors decode each protocol; display filters operate on the dissected fields.'],D+'ref-039.png','Packet processing elements (the GUI is Qt-based in current releases)','ARCHITECTURE'),
    ('text_image','The Wireshark Window',['Packet List — one summary row per frame.','Packet Details — the decoded protocol tree.','Packet Bytes — the raw hex for the selected field.','Status bar — packet counts, profile and file information.'],D+'ref-042.png','The three main panes plus toolbars and status bar','USER INTERFACE'),
    ('shot',D+'ref-043.png','The Main Toolbar','Start/stop capture, open/save, find and go-to packet, colourise and zoom controls','USER INTERFACE'),
    ('shot',D+'ref-044.png','The Display Filter Toolbar','Green = valid expression, red = invalid; bookmark saved filters and add filter buttons','USER INTERFACE'),
    ('text_image','Status Bar and Intelligent Scrollbar',['The status bar shows packets captured vs. displayed and the active profile.','The intelligent scrollbar mirrors packet colouring — red/black bands reveal resets, aborts or low-TTL packets at a glance.'],D+'ref-046.png','Coloured scrollbar bands mark problem packets','USER INTERFACE')],
 2:[('text_image','Where to Tap Into the Network',['Client A complains about reaching the servers — where do you put the analyzer?','Capture as close as possible to the complaining host first, then move toward the servers.','Each point sees only the traffic that physically passes it.'],D+'ref-065.png','Choose the observation point before you capture','CAPTURE PLACEMENT'),
    ('two_col','What a Switch Port Can See','Switch port (default)',['Broadcast traffic','Multicast traffic (if forwarded)','Traffic to and from your own host','Not other hosts\' unicast traffic'],'Ways to see more',['Hub in half-duplex segment (lab only)','Network TAP — passive, in-line','SPAN / port mirroring on the switch','Capture on the target host itself'],'SWITCHED NETWORKS'),
    ('text_image','Test Access Points (TAPs)',['A TAP sits in-line and passively copies traffic to the analyzer.','Full-duplex TAPs forward both directions — and can pass physical-layer errors.','Aggregating TAPs merge both directions onto one monitor port.'],D+'ref-069.png','A non-aggregating TAP with two monitor ports','TAPS'),
    ('shot',D+'ref-070.png','Aggregating vs Non-aggregating TAPs','Non-aggregating: one port per direction. Aggregating: both directions combined on one port — can oversubscribe at high load','TAPS'),
    ('text_image','SPAN / Port Mirroring',['The switch copies traffic from source ports or VLANs to a destination port.','Mirrored traffic can drop under load and normally excludes errored frames.','Example (Cisco): monitor session 1 source interface g1/0/11 both.'],D+'ref-072.png','SPAN copies transmitted and received frames to the analyzer port','SPAN'),
    ('text_image','Wireless Capture',['Promiscuous mode on Wi-Fi usually shows only your own traffic.','Monitor mode captures 802.11 frames from all stations on a channel — needs a supporting adapter/driver.','Decrypting WPA2 traffic requires the passphrase and the 4-way handshake.'],D+'ref-079.png','Wireless capture depends on the adapter mode','WIRELESS'),
    ('two_col','Capture Filters vs Display Filters','Capture filter (BPF)',['Applied before packets are stored','Syntax: host 10.1.1.5 and tcp port 80','Discarded packets cannot be recovered','Use to limit file size on busy links'],'Display filter',['Applied to packets already captured','Syntax: ip.addr == 10.1.1.5 && tcp.port == 80','Clear it to see everything again','Use for analysis and evidence'],'FILTERING')],
 3:[('text_image','Configuration Profiles',['A profile bundles preferences, columns, colouring rules and filter buttons.','Switch profiles from the status bar or Edit > Configuration Profiles.','Create task profiles: Troubleshooting, Security, VoIP, Wireless.'],D+'ref-048.png','Right-click the Profile area in the status bar to switch or create','PROFILES'),
    ('text_image','Where Settings Live',['Help > About Wireshark > Folders shows personal and global configuration paths.','Copy a profile folder to share it with your team.','Keep a clean Default profile untouched.'],D+'ref-112.png','The Folders tab lists personal configuration locations','CONFIGURATION'),
    ('cards3','Preferences That Change Interpretation',[('Name resolution',['Off by default for evidence','MAC/transport names are local look-ups','Network names cause extra DNS traffic']),('Columns',['Add fields as columns (Apply as Column)','e.g. tcp.time_delta, http.host','Save them in the profile']),('Protocol settings',['TCP: calculate conversation timestamps','TCP: relative sequence numbers','TLS: key log file per lab'])],'PREFERENCES'),
    ('text_image','Apply as Column',['Right-click any field in Packet Details > Apply as Column.','Sort the new column to find extremes — largest delay, largest window, error codes.','Columns are saved in the active profile.'],D+'ref-058.png','Right-click | Apply As Column','PRODUCTIVITY')],
 4:[('text_image','Colouring Rules',['Rules are evaluated top-down — the first match colours the packet.','Default rules flag Bad TCP, HTTP, DNS, ARP, ICMP errors and more.','View > Coloring Rules to edit, import or export a rule set.'],D+'ref-115.png','The coloring rules list is processed in order','COLOURING'),
    ('text_image','Why Is a Packet This Colour?',['Expand the Frame section of Packet Details.','Coloring Rule Name and Coloring Rule String show which rule matched.','Use this to explain colours in a report.'],D+'ref-116.png','Frame > Coloring Rule Name / String','COLOURING'),
    ('text_image','Colourise a Conversation',['Right-click a packet > Colorize Conversation to tag a TCP/UDP stream temporarily.','Ten temporary colours make parallel conversations easy to tell apart.','View > Colorize Conversation > Reset to clear.'],D+'ref-117.png','Temporary conversation colouring','COLOURING'),
    ('text_image','Marking and Annotating Packets',['Mark (Ctrl+M) for quick navigation — marks are lost when the file closes.','Packet comments are saved in pcapng and travel with the evidence.','Time Shift corrects clock offsets between captures.'],D+'ref-057.png','Right-click | Packet Comment','ANNOTATION'),
    ('text_image','Navigation Shortcuts',['Ctrl+G — go to packet number.','Ctrl+F — find by display filter, hex or string.','Ctrl+. / Ctrl+, — next/previous packet in the conversation.','Ctrl+Space — collapse/expand the Packet Details tree.'],D+'ref-055.png','Edit | Mark / Ignore packets','NAVIGATION')],
 5:[('text_image','Time Display Formats',['View > Time Display Format chooses absolute, relative or delta time.','Seconds Since Beginning of Capture — default overview.','Seconds Since Previous Displayed Packet — finds gaps in a filtered view.'],D+'ref-181.png','Precision depends on the capture hardware and file format','TIME VALUES'),
    ('text_image','Captured vs Displayed Delta',['Delta since previous CAPTURED packet ignores the filter.','Delta since previous DISPLAYED packet changes when you change the filter.','State which delta you used in every finding.'],D+'ref-182.png','Same packets — different deltas','TIME VALUES'),
    ('text_image','End-to-End Path Delay',['SYN → SYN/ACK gives the initial round-trip time (iRTT) near the client.','Request → response adds server processing time.','Large gaps after an ACK point to the server, not the path.'],D+'ref-189.png','Sort a delta-time column to find the largest gaps','DELAY TYPES'),
    ('cards3','Three Kinds of Delay',[('Path delay',['SYN → SYN/ACK (iRTT)','tcp.analysis.ack_rtt','Affects every exchange']),('Server delay',['ACK → first response byte','http.time for HTTP','Grows with server load']),('Client delay',['Response → next request','Think time or app processing','Often not a network problem'])],'DIAGNOSIS'),
    ('content','Time Reference and Timestamps',['Ctrl+T sets a time reference — times are then measured from that packet.','Use a reference per conversation to time one transaction in isolation.','Timestamp precision is set by the capture system; you cannot add precision later.','Clock offsets between capture points need Time Shift before comparing.'],'TOOLS')],
 6:[('text_image','Capture File Properties',['Statistics > Capture File Properties: file, time span, interface and drop counts.','Check packets dropped before blaming the network for loss.','Record these facts at the start of every analysis.'],D+'ref-209.png','Statistics | Protocol Hierarchy shows the protocol mix','TRACE STATISTICS'),
    ('text_image','Conversations and Endpoints',['Statistics > Conversations lists pairs at Ethernet, IPv4/6, TCP and UDP level.','Sort by Bytes to find the most active conversation.','Right-click a row to filter on it.'],D+'ref-214.png','Statistics | Conversations — TCP tab, sorted by bytes','TRACE STATISTICS'),
    ('text_image','Packet Lengths',['Statistics > Packet Lengths shows the size distribution.','Many tiny packets moving bulk data suggest inefficient application behaviour.','A full-size Ethernet frame is 1518 bytes; TCP payload at MTU 1500 is 1460.'],D+'ref-216.png','Frame size components','TRACE STATISTICS'),
    ('text_image','Flow Graph and HTTP Statistics',['Statistics > Flow Graph draws the exchange between hosts as a ladder diagram.','Statistics > HTTP > Packet Counter summarises requests and response codes.','Use both to explain sequence and outcome in a report.'],D+'ref-223.png','Statistics | HTTP | Packet Counter','TRACE STATISTICS'),
    ('text_image','Voice over IP (VoIP)',['SIP signals the call: INVITE, 100 Trying, 180 Ringing, 200 OK, ACK.','RTP carries the media; gaps in RTP sequence numbers indicate loss.','Telephony > VoIP Calls, SIP Flows and RTP Streams analyse calls.'],D+'ref-291.png','SIP call set-up between two phones and a telephony server','VOIP')],
 7:[('text_image','Display Filter Operators',['Comparison: == != > < >= <= (or eq ne gt lt ge le).','Logical: && (and), || (or), ! (not); parentheses make intent explicit.','Strings in double quotes; contains and matches search payload text.'],D+'ref-088.png','Comparison operators with C-like and English forms','SYNTAX'),
    ('two_col','The != Trap (Wireshark 3.6+)','ip.addr != 10.2.4.1',['Means ALL ip.addr fields are not 10.2.4.1','Excludes every packet to OR from 10.2.4.1','This is the current behaviour'],'ip.addr ~= 10.2.4.1',['"Any not equal" — the old meaning of !=','Keeps packets where either address differs','Prefer !(ip.addr == 10.2.4.1) for clarity'],'COMMON MISTAKE'),
    ('content','Filter Building Techniques',['Right-click a field > Apply as Filter / Prepare as Filter.','Start typing — autocomplete lists valid field names.','Save frequent filters as filter buttons in your profile.','Test field existence (tcp.analysis.flags) vs a value (tcp.flags.syn == 1).'],'TECHNIQUES'),
    ('tiles','Filters You Will Use All Week',[('arp || icmp','Local resolution and reachability'),('dns.flags.rcode != 0','DNS errors'),('tcp.flags.syn == 1 && tcp.flags.ack == 0','Connection attempts'),('tcp.analysis.flags','All TCP expert warnings'),('http.response.code >= 400','Client and server errors'),('frame.time_delta_displayed > 1','Gaps over 1 s in the view')],'CHEAT SHEET')],
 8:[('text_image','The TCP/IP Protocol Suite',['Application: HTTP, DNS, SMTP, SNMP …','Transport: TCP (reliable) and UDP (best-effort).','Network: IP, ICMP, ARP sits between network and link.'],D+'ref-022.png','Where common protocols sit','PROTOCOL SUITE'),
    ('text_image','Switching Overview',['Switches learn MAC addresses and forward frames within a broadcast domain.','Source and destination MAC stay the same across a switch.','ARP resolves the next-hop MAC before the first frame is sent.'],D+'ref-029.png','A frame crossing a switch keeps its MAC addresses','LAYER 2'),
    ('text_image','Routing Overview',['Routers forward on destination IP and rewrite the link-layer addresses.','TTL decreases by one at every router hop.','The IP addresses are unchanged across routers (without NAT).'],D+'ref-030.png','MAC addresses change hop-by-hop; IP addresses stay end-to-end','LAYER 3'),
    ('text_image','Firewalls and NAT',['NAT/PAT rewrites addresses and ports — capture on both sides to correlate.','Firewalls may drop silently or reply with RST / ICMP unreachable.','A proxy creates two separate TCP connections.'],D+'ref-031.png','Address translation changes what each capture point sees','MIDDLEBOXES'),
    ('flow','The Dependency Chain',['ARP resolves the gateway MAC','DNS resolves the server name','TCP handshake opens the connection','Application request and response','Teardown: FIN or RST'],'RECONSTRUCT THE STORY')],
 9:[('text_image','How DNS Works',['The client asks its resolver; the resolver walks the hierarchy or answers from cache.','Queries normally use UDP 53; large answers and zone transfers use TCP.','Transaction ID pairs each response with its query.'],D+'ref-028.png','Name resolution through a local resolver','DNS'),
    ('cards3','Reading DNS Evidence',[('Success',['rcode 0 (NoError)','Answer records present','Check TTL and address']),('Failure',['rcode 3 = NXDOMAIN','rcode 2 = SERVFAIL','Name or zone problem']),('Silence',['Query with no response','Retries after timeout','Path, firewall or resolver'])],'DNS OUTCOMES'),
    ('content','Useful DNS Filters',['dns.flags.response == 0 — queries only.','dns.flags.rcode == 3 — name does not exist.','dns.time > 0.5 — responses slower than 500 ms.','dns.qry.name contains "example" — one domain family.'],'FILTERS')],
 10:[('cards3','ARP in Practice',[('Request',['Broadcast to ff:ff:ff:ff:ff:ff','"Who has 192.0.2.20? Tell 192.0.2.10"','arp.opcode == 1']),('Reply',['Unicast back to the requester','"192.0.2.20 is at 02:00:…"','arp.opcode == 2']),('Gratuitous',['Sender announces its own IP','Used after failover / IP change','arp.isgratuitous'])],'ADDRESS RESOLUTION'),
    ('two_col','ARP Problems to Recognise','Symptoms',['Repeated requests with no reply','Duplicate IP address detected warnings','One IP mapped to two MAC addresses','Excessive ARP broadcasts'],'Possible causes',['Host down or wrong subnet','Two hosts configured with the same IP','ARP spoofing — corroborate first','Scanning or misconfigured devices'],'DIAGNOSIS')],
 11:[('text_image','IPv4 Header Essentials',['TTL — hops remaining; not a measure of time.','Protocol — 1 ICMP, 6 TCP, 17 UDP.','Flags/Fragment offset — fragmentation handling.','DSCP — quality-of-service marking.'],D+'ref-137.png','Header layout (TCP header shown; IPv4 uses the same 32-bit rows)','IPV4'),
    ('cards3','Address Scope',[('Unicast',['One sender to one receiver','Most application traffic','ip.dst == host']),('Broadcast',['All hosts on the subnet','255.255.255.255 or directed','Not forwarded by routers']),('Multicast',['224.0.0.0/4 group addresses','224.0.0.1 = all hosts','Joined with IGMP'])],'SCOPE'),
    ('content','IPv4 Filters and Checks',['ip.ttl < 10 — packets close to expiring.','ip.flags.mf == 1 || ip.frag_offset > 0 — fragments.','ip.dst == 224.0.0.0/4 — all multicast.','Missing fragments may be a capture limitation — check drops first.'],'FILTERS')],
 12:[('cards3','ICMP Messages to Know',[('Echo',['Type 8 request, Type 0 reply','ping / reachability','Match on identifier + sequence']),('Unreachable',['Type 3','Code 3 = port unreachable','Code 1 = host unreachable']),('Time exceeded',['Type 11','TTL expired in transit','How traceroute works'])],'ICMP'),
    ('content','Interpreting ICMP Evidence',['An unreachable message quotes the original IP header — read it to find the failed flow.','No echo reply can mean filtering, not a down host.','Rate-limited ICMP can hide real loss.','icmp.type == 3 && icmp.code == 3 finds closed UDP ports.'],'INTERPRETATION')],
 13:[('text_image','TCP vs UDP',['UDP: connectionless, 8-byte header, no retransmission or ordering.','TCP: connection-oriented, reliable, ordered, flow-controlled.','Choose the analysis by the transport: UDP problems show up at the application.'],D+'ref-141.png','Header and feature comparison','TRANSPORT'),
    ('text_image','Ports and Sockets',['A socket is IP address + port.','A conversation is the pair of sockets — the 5-tuple with the protocol.','Ephemeral client ports change per connection.'],D+'ref-144.png','Socket pairs identify each conversation','SOCKETS'),
    ('content','Analysing UDP',['Follow > UDP Stream reassembles a datagram conversation.','A UDP request answered by ICMP port unreachable = closed port.','Missing responses need application-level timing to interpret.','Decode As lets you dissect traffic on non-standard ports.'],'TECHNIQUES')],
 14:[('text_image','The Three-Way Handshake',['SYN → SYN/ACK → ACK establishes the connection.','Options are negotiated here: MSS, window scale, SACK permitted.','The SYN → SYN/ACK gap is the initial RTT seen by the client.'],D+'ref-138.png','Connection establishment','TCP'),
    ('text_image','Sequence Numbers and Error Recovery',['Sequence numbers count bytes sent; ACK = next byte expected.','A gap triggers duplicate ACKs and retransmission.','Wireshark shows relative sequence numbers by default.'],D+'ref-139.png','Lost segment recovered after the receiver asks again','TCP'),
    ('text_image','TCP Windowing',['The receive window advertises buffer space available.','Window scaling multiplies it for high-bandwidth paths.','Window = 0 (Zero Window) stops the sender until a window update.'],D+'ref-140.png','Flow control with window advertisements','FLOW CONTROL'),
    ('text_image','Retransmissions',['Timeout retransmission (RTO): no ACK in time — backs off exponentially.','Fast retransmission: three duplicate ACKs trigger an early resend.','Spurious retransmissions repeat data that was already received.'],D+'ref-162.png','Retransmission timers on a lossy path','LOSS'),
    ('tiles','TCP Expert Flags',[('Retransmission','Data sent again'),('Duplicate ACK','Receiver still waiting for a gap'),('Previous segment not captured','Gap — loss or capture drop'),('Zero Window','Receiver buffer full'),('Window Full','Sender filled the advertised window'),('RST','Abrupt connection reset')],'EXPERT INFORMATION'),
    ('text_image','TCP Preferences',['Analyze TCP sequence numbers — enables tcp.analysis.* flags.','Calculate conversation timestamps — adds tcp.time_delta.','Relative sequence numbers make streams readable.'],D+'ref-147.png','Edit | Preferences | Protocols | TCP','PREFERENCES')],
 15:[('text_image','I/O Graphs',['Statistics > I/O Graphs plots packets, bytes or bits per interval.','Add graphs with filters — e.g. total vs tcp.analysis.flags.','Use log scale and moving averages to compare very different values.'],D+'ref-251.png','Multiple graphs with different filters on one chart','GRAPHS'),
    ('shot',D+'ref-253.png','Reading an I/O Graph','Drops in throughput that line up with TCP expert events point to the cause','GRAPHS'),
    ('text_image','Round Trip Time Graph',['Statistics > TCP Stream Graphs > Round Trip Time.','Graphs are unidirectional — pick the data-sending direction.','Spikes show where the path or receiver was slow to acknowledge.'],D+'ref-279.png','RTT per acknowledged segment','GRAPHS'),
    ('text_image','Time/Sequence (Stevens) Graph',['Sequence number vs time — the slope is throughput.','Flat steps reveal stalls such as zero window.','Vertical repeats indicate retransmissions.'],D+'ref-283.png','A flat region marks a zero-window stall','GRAPHS'),
    ('text_image','Window Scaling Graph',['Plots the receiver\'s advertised window alongside bytes in flight.','When bytes in flight meet the window, the receiver is the bottleneck.','A collapsing window points at the receiving application.'],D+'ref-289.png','Stable window, instability and zero window','GRAPHS')],
 16:[('cards3','HTTP Response Codes',[('2xx / 3xx',['200 OK','301/302 redirect','304 not modified']),('4xx client',['400 bad request','403 forbidden','404 not found']),('5xx server',['500 internal error','502 bad gateway','503 unavailable'])],'HTTP'),
    ('text_image','Follow the Stream',['Right-click > Follow > TCP Stream (or HTTP Stream) reassembles the conversation.','Client data in red, server data in blue.','The filter changes to tcp.stream == N — clear it to return.'],D+'ref-240.png','Follow Stream reassembles the transferred data','REASSEMBLY'),
    ('text_image','Export HTTP Objects',['File > Export Objects > HTTP lists every transferred object.','Save files for inspection — handle unknown content safely.','http.time measures each response time.'],D+'ref-054.png','File | Export Objects | HTTP','EXPORT'),
    ('two_col','HTTP/1.1 vs HTTP/2','HTTP/1.1',['Text headers, one request at a time per connection','Readable directly in the packet list','http.request.method, http.response.code'],'HTTP/2',['Binary frames multiplexed into streams','Usually inside TLS (ALPN h2)','http2.type, http2.streamid; Decode As for clear-text test ports'],'PROTOCOLS')],
 17:[('cards3','TLS Handshake Evidence',[('Client Hello',['SNI = requested server name','Offered versions and ciphers','tls.handshake.type == 1']),('Server Hello',['Chosen version and cipher','Certificate (TLS 1.2)','tls.handshake.type == 2']),('Application Data',['Encrypted records','Sizes and timing still visible','tls.record.content_type == 23'])],'TLS'),
    ('two_col','Decrypting TLS — Authorised Only','Works',['Key log file from the client (SSLKEYLOGFILE)','Preferences > Protocols > TLS > (Pre)-Master-Secret log filename','Works for TLS 1.2 and TLS 1.3'],'Does not work',['RSA private key with (EC)DHE or TLS 1.3 sessions','Captures without the matching session secrets','Anything you are not authorised to inspect'],'DECRYPTION'),
    ('flow','Encrypted vs Decrypted View',['Open the TLS capture — only handshake and Application Data','Note what metadata is still visible','Load the lab key log file','HTTP requests and responses appear','Remove the key log before the next lab'],'LAB 17 PREVIEW')],
 18:[('flow','Ten-Step Troubleshooting Method',['Baseline "normal" traffic','Check conversations and endpoints','Apply focused filters and colour','Measure time and TCP evidence','Graph, follow streams and report'],'METHOD'),
    ('text_image','Export and Preserve Evidence',['File > Export Specified Packets saves only the relevant frames.','Export Packet Dissections produces text/CSV for reports.','Keep the original capture unchanged and record its hash.'],D+'ref-248.png','File | Export Packet Dissections','EVIDENCE'),
    ('cards3','Writing the Incident Report',[('Observed facts',['Frame numbers','Filters used','Measured times and counts']),('Interpretation',['What the evidence suggests','Alternative explanations','Confidence level']),('Next actions',['Further captures needed','Owner and system to check','Limitations of this trace'])],'REPORTING')],
}

# ------------------------------------------------------------------ lab briefs (deck scenario + summary; lab instruction files)
# The deck shows only the scenario and a 4-task summary per lab; full steps live in the LG
# and in labs/lab-NN-*/LAB-NN-Instructions.md/.pdf.
LAB_STEPS_IN_DECK=False
_B=[
 ("The branch help desk has received a capture from the client PC (192.0.2.10), but nobody has checked what it contains. Before anyone diagnoses a fault, you establish a trusted baseline of the trace.",
  ["Verify the lab fixture with verify.py","Record packet count and capture duration","Trace a field from Packet Details to bytes","Pair the ARP request and reply"],
  "A baseline record of the capture and the ARP exchange",[]),
 ("A user on the branch LAN reports slow web pages. Your manager asks where a sensor should go — and what it would see — before anyone touches the switch.",
  ["Mark three sensor points on the topology","Check capture-filter syntax (tcp port 80)","Compare capture vs display filtering","Complete the capture plan and permissions"],
  "A completed capture plan with sensor placement and limits",[("assets/topology.md","Fictional branch topology"),("assets/capture-plan.md","Capture plan template you complete")]),
 ("Three analysts will share findings on the same case. To make results reproducible, you build a named analyst profile with numeric addresses and evidence columns.",
  ["Create the C1123-Analyst profile","Turn off name resolution","Add stream index and delta columns","Record and export the profile folder"],
  "A reusable C1123-Analyst profile and its folder path",[]),
 ("Users see intermittent web errors. You need the failing responses to stand out, and annotations that travel with the evidence.",
  ["Filter HTTP 4xx and 5xx responses","Add a LAB HTTP Error colouring rule","Mark and comment the 500 response","Save and reopen the annotated pcapng"],
  "An annotated pcapng with a comment on the failing response",[]),
 ("The /slow page takes almost a second to load. The network team blames the server and the server team blames the network — your timing evidence decides.",
  ["Measure SYN→SYN/ACK and initial RTT","Time the /slow request to its response","Compare captured vs displayed deltas","Write a hypothesis and next capture point"],
  "Timing evidence separating path delay from server delay",[]),
 ("Management wants a one-page summary of what crossed the branch link, including a test voice call that users said sounded choppy.",
  ["Review Protocol Hierarchy and Conversations","Graph all traffic in bits per second","Identify the SIP INVITE and 200 OK","Decode RTP and find the missing sequence"],
  "A traffic summary and RTP loss evidence",[]),
 ("The team keeps sharing filters that silently hide evidence. You build a tested filter matrix so everyone answers the same question the same way.",
  ["Find the NXDOMAIN response and SYNs","Compare two bracketings of one filter","Test !(ip.addr == x) vs ip.addr != x","Save five verified filters with frames"],
  "A filter evidence matrix with verified frame numbers",[("assets/filter-matrix.csv","Filter matrix template (question, filter, frames)")]),
 ("A user says \"the portal is down\". Before blaming the web server, you rebuild every dependency the browser needed: address resolution, name resolution, connection and request.",
  ["Locate the ARP exchange and DNS lookup","Draw the TCP/HTTP exchange in Flow Graph","Fill in the dependency map","Contrast a local and a routed next hop"],
  "A completed dependency map with frame ranges",[("assets/dependency-map.md","Dependency chain template"),("assets/topology.md","Fictional branch topology")]),
 ("Users report that some names fail and others resolve slowly. You separate a missing name from a slow resolver using the DNS evidence.",
  ["Pair DNS queries and responses by ID","Explain the NXDOMAIN response","Measure the 0.8 s slow transaction","Record observations and next steps"],
  "A DNS observations sheet with measured intervals",[("assets/dns-observations.csv","DNS observations sheet you complete")]),
 ("A technician suspects an ARP problem on the branch LAN. You check what the capture actually proves before anyone raises a spoofing alert.",
  ["Record ARP request and reply fields","Confirm the server IP-to-MAC mapping","Verify the opcode in the packet bytes","Test the hypotheses against the evidence"],
  "A verified ARP table entry and an evidence-based conclusion",[("assets/arp-table.csv","ARP table you complete"),("assets/arp-hypotheses.md","Competing explanations to test")]),
 ("The security team asks whether any unusual IPv4 traffic — multicast, broadcast or fragments — appears in the branch capture.",
  ["Record IPv4 header fields of an echo","Compare multicast MAC and IP destination","Check for fragmented packets","Classify scope in the IP header sheet"],
  "A completed IPv4 header and scope sheet",[("assets/ip-header.csv","IPv4 header sheet you complete")]),
 ("Ping to the server works, yet a diagnostic tool on UDP port 9999 fails. You use ICMP evidence to explain the difference.",
  ["Pair echo requests and replies","Read the quoted headers in the unreachable","Find the original UDP datagram","Record the events and your conclusion"],
  "An ICMP event log explaining the service refusal",[("assets/icmp-events.csv","ICMP event log you complete")]),
 ("The diagnostic application sends UDP and never hears back. You follow the datagrams to show what was sent and why there is no transport-level acknowledgement.",
  ["Tell the datagram from its ICMP quote","Follow the UDP stream (LAB-UDP)","Decode the RTP stream on port 4002","Explain the refusal without UDP ACKs"],
  "A saved UDP stream and an explanation of the refusal",[]),
 ("A file download stalls part-way through. You must show whether the sender, the receiver or the path held things up.",
  ["Read Expert Information for stream 3","Compare the retransmitted segment","Confirm the zero-window advertisement","Identify the port 81 reset"],
  "A TCP evidence sheet for retransmission, zero window and reset",[("assets/tcp-evidence.csv","TCP evidence sheet you complete")]),
 ("Management wants a picture, not a packet list. You graph the stalled transfer so the retransmission and zero-window events are obvious.",
  ["Open the Stevens time/sequence graph","Graph retransmission and zero-window events","Compare RTT samples with the handshake","Write graph notes with units and limits"],
  "Graph notes with interval, unit, stream and limitation",[("assets/graph-notes-template.md","Graph notes template")]),
 ("The web team wants to know which pages fail and whether the new HTTP/2 test service is negotiating correctly.",
  ["Pair four URIs with their status codes","Follow the stream and export an object","Decode port 8080 as HTTP/2","Summarise outcomes and next steps"],
  "An HTTP outcome summary and an exported object",[("assets/http-summary.csv","HTTP summary template")]),
 ("Under an authorised test, the portal's HTTPS traffic must be inspected. You compare what an analyst sees with and without the session secrets.",
  ["Inspect the encrypted TLS view","Read the SNI in the ClientHello","Load the key log and view the HTTP","Verify, then remove the key log"],
  "A comparison of the encrypted and decrypted views",[("data/tls-session.pcap","Synthetic TLS capture"),("data/lab-tls.keys","Synthetic session secrets for this capture only")]),
 ("Ticket BR-104 combines several user complaints. You produce a reproducible incident report that separates observed facts from hypotheses.",
  ["Read the incident ticket","Collect evidence for each symptom","Write the report from the template","Peer-review with the ten-step checklist"],
  "An evidence-led incident report",[("assets/incident-ticket.md","Incident ticket BR-104"),("assets/report-template.md","Report template"),("assets/ten-step-checklist.md","Ten-step review checklist")]),
]
LAB_BRIEFS={i:dict(scenario=s,tasks=t,produce=p,files=f) for i,(s,t,p,f) in enumerate(_B,1)}

# ------------------------------------------------------------------ v5.1 enrichment: detailed concept slides with visuals
# Visuals under courseware/assets/visuals/ are drawn from the labs' own captures by
# scripts/build_concept_visuals.py. Topic additions draw on the external sources in SOURCES.
V='visuals/'
def _add(topic, after_title, *specs):
    """Insert specs after the slide whose title matches after_title (None = append)."""
    lst = TOPIC_SLIDES.setdefault(topic, [])
    idx = len(lst)
    if after_title:
        for i, sp in enumerate(lst):
            if after_title in sp:
                idx = i + 1; break
    lst[idx:idx] = list(specs)

_add(1, 'The TCP/IP and OSI Models',
 ('text_image','Anatomy of a Packet',['Every frame is nested headers: Ethernet II (14 B) › IPv4 (20 B) › TCP (20 B) › application payload.','Packet Details lists them in the same top-to-bottom order.','Clicking a field highlights its exact bytes in the Packet Bytes pane.'],V+'diagram-encapsulation.png','Frame 21 of the lab capture: GET /health, 124 bytes','ENCAPSULATION'))
_add(1, None,
 ('content','Capture Your Own Baseline',['Pick the busy interface — the sparkline beside each interface shows live traffic.','Capture 30–60 s of normal activity on a network you are authorised to monitor, then stop.','Save as pcapng so comments and interface details are kept.','Record interface, start time, duration and dropped packets (Statistics > Capture File Properties).'],'GETTING STARTED'),
 ('tiles','TShark — Wireshark on the Command Line',[('tshark -D','List capture interfaces'),('tshark -i 1 -a duration:60 -w base.pcapng','Timed capture to a file'),('tshark -r base.pcapng -Y "dns"','Read a file with a display filter'),('-T fields -e ip.src -e dns.qry.name','Print chosen fields only'),('-q -z io,phs','Protocol hierarchy statistics'),('-q -z conv,tcp','TCP conversation table')],'TSHARK'))
_add(2, 'Where to Tap Into the Network',
 ('text_image','Choosing the Observation Point',['A — on the client: sees everything the client sends and receives.','B — SPAN on the switch: copies frames, may drop under load and hides errored frames.','C — TAP on the uplink: both directions, including physical-layer errors.','D — at the server: shows server-side timing.'],V+'diagram-capture-points.png','The same problem looks different from each capture point','CAPTURE PLACEMENT'))
_add(2, 'Capture Filters vs Display Filters',
 ('shot',V+'diagram-filter-pipeline.png','The Filtering Pipeline','Capture filters (BPF) decide what is stored; display filters only decide what is shown','FILTERING'),
 ('tiles','Capture Filter (BPF) Cheat Sheet',[('host 192.0.2.10','To or from one host'),('net 192.0.2.0/24','One subnet'),('tcp port 80','One TCP port'),('port 53','DNS over UDP or TCP'),('not arp and not stp','Drop background noise'),('tcp[tcpflags] & tcp-syn != 0','TCP SYN packets only')],'BPF SYNTAX'),
 ('content','Capture Options for Long Captures',['Ring buffer: e.g. 10 files × 100 MB keeps the most recent traffic without filling the disk.','Auto-stop after a duration, file size or packet count.','Snapshot length can limit stored bytes per packet for privacy and size.','Always check “dropped” counts before trusting a gap.'],'CAPTURE OPTIONS'))
_add(3, 'Apply as Column',
 ('tiles','Recommended Analyst Columns',[('frame.time_delta_displayed','Gap from the previous shown packet'),('tcp.stream','Which conversation'),('tcp.time_delta','Gap within the TCP stream'),('dns.time','DNS response time'),('http.time','HTTP response time'),('tcp.window_size','Receiver window (scaled)')],'PROFILES'))
_add(4, 'Colouring Rules',
 ('tiles','Default Colours — What They Mean',[('Black + red text','Bad TCP: retransmission, zero window, RST'),('Light green','HTTP'),('Light purple','TCP'),('Light blue','UDP (DNS, SIP, RTP …)'),('Pale yellow','ARP and routing'),('Black + green text','ICMP errors')],'COLOURING'))
_add(5, 'End-to-End Path Delay',
 ('text_image','Timing the Slow Request',['Stream 1 handshake: SYN → SYN/ACK 30 ms, complete in 40 ms.','The server ACKs GET /slow in 10 ms …','… then needs 750 ms before the 200 OK.','The path is fast; the delay is server processing.'],V+'ladder-slow.png','TCP stream 1 from the lab capture','EVIDENCE'),
 ('shot',V+'chart-delay-breakdown.png','Where the 0.8 Seconds Went','Measured intervals inside TCP stream 1 — path delay is small; server processing dominates','DELAY BREAKDOWN'))
_add(6, 'Capture File Properties',
 ('shot',V+'chart-protocol-mix.png','Packets vs Bytes by Protocol','Protocol Hierarchy of the lab capture: TCP has the most packets, but byte share tells a different story','PROTOCOL HIERARCHY'),
 ('shot',V+'chart-io-graph.png','Reading the I/O Graph','Gaps show waiting; the red bar marks the retransmission/zero-window events','I/O GRAPH'))
_add(6, 'Voice over IP (VoIP)',
 ('text_image','SIP Signalling and RTP Media',['INVITE / 200 OK set up the call on UDP 5060.','RTP carries the voice — here on UDP 4002, decoded with Decode As.','Sequence 100, 101, 103, 104: number 102 never arrived at this capture point.'],V+'ladder-sip-rtp.png','The lab capture’s test call','VOIP'))
_add(7, 'Filter Building Techniques',
 ('tiles','Operators and Functions Worth Knowing',[('tcp.port in {80, 443, 8080}','Set membership (comma-separated)'),('http.host contains "example"','Substring match'),('dns.qry.name matches "^miss"','Regular expression'),('eth.src[0:3] == 02:00:00','Byte slice of a field'),('len(http.request.uri) > 50','Length of a field'),('!(arp || dns)','Exclude whole protocols')],'DISPLAY FILTERS'))
_add(8, 'The TCP/IP Protocol Suite',
 ('text_image','One Web Request, Step by Step',['Three-way handshake: SYN, SYN/ACK, ACK.','GET /health, server ACK, 200 OK, client ACK.','FIN/ACK closes the connection.','Every arrow is a frame you can click in the lab.'],V+'ladder-tcp-http.png','TCP stream 0 from the lab capture','TCP/IP IN ACTION'))
_add(8, 'Firewalls and NAT',
 ('shot',V+'diagram-nat.png','NAT Changes What Each Capture Point Sees','Inside and outside captures show different addresses and ports for the same flow','NAT'),
 ('text_image','DHCP — How a Host Gets Its Address',['Discover and Request are broadcasts from 0.0.0.0 (UDP 68 → 67).','Offer and ACK carry the address, lease, gateway and DNS server.','No DHCP ACK means no address — check for Offers first.'],V+'diagram-dhcp-dora.png','Discover, Offer, Request, ACK','DHCP'))
_add(9, 'How DNS Works',
 ('text_image','DNS in the Lab Capture',['ARP first, then three DNS transactions to the resolver.','0x0066 returns NXDOMAIN in 20 ms — a fast, definite “no”.','0x0067 takes 800 ms — slow, but successful.'],V+'ladder-arp-dns.png','Frames 1–8 of the lab capture','DNS EVIDENCE'),
 ('shot',V+'chart-dns-time.png','Measuring DNS Response Time','dns.time on each response: a failing name and a slow name are different problems','DNS TIMING'),
 ('tiles','DNS Record Types You Will See',[('A / AAAA','IPv4 / IPv6 address'),('CNAME','Alias to another name'),('MX','Mail server'),('NS','Authoritative name server'),('PTR','Reverse lookup (address → name)'),('TXT','Text, e.g. SPF or verification')],'DNS'))
_add(10, 'ARP in Practice',
 ('two_col','The Ethernet II Frame','Fields',['Destination MAC (6 B)','Source MAC (6 B)','EtherType (2 B)','Payload, then FCS (4 B, rarely captured)'],'Values to recognise',['ff:ff:ff:ff:ff:ff — broadcast','01:00:5e:… — IPv4 multicast','0x0800 IPv4 · 0x0806 ARP','0x86DD IPv6 · 0x8100 VLAN tag'],'LAYER 2'))
_add(10, 'ARP Problems to Recognise',
 ('content','Spotting ARP Spoofing — Carefully',['arp.duplicate-address-detected flags one IP seen with two MACs.','A flood of gratuitous replies (arp.isgratuitous) is suspicious.','Legitimate causes exist: failover, VRRP, a replaced NIC.','Corroborate with switch CAM tables before calling it an attack.'],'SECURITY'))
_add(11, 'IPv4 Filters and Checks',
 ('two_col','IPv4 vs IPv6 at a Glance','IPv4',['20-byte header (with options: more)','TTL limits hops','ARP resolves MAC addresses','Routers may fragment','Filter: ip, icmp'],'IPv6',['Fixed 40-byte header + extension headers','Hop Limit replaces TTL','Neighbor Discovery (ICMPv6 135/136)','Only the source fragments','Filter: ipv6, icmpv6'],'IPV6'))
_add(12, 'ICMP Messages to Know',
 ('text_image','Echo, Refusal and Reset in the Lab Capture',['Three echo pairs, 30 ms each — the host is reachable.','UDP to port 9999 → ICMP Type 3 Code 3: nothing listening.','TCP SYN to port 81 → RST: the TCP equivalent of “closed”.'],V+'ladder-icmp-udp.png','Frames 9–16 and 55–56','ICMP EVIDENCE'),
 ('content','Traceroute and TTL Exceeded',['Traceroute sends probes with TTL 1, 2, 3 …','Each router that drops a probe returns ICMP Type 11 (Time Exceeded).','Filter icmp.type == 11 to list the hops.','Windows uses ICMP probes; Linux/macOS use UDP by default.'],'ICMP'))
_add(13, 'Analysing UDP',
 ('tiles','UDP Services You Will Meet',[('DNS · 53','Name resolution'),('DHCP · 67/68','Address assignment'),('NTP · 123','Time synchronisation'),('SNMP · 161/162','Device monitoring'),('Syslog · 514','Log forwarding'),('QUIC · 443','HTTP/3 transport')],'UDP'))
_add(14, 'Retransmissions',
 ('text_image','Retransmission and Zero Window in Stream 3',['The server sends the HTTP 500 at 2.270 s.','No ACK arrives — the same bytes are resent 1.000 s later.','The client then advertises Win=0: its buffer is full.','Finally FIN/ACK closes the stream.'],V+'ladder-retrans.png','TCP stream 3 from the lab capture','TCP EVIDENCE'),
 ('content','Closing a Connection',['FIN/ACK from each side is an orderly close (four-way, often three packets).','RST aborts immediately — refused port, crash or firewall.','A RST straight after a SYN means nothing is listening on that port.','Long gaps before FIN usually mean idle timeouts.'],'TEARDOWN'))
_add(15, 'Time/Sequence (Stevens) Graph',
 ('shot',V+'chart-stevens.png','Stevens Graph of the Stalled Transfer','Drawn from stream 3 of the lab capture: the same bytes appear twice, then the zero window follows','GRAPHS'))
_add(16, 'HTTP/1.1 vs HTTP/2',
 ('content','Export Objects — and Prove What You Exported',['File > Export Objects > HTTP saves every transferred object.','Hash each file (shasum -a 256 <file>) and record the hash in your report.','Never open or run exported files on your workstation.','TShark: tshark -r file -q --export-objects http,outputs/objects'],'EVIDENCE HANDLING'),
 ('two_col','HTTP/3 and QUIC','What changes',['HTTP/3 runs over QUIC on UDP 443','QUIC encrypts almost all transport headers','Connection IDs replace the 4-tuple'],'What you can still see',['Filter: quic','Initial packets and SNI (with care)','Full decryption needs the key log, as with TLS'],'MODERN WEB'))
_add(17, 'TLS Handshake Evidence',
 ('text_image','TLS 1.2 Handshake in the Lab Capture',['TCP handshake, then Client Hello with SNI portal.example.test.','Server Hello, Certificate and key exchange; both sides send Finished.','With lab-tls.keys loaded, GET /health and 200 OK appear as HTTP.'],V+'ladder-tls.png','tls-session.pcap, decrypted view','TLS'))
_add(18, 'Writing the Incident Report',
 ('tiles','Security Patterns to Recognise',[('Port scan','Many SYNs to different ports, answered by RST'),('ARP spoofing','One IP, two MACs; gratuitous floods'),('DNS tunnelling','Very long or random query names'),('Cleartext credentials','http.authorization, ftp PASS, telnet'),('Beaconing','Regular small connections to one host'),('Unusual ports','Services where they should not be')],'SECURITY ANALYSIS'),
 ('content','Build and Use a Baseline',['Capture “normal” at known-good times: login, file copy, a web page.','Note protocols, top talkers, typical response times and packet sizes.','Compare a problem trace against the baseline, not against guesses.','Keep baselines with dates — networks change.'],'BASELINING'),
 ('tiles','Keep Learning',[('Wireshark User’s Guide','wireshark.org/docs'),('Sample captures','wiki.wireshark.org/SampleCaptures'),('Kurose & Ross Wireshark labs','gaia.cs.umass.edu/kurose_ross/wireshark.php'),('Ask Wireshark','ask.wireshark.org'),('SharkFest talks','youtube.com/@WireSharkFest'),('Wireshark Certified Analyst','wireshark.org/certifications')],'RESOURCES'))

# ------------------------------------------------------------------ v5.1 enrichment: per-lab TShark equivalent + optional extension
KR='J.F. Kurose and K.W. Ross, Wireshark Labs (gaia.cs.umass.edu/kurose_ross/wireshark.php)'
SC='Wireshark sample captures (wiki.wireshark.org/SampleCaptures)'
LAB_EXTENSIONS={
 1:('tshark -n -r data/branch-office.pcap -Y arp', f'Getting Started lab — capture your own short baseline on an authorised network and compare its protocol mix with this file. Source: {KR}.'),
 2:('tshark -D', f'Getting Started lab — list your interfaces and identify which one carries traffic before planning a capture. Source: {KR}.'),
 3:('tshark -n -r data/branch-office.pcap -Y dns -T fields -e frame.number -e ip.src -e ip.dst -e dns.qry.name', 'Export your C1123-Analyst profile folder and import it on a second machine; confirm the columns appear.'),
 4:('tshark -n -r data/branch-office.pcap -Y "http.response.code >= 400" -T fields -e frame.number -e http.response.code -e http.request_in -e http.time', f'HTTP lab — apply your LAB HTTP Error rule to the HTTP trace from the Kurose & Ross labs. Source: {KR}.'),
 5:('tshark -n -r data/branch-office.pcap -Y "tcp.stream == 1 && http.time" -T fields -e frame.number -e tcp.analysis.initial_rtt -e http.time', f'TCP lab — measure the initial RTT and response times in the TCP trace supplied with the Kurose & Ross labs. Source: {KR}.'),
 6:('tshark -n -r data/branch-office.pcap -q -z io,phs', f'Analyse a longer SIP/RTP call from the {SC} with Telephony > VoIP Calls.'),
 7:('tshark -n -r data/branch-office.pcap -Y "dns.flags.rcode == 3"', 'Rewrite two of your matrix filters with the set (in {…}) and matches operators and confirm the frame lists are unchanged.'),
 8:('tshark -n -r data/branch-office.pcap -Y "arp || dns.id == 0x0065 || tcp.stream == 0"', f'Ethernet and ARP lab — trace the dependency chain for a page you load on an authorised network. Source: {KR}.'),
 9:('tshark -n -r data/branch-office.pcap -Y "dns.flags.response == 1" -T fields -e dns.id -e dns.qry.name -e dns.flags.rcode -e dns.time', f'DNS lab — compare A, NS and MX lookups in the DNS trace from the Kurose & Ross labs. Source: {KR}.'),
 10:('tshark -n -r data/branch-office.pcap -Y arp -T fields -e arp.opcode -e arp.src.proto_ipv4 -e arp.src.hw_mac', f'Ethernet and ARP lab — read the ARP cache on your own machine (arp -a) and match it to captured replies. Source: {KR}.'),
 11:('tshark -n -r data/branch-office.pcap -Y "ip.dst == 224.0.0.1" -T fields -e eth.dst -e ip.dst -e ip.ttl', f'IP lab — study TTL and fragmentation in the traceroute trace from the Kurose & Ross labs. Source: {KR}.'),
 12:('tshark -n -r data/branch-office.pcap -Y icmp -T fields -e frame.number -e icmp.type -e icmp.code -e icmp.seq', f'ICMP lab — identify Time Exceeded (type 11) messages in the traceroute trace. Source: {KR}.'),
 13:('tshark -n -r data/branch-office.pcap -q -z follow,udp,ascii,3', f'UDP lab — examine UDP header fields and lengths in the UDP trace from the Kurose & Ross labs. Source: {KR}.'),
 14:('tshark -n -r data/branch-office.pcap -q -z expert', f'TCP lab — find retransmissions and window behaviour in a larger file transfer trace. Source: {KR}.'),
 15:('tshark -n -r data/branch-office.pcap -q -z "io,stat,1,tcp.analysis.retransmission,tcp.analysis.zero_window"', f'TCP lab — draw the Stevens graph of the file upload trace and estimate throughput. Source: {KR}.'),
 16:('tshark -n -r data/branch-office.pcap -q --export-objects http,outputs/objects', f'HTTP lab — compare conditional GET (304) behaviour in the HTTP traces. Hash every exported object with shasum -a 256. Source: {KR}.'),
 17:('tshark -n -r data/tls-session.pcap -o tls.keylog_file:data/lab-tls.keys -Y http', f'TLS lab — identify the handshake records and cipher suite in the TLS trace from the Kurose & Ross labs. Source: {KR}.'),
 18:('tshark -n -r data/branch-office.pcap -q -z conv,tcp', f'Write a second incident report from a capture in the {SC}, using the same template and checklist.'),
}

SOURCES=[('Wireshark — Learn','https://www.wireshark.org/learn'),
 ('Kurose & Ross — Wireshark Labs (v9.0)','https://gaia.cs.umass.edu/kurose_ross/wireshark.php'),
 ('UMass — Wireshark lab files','https://gaia.cs.umass.edu/wireshark-labs/'),
 ('Cyber Defence Kit — Wireshark hands-on labs','https://docs.cyberdefencekit.org/wireshark/hands-on-labs.html'),
 ('LabEx — Wireshark tutorials','https://labex.io/tutorials/category/wireshark'),
 ('LabEx — Wireshark skill tree','https://labex.io/classroom/skilltrees/wireshark'),
 ('LabEx — learn-wireshark (GitHub)','https://github.com/labex-labs/learn-wireshark'),
 ('Wireshark.com — Learn','https://wireshark.com/learn/'),
 ('101 Labs — Wireshark WCNA','https://www.101labs.net/courses/101-labs-wireshark-wcna/'),
 ('WPI CS3516 — Wireshark lab 1','https://web.cs.wpi.edu/~cs3516/b09/wireshark/wire1/'),
 ('Wireshark sample captures','https://wiki.wireshark.org/SampleCaptures')]
