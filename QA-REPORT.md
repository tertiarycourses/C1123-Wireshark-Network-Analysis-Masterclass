# C1123 QA report — v5.0 (5 October 2026)

**Result: PASS**

| Check | Result |
|---|---|
| Prohibited-content scan (`non-wsq-courseware-qa/scan_prohibited.py`) | PASS — 133 artifacts, 0 hits |
| Cover version vs filename | `Version v5.0` on the cover; file `…(C1123)-v5.0.pptx` |
| Document Version Control Record | LP and LG each have a 5.0 row (4.0 row retained) |
| Lab alignment | Labs 1–18 appear in the deck, LG (DOCX + MD), LP and `labs/` (18 folders) |
| LP timing | Each of the 4 days = 480 training minutes, lunch excluded (asserted in `course_data.SCHEDULE`) |
| Non-WSQ structure | "How You'll Learn" present. No assessment, TRAQOM or digital-attendance slides. Closes with What You Achieved → Continue Your Learning → Keep Practising → Thank You |
| Superseded files | v4.0 PPT/PDF, LP, LG and LG.md moved to `courseware/archive/` |
| Visual check | All 332 slides, the 43 LG pages and the 8 LP pages rendered and inspected. No clipped, overlapping or overflowing text |

## Design alignment with C735 (Agentic AI with n8n)

The deck is built by the same house non-WSQ engine. It has:

- the same cover
- the Welcome & Housekeeping opener: two trainer cards, ice-breaker, ground rules, LMS portal screenshot, lesson plan, learning outcomes and How You'll Learn
- a core-concepts section
- numbered topic dividers
- per-topic concept and diagram slides
- for each lab: an activity overview, one slide per step and a Test it slide
- topic recaps, day dividers and tea/lunch break slides that mirror the LP

## Content provenance

- **Reference diagrams.** These 60 diagrams are cropped from the private v3 reference deck (`scripts/extract_reference_diagrams.py`). Captions note where an old diagram shows superseded tooling (for example, the GUI is now Qt).
- **Expected Evidence figures.** These are produced with TShark 4.6.8 from each lab's own synthetic capture and its `assets/checks.json` filters (`scripts/build_evidence_visuals.py`).
