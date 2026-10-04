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
