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
