# Data Policy

## Purpose

The Linear A Open Corpus is a provenance-first, machine-readable research corpus. Its purpose is to make Linear A evidence easier to inspect, compare, reproduce, and analyze without collapsing observations into interpretations.

## Core principles

1. Observation before interpretation.
2. Source before normalization.
3. Provenance is data.
4. Licenses travel with derived records.
5. Uncertainty is preserved rather than silently resolved.
6. Sign identity is not decipherment.
7. Linear B correspondence is not automatically a Linear A reading.
8. Hypotheses are recorded as hypotheses.
9. Releases are reproducible and versioned.
10. Openness applies to our own material to the maximum extent legally possible.

## Data layers

### Source layer
The source layer records what an upstream database or publication supplies.

### Normalized layer
The normalized layer maps source concepts to stable project fields. Transformations must be documented.

### Analytical layer
Derived statistics, classifications, and computational results are explicitly marked as derived.

### Hypothesis layer
Interpretive claims are stored separately from observations and carry evidence, counterevidence, status, confidence, and sources.

## No silent corrections

If an imported record appears incorrect, do not silently replace the source value. Preserve the source value and record a project-level correction or reconciliation with its evidence.

## Reproducibility

Every release should identify:
- upstream source(s);
- upstream version or retrieval date;
- transformation scripts;
- schema version;
- validation results;
- applicable licenses.
