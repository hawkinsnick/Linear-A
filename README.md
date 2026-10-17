# Linear A Open Corpus

<!-- CURRENT-STATUS:START -->
## Current evidence status

Native release version: **3.0.15**; researcher-tooling checkpoint: **3.0.21** (a separate capability milestone). Known-answer calibration executed: **false**. Prospective evidence remains sealed; historical 2.5 analyses remain quarantined. Source permissions/access and admissible independent evidence govern further evidence growth.

Authorities: [current state](analysis/current-status.json) and [residual evidence gates](research/residual-blocker-ledger-3.0.21.json). Historical release reports retain their original scope and dates.

Combined coverage checkpoint (2026-10-12): **18 corpora, 9,562 heterogeneous native-view rows**, including all 287 Anatolian dossiers and 210 Cypriot syllabic discovery identifiers. These are overlapping view rows, not unique inscriptions. [Expansion scope and remaining work](corpus-factory/COVERAGE-EXPANSION-2026-10-12.md).

Earlier available-evidence checkpoint: **18 corpora / 10,527 heterogeneous rows**. [Added source layers and qualifications](corpus-factory/AVAILABLE-EVIDENCE-GROWTH-2026-10-12.md). No new readings, calibration or expert acceptance.

Latest CH/CM checkpoint: **18 corpora / 10,759 heterogeneous rows**. [Source discovery and primary context](corpus-factory/CH-CM-SOURCE-GROWTH-2026-10-12.md). Reading and expert-acceptance gates remain unchanged.
<!-- CURRENT-STATUS:END -->

## Researcher interfaces (3.0.19)

The corpus now includes working read-only researcher tooling over the committed public source layer:

- `python scripts/research_api.py documents --text HT --limit 20` — stable-ID/text API for documents, source-defined groups and signs.
- `python scripts/build_researcher_browser.py` — builds a compact searchable browser index.
- `python scripts/build_source_context.py` — extracts only explicitly source-reported context assertions.
- `python scripts/export_research_layer.py documents jsonld /tmp/documents.jsonld` — loss-aware JSON/CSV/JSON-LD/EpiDoc-compatible exports with manifests.
- `python scripts/advanced_query.py --kwic <TOKEN>` — KWIC; also supports collocations, patterns and form-family comparisons.
- `python scripts/accounting_check.py RECORD MODEL` — model-explicit accounting checks without assigning unstated values.

These tools do not establish decipherment, source independence or expert epigraphic validation. GORILA remains outside structured ingestion under the EFA project-specific refusal. See `research/rights-compatible-evidence-frontier.json`.

## AI research skill

**New to the corpus collection? [Start here](combined-ai-skill/START-HERE.md)** — download one master-instruction file, upload it to your AI assistant, and choose the evidence relevant to your research. [Starter downloads](combined-ai-skill/downloads/README.md).

This corpus project includes a vendor-neutral, evidence-first AI research skill in [`ai-skill/`](ai-skill/). The corpus remains the scholarly source of truth; the skill is an interface to it, not a second corpus and not an independent authority.

Researchers using ChatGPT, Claude, Gemini, or another capable model can provide the repository (or its AI-ready bundle) together with [`ai-skill/SKILL.md`](ai-skill/SKILL.md). The skill requires the model to preserve provenance, uncertainty, exclusions, source dependence, rights, and this project's scientific gates. Before substantive use, check [`ai-skill/generated/source-state.json`](ai-skill/generated/source-state.json) and the generated research-bundle index for the corpus commit represented by the AI package.

For questions spanning multiple corpus projects, use the **Combined Corpus Research AI** documented in [`combined-ai-skill/`](combined-ai-skill/). It orchestrates the registered individual skills while keeping their evidence models and rights separate. Membership in the combined system does **not** imply linguistic relationship, sign equivalence, chronology, decipherment, or independent replication.

## Reuse and attribution

Current project-original software is licensed under **PolyForm Noncommercial 1.0.0**; current project-owned non-software content is **CC BY-NC 4.0**, subject to [LICENSE-CONTENT.md](LICENSE-CONTENT.md). Earlier material already released under broader irrevocable terms retains any rights previously granted.

**Imported and source-derived material retains its upstream terms.** The
repository as a whole is not covered by an attribution-only data license.
See [the data license matrix](DATA-LICENSE-MATRIX.md) and [third-party notices](THIRD-PARTY-NOTICES.md).

## Historical source checkpoint — 3.0.15

Pinned statistical repair executed twice with byte-identical results on 1283 nonempty source words, 836 types and 451 documents. The 5000-replicate document-bootstrap diagnostic retains 6 of 12 candidates above the historical lower-z threshold. This is conditional same-corpus sensitivity, not independent or prospective confirmation. Historical 2.5 remains quarantined; prospective input independence and known-answer calibration remain blocked.

The historical family contract 1.2 snapshot aligns all five projects with [Phaistos Disc 1.6.0](https://github.com/hawkinsnick/Phaistos-Disc/releases/tag/v1.6.0). The historical shared readiness report preserves native sampling units, source rights and blocked linguistic controls. It authorizes no pooling or linguistic relationship claim. See [`research/family-readiness-v1.json`](research/family-readiness-v1.json).

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

## Historical architecture and source baseline

**Architecture baseline: 3.0.0; native release version: 3.0.15**

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


## 3.0.21 pre-expert maximum / rights-dominant gate
The Linear A corpus has reached its machine-resolvable pre-expert maximum under currently admitted evidence. Read `research/residual-blocker-ledger-3.0.21.json` and `docs/RIGHTS-ONLY-READINESS-3.0.21.md`. Do not describe independent epigraphic confirmation or the sealed prospective experiment as unfinished software: they require admissible independent evidence and/or human object review. Current evidence-growth gates are dominated by source rights/access (GORILA/EFA refusal, Raison–Pope rights/access, and permission for richer object-level datasets). Optional UI/statistical/export depth may continue but is not prerequisite to ingesting lawful independent evidence.

Fleet software admission reconciliation and retained scholarly gates: [10 October record](docs/FLEET-RECONCILIATION-2026-10-10.md).

## Publication and dependency repairs

The [2026-10-12 defect checkpoint](corpus-factory/DEFECT-REMEDIATION-2026-10-12.md) records source-parent publication guards, removal of duplicate publishers and restoration of the master source-dependency register. These engineering repairs grant no scholarly acceptance.

## Unified corpus and prepared calibration inputs

The master corpus builder now materializes the declared native views of all 18 language members while retaining context and component rights. [Mega-corpus guide](https://github.com/hawkinsnick/Linear-A/blob/main/corpus-factory/MEGA-CORPUS.md). Linear B has a real 5,932-record observation package; linguistic annotations and graphical occurrences remain separate source-delivery dependencies. Coverage growth proceeds before final expert acceptance.

## Source access and delivery — 2026-10-12

Current route receipts and a concrete, unsent request are recorded in [docs/RAISON-POPE-ACCESS-FOLLOWUP.md](docs/RAISON-POPE-ACCESS-FOLLOWUP.md) and [research/source-access-delivery-2026-10-12.json](research/source-access-delivery-2026-10-12.json). Access, intended-use rights, source delivery and scientific acceptance remain separate. No missing edition payload, annotation package or graphical baseline was acquired by this checkpoint.


### Linear A Explorer reference — 2026-10-12

Added [an attributed secondary-reference notice](docs/LINEARA-XYZ-REFERENCE.md), with explicit GORILA non-permission and source-dependence rules in the individual and master AI skills. No external corpus payload is imported.

## Available evidence growth — 2026-10-12

See [docs/SIGLA-SOURCE-LAYOUT.md](docs/SIGLA-SOURCE-LAYOUT.md) for the expanded source-bound evidence layer, scope and unresolved qualifications. No new canonical readings or scientific acceptance are granted.

## CH primary H/Y discovery checkpoint — 2026-10-13

[Cretan Hieroglyphic’s primary-concordance supplement](corpus-factory/CH-HY-FRONTIER-2026-10-13.md) supplies historical context for the former 127-route gap. The three-route union is 331/331 catalogue identities; encoded reading coverage remains six entries. Master instructions and starter downloads carry the updated limits. The mixed mega-corpus has not been rebuilt at this checkpoint.

## CM coverage and LB calibration controls — 2026-10-14

[Current checkpoint](corpus-factory/CM-LB-PROGRESS-2026-10-14.md): CM source coverage grows to 26 assertions on 12/21 rich records. LB adds tested private pre-reveal byte binding; actual calibration remains blocked by linked gold/graphical source dependencies. Individual and master instructions preserve the distinct evidence and acceptance boundaries.

Current one-record CM checkpoint: 28 source assertions on 13/21 rich records; eight lack encoded positions. CMOC-0209 contributes two isolated positions, one uncertain; internal source disagreement and expert gates remain open. [Scope and source controls](corpus-factory/CM209-SOURCE-CHECK-2026-10-14.md).

Priorities 2/3 checkpoint: Linear B published ID evidence, TL55 count-voice reconciliation and Byblos source-drawing count partition. Source delivery and full primary collation remain open. [Evidence and limits](corpus-factory/INPUTS-AND-RECONCILIATION-2026-10-14.md).

## Evidence and alternative-reading queries — 2026-10-15

The [critical evidence query guide](docs/CRITICAL-EVIDENCE-QUERIES.md) provides exact-ID dossiers over the existing 10-entry pilot: 168 source attestation slots and 51 attributed assertions. Source witness data, editorial assertions and legacy alternatives remain separate. The [coverage report](analysis/critical-evidence-coverage-v1.json) explicitly retains five unjoined queue cases. No alternative pair has yet been individually collated to attributed witnesses in this pilot; no readings or expert acceptance are added.

## Evidence and alternative-reading queries

[Query source evidence and unresolved alternatives](docs/EVIDENCE-AND-ALTERNATIVES.md) using exact native IDs, full source records, pinned artifact locators and explicit corpus-specific scope. [Coverage by native view](analysis/evidence-query-coverage.json) keeps catalogue entries, reading versions, assertions and research issues distinct. This interface adds no source collation, canonical reading or expert acceptance.

## Evidence queries across the language collection

The [18-corpus evidence guide](corpus-factory/EVIDENCE-AND-ALTERNATIVES.md) routes researchers to each native query, source/rights context and measured coverage. Native units remain separate; searchable alternatives do not establish completed scholarly collation.

Milyan now has a bounded Schürr2005 comparison and qualified nine-row researcher view, retaining six selected issues and all114 frozen strings. [Scope, source layers and remaining gates](corpus-factory/MILYAN-SCHUERR2005-COLLATION.md).


Milyan TL55 now has completed first-pass review coverage for9 revised lines and74 apparatus entries, with4 digital boundary markers accounted for. The independent-review packet is prepared; full critical collation and expert adjudication remain open. [Evidence and review scope](corpus-factory/MILYAN-SCHUERR2005-COLLATION.md).

## Ten-case source-attribution pass

The [joined legacy-case audit](docs/LEGACY-CASE-ATTRIBUTION.md) examines all ten exact joined cases and preserves all twenty queued alternatives. It identifies three qualified publication contexts and specific evidence gaps for every case, correcting unsupported numerical, locus and physical-adjudication claims in older project registers. No two-source same-locus competing pair, new reading or expert acceptance is established. The query interfaces expose the audit beside unchanged historical records.

Bounded attribution and comparison review: [source qualifications and remaining gaps](docs/ATTRIBUTION-REVIEW.md).

All18 language corpora: [bounded attribution review and source gaps](corpus-factory/ATTRIBUTION-REVIEW.md).

[Selected source collation: Cypro-Minoan, Lydian, Sidetic and Pisidian](corpus-factory/FOUR-CORPUS-SOURCE-COLLATION-2026-10-15.md).


Milyan TL55 now includes an exhaustive encoded-sign comparison and a152-item pending adjudication supplement. All reference/source positions are accounted for;36 candidate alignments remain ambiguous. [Scope and usage](corpus-factory/MILYAN-SCHUERR2005-COLLATION.md). No expert acceptance is claimed.


Milyan TL55: bounded documentary sign comparison complete, including source-located assessments of all152 flagged records. Non-unique ranges are preserved; independent expert adjudication remains open. [Scope and usage](corpus-factory/MILYAN-SCHUERR2005-COLLATION.md).


## 2026-10-16 — Milyan TL44 source checkpoint

Confirmed two modern DOI identities and105 existing digital row-label routes to visually inspected Kalinka pages. Three selected boundary/inventory observations preserve frozen strings; modern article PDFs, sign/apparatus collation and West pagination confirmation remain open. [Source scope and next dependency](corpus-factory/MILYAN-TL44-SOURCE-CHECKPOINT.md). Both native and combined AI instructions retain the limits; no accepted reading or independent review is claimed.

## Research-readiness P0 controls — Linear A pilot

[Audit, reproduction steps and remaining gaps](docs/NORTHWESTERN-RESEARCH-READINESS.md).
The public source view now has regression-tested provenance and interpretation
boundaries, corrected source context extraction, byte-bound exports and an offline
replayable research package. These engineering checks do not establish full primary
collation or expert acceptance. [Measured scope](analysis/research-readiness.json).
