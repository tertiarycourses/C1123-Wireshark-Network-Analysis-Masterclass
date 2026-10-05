# Lab 09 — Diagnose DNS failure and delay

Users report that some names fail and others resolve slowly. You separate a missing name from a slow resolver using the DNS evidence.

## Instructions

- [LAB-09-Instructions.md](LAB-09-Instructions.md) — full step-by-step instructions
- [LAB-09-Instructions.pdf](LAB-09-Instructions.pdf) — the same instructions, printable

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
