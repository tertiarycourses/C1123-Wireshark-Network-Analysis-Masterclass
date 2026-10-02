# Lab 14 — Investigate retransmission and zero window

C1123 | v4.0 | 45 minutes

## Goal

Sequence numbers count bytes; ACK numbers indicate the next expected byte.

## What you will build

A packet evidence table and written findings for investigate retransmission and zero window.

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

### 2. Open data/branch-office.pcap. Apply tcp.stream == 3. Open Analyze > Expert Information and note the repeated server segment.

### 3. Apply tcp.analysis.retransmission and expand TCP. Compare the same sequence range and payload in the earlier segment; the repeat occurs 1.000 second later.

### 4. Apply tcp.window_size_value == 0. Confirm the client ACK advertises zero receive window in stream 3. Examine the SYN options: window scaling is negotiated, but zero remains zero.

### 5. Apply tcp.flags.reset == 1. Identify the port 81 refusal. Complete assets/tcp-evidence.csv with stream, frame, flag/analysis, measured interval and a limitation. Discuss SACK, fast recovery and out-of-order evidence without claiming those events occur in this fixture.

### 6. Export a reproducible packet table. Record the filter, frame numbers, measurement, explanation and limitation in outputs/findings.md.

```bash
python3 scripts/export_evidence.py
```

## Test it

The supplied tcp.analysis.retransmission expression matches 1 frame(s) in the specified capture. Run scripts/verify.py and compare the listed frame numbers. Keep your findings and exported table in outputs/. Explain the observed result rather than only copying a count.

## Troubleshooting

TShark not found: install Wireshark CLI tools and add the installation folder to PATH; on Windows use the Wireshark install directory. A filter returns zero: clear other filters, use the specified capture, and check the expression is in the display toolbar. TLS remains opaque: select the matching lab-tls.keys file by absolute path, reload, and remove a key-log preference from another lab.

## Challenge

Create a second filter that answers the same question, then identify one packet it includes or excludes differently. Support your explanation with a frame number.

## Reflection

What additional observation would turn your leading hypothesis into a stronger conclusion?

## Reset and regeneration

Keep the supplied captures for the core lab. Optional regeneration requires `python3 -m pip install -r requirements.txt` and OpenSSL, then `python3 scripts/generate_data.py`. Do not send packets or capture an unauthorised interface. Clear TLS key-log preferences after the exercise.
