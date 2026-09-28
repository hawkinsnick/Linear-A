# 2.4.4 — Interoperability foundation

The project defines a stable interchange boundary around documents, source-defined words, sign/evidence instances, witness assertions, source lineages and disagreements.

Canonical project CSV/JSON remains loss-aware. Exporters must preserve source IDs, version/provenance, certainty and rights. Formats that cannot express competing assertions must either emit a documented lossy view or refuse the export.

Planned interchange targets include JSON, CSV, JSON-LD and EpiDoc. Parquet is an optimization format, not a semantic authority. No external project's schema is copied as the canonical model.
