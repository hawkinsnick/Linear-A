# Cross-project roadmap: Linear A + Cypro-Minoan

## Current rule
Keep `hawkinsnick/Linear-A` and `hawkinsnick/Cypro-Minoan` as separate repositories with independent main branches, releases, source histories, rights, sign systems and scientific claims.

## Phase I — harmonize interfaces (now)
- Publish the Aegean Epigraphy Interoperability Contract in both projects.
- Add native-to-interchange mapping documentation.
- Keep all corpus bytes and script-specific models local to their repositories.
- Use the second corpus as an adversarial test: a proposed "generic" abstraction is rejected if it silently assumes Linear A/SigLA or Cypro-Minoan conventions.

## Phase II — prove shared demand
Extract candidate shared validators only when both repositories independently use them: provenance validation, rights checks, assertion validation, lineage/independence accounting, manifest generation, claim/errata checks.

## Phase III — shared toolkit
Create a separate `aegean-epigraphy-core` repository/package only after the interfaces stabilize. It should contain code and neutral schemas, not duplicated corpus data.

## Phase IV — comparative tools
Build cross-script analyses over adapters: recurrence, positional distributions, entropy, document clustering, graph structure and uncertainty sensitivity. Preserve each corpus's observational units and null models.

## Phase V — Linear B
Add Linear B as a third adapter/control corpus after the neutral core has survived both undeciphered corpora. Deciphered-language morphology and phonetic values remain optional extensions, never core requirements.

## Governance test
No shared-core change may force one corpus to encode an unsupported observation merely to satisfy another corpus's model.
