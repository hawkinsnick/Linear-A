# Architecture 3.0

## Stable layers
**Evidence:** documents, occurrences, source-defined structural units, context assertions, palaeographic/evidence instances.

**Witnesses:** document identity, source assertions, source lineage, disagreements/adjudication.

**Research:** frozen candidate registries, statistical specifications, null models, calibration/prospective gates, results and errata.

**Interchange:** Research API v1 and Aegean Epigraphy Interchange v0.1.

**Clients:** future CLI/Python/UI/export adapters. Clients do not redefine corpus truth.

## Dependency direction
Clients → interchange → research/evidence layers → provenance/source records.

Interpretive hypotheses may depend on observations. Observations may not depend on interpretive hypotheses.

## 3.0 stability promise
Breaking changes to stable interchange contracts require a versioned successor. Native source schemas may evolve when upstream evidence demands it, with migrations/provenance.

## Explicit non-goals
3.0 does not claim corpus completeness, decipherment, phonetic proof, morphological identification, language-family identification, independent replication where lineage is shared, or successful known-answer calibration.
