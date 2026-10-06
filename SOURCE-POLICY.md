# Source Policy

## Priority

For corpus ingestion, prefer sources that are:
1. authoritative or maintained by the original researchers;
2. openly licensed;
3. machine-readable;
4. explicit about provenance and uncertainty;
5. stable enough to support reproducible releases.

## SigLA

SigLA is a primary upstream source because it was created as an open-access Linear A palaeographical database and is designed around documents, signs, sequences, words, and contextual/palaeographic comparison.

SigLA currently states that its dataset and drawings are available under CC BY-NC-SA 4.0.

Upstream source:
https://sigla.phis.me/

Documentation:
https://sigla.phis.me/about.html
https://sigla.phis.me/paper.html
https://sigla.phis.me/help.html

## GORILA

GORILA is a foundational scholarly reference, but the project will not assume that the published corpus text or images are freely redistributable. GORILA references may be stored as bibliographic/cross-reference metadata while copyrighted content is handled according to applicable rights.

## Source identifiers

Every imported record should carry:
- source_id;
- source_record;
- source URL where available;
- source version/retrieval date;
- license;
- provenance_id.

## Conflicts

When sources disagree, retain both claims as source-specific records when practical. Reconciliation belongs in a separate analytical or hypothesis layer.

## EFA rights decision (2026-10-06)

The École française d’Athènes expressly declined permission for this project to reproduce or publish GORILA visual material and also declined permission to create, publish, redistribute, or exploit structured or machine-readable datasets derived from GORILA, including for computational or AI-assisted research and including non-commercial academic projects.

Accordingly, this repository applies a fail-closed GORILA rule:
- do not ingest GORILA as a corpus source;
- do not transcribe GORILA systematically into structured records;
- do not publish or redistribute GORILA-derived machine-readable datasets;
- do not reproduce GORILA photographs, facsimiles, drawings, plates, or other visual material;
- retain only lawful bibliographic citations, edition/page locators, source-attributed scholarly discussion, and independently sourced observations where those are otherwise permitted;
- do not reconstruct GORILA content indirectly from page routes, downstream reproductions, AI extraction, or cross-source joins.

Existing project artifacts that report bounded historical inspections must be treated as research-history/audit records, not as authorization for further extraction or redistribution. New evidence growth must come from sources whose terms permit the intended use or from original observations the project is entitled to publish.

This policy records the publisher's project-specific decision and is intentionally more restrictive than a generic copyright-risk heuristic. It is not legal advice.
