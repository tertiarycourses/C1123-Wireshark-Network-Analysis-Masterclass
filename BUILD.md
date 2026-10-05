# C1123 build notes

Single source: `.claude/skills/non-wsq-courseware-build/build/course_data.py` plus `data_domain1.py` … `data_domain18.py`. The current learner package is **v5.0**. Each of the four LP days runs 09:30–18:30 with 480 training minutes (tea breaks included, lunch excluded). The schedule is set per topic: concepts and demo, then the hands-on lab.

Since v5.0 the deck is built by the house non-WSQ engine (`build_slides.py`), which is the same design system as C735 *Agentic AI with n8n*. It is no longer a patched copy of the legacy v3 deck. The local engine copy adds optional, data-driven hooks, all rendered with the engine's own components:

- `TOPIC_SLIDES`: per-topic concept, diagram and text-plus-image slides.
- `LAB_SHOTS` / `LAB_SHOT_KICKER`: an "Expected Evidence" packet-list figure per lab.
- `DAY_START_TOPIC` / `BREAK_AFTER_TOPIC`: day dividers and tea/lunch break slides that mirror the LP.
- `PORTAL_SHOT`: the LMS portal screenshot on the Download Course Material slide.

Visual assets:

- `courseware/assets/reference-diagrams/ref-NNN.png`: diagrams cropped from the private v3 reference deck by `scripts/extract_reference_diagrams.py`. It needs the reference deck in `reference/`.
- `courseware/assets/screenshots/lab-NN-evidence.png`: produced by `scripts/build_evidence_visuals.py`. It runs TShark against each lab's own capture with the filters in `assets/checks.json`.

Install the Python dependencies from requirements.txt, plus LibreOffice and Wireshark/TShark. Then run:

```bash
bash .claude/skills/non-wsq-courseware-build/build/build_courseware.sh
```

To check a lab fixture, run this from the lab's own folder:

```bash
python3 scripts/verify.py
```

The optional lab data generator uses Scapy and OpenSSL and sends no network traffic. It regenerates the synthetic TLS capture and its matching session secrets together. Use `scripts/prepare_course.py` only when you deliberately want to regenerate all lab fixtures, because it overwrites the mock datasets. `scripts/build_deck.py` (the v4.0 legacy-deck patcher) is superseded and no longer called.

Superseded deliverables are kept in `courseware/archive/`.
