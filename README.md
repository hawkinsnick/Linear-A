# Linear A Open Corpus

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

## Current status — 3.0.15

Pinned statistical repair executed twice with byte-identical results on 1283 nonempty source words, 836 types and 451 documents. The 5000-replicate document-bootstrap diagnostic retains 6 of 12 candidates above the historical lower-z threshold. This is conditional same-corpus sensitivity, not independent or prospective confirmation. Historical 2.5 remains quarantined; prospective input independence and known-answer calibration remain blocked.

Family contract 1.2 aligns all five projects with [Phaistos Disc 1.6.0](https://github.com/hawkinsnick/Phaistos-Disc/releases/tag/v1.6.0). The shared readiness report preserves native sampling units, source rights and blocked linguistic controls. It authorizes no pooling or linguistic relationship claim. See [`research/family-readiness-v1.json`](research/family-readiness-v1.json).

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


## 3.0.21 pre-expert maximum / rights-dominant gate
The Linear A corpus has reached its machine-resolvable pre-expert maximum under currently admitted evidence. Read `research/residual-blocker-ledger-3.0.21.json` and `docs/RIGHTS-ONLY-READINESS-3.0.21.md`. Do not describe independent epigraphic confirmation or the sealed prospective experiment as unfinished software: they require admissible independent evidence and/or human object review. Current evidence-growth gates are dominated by source rights/access (GORILA/EFA refusal, Raison–Pope rights/access, and permission for richer object-level datasets). Optional UI/statistical/export depth may continue but is not prerequisite to ingesting lawful independent evidence.

Fleet software admission reconciliation and retained scholarly gates: [10 October record](docs/FLEET-RECONCILIATION-2026-10-10.md).
