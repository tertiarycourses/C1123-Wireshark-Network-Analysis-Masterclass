# Lab 16 — Inspect HTTP outcomes and HTTP/2 frames

The web team wants to know which pages fail and whether the new HTTP/2 test service is negotiating correctly.

## Instructions

- [LAB-16-Instructions.md](LAB-16-Instructions.md) — full step-by-step instructions
- [LAB-16-Instructions.pdf](LAB-16-Instructions.pdf) — the same instructions, printable

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
