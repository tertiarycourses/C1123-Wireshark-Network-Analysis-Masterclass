# Labs — Wireshark Network Analysis Masterclass

**Course code:** C1123  |  **Version v5.1 · 5 October 2026**

All 18 labs use the same fictional branch office and supplied synthetic captures — no live network access is needed. Each lab folder is self-contained.

Every folder holds `LAB-NN-Instructions.md` and `LAB-NN-Instructions.pdf` (full steps), a scenario ticket, the expected evidence, templates, a findings sheet and the verification scripts.

| Topic | Lab | Activity | Instructions | You produce |
|---|---:|---|---|---|
| 01 | 01 | [Establish a trace baseline](lab-01-establish-a-trace-baseline/README.md) | [MD](lab-01-establish-a-trace-baseline/LAB-01-Instructions.md) · [PDF](lab-01-establish-a-trace-baseline/LAB-01-Instructions.pdf) | A baseline record of the capture and the ARP exchange |
| 02 | 02 | [Plan capture placement](lab-02-plan-capture-placement/README.md) | [MD](lab-02-plan-capture-placement/LAB-02-Instructions.md) · [PDF](lab-02-plan-capture-placement/LAB-02-Instructions.pdf) | A completed capture plan with sensor placement and limits |
| 03 | 03 | [Create an analyst profile](lab-03-create-an-analyst-profile/README.md) | [MD](lab-03-create-an-analyst-profile/LAB-03-Instructions.md) · [PDF](lab-03-create-an-analyst-profile/LAB-03-Instructions.pdf) | A reusable C1123-Analyst profile and its folder path |
| 04 | 04 | [Color and annotate evidence](lab-04-color-and-annotate-evidence/README.md) | [MD](lab-04-color-and-annotate-evidence/LAB-04-Instructions.md) · [PDF](lab-04-color-and-annotate-evidence/LAB-04-Instructions.pdf) | An annotated pcapng with a comment on the failing response |
| 05 | 05 | [Separate path and server delay](lab-05-separate-path-and-server-delay/README.md) | [MD](lab-05-separate-path-and-server-delay/LAB-05-Instructions.md) · [PDF](lab-05-separate-path-and-server-delay/LAB-05-Instructions.pdf) | Timing evidence separating path delay from server delay |
| 06 | 06 | [Summarize traffic and a voice stream](lab-06-summarize-traffic-and-a-voice-stream/README.md) | [MD](lab-06-summarize-traffic-and-a-voice-stream/LAB-06-Instructions.md) · [PDF](lab-06-summarize-traffic-and-a-voice-stream/LAB-06-Instructions.pdf) | A traffic summary and RTP loss evidence |
| 07 | 07 | [Build a filter evidence matrix](lab-07-build-a-filter-evidence-matrix/README.md) | [MD](lab-07-build-a-filter-evidence-matrix/LAB-07-Instructions.md) · [PDF](lab-07-build-a-filter-evidence-matrix/LAB-07-Instructions.pdf) | A filter evidence matrix with verified frame numbers |
| 08 | 08 | [Reconstruct an application dependency chain](lab-08-reconstruct-an-application-dependency-chain/README.md) | [MD](lab-08-reconstruct-an-application-dependency-chain/LAB-08-Instructions.md) · [PDF](lab-08-reconstruct-an-application-dependency-chain/LAB-08-Instructions.pdf) | A completed dependency map with frame ranges |
| 09 | 09 | [Diagnose DNS failure and delay](lab-09-diagnose-dns-failure-and-delay/README.md) | [MD](lab-09-diagnose-dns-failure-and-delay/LAB-09-Instructions.md) · [PDF](lab-09-diagnose-dns-failure-and-delay/LAB-09-Instructions.pdf) | A DNS observations sheet with measured intervals |
| 10 | 10 | [Verify link-local resolution](lab-10-verify-link-local-resolution/README.md) | [MD](lab-10-verify-link-local-resolution/LAB-10-Instructions.md) · [PDF](lab-10-verify-link-local-resolution/LAB-10-Instructions.pdf) | A verified ARP table entry and an evidence-based conclusion |
| 11 | 11 | [Classify IPv4 scope and headers](lab-11-classify-ipv4-scope-and-headers/README.md) | [MD](lab-11-classify-ipv4-scope-and-headers/LAB-11-Instructions.md) · [PDF](lab-11-classify-ipv4-scope-and-headers/LAB-11-Instructions.pdf) | A completed IPv4 header and scope sheet |
| 12 | 12 | [Interpret echo and unreachable messages](lab-12-interpret-echo-and-unreachable-messages/README.md) | [MD](lab-12-interpret-echo-and-unreachable-messages/LAB-12-Instructions.md) · [PDF](lab-12-interpret-echo-and-unreachable-messages/LAB-12-Instructions.pdf) | An ICMP event log explaining the service refusal |
| 13 | 13 | [Follow datagrams and service refusal](lab-13-follow-datagrams-and-service-refusal/README.md) | [MD](lab-13-follow-datagrams-and-service-refusal/LAB-13-Instructions.md) · [PDF](lab-13-follow-datagrams-and-service-refusal/LAB-13-Instructions.pdf) | A saved UDP stream and an explanation of the refusal |
| 14 | 14 | [Investigate retransmission and zero window](lab-14-investigate-retransmission-and-zero-window/README.md) | [MD](lab-14-investigate-retransmission-and-zero-window/LAB-14-Instructions.md) · [PDF](lab-14-investigate-retransmission-and-zero-window/LAB-14-Instructions.pdf) | A TCP evidence sheet for retransmission, zero window and reset |
| 15 | 15 | [Graph bytes, RTT and recovery](lab-15-graph-bytes-rtt-and-recovery/README.md) | [MD](lab-15-graph-bytes-rtt-and-recovery/LAB-15-Instructions.md) · [PDF](lab-15-graph-bytes-rtt-and-recovery/LAB-15-Instructions.pdf) | Graph notes with interval, unit, stream and limitation |
| 16 | 16 | [Inspect HTTP outcomes and HTTP/2 frames](lab-16-inspect-http-outcomes-and-http-2-frames/README.md) | [MD](lab-16-inspect-http-outcomes-and-http-2-frames/LAB-16-Instructions.md) · [PDF](lab-16-inspect-http-outcomes-and-http-2-frames/LAB-16-Instructions.pdf) | An HTTP outcome summary and an exported object |
| 17 | 17 | [Compare encrypted and decrypted views](lab-17-compare-encrypted-and-decrypted-views/README.md) | [MD](lab-17-compare-encrypted-and-decrypted-views/LAB-17-Instructions.md) · [PDF](lab-17-compare-encrypted-and-decrypted-views/LAB-17-Instructions.pdf) | A comparison of the encrypted and decrypted views |
| 18 | 18 | [Produce an evidence-led incident report](lab-18-produce-an-evidence-led-incident-report/README.md) | [MD](lab-18-produce-an-evidence-led-incident-report/LAB-18-Instructions.md) · [PDF](lab-18-produce-an-evidence-led-incident-report/LAB-18-Instructions.pdf) | An evidence-led incident report |

## Further learning

These sources informed the v5.1 labs and are recommended for extra practice. Kurose & Ross material is used with acknowledgement, as its terms require; no lab text is copied.

- [Wireshark — Learn](https://www.wireshark.org/learn)
- [Kurose & Ross — Wireshark Labs (v9.0)](https://gaia.cs.umass.edu/kurose_ross/wireshark.php)
- [UMass — Wireshark lab files](https://gaia.cs.umass.edu/wireshark-labs/)
- [Cyber Defence Kit — Wireshark hands-on labs](https://docs.cyberdefencekit.org/wireshark/hands-on-labs.html)
- [LabEx — Wireshark tutorials](https://labex.io/tutorials/category/wireshark)
- [LabEx — Wireshark skill tree](https://labex.io/classroom/skilltrees/wireshark)
- [LabEx — learn-wireshark (GitHub)](https://github.com/labex-labs/learn-wireshark)
- [Wireshark.com — Learn](https://wireshark.com/learn/)
- [101 Labs — Wireshark WCNA](https://www.101labs.net/courses/101-labs-wireshark-wcna/)
- [WPI CS3516 — Wireshark lab 1](https://web.cs.wpi.edu/~cs3516/b09/wireshark/wire1/)
- [Wireshark sample captures](https://wiki.wireshark.org/SampleCaptures)

Use only authorised data. The TLS key log in Lab 17 is synthetic session material for the supplied capture only.

---

*Wireshark Network Analysis Masterclass · C1123 · Version v5.1 · © 2026 Tertiary Infotech Academy Pte Ltd*
