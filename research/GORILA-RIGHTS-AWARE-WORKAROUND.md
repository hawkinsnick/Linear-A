# GORILA rights-aware workaround (2026-10-19)

Status: **permission pending; no redistribution authorization received**. A final inquiry is planned for 2026-11-19. Silence is not permission.

## Scope
This plan is a workflow, not a claim that any GORILA-derived dataset has been imported or cleared. Do not mirror or bulk extract protected GORILA text, plates, photographs, editorial apparatus, or curated transcriptions. Do not use a public URL as evidence of a redistribution license. Assess database rights, terms of access, copyright, and jurisdiction before automated acquisition.

## Permitted-path workflow
1. Inventory independently sourced inscription identifiers, findspots, physical descriptions, dates, material, holding institutions, and bibliography; document provenance for each factual claim.
2. Store external references and stable links to GORILA and other catalogues, without copying restricted content.
3. Record transcriptions only when demonstrably independently prepared, public-domain, openly licensed for the intended use, or expressly authorized. Similarity and derivation review is required before publication.
4. Track each record's source URL or citation, source access date, creator, asserted license, evidence for license, rights jurisdiction, review status, and human verification status.
5. Keep ambiguous or disputed readings in separate evidence/interpretation fields, with alternative hypotheses and citations. Do not label machine-generated guesses as scholarly readings.
6. Validate identifiers, cross-references, provenance completeness, deduplication, reproducibility, and licensing before release.

## Rights statuses
- `independent_verified`: provenance documented and reviewed.
- `open_licensed_verified`: compatible license and attribution documented.
- `public_domain_verified`: public-domain determination documented for applicable jurisdictions.
- `permission_granted`: written permission and scope recorded.
- `restricted_reference_only`: bibliographic reference or link only; no source content copied.
- `unresolved_quarantine`: not exportable, pending legal or scholarly review.

Default all unreviewed GORILA-related material to `restricted_reference_only` or `unresolved_quarantine`. A factual identifier does not automatically authorize reproducing a curated dataset in bulk.

## AI skill requirements
All Linear A and combined corpus skills must enforce the above export gate, distinguish citation from license, avoid implying GORILA access or redistribution rights, and report blocked content transparently. Apply this rule in skill implementation and validation before asserting compliance.

## Release acceptance criteria
Zero unlicensed restricted content in distributed exports; 100% of published records have provenance and rights status; uncertain readings labeled; crosswalks reproducible; sample audit independently reviewed. Human expert validation remains a separate gate.
