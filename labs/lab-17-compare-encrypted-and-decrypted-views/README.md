# Lab 17 — Compare encrypted and decrypted views

Under an authorised test, the portal's HTTPS traffic must be inspected. You compare what an analyst sees with and without the session secrets.

## Instructions

- [LAB-17-Instructions.md](LAB-17-Instructions.md) — full step-by-step instructions
- [LAB-17-Instructions.pdf](LAB-17-Instructions.pdf) — the same instructions, printable

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
