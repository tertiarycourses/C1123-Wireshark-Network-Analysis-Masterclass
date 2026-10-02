# C1123 build notes

Metadata and lab content: `scripts/course_content.py`, `scripts/prepare_course.py`, `.claude/skills/non-wsq-courseware-build/build/course_data.py` and the domain files. The current learner package is v4.0. The LP has four 09:30–18:30 days: 450 instructional minutes, 30 tea-break minutes and 60 lunch minutes per day.

The PPT builder copies the private original reference deck, retains useful concept diagrams/screenshots and integrates the current 18-topic sequence with new activity briefs. Superseded procedural teaching is carried by the detailed LG/labs instead. The original remains unchanged in reference/.

Install Python dependencies from requirements.txt and LibreOffice. With the private reference deck present, run:

```bash
bash .claude/skills/non-wsq-courseware-build/build/build_courseware.sh
```

Run a lab fixture check from its own folder:

```bash
python3 scripts/verify.py
```

The optional lab data generator uses Scapy and OpenSSL without sending network traffic. It regenerates the synthetic TLS capture and matching session secrets together. Use `scripts/prepare_course.py` only when deliberately regenerating all lab fixtures; it overwrites mock datasets.

Technical sources checked 2 October 2026: official course syllabus; Wireshark User Guide capture/display filtering; Wireshark TLS Wiki. Actual fixture checks were executed with TShark 4.6.8. Diagram and screenshot provenance is in scripts/deck-provenance.json; mock-data provenance is in each lab data/README.md.
