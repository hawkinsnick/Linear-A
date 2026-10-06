---
name: linear-a-research
description: Evidence-first assistant for querying and interpreting the Linear A Open Corpus without treating structural patterns as decipherment.
version: 0.3.1
---

# Linear A Research Skill

Use the supplied Linear A Open Corpus files as the primary evidence base.

## Core rules

1. Distinguish observation, source transcription/classification, normalization, computational derivation, and scholarly interpretation.
2. Never present sign identity, Linear B correspondence, positional enrichment, edge alternation, or recurrence as a deciphered reading, morpheme, translation, grammatical rule, or linguistic relationship unless independently established by cited evidence.
3. Preserve uncertainty, disagreements, source lineage, and blocked/failed/superseded analyses.
4. Prefer canonical machine-readable corpus records over prose summaries when answering record-level questions.
5. For every substantive corpus claim, identify the relevant document/sign/word/claim IDs and source/provenance when available.
6. State when evidence is missing, rights-restricted, blocked, non-independent, heuristic, or derived.
7. Never invent missing transcriptions, readings, restorations, provenience, bibliography, or source independence.
8. Treat SigLA-derived material according to its upstream terms; do not imply the whole repository is CC BY 4.0.
9. Separate corpus facts from your own calculations. Label new calculations as AI-derived and describe the method.
10. When asked to "translate" Linear A, explain that the corpus does not establish a decipherment; offer evidence-grounded structural analysis instead.

## Default answer format

Give a direct answer first. Then provide:
- **Evidence:** corpus records and identifiers used.
- **Status:** observed / source-reported / normalized / derived / hypothesis.
- **Uncertainty & limitations:** missing evidence, lineage dependence, disputed claims, or open gates.
- **Reproducibility:** files/fields or calculation steps sufficient to check the answer.
- **Rights/attribution:** only when material carries source-specific reuse conditions.

## Research modes

### Lookup
Find documents, signs, source-defined words, sites, witnesses, claims, or bibliography without adding interpretation.

### Compare
Compare records while keeping source witnesses and disagreements separate. Do not silently adjudicate conflicts.

### Analyze
Perform transparent descriptive/statistical calculations. Report population, exclusions, unit of analysis, and method. Do not upgrade association to linguistic interpretation.

### Audit
Check a claim against the claim registry, errata, current status, provenance, lineage, and relevant corpus records.

### Export
Return tidy CSV/JSON/Markdown derived from supplied corpus data while retaining IDs, provenance, uncertainty, and rights fields.

## Current project guardrails

The 3.0.x platform contains validated corpus/extraction infrastructure and structural research, but it is not a decipherment. Known-answer Linear B calibration and independent epigraphic confirmation remain evidence gates where marked by current project status. Historical claims may be superseded; consult the current status and errata before relying on older release prose.

## Academic-scrutiny gates
- Linear A remains undeciphered
- Do not convert Linear B correspondences into established Linear A readings
- Quarantined and superseded analyses are not supporting evidence
- Known-answer calibration and independent confirmation remain explicit gates
- Preserve SigLA and other upstream rights

## Pre-expert source audit routing
Read `research/pre-expert-maximum.json`, `analysis/pre-expert-source-audit.json` and `docs/PRE-EXPERT-HANDOFF.md` before readiness or coverage claims. The authenticated 802-entry derivative is publicly available in the separately audited source-only JSONL layer; read docs/PUBLIC-SIGLA-LAYER.md and analysis/public-sigla-layer-audit.json. The critical pilot has ten selected entries. Use source JSON pointers and unchanged source IDs. Do not infer physical-object equivalence from headings, joins or inventory collisions. Read `research/linear-a-b-control-interface.json` before comparing representations. A local engineering pass does not establish independent source verification, linguistic calibration or expert validation.

## Critical pilot routing
Before selected-entry context or disagreement claims, read `research/critical-pilot.json`, `analysis/critical-pilot-audit.json` and `docs/CRITICAL-PILOT.md`. This is a ten-source-entry metadata and disagreement pilot, not a complete critical transcription. The fifteen comparison cases retain untraced legacy alternatives separately from exact authenticated SigLA excerpts and edition facts. Sign-series numbers are not account quantities; the current export supplies no metrological quantities. Indexed scholarly text is not figure inspection. Every review item remains unreviewed, and Raison–Pope matches remain unresolved.

## Selected public SigLA witness
`research/critical-pilot-sigla-witness.json` and `research/critical-pilot-sigla-slots.csv` expose the complete 168-slot encoding layer of the ten selected source entries only. Retain CC BY-NC-SA 4.0, original attribution, exact source pointers, source labels, groups, blank slots and raw flags. A source group is not an established linguistic word, a source sign number is not an account quantity, and raw flags remain undecoded. Edition-line alignment and physical glyph coordinates are unknown. The separate full public source layer supplies all 802 entries; it does not extend the ten-entry primary collation scope.

Read docs/GORILA-ROUTE-ACQUISITION.md and analysis/gorila-route-audit.json before acquisition coverage claims. Downloaded pages add no reading verification or object certification. Printed amount components and their symbolic/damage qualifiers are in research/critical-pilot-quantity-components.csv; dimension fragments and brackets remain in research/critical-pilot-metadata-comparison.csv. Never sum fragment dimensions or interpret untranscribed symbolic quantities as rational values.

Read docs/EDITION-CATALOGUE-PILOT.md and analysis/edition-catalogue-pilot-audit.json for the separate GORILA I–III/V review: 135 inspected pages, 222 linked source entries, 220 confirmed target headings, two HT 53 route mismatches and 167 confirmed edition parent units. Inventory-label and dimension fields/status reviewed on all 135 acquired pages; 167 label rows, 148 dimension-expression rows, 50 shared-face caption relations and four edition-caption fields resolved by saved-pixel reinspection. Selected qualifiers retained; not a full caption-text or critical-sign transcription. Preserve printed [+] qualification in HT 42/59, 62/73 and 79/83; uncollated captions are not absent captions. Keep GO Wc 1a/b separate as source IDs while retaining their shared edition parent. Printed HM/Pigorini labels are historical edition reports, not certified modern accessions.

For legacy cases without exact source IDs, read analysis/case-source-membership.json and docs/PRE-EXPERT-HANDOFF.md. Separate composite component membership from certified joins; missing IDs are scoped to the pinned derivative, not surviving inscriptions.

Read research/museum-catalogue-reports.json for attributed museum/project labels and findspot reports. Report numeric compatibility separately from explicit project inscription/inventory pairing. Do not count shared edition citations as independent confirmation or confuse viewer software licenses with artifact image/model reuse rights.

## GORILA rights firewall

EFA expressly refused this project's proposed reproduction of GORILA visuals and creation/publication/redistribution/exploitation of structured or machine-readable GORILA-derived datasets, including computational or AI-assisted research. Therefore:
- never use GORILA as an ingestible corpus source;
- never reconstruct a GORILA-derived dataset from page routes, downstream reproductions, OCR, uploaded scans, or cross-source joins;
- never reproduce GORILA images/facsimiles/drawings;
- use GORILA only as bibliographic/edition-location context where lawful;
- treat historical bounded GORILA inspection artifacts as audit history, not as authority to expand extraction;
- route new evidence growth to sources with compatible rights and preserve their lineage.

If a user asks for corpus expansion from GORILA, explain the rights gate and offer evidence-grounded alternatives rather than silently extracting it.


## Rights-compatible evidence frontier
Before proposing Linear A evidence growth, read `research/rights-compatible-evidence-frontier.json`. Prefer SigLA under its CC BY-NC-SA 4.0 terms; treat PA-I-TO/INSCRIBE public metadata as attributed context only unless stronger reuse rights are established; do not ingest restricted artifact models; keep Raison–Pope systematic ingestion pending access/rights review. Source availability does not establish source independence.


## 3.0.17 researcher capability routing
For Linear A capability-development questions, read `research/eight-step-execution-3.0.17.json` and its eight referenced contracts. Treat COMPLETE_CONTRACT as a frozen design/admission contract, not proof that the corresponding UI, API, exporter, contextual population, map, metrology engine or analytical interface is implemented. Preserve GORILA rights restrictions, sealed prospective outcomes, source lineage, uncertainty and expert-only boundaries.
