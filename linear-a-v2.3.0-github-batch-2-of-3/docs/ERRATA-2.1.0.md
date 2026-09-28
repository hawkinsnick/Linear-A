# 2.1.0 post-2.0 errata

## E-001 — stale canonical-site count

The 1.1 summary recorded `18` canonical sites. Recomputing the released
`document_site_mapping.csv` yields `19` distinct non-empty canonical site IDs
across `488` mapped documents.

The released leave-one-site-out analysis iterated over the mapping table itself, so this
is presently classified as a summary/audit defect rather than evidence that one site was
omitted from that computation. The 2.1 audit now recomputes the count.

## E-002 — DĀMOS acquisition review false alarm

During the postmortem a broad GitHub release-list query did not surface the DĀMOS asset.
A direct lookup of tag `damos-corpus-v2` resolved the release and its asset:
`damos-corpus.json`, 3,104,186 bytes, GitHub digest
`sha256:eab9ccdfc4324b62f015bccd5e3f917f256cab8c058840842127eadecfbca2d2`.

This restores the previously recorded artifact identity. The episode is retained because
it demonstrates that absence from an incomplete listing is not evidence of non-existence.
