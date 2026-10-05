# Lab 08 — Reconstruct an application dependency chain

A user says "the portal is down". Before blaming the web server, you rebuild every dependency the browser needed: address resolution, name resolution, connection and request.

## Instructions

- [LAB-08-Instructions.md](LAB-08-Instructions.md) — full step-by-step instructions
- [LAB-08-Instructions.pdf](LAB-08-Instructions.pdf) — the same instructions, printable

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
