# Linear A Open Corpus

An open, provenance-first, machine-readable research corpus for Minoan Linear A.

## Project goal

The long-term goal is a comprehensive, reproducible corpus of Linear A evidence that is free to access and reuse by everyone to the maximum extent legally possible.

The corpus distinguishes physical/document observations, source transcriptions and classifications, normalized representations, computationally derived data, and scholarly interpretations/hypotheses. It does not assume that Linear B correspondences constitute deciphered Linear A readings.

## Current research state

**0.7.0 — source-word analytical release**

The project now includes a validated local SigLA decoding path, source reconciliation and uncertainty architecture, context-aware structural units, and analysis over SigLA's explicit serialized Word objects.

Current validated snapshot invariants include:
- 802 decoded documents
- 5,144 sign attestations
- 1,401 serialized SigLA Word objects
- 1,283 nonempty source-defined words
- 836 distinct source-word types
- 168 recurrent source-word types

Two separately implemented executable decoding paths, checked against the published reference field semantics and run on the same SigLA snapshot, agreed on all 5,144 attestations across 46,296 compared fields. This is a decoder/extraction validation claim, not an epigraphic or decipherment claim.

See `docs/RESEARCH-HISTORY-0.3-0.7.md` for the consolidated post-0.2 research history and corrections.

## Core design principles

1. Sign identity is not decipherment.
2. Linear B correspondences are not automatically Linear A readings.
3. Observation and interpretation remain separate.
4. Every external record carries provenance.
5. Uncertainty is preserved.
6. Licensing is tracked at the record/source level.
7. Conflicting scholarly claims remain distinguishable.
8. Releases should be reproducible.
9. Original project contributions should be maximally open.
10. Failed/superseded analytical models are documented rather than silently erased.

## Source-word architecture

0.6.0 established that SigLA's serialized document objects contain explicit Word lists. Source-word membership is therefore decoded from those lists and **not reconstructed from the unresolved f3 field**.

0.7.0 reports distributional analyses over those source-defined words. No result is asserted to be a prefix, suffix, morpheme, grammatical rule, phonotactic rule, translation or decipherment.

## f3

The f3 field remains evidence-tiered and semantically unresolved. Earlier attempted boundary interpretations were tested and superseded. It is not used as a substitute for source-defined word membership.

## Important 0.7 correction

A site_id field in the initial 0.6 local export was derived from document-label prefixes. Public 0.7 documentation corrects this to `site_group_heuristic`. It is not canonical source-explicit site metadata.

## SigLA and licensing

SigLA is a major upstream source. SigLA-derived records and aggregates retain applicable CC BY-NC-SA 4.0 obligations. Raw SigLA payloads and drawings are not bundled. GORILA text/plates/images are not redistributed without rights.

See `THIRD-PARTY-NOTICES.md`, `DATA-LICENSE-MATRIX.md`, and `SOURCE-POLICY.md`.

## Roadmap

- 0.1.0 — Unicode sign inventory.
- 0.2.0 — corpus architecture, provenance and licensing framework.
- 0.3.0 — reproducible SigLA decoder/import foundation.
- 0.4.0 — source reconciliation, uncertainty, structural forensics and computational baselines.
- 0.5.0 — context-aware corpus architecture.
- 0.6.0 — explicit serialized SigLA Word-object layer.
- 0.7.0 — source-word distributional analysis and methodology correction.
- 1.0.0 — reproducible, release-versioned research corpus suitable for general computational and scholarly use.

## Reproducible SigLA import

The repository does not bundle the upstream SigLA payload. The importer remains opt-in; fetched source and generated corpus should remain under gitignored local paths. Derived material must retain provenance and applicable upstream licensing.

## Legal note

This repository is a research project, not legal advice. Check the license attached to a source or record before redistributing derived material.
