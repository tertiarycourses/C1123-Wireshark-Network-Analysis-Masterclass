# Wireshark Network Analysis Masterclass

Learn to turn packet captures into evidence for network and application troubleshooting.

| Course detail | Information |
|---|---|
| Course code | `C1123` |
| Programme | Non-WSQ commercial short course |
| Duration | 4 days / 30 instructional hours |
| Registration | [View course details and register](https://www.tertiarycourses.com.sg/wireshark-network-analysis-masterclass.html) |
| Current version | v5.1 — 5 October 2026 |

## About the course

Practise capture planning, reproducible profiles, packet navigation, protocol diagnosis, timing, graphs and incident reporting with Wireshark. The course uses a fictional branch-office scenario and supplied synthetic captures, so the new labs work without external trace downloads.

## Learning outcomes

- Plan scoped captures and configure an analyst profile.
- Navigate, filter, summarize and time network exchanges.
- Interpret DNS, ARP, IPv4, ICMP and UDP evidence.
- Diagnose TCP and application behaviour, including HTTP and authorised TLS inspection.
- Report facts, hypotheses and next actions with reproducible evidence.

## Topics covered

1. Introduction to Network Analysis and Wireshark
2. Capture Methods and Capture Filters
3. Global Preferences and Troubleshooting Profiles
4. Navigation and Coloring Techniques
5. Time Values and Delay Types
6. Trace Statistics and VoIP Overview
7. Display Filters
8. TCP/IP Communications and Resolution
9. DNS Traffic Analysis
10. ARP Traffic Analysis
11. IPv4 Traffic Analysis
12. ICMP Traffic Analysis
13. UDP Traffic Analysis
14. TCP Protocol Analysis
15. Traffic Graphs
16. HTTP and HTTP/2 Analysis
17. TLS-Encrypted Traffic Analysis
18. Ten Troubleshooting Steps and Reporting

## Labs

Each lab folder contains its own step-by-step instructions in **Markdown and PDF** (`LAB-NN-Instructions.md` / `.pdf`). It also has a scenario ticket, the supplied captures, the expected-evidence image, templates, a findings sheet, verification and export scripts, and a TShark equivalent for the lab.

- [Lab 01: Establish a trace baseline](labs/lab-01-establish-a-trace-baseline/README.md)
- [Lab 02: Plan capture placement](labs/lab-02-plan-capture-placement/README.md)
- [Lab 03: Create an analyst profile](labs/lab-03-create-an-analyst-profile/README.md)
- [Lab 04: Color and annotate evidence](labs/lab-04-color-and-annotate-evidence/README.md)
- [Lab 05: Separate path and server delay](labs/lab-05-separate-path-and-server-delay/README.md)
- [Lab 06: Summarize traffic and a voice stream](labs/lab-06-summarize-traffic-and-a-voice-stream/README.md)
- [Lab 07: Build a filter evidence matrix](labs/lab-07-build-a-filter-evidence-matrix/README.md)
- [Lab 08: Reconstruct an application dependency chain](labs/lab-08-reconstruct-an-application-dependency-chain/README.md)
- [Lab 09: Diagnose DNS failure and delay](labs/lab-09-diagnose-dns-failure-and-delay/README.md)
- [Lab 10: Verify link-local resolution](labs/lab-10-verify-link-local-resolution/README.md)
- [Lab 11: Classify IPv4 scope and headers](labs/lab-11-classify-ipv4-scope-and-headers/README.md)
- [Lab 12: Interpret echo and unreachable messages](labs/lab-12-interpret-echo-and-unreachable-messages/README.md)
- [Lab 13: Follow datagrams and service refusal](labs/lab-13-follow-datagrams-and-service-refusal/README.md)
- [Lab 14: Investigate retransmission and zero window](labs/lab-14-investigate-retransmission-and-zero-window/README.md)
- [Lab 15: Graph bytes, RTT and recovery](labs/lab-15-graph-bytes-rtt-and-recovery/README.md)
- [Lab 16: Inspect HTTP outcomes and HTTP/2 frames](labs/lab-16-inspect-http-outcomes-and-http-2-frames/README.md)
- [Lab 17: Compare encrypted and decrypted views](labs/lab-17-compare-encrypted-and-decrypted-views/README.md)
- [Lab 18: Produce an evidence-led incident report](labs/lab-18-produce-an-evidence-led-incident-report/README.md)

## Public package

- [LG-Wireshark Network Analysis Masterclass (C1123).docx](courseware/LG-Wireshark%20Network%20Analysis%20Masterclass%20%28C1123%29.docx)
- [LG-Wireshark Network Analysis Masterclass (C1123).pdf](courseware/LG-Wireshark%20Network%20Analysis%20Masterclass%20%28C1123%29.pdf)
- [LP-Wireshark Network Analysis Masterclass (C1123).docx](courseware/LP-Wireshark%20Network%20Analysis%20Masterclass%20%28C1123%29.docx)
- [LP-Wireshark Network Analysis Masterclass (C1123).pdf](courseware/LP-Wireshark%20Network%20Analysis%20Masterclass%20%28C1123%29.pdf)
- [Wireshark Network Analysis Masterclass (C1123)-v5.1.pdf](courseware/Wireshark%20Network%20Analysis%20Masterclass%20%28C1123%29-v5.1.pdf)
- [Wireshark Network Analysis Masterclass (C1123)-v5.1.pptx](courseware/Wireshark%20Network%20Analysis%20Masterclass%20%28C1123%29-v5.1.pptx)
- [Learner Guide Markdown](LG-Wireshark%20Network%20Analysis%20Masterclass%20%28C1123%29.md)
- [All lab activities](labs/README.md)

## Using the package

Start with the Learner Guide or a lab README. Wireshark 4.6 or later is recommended. TShark and Python 3 enable the fixture checks and CSV export scripts. Scapy and OpenSSL are only required when regenerating mock captures. On Windows, use `py -3` in place of `python3` and add the Wireshark installation directory to PATH.

Version 5.1 slides explain each concept in detail with visuals: ladder diagrams, timing charts and I/O and Stevens graphs drawn from the labs' own captures, plus the original course diagrams. For each lab, the slides show only the scenario and a four-task summary. The full steps are in the Learner Guide and in each lab's instruction files. Content on DHCP, NAT, IPv6, TShark, evidence hashing, HTTP/3/QUIC and security analysis draws on the sources listed in [labs/README.md](labs/README.md#further-learning).

## Public and private distribution

The current PPT/PDF, LP DOCX/PDF, LG DOCX/PDF/Markdown and the whole lab tree are public. `reference/` and `assessment/` are private and excluded. Credentials, dependencies and superseded archives are excluded. The TLS key logs are intentionally shared synthetic session material for the supplied lab captures; they are not production credentials.

## Build and provenance

[Build notes](BUILD.md) describe the source and rendering pipeline. Reusable diagrams were cropped from the private original deck into [courseware/assets/reference-diagrams](courseware/assets/reference-diagrams/). The per-lab evidence figures in [courseware/assets/screenshots](courseware/assets/screenshots/) are generated with TShark by `scripts/build_evidence_visuals.py`. [Image generation prompts](courseware/assets/image-prompts.md) record the generated illustration specifications.

Provided by **Tertiary Infotech Academy Pte Ltd**, Singapore.
