# Lab 14 — Investigate retransmission and zero window

A file download stalls part-way through. You must show whether the sender, the receiver or the path held things up.

## Instructions

- [LAB-14-Instructions.md](LAB-14-Instructions.md) — full step-by-step instructions
- [LAB-14-Instructions.pdf](LAB-14-Instructions.pdf) — the same instructions, printable

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
