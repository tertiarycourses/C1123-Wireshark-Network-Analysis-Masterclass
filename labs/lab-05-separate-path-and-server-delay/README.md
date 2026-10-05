# Lab 05 — Separate path and server delay

The /slow page takes almost a second to load. The network team blames the server and the server team blames the network — your timing evidence decides.

## Instructions

- [LAB-05-Instructions.md](LAB-05-Instructions.md) — full step-by-step instructions
- [LAB-05-Instructions.pdf](LAB-05-Instructions.pdf) — the same instructions, printable

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
