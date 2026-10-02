# Lab 01 — Establish a trace baseline

C1123 | v4.0 | 45 minutes

## Goal

A capture is a measurement at one observation point, not a complete network history.

## What you will build

A packet evidence table and written findings for establish a trace baseline.

## Prerequisites

Wireshark 4.6 or later, Python 3 for optional scripts, TShark CLI tools. No earlier lab required.

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

### 2. Open data/branch-office.pcap with File > Open. Clear the display filter. Record the packet count from the status bar and the capture duration from Statistics > Capture File Properties.

### 3. Select frame 1. Expand Ethernet II and Address Resolution Protocol in Packet Details. Click the sender IP field and observe the corresponding bytes.

### 4. Apply arp in the display filter toolbar. Compare request and reply sender/target IP and MAC addresses. Save the two frame numbers in outputs/findings.md.

### 5. Export a reproducible packet table. Record the filter, frame numbers, measurement, explanation and limitation in outputs/findings.md.

```bash
python3 scripts/export_evidence.py
```

## Test it

The supplied arp expression matches 2 frame(s) in the specified capture. Run scripts/verify.py and compare the listed frame numbers. Keep your findings and exported table in outputs/. Explain the observed result rather than only copying a count.

## Troubleshooting

TShark not found: install Wireshark CLI tools and add the installation folder to PATH; on Windows use the Wireshark install directory. A filter returns zero: clear other filters, use the specified capture, and check the expression is in the display toolbar. TLS remains opaque: select the matching lab-tls.keys file by absolute path, reload, and remove a key-log preference from another lab.

## Challenge

Create a second filter that answers the same question, then identify one packet it includes or excludes differently. Support your explanation with a frame number.

## Reflection

What additional observation would turn your leading hypothesis into a stronger conclusion?

## Reset and regeneration

Keep the supplied captures for the core lab. Optional regeneration requires `python3 -m pip install -r requirements.txt` and OpenSSL, then `python3 scripts/generate_data.py`. Do not send packets or capture an unauthorised interface. Clear TLS key-log preferences after the exercise.
