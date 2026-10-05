# Lab 15 — Graph bytes, RTT and recovery

Management wants a picture, not a packet list. You graph the stalled transfer so the retransmission and zero-window events are obvious.

## Instructions

- [LAB-15-Instructions.md](LAB-15-Instructions.md) — full step-by-step instructions
- [LAB-15-Instructions.pdf](LAB-15-Instructions.pdf) — the same instructions, printable

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
