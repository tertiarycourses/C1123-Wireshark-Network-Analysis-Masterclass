# Lab 04 — Color and annotate evidence

**Course:** Wireshark Network Analysis Masterclass (C1123) | **Topic:** 04 — Navigation and Coloring Techniques | **Learning outcome:** LO1 — Plan scoped captures and configure a reproducible analyst profile. | **Time:** about 75 minutes | **Version:** v5.1 · 5 October 2026

## Scenario

Users see intermittent web errors. You need the failing responses to stand out, and annotations that travel with the evidence.

## Goal

Color rules are applied in order; the first matching rule wins.

## What you will produce

An annotated pcapng with a comment on the failing response.

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

## Lab at a glance

1. Filter HTTP 4xx and 5xx responses
2. Add a LAB HTTP Error colouring rule
3. Mark and comment the 500 response
4. Save and reopen the annotated pcapng

## Step-by-step

1. Prepare your lab workspace. Open this lab folder in a terminal. Windows uses py -3 in place of python3. Wireshark GUI alone is sufficient for the investigation; CLI scripts require TShark on PATH. Run the fixture verification first.

   ```bash
   python3 scripts/verify.py
   ```

2. Open data/branch-office.pcap. Apply http.response.code >= 400. Record the 404 and 500 frame numbers.

3. Open View > Coloring Rules. Add LAB HTTP Error with expression http.response.code >= 400, dark text and a pale amber background. Move it above a general HTTP rule.

4. Select the 500 response, mark it using Edit > Mark/Unmark Packet and add a packet comment describing the observed status only. Save As outputs/annotated.pcapng to preserve comments.

5. Clear the filter. Use Edit > Find Packet with Display filter http.response.code == 500. Reopen the saved pcapng and confirm the comment persists.

6. Export a reproducible packet table. Record the filter, frame numbers, measurement, explanation and limitation in outputs/findings.md.

   ```bash
   python3 scripts/export_evidence.py
   ```

## Expected evidence

With the lab filter applied, your packet list should match the frames below (produced by TShark from this lab's own capture).

![Lab 04 expected evidence](assets/expected-evidence.png)

## Test it

The supplied http.response.code >= 400 expression matches 2 frame(s) in the specified capture. Run scripts/verify.py and compare the listed frame numbers. Keep your findings and exported table in outputs/. Explain the observed result rather than only copying a count.

## Troubleshooting

- TShark not found: install Wireshark CLI tools and add the installation folder to PATH; on Windows use the Wireshark install directory.
- A filter returns zero: clear other filters, use the specified capture, and check the expression is in the display toolbar.
- TLS remains opaque: select the matching lab-tls.keys file by absolute path, reload, and remove a key-log preference from another lab.

## Try it with TShark

The same evidence from the command line — run it from this lab folder:

```bash
tshark -n -r data/branch-office.pcap -Y "http.response.code >= 400" -T fields -e frame.number -e http.response.code -e http.request_in -e http.time
```

## Challenge

Develop and explain an alternative filter.

## Reflection

Which second observation point would strengthen your conclusion?

## Extension (optional)

HTTP lab — apply your LAB HTTP Error rule to the HTTP trace from the Kurose & Ross labs. Source: J.F. Kurose and K.W. Ross, Wireshark Labs (gaia.cs.umass.edu/kurose_ross/wireshark.php).

## Reset

Clear all display filters and return to the C1123-Analyst or Default profile. If you loaded a TLS key log, remove it from Preferences > Protocols > TLS. The supplied captures never need regenerating for the core lab.

> **Note:** The same steps appear in the Learner Guide. The slides show only the scenario and a summary.

---

*Wireshark Network Analysis Masterclass · C1123 · Version v5.1 · © 2026 Tertiary Infotech Academy Pte Ltd*
