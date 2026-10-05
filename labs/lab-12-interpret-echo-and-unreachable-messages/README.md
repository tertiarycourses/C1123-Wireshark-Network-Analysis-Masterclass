# Lab 12 — Interpret echo and unreachable messages

Ping to the server works, yet a diagnostic tool on UDP port 9999 fails. You use ICMP evidence to explain the difference.

## Instructions

- [LAB-12-Instructions.md](LAB-12-Instructions.md) — full step-by-step instructions
- [LAB-12-Instructions.pdf](LAB-12-Instructions.pdf) — the same instructions, printable

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
