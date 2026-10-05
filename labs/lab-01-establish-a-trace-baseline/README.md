# Lab 01 — Establish a trace baseline

The branch help desk has received a capture from the client PC (192.0.2.10), but nobody has checked what it contains. Before anyone diagnoses a fault, you establish a trusted baseline of the trace.

## Instructions

- [LAB-01-Instructions.md](LAB-01-Instructions.md) — full step-by-step instructions
- [LAB-01-Instructions.pdf](LAB-01-Instructions.pdf) — the same instructions, printable

## Quick start

```bash
python3 scripts/verify.py
```

## Folder contents

- `data/` — synthetic captures (and, for the TLS lab, synthetic session secrets)
- `assets/` — scenario ticket, expected evidence, templates and fixture checks
- `scripts/` — verification, evidence export and optional data regeneration
- `checkpoints/` — how to rejoin if you missed an earlier lab
- `outputs/` — your findings and exported evidence

*Wireshark Network Analysis Masterclass · C1123 · Version v5.1*
