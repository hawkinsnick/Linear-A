# Research history: 0.3.0 through 0.7.0

This document records the consolidated research state developed after the 0.2.0 corpus architecture.

## 0.3.0 — reproducible SigLA decoding

A local, opt-in SigLA importer and minimal OCaml Marshal decoder were developed. Raw upstream payloads remain excluded from the repository. Two separately implemented executable decoding paths, checked against the published reference field semantics and run on the same SigLA snapshot, agreed on all 5,144 attestations across 46,296 compared fields. This validates the tested decoding/extraction semantics; it does not establish epigraphic correctness or decipherment.

Snapshot invariants: 802 decoded documents; 5,144 attestations; 4,712 confident; 44 doubtful; 388 unreadable/unclassified; 104 erasures; 7 ghosts.

## 0.4.0 — reconciliation, uncertainty and structural forensics

0.4 introduced source-specific observations, paleographic observations, numeral/hypothesis branches, visual-evidence tracking and explicit reconciliation rather than silent correction.

Cross-witness work isolated the AB21/AB22 family, numeral alignment defects, sign-identity disagreements and segmentation/damage cases. KN Zc 6 received independent published support for a physical punctuation separator, while its linguistic function remains unasserted.

Computational RCs explored frequency, structural adjacency, positional concentration, motifs, variable-slot frames and source/site portability. Several early boundary models were deliberately superseded:
- RC7 sliding-window variable-slot families were exploratory and affected by a confidence-filter bridging problem.
- RC8 zero-boundary segmentation was a stress test, not a semantic interpretation.
- RC9's attempted small-enum interpretation of f3 was falsified by the observed integer range.
- RC10–RC15 retained f3 as evidence-tiered structural data rather than asserting universal word coordinates.

Final f3 policy: preserve raw topology/pair values/evidence tier; semantic interpretation remains unresolved.

## 0.5.0 — context-aware architecture

Added provenance-bearing document context, field-level context assertions, typed structural units and a machine-readable analysis-eligibility matrix.

Critical invariant: candidate_f3_group != source_word.

Structural units distinguish source words, source sign groups, physical lines, physical-separator groups, candidate f3 groups and analytical windows.

## 0.6.0 — explicit SigLA Word objects

The serialized document object graph was found to contain explicit Word lists, independently of f3. The decoded snapshot contains 1,401 serialized Word objects: 1,283 nonempty and 118 empty. Six current-page word-count checks agreed 6/6; no malformed membership lists or duplicate occurrence IDs were found in the nonempty words.

Document type, find-place and optional period were decoded from document metadata. Dimensions remain withheld pending independent float validation.

Within source-defined words, 121 recurring directed adjacency pairs were tested under 500 within-word permutations; 54 positive pairs survived BH q <= .05. These are structural enrichments under the stated null, not phonotactic or morphological claims.

## 0.7.0 — source-word analytical release

Across 1,283 nonempty source-word tokens there are 836 distinct types, 668 hapax types and 168 recurrent types. Word lengths are concentrated at 2–3 signs.

A 1,000-permutation within-word positional null tested 116 sign/position cases; 22 positive cases survived BH-FDR q <= .05. Strong examples include AB008 and AB081 word-initial, and AB002 and AB024 word-final.

There are 79 variable-slot families under the stated recurrence criterion, but the within-word shuffle null has mean 74.37 and empirical upper-tail p = 0.0598 (300 permutations). This does not meet the conventional .05 threshold under that test.

The release also records 4,681 Hamming-distance-one links and 651 form pairs related by one added initial/final sign. These are form-distribution candidates only; no prefix, suffix, morpheme, grammar, phonotactics, translation or decipherment is asserted.

### 0.7 site correction

The site_id field inherited from the first 0.6 export was document-label-prefix derived. It is corrected to site_group_heuristic in the 0.7 methodology. Cross-group portability based on that field is descriptive sensitivity only, not canonical source-explicit site metadata.

## Licensing

SigLA-derived records and aggregates retain applicable CC BY-NC-SA 4.0 obligations. Raw SigLA payloads, drawings and GORILA plates/text are not redistributed. Third-party validation source code is not redistributed.
