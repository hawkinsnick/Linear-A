# Site mapping policy

The 0.7 correction remains in force: document-label prefixes are not source-explicit
find-place fields. Version 1.1 makes the mapping explicit and reviewable rather than
silently calling a prefix `site_id`.

`document_site_mapping.csv` records identifier prefix, canonical site id/name, mapping
status, and basis. A future direct join of the decoded SigLA metadata find-place field
may strengthen provenance without changing the canonical identifier layer.
