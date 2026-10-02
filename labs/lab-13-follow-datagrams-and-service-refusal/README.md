# Lab 13 — Follow datagrams and service refusal

C1123 | v4.0 | 45 minutes

## Goal

UDP has no transport handshake or retransmission; the application may provide reliability.

## What you will build

A packet evidence table and written findings for follow datagrams and service refusal.

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

### 2. Open data/branch-office.pcap. Apply udp.dstport == 9999. One frame is the original datagram and one is the UDP header quoted inside ICMP; inspect the outer protocol to distinguish them.

### 3. Select the original datagram and use Analyze > Follow > UDP Stream. Confirm the payload LAB-UDP. Save a text view to outputs/udp-stream.txt.

### 4. Apply udp.port == 4002 and decode RTP using Analyze > Decode As. Compare datagram framing with the earlier TCP stream.

### 5. Record why no UDP transport ACK exists in the trace. Use the ICMP refusal to explain why an application can fail even though a datagram was transmitted.

### 6. Export a reproducible packet table. Record the filter, frame numbers, measurement, explanation and limitation in outputs/findings.md.

```bash
python3 scripts/export_evidence.py
```

## Test it

The supplied udp.dstport == 9999 expression matches 2 frame(s) in the specified capture. Run scripts/verify.py and compare the listed frame numbers. Keep your findings and exported table in outputs/. Explain the observed result rather than only copying a count.

## Troubleshooting

TShark not found: install Wireshark CLI tools and add the installation folder to PATH; on Windows use the Wireshark install directory. A filter returns zero: clear other filters, use the specified capture, and check the expression is in the display toolbar. TLS remains opaque: select the matching lab-tls.keys file by absolute path, reload, and remove a key-log preference from another lab.

## Challenge

Create a second filter that answers the same question, then identify one packet it includes or excludes differently. Support your explanation with a frame number.

## Reflection

What additional observation would turn your leading hypothesis into a stronger conclusion?

## Reset and regeneration

Keep the supplied captures for the core lab. Optional regeneration requires `python3 -m pip install -r requirements.txt` and OpenSSL, then `python3 scripts/generate_data.py`. Do not send packets or capture an unauthorised interface. Clear TLS key-log preferences after the exercise.
