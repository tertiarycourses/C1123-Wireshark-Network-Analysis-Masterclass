# Lab 15 — Graph bytes, RTT and recovery

C1123 | v4.0 | 45 minutes

## Goal

An I/O graph bins observed events; units and interval determine what it means.

## What you will build

A packet evidence table and written findings for graph bytes, rtt and recovery.

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

### 2. Open data/branch-office.pcap. Select a packet in TCP stream 3. Open Statistics > TCP Stream Graphs > Time Sequence (Stevens) and inspect the repeated server sequence.

### 3. Open Statistics > I/O Graphs. Add a retransmission graph with filter tcp.analysis.retransmission and a zero-window graph with filter tcp.analysis.zero_window. Use packets and a 1 second interval; record their event bins.

### 4. Open TCP Stream Graphs > Round Trip Time. Compare eligible ACK samples with the 30 ms SYN-to-SYN/ACK interval and the 40 ms complete handshake/initial_rtt on the final ACK. Explain why no ACK sample exists for an unacknowledged segment before its repeat.

### 5. Run the report script to export timestamps and byte lengths, then write outputs/graph-notes.md with interval, unit, stream, visible pattern and limitation. Do not use SUM(tcp.seq) as throughput.

### 6. Export a reproducible packet table. Record the filter, frame numbers, measurement, explanation and limitation in outputs/findings.md.

```bash
python3 scripts/export_evidence.py
```

## Test it

The supplied tcp.analysis.retransmission || tcp.analysis.zero_window expression matches 2 frame(s) in the specified capture. Run scripts/verify.py and compare the listed frame numbers. Keep your findings and exported table in outputs/. Explain the observed result rather than only copying a count.

## Troubleshooting

TShark not found: install Wireshark CLI tools and add the installation folder to PATH; on Windows use the Wireshark install directory. A filter returns zero: clear other filters, use the specified capture, and check the expression is in the display toolbar. TLS remains opaque: select the matching lab-tls.keys file by absolute path, reload, and remove a key-log preference from another lab.

## Challenge

Create a second filter that answers the same question, then identify one packet it includes or excludes differently. Support your explanation with a frame number.

## Reflection

What additional observation would turn your leading hypothesis into a stronger conclusion?

## Reset and regeneration

Keep the supplied captures for the core lab. Optional regeneration requires `python3 -m pip install -r requirements.txt` and OpenSSL, then `python3 scripts/generate_data.py`. Do not send packets or capture an unauthorised interface. Clear TLS key-log preferences after the exercise.
