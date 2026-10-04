# Pre-expert validation handoff — Linear-A

This package records a reproducible engineering audit of the exact supplied derivative snapshot. It is not expert validation, independent source confirmation, or a claim of complete surviving inscription coverage. Current disposition: **PRE_EXPERT_HANDOFF_SOURCE_DEPENDENCIES_REMAIN**. Consult `research/pre-expert-maximum.json` for individual unfinished gates.

## Reproduce

From the repository root, supply your authorized local sigla-corpus.json snapshot:

```sh
python scripts/build_pre_expert_audit.py /path/to/sigla-corpus.json
python scripts/validate_pre_expert_audit.py
python scripts/test_pre_expert_audit.py
```

The importer refuses bytes that differ from the pinned checksum. Outputs under `data/generated/pre-expert/` are deliberately ignored by git and retain CC BY-NC-SA 4.0 source provenance. `records.json` preserves stable source IDs, source fields and exact JSON pointers. The public `analysis/pre-expert-source-audit.json` contains counts, missingness and derivative hashes. These outputs are deterministic and do not read prospective cohorts, predictions, experiment outcomes or gold.

## Reviewer workflow

1. Reproduce the audit and inspect the source-specific representation boundaries.
2. Review local record/source pointers and the canonical source itself for any selected claim.
3. Keep editorial disagreements, source dependencies and missing fields visible.
4. Use `research/linear-a-b-control-interface.json` before cross-script analysis.
5. Record an expert decision as a separate attributed assertion; never overwrite a source witness silently.

## Rights and scope

Repository-original tooling follows the repository software terms. SigLA/DAMOS fields and local derivatives retain upstream rights and attribution. This change publishes no source-record export or primary-edition image. Historical statistical artifacts and their pinned inputs are untouched. Engineering reproducibility does not authorize scoring a sealed experiment.

## Linear A boundaries

802 source document entries; 5,144 attestations; 1,401 source word groups; 376 source sign entries. Source display labels are not deciphered phonetic values. Four occurrence sign keys are absent from the supplied sign inventory; 388 occurrences have no series/number key. Preserve them as source gaps. Conventional metrological quantities are not supplied by SigLA. The 15 disagreement cases remain separately tracked; no new linguistic or metrological adjudication is claimed. `unresolved-source-locators.json` is local. The root CSV scaffolds do not become a public source export.

## Bounded primary collation

`analysis/pre-expert-primary-collation.json` records identified primary pages inspected for 13 of the 15 existing case entries. GORILA I page 35 explicitly reports 38 for HT 17; this is an edition-level check, not an object-level ruling. The other inspected cases retain competing labels and segmentation. SY Zb 7 still lacks a verified primary image locator. Fraction K remains a model/interpretation boundary. All physical readings remain unadjudicated by experts. No images are republished.

## Validation performed

Exact source checksums matched. Record exports and aggregate audits reproduced byte-for-byte on repeat. Current-state, source accounting, AI-bundle and existing Python regression checks passed. Linear B's existing real-source mapping audit and invented-field corruption checks also passed. CI now replays the source audit from the pinned public release asset. Remote CI results are tracked separately from this local validation.

## Whole-snapshot edition accounting

Read [the Step 1 concordance guide](EDITION-CONCORDANCE.md) before coverage or edition-equivalence claims. All 802 source entries have edition-specific statuses, including 755 attributed GORILA page links, 24 later-publication links and 23 unusable references. Existing primary inspection joins ten case entries to eight source records; three inspected case identities remain unjoined. Both Raison–Pope editions remain entry-level unresolved. The public concordance contains source-derived identifiers and bibliographic locators under retained CC BY-NC-SA 4.0, not source readings or raw records. This does not alter historical audit denominators or sealed scientific experiments.
