# Lab 07 — Build a filter evidence matrix

**Course:** Wireshark Network Analysis Masterclass (C1123) | **Topic:** 07 — Display Filters | **Learning outcome:** LO2 — Navigate, filter, summarize and time network exchanges. | **Time:** about 30 minutes | **Version:** v5.1 · 5 October 2026

## Scenario

The team keeps sharing filters that silently hide evidence. You build a tested filter matrix so everyone answers the same question the same way.

## Goal

Parentheses make mixed and/or expressions explicit.

## What you will produce

A filter evidence matrix with verified frame numbers.

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
| `assets/filter-matrix.csv` | Filter matrix template (question, filter, frames) |

## Lab at a glance

1. Find the NXDOMAIN response and SYNs
2. Compare two bracketings of one filter
3. Test !(ip.addr == x) vs ip.addr != x
4. Save five verified filters with frames

## Step-by-step

1. Prepare your lab workspace. Open this lab folder in a terminal. Windows uses py -3 in place of python3. Wireshark GUI alone is sufficient for the investigation; CLI scripts require TShark on PATH. Run the fixture verification first.

   ```bash
   python3 scripts/verify.py
   ```

2. Open data/branch-office.pcap. Apply dns.flags.rcode == 3 and record the returned response frame. Clear the filter and apply tcp.flags.syn == 1.

3. Compare (ip.src == 192.0.2.10 && udp.port == 53) || tcp.port == 80 with ip.src == 192.0.2.10 && (udp.port == 53 || tcp.port == 80). Record both counts and the direction excluded by the second expression.

4. Apply !(ip.addr == 192.0.2.53). Verify that DNS packets disappear; compare ip.addr != 192.0.2.53 on Wireshark 4.6 or later. Record the actual version and equality behaviour.

5. Save five useful filters in outputs/filters.txt. For each, state the question, filter and matching frame numbers; compile them with scripts/verify.py.

6. Export a reproducible packet table. Record the filter, frame numbers, measurement, explanation and limitation in outputs/findings.md.

   ```bash
   python3 scripts/export_evidence.py
   ```

## Expected evidence

With the lab filter applied, your packet list should match the frames below (produced by TShark from this lab's own capture).

![Lab 07 expected evidence](assets/expected-evidence.png)

## Test it

The supplied dns.flags.rcode == 3 expression matches 1 frame(s) in the specified capture. Run scripts/verify.py and compare the listed frame numbers. Keep your findings and exported table in outputs/. Explain the observed result rather than only copying a count.

## Troubleshooting

- TShark not found: install Wireshark CLI tools and add the installation folder to PATH; on Windows use the Wireshark install directory.
- A filter returns zero: clear other filters, use the specified capture, and check the expression is in the display toolbar.
- TLS remains opaque: select the matching lab-tls.keys file by absolute path, reload, and remove a key-log preference from another lab.

## Try it with TShark

The same evidence from the command line — run it from this lab folder:

```bash
tshark -n -r data/branch-office.pcap -Y "dns.flags.rcode == 3"
```

## Challenge

Develop and explain an alternative filter.

## Reflection

Which second observation point would strengthen your conclusion?

## Extension (optional)

Rewrite two of your matrix filters with the set (in {…}) and matches operators and confirm the frame lists are unchanged.

## Reset

Clear all display filters and return to the C1123-Analyst or Default profile. If you loaded a TLS key log, remove it from Preferences > Protocols > TLS. The supplied captures never need regenerating for the core lab.

> **Note:** The same steps appear in the Learner Guide. The slides show only the scenario and a summary.

---

*Wireshark Network Analysis Masterclass · C1123 · Version v5.1 · © 2026 Tertiary Infotech Academy Pte Ltd*
