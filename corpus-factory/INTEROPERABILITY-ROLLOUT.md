# Fleet interoperability rollout

## Gate A — EpiDoc
Every applicable corpus must declare: native record unit; mapping coverage; reversible fields; one-way/lossy fields; rights exclusions; validation command; and an export manifest. Existing “EpiDoc-compatible” outputs are provisional until tested against this contract.

## Gate B — Universal identity graph
Every corpus must distinguish project record, physical object, text-bearing surface, text, edition assertion, place, collection, bibliography and external catalogue identity where those concepts exist. Edges require evidence and certainty. Negative/disputed joins are retained.

## Rollout order
1. Linear A — harden existing exporter and map SigLA/project/source identities without violating the GORILA firewall.
2. Phrygian — identity-graph pilot already active; extend TM/TITUS/catalogue/object joins only when record-specific evidence exists.
3. Linear B — DĀMOS/catalogue/tablet/scribe/place identity graph plus EpiDoc mapping.
4. Cypro-Minoan and Cretan Hieroglyphs — object/text/surface/sign identities and uncertainty-heavy EpiDoc mappings.
5. Remaining alphabetic corpora — TM/Pleiades/museum/edition concordances, then EpiDoc.
6. Small/disputed corpora — use the same contracts but permit explicit NOT_APPLICABLE fields rather than fabricated metadata.

## Completion
A corpus is fleet-interoperable only when both gates are machine-tested. Passing either gate is not scholarly validation.
