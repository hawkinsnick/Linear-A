# Linear A Open Corpus

## Current status — 3.0.15

Pinned statistical repair executed twice with byte-identical results on 1283 nonempty source words, 836 types and 451 documents. The 5000-replicate document-bootstrap diagnostic retains 6 of 12 candidates above the historical lower-z threshold. This is conditional same-corpus sensitivity, not independent or prospective confirmation. Historical 2.5 remains quarantined; prospective input independence and known-answer calibration remain blocked.

Family contract 1.2 aligns all five projects with [Phaistos Disc 1.2.1](https://github.com/hawkinsnick/Phaistos-Disc/releases/tag/v1.2.1). The shared readiness report preserves native sampling units, source rights and blocked linguistic controls. It authorizes no pooling or linguistic relationship claim. See [`research/family-readiness-v1.json`](research/family-readiness-v1.json).

The authoritative current gate summary is [`analysis/current-status.json`](analysis/current-status.json). Historical release reports below retain their original versions and claims.

Validate this checkout with:

```sh
python -m pip install -r requirements-validation.txt
python scripts/validate_current_state.py
python scripts/test_current_state.py
```


An open, provenance-first, machine-readable research corpus and experimental framework for Minoan Linear A.

## Project goal

The long-term goal is a comprehensive, reproducible corpus of Linear A evidence that is free to access and reuse by everyone to the maximum extent legally possible.

The corpus distinguishes physical/document observations, source transcriptions and classifications, normalized representations, computationally derived data, and scholarly interpretations/hypotheses. It does not assume that Linear B correspondences constitute deciphered Linear A readings.

## Current research state

**Architecture baseline: 3.0.0; current maintenance version: 3.0.15**

The project now includes a validated SigLA decoding/extraction path, explicit source-defined Word objects, provenance and uncertainty architecture, adversarial and document-resampled structural analyses, cross-representation replication, edge-form null models, a checksum-gated known-answer Linear B calibration protocol, and a preregistered Linear-A-like degradation experiment.

Current validated corpus invariants include:
- 802 decoded documents
- 5,144 sign attestations
- 1,401 serialized SigLA Word objects
- 1,283 nonempty source-defined words
- 836 distinct source-word types
- 668 hapax types
- 168 recurrent source-word types

Two separately implemented executable decoding paths, checked against the published reference field semantics and run on the same SigLA snapshot, agreed on all 5,144 attestations across 46,296 compared fields. This is a decoder/extraction validation claim, not an epigraphic or decipherment claim.

The current conservative structural result is narrower than the historical 0.8 screen: 12 sign/position combinations survived the 0.8 adversarial screen, but only **6/12** retain a document-cluster-bootstrap 2.5th-percentile enrichment z above 1.96 in 1.7. These remain structural candidates, not morphemes or affixes.

The known-answer Linear B experiment remains unexecuted because authoritative linguistic gold and the required graphical baseline are missing. Exact DĀMOS v2 bytes have been authenticated. The historical 2.3/2.4 protocols have no calibration-performance result.

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
10. Failed, blocked, corrected and superseded analyses are documented rather than silently erased.

## Source-word architecture

0.6.0 established that SigLA's serialized document objects contain explicit Word lists. Source-word membership is decoded from those lists and **not reconstructed from the unresolved f3 field**.

No source-word result in this project is asserted to be a prefix, suffix, morpheme, grammatical rule, phonotactic rule, translation or decipherment unless future evidence independently establishes that interpretation.

## f3

The f3 field remains evidence-tiered and semantically unresolved. Earlier attempted boundary interpretations were tested and superseded. It is not used as a substitute for source-defined word membership. The 2.2 postmortem formally quarantines global f3 semantics.

## SigLA and licensing

SigLA is a major upstream source. SigLA-derived records and aggregates retain applicable CC BY-NC-SA 4.0 obligations. Raw SigLA payloads and drawings are not bundled. GORILA text/plates/images are not redistributed without rights.

See `THIRD-PARTY-NOTICES.md`, `DATA-LICENSE-MATRIX.md`, and `SOURCE-POLICY.md`.

## Changelog

The entries below summarize the research releases. Historical claims remain subject to later corrections and re-evaluations; later entries do not silently rewrite earlier releases.

### 0.1.0 — initial sign inventory
Established the initial open project and Unicode-oriented Linear A sign inventory.

### 0.2.0 — corpus architecture and provenance
Established the provenance-first corpus architecture, source/license tracking, uncertainty policy and separation between observation, normalization and interpretation.

### 0.3.0 — reproducible SigLA decoding
Developed the local opt-in SigLA importer and minimal Marshal decoding path. On the tested snapshot, two executable decoding implementations agreed across 5,144 attestations and 46,296 compared fields. Raw upstream payloads remained excluded.

### 0.4.0 — reconciliation and structural forensics
Introduced source-specific reconciliation, uncertainty, paleographic observations, numeral/hypothesis branches and structural exploratory work. Several early boundary/f3 models were falsified or superseded; f3 was retained as unresolved evidence-tiered structure rather than assigned global semantics.

### 0.5.0 — context-aware architecture
Added provenance-bearing document context, field-level assertions, typed structural units and analysis eligibility. Established the critical invariant that a candidate f3 group is not a source word.

### 0.6.0 — explicit SigLA Word objects
Decoded SigLA's explicit serialized Word lists independently of f3: 1,401 Word objects, including 1,283 nonempty and 118 empty objects. Six live-page word-count checks agreed 6/6.

### 0.7.0 — source-word analytical release
Measured 836 distinct types, 668 hapax types and 168 recurrent types among 1,283 nonempty source words. A within-word positional permutation screen produced 22 BH-FDR-positive sign/position cases. The release also corrected the inherited document-prefix `site_id` label to `site_group_heuristic`.

### 0.8.0 — adversarial positional robustness
Challenged the 22 positional signals with type deduplication, leave-one-document-out, leave-one-heuristic-group-out and dominant-word-type ablation. **12/22** survived the full strict screen; 10 were downgraded or context-sensitive.

### 0.9.0 — frozen dossiers and multiverse
Froze the 12 strict candidates and added per-candidate evidence dossiers, type-level multiverse testing and an internal-position negative control. Known-answer Linear B calibration was explicitly blocked rather than simulated.

### 1.0.0 — first architecture freeze
Froze the first complete research architecture: provenance schemas, decoder validation, source reconciliation, explicit Word extraction, structural analyses, evidence dossiers and a machine-readable claim registry. The release explicitly left independent replication, known-answer calibration and linguistic interpretation open.

### 1.1.0 — canonical-site sensitivity
Added an explicit reviewed document-to-site mapping and reran leave-one-site-out sensitivity for the 12 frozen candidates. A later 2.1 audit corrected the release summary from **18 to 19** distinct canonical site IDs; the analysis iterated over the mapping table itself.

### 1.2.0 — known-answer calibration gate
Froze the DĀMOS-based Linear B calibration protocol and exact checksum-pinned derivative identity. Execution remained blocked by corpus materialization rather than using an illustrative or synthetic substitute.

### 1.3.0 — cross-representation replication
Tested the 12 frozen signals against a pinned separately encoded Linear A representation: 1,402 eligible token occurrences and 1,009 unique types. All 12 reproduced their enriched boundary direction at type-level z > 1.96. This is **cross-representation replication, not independent epigraphic replication**, because important upstream ancestry is shared.

### 1.4.0 — calibration acquisition and falsification discipline
Verified the public DĀMOS route while preserving the distinction between the frozen derivative, live/current DĀMOS data and calibration outputs. The full pinned corpus still could not be materialized, and no miniature or synthetic substitute was promoted to a calibration result.

### 1.5.0 — edge-alternation structure
Found 651 attested directed one-edge-removal relations in four connected components. **11/12** frozen positional candidates participate in at least two such relations. These are form relations, not stems, affixes or paradigms.

### 1.6.0 — context-conditioned structure
Joined the frozen boundary signals to source-explicit document type and period metadata. Two of 12 candidates showed breadth across at least two document types and 9/12 across at least two period labels under the stated descriptive criterion. No semantic or chronological interpretation was assigned.

### 1.7.0 — document-cluster bootstrap
Resampled whole documents rather than treating words as independent. Across 1,000 cluster-bootstrap replicates, only **6/12** frozen candidates retained a 2.5th-percentile enrichment z above 1.96. This became the more conservative structural core in the later 2.2 re-evaluation.

### 1.8.0 — edge-alternation null
Compared the 651 directed edge-removal relations with a within-type sign-order shuffle null: null mean 587.2, SD 8.5, empirical upper-tail p = 0.000999. This supports excess order-sensitive form structure under that null, not morphology.

### 1.9.0 — scholarly interoperability
Formalized how the project represents external scholarship: preserve attribution and operational differences, do not rank researchers, and do not convert non-reproduction under this pipeline into claims that another scholar has been disproved.

### 2.0.0 — second architecture freeze
Froze the second research architecture and evidence ladder spanning source structure, internal enrichment, adversarial robustness, geographic sensitivity, cross-representation replication, form-network evidence and document-cluster robustness. Known-answer calibration and independent epigraphic replication remained open gates.

### 2.1.0 — postmortem correction and DĀMOS provenance
Corrected the stale 1.1 canonical-site count from 18 to **19** and changed the audit to recompute the invariant. A temporary DĀMOS provenance false alarm was also corrected by direct tag lookup: the pinned v2 asset identity and SHA-256 digest were verified. The corpus bytes still were not materialized, so no calibration result was claimed.

### 2.2.0 — re-evaluation gate
Performed a project-wide postmortem. Decoder/source-word structure was retained; global f3 semantics were quarantined; the 12-candidate set was retained only as the frozen adversarial screen; the **6/12 document-cluster-bootstrap survivors** were promoted as the conservative structural core; cross-representation evidence retained its non-independent limitation; and pseudo-Linear-A degradation was blocked until real known-answer calibration.

### 2.3.0 — executable blind Linear B calibration gate
Converted the known-answer protocol into an executable SHA-256-gated blind runner. Stage A can consume only detector-facing DĀMOS transliteration data, freezes predictions before gold reveal, and aborts on the wrong corpus hash. Exact input bytes have not yet been materialized, so `calibration_result` remains null.

### 2.4.0 — preregistered degraded-corpus calibration
Froze the Linear-A-like degradation experiment before seeing the 2.3 answer. The protocol uses whole-document optimized sampling toward the 1,283-token Linear A scale, deterministic 1,000-replicate conditions, 0/5/10/20% sign masking, undegraded/scale-only/damage-only/combined controls, explicit boundary/internal/full-mask diagnostics, recurrence mismatch reporting without manufacturing vocabulary agreement, authenticated 2.3 handoff checks and a machine-readable result schema.

**Release state:** protocol complete.  
**Experiment state:** blocked pending the authenticated 2.3 baseline.  
**Calibration result:** null.

### 2.4.1 — corpus expansion and source audit
Froze the original SigLA analytical snapshot and a 24-label prospective cohort from SigLA's May/June 2026 public update log before candidate-outcome inspection. Added a source/rights registry, source-lineage and evidence-instance schemas, and pinned the current pyaegean `sigla-corpus-v4` derivative identity (1,335,389 bytes; SHA-256 `9a5e4783…f03dd8`). The current bytes are not yet materialized locally, so no old-vs-new corpus delta or prospective structural result is claimed. Frozen 2.3/2.4 hypotheses remain unchanged.

### 2.4.2 — multi-witness epigraphic layer
Established separate schemas for canonical document identity, source-specific witness assertions, source lineage/independence and explicit disagreements/adjudication. Added a lineage-aware validator and hostile shared-upstream fixture so multiple digital reproductions of one upstream edition cannot be counted as independent epigraphic confirmations. Infrastructure is complete; source-by-source population remains ongoing and rights-aware.

### 2.4.3 — archaeological and palaeographic context
Formalized scribe, support, period, findspot, layout, damage, image/tracing and palaeographic context as provenance-bearing source assertions. The existing site mapping remains explicitly identifier-derived rather than being relabeled as direct excavation metadata.

### 2.4.4 — interoperability foundation
Froze a loss-aware interchange contract around documents, source-defined words, evidence instances, witness assertions, lineages and disagreements. CSV/JSON remain canonical working formats; JSON-LD, EpiDoc and Parquet are adapter targets. Lossy exports must be declared.

### 2.4.5 — toolset benchmark baseline
Added an evidence-based capability benchmark against SigLA, lineara.xyz and the Linear A Workbench/pyaegean ecosystem. The project records its current strengths in evidence lineage, claim auditing and experimental falsifiability, while explicitly recording gaps in interactive UI, Python API, broad export adapters and populated palaeographic context.

### 2.5.0 — statistical multiverse framework
Froze an executable multiverse/document-cluster specification for the 12 historical candidates and performed a backward statistical inheritance audit. The displayed 0.9 Holm-adjusted table passes an arithmetic recheck. The 0.9 random-internal-position negative control is superseded because its boundary and internal-position populations have mismatched eligibility/support. The historical 1.7 6/12 cluster-bootstrap result remains the conservative structural result pending execution/freeze of the new 2.5 framework.

### 2.6.0–2.9.0 — platform stabilization
Froze Research API v1, reproducible pipeline semantics, machine-readable experiment gates and the client/adapter boundary. Blocked experiments remain first-class scientific states rather than being omitted or substituted.

### 3.0.0 — architecture freeze
First architecture-stable research-platform release. Freezes the evidence/witness/research/interchange layering, claim/errata guardrails and cross-script neutral boundary. Open scientific gates remain open: DĀMOS gold scoring, degraded-corpus execution and the prospective 2026 SigLA result. 3.0 is neither corpus-completeness nor decipherment.

## Research-history and correction records

For more detail, see:
- `docs/RESEARCH-HISTORY-0.3-0.7.md`
- version-specific `README-<version>.md` files
- `release/CLAIM-REGISTRY.csv`
- `docs/ERRATA-2.1.0.md`
- `release/POSTMORTEM-REEVALUATION-2.2.csv`

## Next research gates

The current roadmap is evidence-gated rather than outcome-gated:

- execute known-answer Linear B calibration only after legitimate gold, required graphical baseline and frozen prediction/scoring contracts exist;
- execute the already-frozen 2.4 degradation protocol only after the 2.3 baseline and gold-scoring contract exist;
- 2.5 — statistical multiverse and document-cluster modeling;
- 2.6 — independent epigraphic leverage/adjudication;
- 2.7 — structural-family and edge-network null models;
- 2.8 — administrative/context structure;
- 2.9 — hostile pre-release audit;
- 3.0 — independently audited experimental framework.

A negative calibration result is an informative result. It must not be tuned away.

## Reproducible SigLA import

The repository does not bundle the upstream SigLA payload. The importer remains opt-in; fetched source and generated corpus should remain under gitignored local paths. Derived material must retain provenance and applicable upstream licensing.

## Legal note

This repository is a research project, not legal advice. Check the license attached to a source or record before redistributing derived material.


### Evidence progress in 3.0.15

Adds a reproducible input-membership independence audit: 7 of 24 frozen cohort labels occur in v3; 17 are absent. The conditional statistical repair and the original-input identity gate are distinguished. No prospective outcomes are scored; 3.1 remains sealed.
