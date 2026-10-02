# Independent QA — C1123 Wireshark Network Analysis Masterclass v4.0

Scope: requested C1123 repository only. No repository artifacts edited by reviewer. Review uses non-wsq-courseware-qa skill and direct artifact/readback checks.

## Current disposition

FINAL PASS. No outstanding findings after final recheck. Completeness, prohibited-content scan, topic/lab alignment, duration totals, fixture execution, document integrity and changed PPT visuals pass.

## Final recheck: remediated medium findings

- **Medium — ambiguous handshake measurement.** `labs/lab-05-separate-path-and-server-delay/README.md:33,39`, `labs/lab-15-graph-bytes-rtt-and-recovery/README.md:37`, mirrored LG/topic source: the text calls 30 ms the handshake and points to `tcp.analysis.initial_rtt` in SYN/ACK. TShark reads SYN frame27=1.180s, SYN/ACK frame28=1.210s, final ACK frame29=1.220s; `tcp.analysis.initial_rtt` is .040 on frame29. Corrected and verified in Labs05/15 and regenerated LG: explicitly distinguishes 30 ms SYN-to-SYN/ACK interval from 40 ms complete three-way handshake/initial RTT and inspects the field on final ACK.
- **Medium — orphaned topic introductory block.** `courseware/LG-Wireshark Network Analysis Masterclass (C1123).pdf` pp8–9 (Topic03), pp14–15 (Topic07): heading and short subtitle sit at bottom of first page while key concepts begin next page. Corrected and verified: Topic03 now starts p9 and Topic07 starts p15, each heading/subtitle/key concepts block remains together. No clipping or missing text.

## Remediated findings, independently verified

- **High:** earlier 195-slide deck slide87 explicitly taught obsolete any-not-equal semantics. Removed obsolete warning sequence; final188-slide deck retains current all-not-equal guidance.
- **High:** old195-slide deck slides182–183 extended question text beyond right edge. Removed legacy questions; final188-page PDF has zero text spans outside page boundaries.
- **Medium:** legacy inherited copyright footer overlapped the new course footer. Final PDF contains zero legacy `This material belongs to` strings.
- **Medium:** LP daily metadata 09:30–18:30 contradicted tables09:00–18:00. Final all four tables match09:30–18:30.

## Verification evidence

- Actual final package: PPTX188slides/PDF188pages; LP DOCX/PDF7pages; LG DOCX/PDF33pages; root LG Markdown;18 contiguous self-contained lab folders.
- Prohibited scan:132artifacts,0hits,exit0 (reference/archive excluded by official scanner). No prohibited programme language in learner/trainer deliverables.
- PPT/LG/LP/labs all identify C1123/v4.0 and align18 topics with Labs01–18. LG maps each lab to a learning outcome; LP lab reference table covers all18. No other C/TGS course-code contamination in lab Markdown.
- LP each day:540 elapsed minutes=450 instructional+30tea+60lunch. Four days=1800 instructional minutes=30hours. Core lab work plus completion blocks allocate180/225/225/240minutes, matching lab README totals45×15+60+60+75=870minutes.
- Each of18lab folders includes its own README, requirements, captures, synthetic TLS session material, scripts, templates and checkpoints. Checkpoints allow restarting from supplied capture without previous lab outputs. Local lab index links all resolve; lab15 name has no comma.
- All18 fixture verification scripts run successfully against included captures. All54Python lab scripts compile without writing files. TLS checks confirm1ClientHello,0HTTP requests without secrets,1request/1HTTP200 with synthetic matching session secrets. RTP sequence100,101,103,104; DNS response times.020,.020,.800s; request/response delay.760s; retransmission and zero window filters identify frames51/52.
- TShark verifies current != semantics: ip.addr!=192.0.2.53 excludes six DNS packets and missing-ip-field ARP packets; !(ip.addr==192.0.2.53) additionally retains ARP. This is useful evidence for lab comparison.
- LG all41TOC entries point to actual final pages. LG/LP version-control records include4.0 dated2October2026. No blank pages or off-page PDF text in LG/LP. Covers, all LP pages, all LG pages and PPT cover/admin/each topic/new practical/closing slides inspected via rendered contact sheets. Current188-page PPT has zero off-page spans.
- PDF render evidence in `/tmp/c1123-qa/`; original screenshots preserve proof of remediated findings.

Limit: no exhaustive live GUI walkthrough on Windows/macOS and no assessment of external publication state. Supplied secrets are deliberate offline synthetic lab session material, not real credentials.

## Final changed-visual verification

Rendered final188-page PPT inspected slides21/87/121/179 (topic introductions02/08/14/17): added OpenAI-generated packet-analysis illustration fits beside explanatory text with readable caption, clean margins and no overlap. Final PDF boundary scan: zero off-page spans in all threePDFs (deck188pages, LG33pages, LP7pages). Final prohibited scan132artifacts/0hits; all41LGTOC entries match final33-page PDF. Previously observed handshake and orphan-heading findings resolved.
