# Lab 10 — Verify link-local resolution

**Course:** Wireshark Network Analysis Masterclass (C1123) | **Topic:** 10 — ARP Traffic Analysis | **Learning outcome:** LO3 — Interpret DNS, ARP, IPv4, ICMP and UDP evidence. | **Time:** about 50 minutes | **Version:** v5.1 · 5 October 2026

## Scenario

A technician suspects an ARP problem on the branch LAN. You check what the capture actually proves before anyone raises a spoofing alert.

## Goal

ARP requests are link-local broadcasts; replies usually return to the requester.

## What you will produce

A verified ARP table entry and an evidence-based conclusion.

## Before you start

- Wireshark 4.6 or later, with the TShark command-line tools on PATH.
- Python 3 for the verification and export scripts (Windows: use py -3 in place of python3).
- Open this lab folder in a terminal; every file the lab needs is inside it.
- Use only the supplied synthetic captures — do not capture on a network you are not authorised to monitor.

## Files for this lab

| File | What it is for |
|---|---|
| `data/branch-office.pcap` | Synthetic branch-office capture used by the lab |
| `assets/scenario.md` | The help-desk ticket that sets the scenario |
| `assets/checks.json` | Filters and frame counts the fixture must satisfy |
| `assets/expected-evidence.png` | The packet list your filter should produce |
| `scripts/verify.py` | Checks the capture facts with TShark |
| `scripts/export_evidence.py` | Exports this lab's evidence rows to outputs/evidence.csv |
| `outputs/findings.md` | Findings sheet you complete |
| `assets/arp-table.csv` | ARP table you complete |
| `assets/arp-hypotheses.md` | Competing explanations to test |

## Lab at a glance

1. Record ARP request and reply fields
2. Confirm the server IP-to-MAC mapping
3. Verify the opcode in the packet bytes
4. Test the hypotheses against the evidence

## Step-by-step

1. Prepare your lab workspace. Open this lab folder in a terminal. Windows uses py -3 in place of python3. Wireshark GUI alone is sufficient for the investigation; CLI scripts require TShark on PATH. Run the fixture verification first.

   ```bash
   python3 scripts/verify.py
   ```

2. Open data/branch-office.pcap. Apply arp. Expand the request and reply, then record sender IP, sender MAC, target IP and opcode.

3. Apply arp.opcode == 2. Confirm the advertised server mapping is 192.0.2.20 to 02:00:00:00:00:20.

4. Use the packet bytes to verify the opcode field is 2 in the reply. Add the mapping to assets/arp-table.csv.

5. Compare assets/arp-hypotheses.md with the evidence. State that this capture shows one successful exchange, without inventing repeated failures or conflicting MACs.

6. Export a reproducible packet table. Record the filter, frame numbers, measurement, explanation and limitation in outputs/findings.md.

   ```bash
   python3 scripts/export_evidence.py
   ```

## Expected evidence

With the lab filter applied, your packet list should match the frames below (produced by TShark from this lab's own capture).

![Lab 10 expected evidence](assets/expected-evidence.png)

## Test it

The supplied arp.opcode == 2 expression matches 1 frame(s) in the specified capture. Run scripts/verify.py and compare the listed frame numbers. Keep your findings and exported table in outputs/. Explain the observed result rather than only copying a count.

## Troubleshooting

- TShark not found: install Wireshark CLI tools and add the installation folder to PATH; on Windows use the Wireshark install directory.
- A filter returns zero: clear other filters, use the specified capture, and check the expression is in the display toolbar.
- TLS remains opaque: select the matching lab-tls.keys file by absolute path, reload, and remove a key-log preference from another lab.

## Try it with TShark

The same evidence from the command line — run it from this lab folder:

```bash
tshark -n -r data/branch-office.pcap -Y arp -T fields -e arp.opcode -e arp.src.proto_ipv4 -e arp.src.hw_mac
```

## Challenge

Develop and explain an alternative filter.

## Reflection

Which second observation point would strengthen your conclusion?

## Extension (optional)

Ethernet and ARP lab — read the ARP cache on your own machine (arp -a) and match it to captured replies. Source: J.F. Kurose and K.W. Ross, Wireshark Labs (gaia.cs.umass.edu/kurose_ross/wireshark.php).

## Reset

Clear all display filters and return to the C1123-Analyst or Default profile. If you loaded a TLS key log, remove it from Preferences > Protocols > TLS. The supplied captures never need regenerating for the core lab.

> **Note:** The same steps appear in the Learner Guide. The slides show only the scenario and a summary.

---

*Wireshark Network Analysis Masterclass · C1123 · Version v5.1 · © 2026 Tertiary Infotech Academy Pte Ltd*
