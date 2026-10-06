# Researcher capability status — 3.0.20

## Working interfaces

- Offline searchable browser: `python scripts/build_researcher_browser.py` generates `workbench/linear-a-browser.html` plus its compact index.
- Read-only API: `scripts/research_api.py`.
- Source-only context population: `scripts/build_source_context.py`.
- Evidence coverage diagnostics: `scripts/report_evidence_coverage.py`.
- Loss-aware JSON, CSV, JSON-LD and EpiDoc-compatible TEI export: `scripts/export_research_layer.py`.
- Scholarship-link validation and provenance-aware GeoJSON conversion are implemented, but rights-clean population remains incomplete.
- Accounting checks keep symbolic/source evidence separate from model assignments and arithmetic.
- Advanced source-sequence analysis supports statistics, regex pattern search, KWIC, collocations and form-family distance.

## What is still missing

The principal software gaps are a portable Parquet strategy and richer browser presentation of context/provenance/disagreements. The principal data gaps are rights-clean scholarship linkage, attributed geospatial coordinates/findspots, deeper palaeographic/context population, and independent expert/object-level review.

Run the coverage reporter rather than inferring completeness from file existence. Missing context is preserved as missing.

## Scientific boundary

These interfaces improve access and reproducibility. They do not decipher Linear A, establish source independence, validate disputed readings, or override source rights. GORILA remains bibliographic/reference-only under the EFA project-specific refusal.
