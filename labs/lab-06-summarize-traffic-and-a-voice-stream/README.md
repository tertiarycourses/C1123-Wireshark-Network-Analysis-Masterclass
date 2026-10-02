# Lab 06 — Summarize traffic and a voice stream

C1123 | v4.0 | 45 minutes

## Goal

Protocol Hierarchy shows captured composition; byte share differs from packet share.

## What you will build

A packet evidence table and written findings for summarize traffic and a voice stream.

## Prerequisites

Wireshark 4.6 or later, Python 3 for optional scripts, TShark CLI tools. Complete earlier navigation/filter labs; all data is included here so you can rejoin independently.

## Files

- data/: offline captures and synthetic TLS session secrets
- scripts/: generation, fixture verification and CSV export
- assets/: topology, observation templates and checks
- checkpoints/: rejoin instructions
- outputs/: your saved evidence

## Steps

### 1. Prepare your lab workspace. Open this lab folder in a terminal. Windows uses py -3 in place of python3. Wireshark GUI alone is sufficient for the investigation; CLI scripts require TShark on PATH. Run the fixture verification first.

```bash
python3 scripts/verify.py
```

### 2. Open data/branch-office.pcap. Open Statistics > Protocol Hierarchy, then Statistics > Conversations. Sort TCP conversations by bytes; save the largest conversation details.

### 3. Open Statistics > I/O Graphs. Create an all-traffic graph with a 1 second interval and Bits as the unit. Record peak interval and explain the difference between observed bits and usable application throughput.

### 4. Apply sip and open Telephony > VoIP Calls or SIP Flows. Identify the INVITE and 200 OK. This minimal synthetic exchange is signalling evidence, not a complete production call.

### 5. Apply udp.port == 4002. Use Analyze > Decode As to decode this UDP port as RTP. Open Telephony > RTP > RTP Streams, select the stream and Analyze. Record sequence numbers 100, 101, 103, 104; the missing sequence is 102.

### 6. Export a reproducible packet table. Record the filter, frame numbers, measurement, explanation and limitation in outputs/findings.md.

```bash
python3 scripts/export_evidence.py
```

## Test it

The supplied sip expression matches 2 frame(s) in the specified capture. Run scripts/verify.py and compare the listed frame numbers. Keep your findings and exported table in outputs/. Explain the observed result rather than only copying a count.

## Troubleshooting

TShark not found: install Wireshark CLI tools and add the installation folder to PATH; on Windows use the Wireshark install directory. A filter returns zero: clear other filters, use the specified capture, and check the expression is in the display toolbar. TLS remains opaque: select the matching lab-tls.keys file by absolute path, reload, and remove a key-log preference from another lab.

## Challenge

Create a second filter that answers the same question, then identify one packet it includes or excludes differently. Support your explanation with a frame number.

## Reflection

What additional observation would turn your leading hypothesis into a stronger conclusion?

## Reset and regeneration

Keep the supplied captures for the core lab. Optional regeneration requires `python3 -m pip install -r requirements.txt` and OpenSSL, then `python3 scripts/generate_data.py`. Do not send packets or capture an unauthorised interface. Clear TLS key-log preferences after the exercise.
