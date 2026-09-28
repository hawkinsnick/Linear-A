# 1.1.0 — canonical site-control release

1.1 replaces the opaque `site_group_heuristic` analysis path with an explicit,
reviewed document-identifier → canonical-site mapping table.

488 source-word documents map to 18 canonical
sites; 0 remain unmapped. The twelve frozen positional candidates
are rerun under leave-one-canonical-site-out sensitivity; 12
of 12 remain above z=1.96 for every site exclusion.

The mapping does not pretend that an identifier prefix is raw find-place metadata.
Direct per-record SigLA raw-find-place export remains a provenance enhancement.
