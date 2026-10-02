# Lab 08 — Reconstruct an application dependency chain

C1123 | v4.0 | 45 minutes

## Goal

ARP resolves a local next-hop MAC; DNS resolves a name to an address.

## What you will build

A packet evidence table and written findings for reconstruct an application dependency chain.

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

### 2. Open data/branch-office.pcap. Locate the ARP exchange and DNS transaction 101 for portal.example.test. Record the server address 192.0.2.20.

### 3. Apply tcp.stream == 0 and open Statistics > Flow Graph with displayed packets selected. Identify SYN, SYN/ACK, ACK, request and response.

### 4. Fill assets/dependency-map.md with the ARP, DNS, TCP and HTTP frame ranges. Distinguish Ethernet next hop from IP destination.

### 5. Contrast a same-subnet server with a routed server using assets/topology.md: a routed destination needs the gateway MAC rather than ARP for the remote host. Record what this trace can and cannot demonstrate.

### 6. Export a reproducible packet table. Record the filter, frame numbers, measurement, explanation and limitation in outputs/findings.md.

```bash
python3 scripts/export_evidence.py
```

## Test it

The supplied dns.qry.name == "portal.example.test" expression matches 2 frame(s) in the specified capture. Run scripts/verify.py and compare the listed frame numbers. Keep your findings and exported table in outputs/. Explain the observed result rather than only copying a count.

## Troubleshooting

TShark not found: install Wireshark CLI tools and add the installation folder to PATH; on Windows use the Wireshark install directory. A filter returns zero: clear other filters, use the specified capture, and check the expression is in the display toolbar. TLS remains opaque: select the matching lab-tls.keys file by absolute path, reload, and remove a key-log preference from another lab.

## Challenge

Create a second filter that answers the same question, then identify one packet it includes or excludes differently. Support your explanation with a frame number.

## Reflection

What additional observation would turn your leading hypothesis into a stronger conclusion?

## Reset and regeneration

Keep the supplied captures for the core lab. Optional regeneration requires `python3 -m pip install -r requirements.txt` and OpenSSL, then `python3 scripts/generate_data.py`. Do not send packets or capture an unauthorised interface. Clear TLS key-log preferences after the exercise.
