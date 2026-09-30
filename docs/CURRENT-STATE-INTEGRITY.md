# Current-state integrity milestone

Repository version: 3.0.11.

Authenticated SigLA v3/v4 descriptive comparison: 781 → 802 documents, 5,065 → 5,144 attestations, 1,376 → 1,401 source-word groups. Seven of 24 frozen cohort labels are present in v3. Historical analytical input identity/independence remains unresolved; prospective outcomes remain sealed. The 2.5 multiverse implementation remains quarantined.

The current-state validator parses every committed JSON file, checks schema validity, citation/family metadata, evidence digests, interchange positive/negative fixtures, native committed counts where available, and blocked-claim boundaries. Regression tests deliberately corrupt metadata and restore it. CI runs these checks on pushes and pull requests.

Artifact content versions are independent of the repository release. Unchanged inscription records, historical baselines, protocols and audits retain their content versions. Mutable current metadata (VERSION, citation, current status, family member version, current index/API examples/manifest) follows the repository version. A software validation pass does not certify epigraphic correctness or open a scientific gate.

## Reproduce the descriptive SigLA delta

Download the upstream `sigla-corpus-v3` and `sigla-corpus-v4` assets locally, retain their CC BY-NC-SA attribution, then run:

```sh
python scripts/compare_sigla_snapshots_2_4_1.py /path/to/v3.json /path/to/v4.json --expected-old-sha256 683fa0147f2b923a78f7c2c1da95cf42d8c05563f9ed53c5dfa8e520f4e38569 --expected-current-sha256 9a5e4783146144fc5ac54c5dc2b372b39cc0e0ea40ca15207243f8c539f03dd8 --out /tmp/sigla-delta.json
```

The committed report is `analysis/sigla-v3-v4-descriptive-delta.json`. This is a derivative-to-derivative descriptive comparison; v3 has not been authenticated as the original analytical baseline. No candidate scoring is performed.
