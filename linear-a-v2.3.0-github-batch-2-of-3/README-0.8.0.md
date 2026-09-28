# Linear A Open Corpus — 0.8.0-local

0.8.0 is the adversarial positional-robustness release.

The 22 source-word positional enrichments from 0.7.0 were challenged with
type deduplication, leave-one-document-out tests, leave-one-heuristic-group-out
tests, and removal of the dominant exact word type carrying each boundary sign.

**12 of 22 survive the full strict screen; 10 are downgraded
or context-sensitive under at least one control.**

The strongest survivor is AB008 word-initial. Other strict survivors are listed
in `analysis/0.8.0_summary.json`.

This release deliberately separates robust positional concentration from
morphological interpretation. No prefix/suffix/case/grammar meaning is assigned.

The inherited site grouping remains `site_group_heuristic`, not canonical site
metadata. `f3` remains unresolved/evidence-tiered and is not used for words.
