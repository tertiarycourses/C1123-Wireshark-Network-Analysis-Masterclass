# Lab 07 — Build a filter evidence matrix

C1123 | v4.0 | 45 minutes

## Goal

Parentheses make mixed and/or expressions explicit.

## What you will build

A packet evidence table and written findings for build a filter evidence matrix.

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

### 2. Open data/branch-office.pcap. Apply dns.flags.rcode == 3 and record the returned response frame. Clear the filter and apply tcp.flags.syn == 1.

### 3. Compare (ip.src == 192.0.2.10 && udp.port == 53) || tcp.port == 80 with ip.src == 192.0.2.10 && (udp.port == 53 || tcp.port == 80). Record both counts and the direction excluded by the second expression.

### 4. Apply !(ip.addr == 192.0.2.53). Verify that DNS packets disappear; compare ip.addr != 192.0.2.53 on Wireshark 4.6 or later. Record the actual version and equality behaviour.

### 5. Save five useful filters in outputs/filters.txt. For each, state the question, filter and matching frame numbers; compile them with scripts/verify.py.

### 6. Export a reproducible packet table. Record the filter, frame numbers, measurement, explanation and limitation in outputs/findings.md.

```bash
python3 scripts/export_evidence.py
```

## Test it

The supplied dns.flags.rcode == 3 expression matches 1 frame(s) in the specified capture. Run scripts/verify.py and compare the listed frame numbers. Keep your findings and exported table in outputs/. Explain the observed result rather than only copying a count.

## Troubleshooting

TShark not found: install Wireshark CLI tools and add the installation folder to PATH; on Windows use the Wireshark install directory. A filter returns zero: clear other filters, use the specified capture, and check the expression is in the display toolbar. TLS remains opaque: select the matching lab-tls.keys file by absolute path, reload, and remove a key-log preference from another lab.

## Challenge

Create a second filter that answers the same question, then identify one packet it includes or excludes differently. Support your explanation with a frame number.

## Reflection

What additional observation would turn your leading hypothesis into a stronger conclusion?

## Reset and regeneration

Keep the supplied captures for the core lab. Optional regeneration requires `python3 -m pip install -r requirements.txt` and OpenSSL, then `python3 scripts/generate_data.py`. Do not send packets or capture an unauthorised interface. Clear TLS key-log preferences after the exercise.
