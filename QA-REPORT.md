# C1123 QA report — v5.1 (5 October 2026)

**Result: PASS**

| Check | Result |
|---|---|
| Non-WSQ prohibited-content scan | PASS: 0 hits |
| Cover version vs filename | The cover shows `Version v5.1` and the file is `…(C1123)-v5.1.pptx` |
| Document Version Control Record | The LP and the LG each have a 5.1 row (4.0 and 5.0 rows are kept) |
| Lab alignment | Labs 1–18 appear in the deck, the LG (DOCX + MD), the LP and `labs/` (18 folders, each with `LAB-NN-Instructions.md` + `.pdf`) |
| Lab fixtures | `scripts/verify.py` and `scripts/export_evidence.py` pass in all 18 lab folders (TShark 4.6.8) |
| TShark equivalents | All 18 commands were run from inside their lab folders against the supplied captures |
| LP timing | Each of the 4 days totals 480 training minutes, lunch excluded |
| Non-WSQ structure | "How You'll Learn" replaces any assessment block. The deck closes with What You Achieved → Continue Your Learning → Keep Practising → Thank You |
| Superseded files | v4.0 and v5.0 deliverables are in `courseware/archive/` |
| Visual check | All 279 slides and a sample lab instruction PDF were rendered and inspected, with no clipped, overlapping or overflowing text |

## v5.1 changes checked

- The slides show only each lab's scenario, a four-task summary, the expected evidence and the "Test it" check. Full steps are in the LG and in each lab's instructions (MD and PDF).
- About 40 new concept slides. Their ladder diagrams, timing charts, I/O and Stevens graphs are drawn from the labs' own captures by `scripts/build_concept_visuals.py`.
- Content added from external sources: DHCP, NAT, IPv6, Ethernet framing, TShark, BPF capture filters, display-filter functions, export-and-hash evidence handling, HTTP/3/QUIC, security patterns and baselining. The sources are listed in the LG (Further Learning) and in `labs/README.md`. Kurose & Ross material is referenced with acknowledgement, and none of its text is copied.
- New lab mock data:
  - a scenario ticket (`assets/scenario.md`)
  - a findings sheet (`outputs/findings.md`)
  - lab-specific templates: filter matrix (Lab 7), graph notes (Lab 15) and HTTP summary (Lab 16)
  - an expected-evidence image
  - an export script that now uses each lab's own capture and filter
