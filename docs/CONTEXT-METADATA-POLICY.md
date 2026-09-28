# Context Metadata Policy — 0.5.0

0.5.0 separates **schema semantics** from **record-level assertions**.

SigLA's current help/search interface documents document type as a searchable
document property and displays metadata such as title, find-place, size and
number of signs. Its published paper additionally describes document typology,
dimensions, sign/word density, sign function, and source-defined word views.

Those descriptions justify fields in our schema. They do **not** justify
assigning a value to a particular document.

A document-level value (for example `Tablet`, `LM IB`, or a scribe assignment)
enters `document_contexts.csv` only when a current source explicitly supplies
that value and its source/license/provenance travel with the assertion.

Rules:
1. Never infer document type from the document identifier.
2. Never infer period from site.
3. Never infer administrative/religious function from support alone.
4. Preserve conflicting source assertions independently.
5. A project normalization is a new derived assertion, not a replacement for
   the raw source value.
6. SigLA-derived record data retain applicable CC BY-NC-SA 4.0 obligations.
