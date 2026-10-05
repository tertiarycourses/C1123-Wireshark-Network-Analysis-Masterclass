# Lab 13 — Follow datagrams and service refusal

The diagnostic application sends UDP and never hears back. You follow the datagrams to show what was sent and why there is no transport-level acknowledgement.

## Instructions

- [LAB-13-Instructions.md](LAB-13-Instructions.md) — full step-by-step instructions
- [LAB-13-Instructions.pdf](LAB-13-Instructions.pdf) — the same instructions, printable

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
