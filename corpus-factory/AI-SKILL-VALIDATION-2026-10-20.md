# Every corpus AI skill — validation, 20 October 2026

The master skill is **[combined-ai-skill/SKILL.md](../combined-ai-skill/SKILL.md)**
in this Linear-A repository. Its registry covers 18 corpus projects. The separate
Egyptian Hieroglyphic Corpus is audited here as a nineteenth project, without
changing master membership. Lycian and Carian share a repository and skill;
Milyan has its own repository and skill. Photography and endurance projects are
excluded.

## Executable evidence

From a parent directory containing the named complete corpus checkouts:

```sh
python Linear-A/corpus-factory/validate_ai_skills.py --checkouts . --output ai-skills.json
```

From any corpus root: `python scripts/validate_ai_skill.py`.
Use Python 3.10+; only the standard library is needed. The check is read-only.
A JSON receipt at [ai-skill-validation-2026-10-20.json](ai-skill-validation-2026-10-20.json)
records source-parent commits, exact skill/bundle hashes, all indexed artifact
checks and source-grounded lookups. Native generated bundles must correspond to
the reviewed source files. Refresh with the native builder only after reviewing
changes; a fresh checksum does not certify a new scholarly assertion.

Each member's `AI skill functional checks` workflow builds its native index,
executes the current workflow and retains a JSON artifact. Local validation and
GitHub job results are separate evidence; a new source revision needs new checks.

## Directory and validated task scope

| Corpus project | Canonical skill | Working task scope |
|---|---|---|
| Linear A | [Linear-A/ai-skill/SKILL.md](https://github.com/hawkinsnick/Linear-A/blob/main/ai-skill/SKILL.md) | Native source/reference lookup, uncertainty and evidence-only research delivery |
| Cypro-Minoan | [Cypro-Minoan/ai-skill/SKILL.md](https://github.com/hawkinsnick/Cypro-Minoan/blob/main/ai-skill/SKILL.md) | Native source/reference lookup, uncertainty and evidence-only research delivery |
| Linear B | [Linear-B/ai-skill/SKILL.md](https://github.com/hawkinsnick/Linear-B/blob/main/ai-skill/SKILL.md) | Native source/reference lookup, uncertainty and evidence-only research delivery |
| Cretan Hieroglyphic | [Cretan-hieroglyphs/ai-skill/SKILL.md](https://github.com/hawkinsnick/Cretan-hieroglyphs/blob/main/ai-skill/SKILL.md) | Native source/reference lookup, uncertainty and evidence-only research delivery |
| Phaistos Disc | [Phaistos-Disc/ai-skill/SKILL.md](https://github.com/hawkinsnick/Phaistos-Disc/blob/main/ai-skill/SKILL.md) | Native source/reference lookup, uncertainty and evidence-only research delivery |
| Byblos syllabary | [Byblos-syllabary/ai-skill/SKILL.md](https://github.com/hawkinsnick/Byblos-syllabary/blob/main/ai-skill/SKILL.md) | Native source/reference lookup, uncertainty and evidence-only research delivery |
| Cypriot syllabic Greek | [Cypriot-syllabic-Greek/ai-skill/SKILL.md](https://github.com/hawkinsnick/Cypriot-syllabic-Greek/blob/main/ai-skill/SKILL.md) | Native source/reference lookup, uncertainty and evidence-only research delivery |
| Eteocypriot | [Eteocypriot/ai-skill/SKILL.md](https://github.com/hawkinsnick/Eteocypriot/blob/main/ai-skill/SKILL.md) | Native source/reference lookup, uncertainty and evidence-only research delivery |
| Eteocretan | [Eteocretan/ai-skill/SKILL.md](https://github.com/hawkinsnick/Eteocretan/blob/main/ai-skill/SKILL.md) | Native source/reference lookup, uncertainty and evidence-only research delivery |
| Lycian, Carian and Milyan | [Lycian-and-Carian/ai-skill/SKILL.md](https://github.com/hawkinsnick/Lycian-and-Carian/blob/main/ai-skill/SKILL.md) | Native source/reference lookup, uncertainty and evidence-only research delivery |
| Phrygian | [Phrygian/ai-skill/SKILL.md](https://github.com/hawkinsnick/Phrygian/blob/main/ai-skill/SKILL.md) | Native source/reference lookup, uncertainty and evidence-only research delivery |
| Anatolian Hieroglyphic | [Anatolian-Hieroglyphic/ai-skill/SKILL.md](https://github.com/hawkinsnick/Anatolian-Hieroglyphic/blob/main/ai-skill/SKILL.md) | Native source/reference lookup, uncertainty and evidence-only research delivery |
| Archanes Script | [Archanes-Script/ai-skill/SKILL.md](https://github.com/hawkinsnick/Archanes-Script/blob/main/ai-skill/SKILL.md) | Native source/reference lookup, uncertainty and evidence-only research delivery |
| Aegean Anomalous | [Aegean-anomalous/ai-skill/SKILL.md](https://github.com/hawkinsnick/Aegean-anomalous/blob/main/ai-skill/SKILL.md) | Native source/reference lookup, uncertainty and evidence-only research delivery |
| Lydian | [Lydian/ai-skill/SKILL.md](https://github.com/hawkinsnick/Lydian/blob/main/ai-skill/SKILL.md) | Native source/reference lookup, uncertainty and evidence-only research delivery |
| Sidetic | [Sidetic/ai-skill/SKILL.md](https://github.com/hawkinsnick/Sidetic/blob/main/ai-skill/SKILL.md) | Native source/reference lookup, uncertainty and evidence-only research delivery |
| Pisidian | [Pisidian/ai-skill/SKILL.md](https://github.com/hawkinsnick/Pisidian/blob/main/ai-skill/SKILL.md) | Native source/reference lookup, uncertainty and evidence-only research delivery |
| Milyan (Lycian B) | [Milyan-Lycian-B/ai-skill/SKILL.md](https://github.com/hawkinsnick/Milyan-Lycian-B/blob/main/ai-skill/SKILL.md) | Native source/reference lookup, uncertainty and evidence-only research delivery |
| Egyptian Hieroglyphic Corpus (independent) | [Egyptian/ai-skill/SKILL.md](https://github.com/hawkinsnick/Egyptian-Hieroglyphic-Corpus/blob/main/ai-skill/SKILL.md) | Museum object metadata/provenance/rights lookup; no verified reading fields |

## Defects addressed

- Correct the Cretan Hieroglyphic manifest's misspelled repository identity.
- Route the historical Phrygian and Milyan skill paths to their canonical skill.
- Add root-relative first-use commands, exact-ID examples and access checks to
  every canonical skill and README; instruction-only files are not corpus data.
- Return explicit structured rejection on invalid native delivery requests,
  replacing uncaught tracebacks without inventing missing records.
- Fingerprint the complete Egyptian skill's authority files and source commit;
  its prior index had six unhashed paths that its validator accepted.
- Replace obsolete marker-only sync scripts with the full native bundle builder.
- Fingerprint operational skill/manifest/check/guide files and add repeatable
  checks of every nonempty native collection, plus all Egyptian object records.

Bounded model-use examples and per-corpus limitations: [usage exercises](ai-skill-usage-exercises-2026-10-20.json). Raw development logs stay outside public corpus payloads; their hashes identify the local exercise artifacts, not independently inspectable scientific evidence.

## Evaluation method and remaining limits

Baseline native validators and native evidence/delivery tests were run before
repairs. Four separate fresh-context AI usage exercises used the raw repository
skills without being given the suspected bugs or expected lookup results. They
performed a real native lookup in all 19 corpora and applied source-specific
limits to unsupported reading/translation questions. Missing-ID requests exposed
the shared traceback defect. These are bounded, non-blinded development exercises,
not a representative model benchmark, pass-rate estimate or cross-platform claim.
No named scholar participated in or endorsed this validation.

Post-repair deterministic checks verify every indexed artifact hash and skill
identity, run native contract checks, retrieve one record from every nonempty
registered collection, compare the returned record with its independent exact
source pointer, and reject missing IDs. The Egyptian check cross-checks all 25
metadata records; it does not inspect local image bytes. Negative regression
checks cover changed/unbound evidence, unsafe/missing paths and CLI rejection.
The master validator and federated evidence workflows remain separate checks.

A passing result means this supplied skill works for its documented evidence
scope. It does not establish accepted readings, decipherment, physical identity,
independent witnesses, source completeness, source permissions, blinded AI
accuracy, Linear B calibration or independent expert acceptance. Existing source
and rights gates remain unchanged. A corpus with no verified transcription can
have a working metadata skill; it cannot truthfully supply verified translation.

## Published confirmation and frozen master replay

All 19 committed native skill receipts were fetched back from their exact
publication commits and matched the tested bytes. GitHub's new `AI skill
functional checks` workflow passed for every corpus. See the
[publication receipt](ai-skill-publication-2026-10-20.json) for per-corpus source
and artifact commits, tree identities and successful workflow URLs.

A post-publication master integration check detected that the frozen
`northwestern-published-revisions.json` still selected the previous adapter
implementation. Refresh the 18 exact source checkpoints, `research-delivery-fleet.json`
and `northwestern-exercises.json` together whenever their native implementation
changes. The repaired frozen set replays all 18 source checkpoints and all five
exercises; all five integration tests pass. This repairs implementation/snapshot
synchronization and grants no new scientific acceptance.

A second fresh-context post-revision use exercise completed all 19 first-use
validations and source lookups without an unexpected failure. All 18 query-corpus
missing-ID requests returned explicit exit 2 absence responses; Egyptian absence
was checked against its object manifest. These bounded exercises carry the same
non-blinded/model-accuracy limitations described above.
