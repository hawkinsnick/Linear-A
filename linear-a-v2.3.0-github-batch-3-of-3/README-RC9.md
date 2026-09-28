# Linear A Open Corpus — 0.4.0-rc9-local

RC9 is a boundary-forensics release.

The published/reference extractor identifies attestation field `f3` as
**word-boundary state** and cites `Bound.t = Here | Unsure | Not_here`.
However, the extractor's normalized `bounds.start` / `bounds.end` values in the
validated snapshot range from 0 to 19. They therefore cannot
themselves be the three OCaml variant constructors.

RC9 explicitly **rejects** the tempting 0=Here, 1=Unsure, 2=Not_here mapping.

Observed adjacent interval relations:
- touch (`previous.end == next.start`): 1367
- gap: 1094
- overlap: 1497

A `touch-contiguous` segmentation is computed only as a structural hypothesis.
It yields 3352 segments, of which 347
have length >=3, and 4 strong variable-slot families. These are
not labeled words.

The semantic mapping remains open pending the upstream importer definition or
occurrence-level validation against explicit physical separators such as KN Zc 6.

This is a correction release: the failed enum interpretation was detected
during RC9 and is not retained as a result.

Nothing has been published to GitHub.
