# Aegean Epigraphy Interoperability Contract — v0.1

## Purpose
Linear A and Cypro-Minoan remain independent scholarly corpora. This contract defines only the decipherment-neutral intersection needed for future shared tooling and comparative research.

It is not a shared corpus, signary, transcription system, segmentation model, or decipherment framework.

## Core interchange concepts
1. **record** — stable project-local identifier for an inscription/document/object record.
2. **identifier** — source/catalogue identifier with source attribution.
3. **assertion** — a source-specific or project-derived claim; never an unqualified truth value.
4. **provenance** — source, locator, responsible agent where known, transformation, version/access information.
5. **uncertainty** — explicit certainty state; unknown is not silently normalized away.
6. **rights** — record/data license plus third-party-material restrictions.
7. **lineage** — relationship to upstream evidence and whether evidential independence can be claimed.
8. **physical locus** — side/face, region, line, sign occurrence or other source-supported location.
9. **representation** — transcription/drawing/encoding/normalized form with declared derivation.
10. **hypothesis** — analytical interpretation kept outside observational ground truth.

## Required cross-project invariants
- Credit follows claims.
- Digital re-encoding does not create independent epigraphic evidence.
- Competing responsible assertions may coexist.
- Project-derived normalization identifies its inputs.
- Rights travel with derived records/material.
- Script identity, sign identity, phonetic value and linguistic interpretation are separate concepts.
- Missing source support remains missing.
- Corrections and supersessions are versioned, not silently overwritten.
- Comparative algorithms must consume the interchange layer, not assume either project's native sign/word model.

## Native mappings

### Linear A
- record → SigLA/GORILA-aligned document identity layer
- assertion → 2.4.2 witness assertion
- provenance/lineage → evidence-instance + source-lineage records
- representation → source-defined words, sign instances, source transcriptions
- hypothesis → analysis/release claim layers

### Cypro-Minoan
- record → CMOC inscription record
- assertion → scholarly assertion schema
- provenance → assertion provenance array
- representation → attributed transcription/segments
- rights → record rights + third-party material
- hypothesis → concordance/analytical layers

## Explicit non-equivalences
Linear A `source_word` is not a universal Aegean-script word object. Cypro-Minoan segmentation must not inherit it.
Linear A AB sign IDs and Cypro-Minoan CMSIGN concepts are not a common sign inventory.
Cypro-Minoan CM0/CM1/CM2/CM3 classifications have no Linear A analogue.
Linear B phonetic/morphological categories must not become required fields when Linear B is added later.

## Extraction rule
A field may enter future shared core software only after at least two script projects need the abstraction without redefining its semantics. Script-specific fields remain adapters/extensions.

## Comparative-research rule
Cross-script statistics must preserve corpus-specific observational units and declare any harmonization. A shared algorithm does not imply shared linguistic structure.
