# Lab 02 — Plan capture placement

C1123 | v4.0 | 45 minutes

## Goal

A switched access port normally observes its own traffic and broadcasts; SPAN or TAP placement changes visibility.

## What you will build

A packet evidence table and written findings for plan capture placement.

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

### 2. Open assets/topology.md. Draw a sensor on the client access port, on a mirrored uplink and beside the server. State which traffic each sees.

### 3. Open Capture > Options and inspect the interface list without starting a capture. Enter tcp port 80 in the capture-filter box and check syntax feedback. Cancel the dialog.

### 4. Open data/branch-office.pcap. Enter tcp.port == 80 in the DISPLAY toolbar. Compare the stored total with the displayed total; explain why clearing it restores hidden packets.

### 5. Complete assets/capture-plan.md with scope, interface, duration, ring-buffer limit and permission owner. Wireless monitor mode requires compatible adapter/driver; USB capture requires platform-specific support. Remote capture should use authorised SSH/extcap, not obsolete unauthenticated RPC instructions.

### 6. Export a reproducible packet table. Record the filter, frame numbers, measurement, explanation and limitation in outputs/findings.md.

```bash
python3 scripts/export_evidence.py
```

## Test it

The supplied tcp.port == 80 expression matches 37 frame(s) in the specified capture. Run scripts/verify.py and compare the listed frame numbers. Keep your findings and exported table in outputs/. Explain the observed result rather than only copying a count.

## Troubleshooting

TShark not found: install Wireshark CLI tools and add the installation folder to PATH; on Windows use the Wireshark install directory. A filter returns zero: clear other filters, use the specified capture, and check the expression is in the display toolbar. TLS remains opaque: select the matching lab-tls.keys file by absolute path, reload, and remove a key-log preference from another lab.

## Challenge

Create a second filter that answers the same question, then identify one packet it includes or excludes differently. Support your explanation with a frame number.

## Reflection

What additional observation would turn your leading hypothesis into a stronger conclusion?

## Reset and regeneration

Keep the supplied captures for the core lab. Optional regeneration requires `python3 -m pip install -r requirements.txt` and OpenSSL, then `python3 scripts/generate_data.py`. Do not send packets or capture an unauthorised interface. Clear TLS key-log preferences after the exercise.
