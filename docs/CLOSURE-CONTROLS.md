# Exact-edition reference exclusions

All 23 source entries with absent or literal-missing reference routes now have explicit, source-pinned dispositions linked to researcher dossiers. Each is excluded from the exact-edition-target cohort. Their resolved edition URL is null and no recovered route is claimed. Other source entries and historical literals remain unchanged.

```sh
python scripts/evidence_query.py --record 'HT 113 ter' --collection source-documents
python scripts/evidence_query.py --record 'HT Wa 1147' --collection closure-controls
```

The control completes ACD-003's accounting/exclusion criterion. Recovering the 23 actual edition locators remains an explicit source-access follow-up. Context citations, source database pages and guessed offsets do not satisfy that follow-up.

## Replay and scope

```sh
python scripts/closure_controls.py --check
python scripts/test_closure_controls.py
```

The tests exercise actual researcher queries, exclusions/nulls and source-pin integrity, and reject inconsistent input evidence. Software controls establish no new expert approval, source reading, material determination or physical identity.
