# Northwestern research program: P0/P1 implementation

This is the implementation and verification record for the three P0 and four P1
recommendations recovered from the Northwestern Candidates Review conversation.
The work applies to all 18 registered language-corpus projects. Egyptian
Hieroglyphic Corpus and LightroomIsSlow remain outside this collection.

## Acceptance and limits

| Priority | Implemented control | Verification | Remaining scholarly scope |
|---|---|---|---|
| P0 evidence provenance | Native profile hashes, exact IDs and pointers, full unmodified records, source/rights context and per-view units | Every selected artifact verified; native reports and source-tamper rejection tests | File pointers do not complete missing edition/page/line attribution or independently verify context/dating |
| P0 facts versus hypotheses | Preserve corpus-specific categories and native records; evidence-only answers forbid added claims or altered citations | Mutation tests reject invented claims, payload changes and false acceptance | Native uncertain readings, source dependence and adjudication remain open |
| P0 reproducibility | Deterministic local research packages with scripts, source/context/license files and manifests | Repeated builds, all file hashes, unpacked offline exact rebuild in every member | Packaging grants no new rights; it is not a DOI deposit, raw-source reauthentication or external EpiDoc validation |
| P1 cross-corpus search | `federated_research.py` searches all native views with repository/collection/ID namespaces | Exact-record equality, scoped filtering, truncation and excluded-member rejection | Search does not merge physical objects, compare unrelated sign values or count independent witnesses |
| P1 defensible AI skills | All member instructions and master routing updated; exact evidence responses and refusal of unsupported inference | Deterministic citation/payload/claim rejection tests and native bundle validators | No empirical model-performance claim; assistant-created analysis still requires qualification and review |
| P1 research/teaching demonstrations | Five executable exercises over actual native evidence | Source tracing, federated retrieval, notation preservation, package replay, draft-review rejection | Workflow demonstrations establish no new historical conclusion or institutional endorsement |
| P1 validation and feedback | Revision-bound draft/submission workflow, reviewer/source disclosures and explicit maintainer gate | Incomplete, stale and falsely accepted submissions rejected; valid form remains unaccepted | Identity, expertise, access, independence and epigraphic judgment require real review |

`research-delivery-fleet.json` records exact native delivery-report and profile
hashes. `northwestern-hosted-leaf-checks.json` records the 17 non-master hosted delivery
and synchronization results. The dedicated **Northwestern research program**
workflow replays the exact 18 published source checkpoints; run
`python corpus-factory/verify_federated_snapshot.py --checkouts /path/to/checkouts`
to compare the saved audit and all five exercises against those checkouts.

`northwestern-exercises.json` records the five execution results, including
all 18 local package hashes. `northwestern-validation.json` records the commands
actually executed and their output. Each member's `analysis/research-delivery.json`
binds its explicit input files. These receipts are snapshots, not perpetual claims
about later repository heads.

## Run the program

1. Use the [corpus download directory](../combined-ai-skill/CORPUS-DOWNLOADS.md).
   Download/extract or check out each registered repository into one parent folder,
   retaining names such as `Linear-A` and `Cypro-Minoan`. Check out the exact
   revisions recorded in `northwestern-published-revisions.json` for this snapshot.
2. Install Python 3.12. Open a terminal in `Linear-A`. For the delivery tools and
   exercises, no third-party Python package is needed. The wider native checks
   retain their declared requirements.
3. Run the audit and exercises, replacing `/path/to/checkouts` with the parent
   folder containing all 18 repositories:

```sh
python corpus-factory/federated_research.py --checkouts /path/to/checkouts --audit
python corpus-factory/federated_research.py --checkouts /path/to/checkouts --exercises
python corpus-factory/test_federated_research.py --checkouts /path/to/checkouts
```

4. Search literal text across native evidence:

```sh
python corpus-factory/federated_research.py --checkouts /path/to/checkouts --search '?' --limit 10
python corpus-factory/federated_research.py --checkouts /path/to/checkouts --id 'HT 1' --repository hawkinsnick/Linear-A --collection source-documents
```

The question-mark exercise demonstrates preservation of literal notation; its
meaning is not assumed to be uniform across scripts, editors or text fields.
Each hit carries its native scope, artifact hash/pointer, context-resource routes
and member skill path. An absent record is a retrieval result, not proof that the
inscription does not exist. No pooled inscription total is reported.

5. For a bounded research question, open the member's `docs/RESEARCH-DELIVERY.md`.
   Retrieve its full dossier, read source and rights qualifications, make a local
   research package if needed, and generate a review draft for a specific target.
   The workflow sends nothing and does not mark a reading accepted.

## Five reproducible exercises

1. **Trace a claim:** follow a stable native ID to the complete source record,
   artifact SHA-256 and exact JSON pointer; separate that locator from missing
   bibliographic attribution.
2. **Compare retrieval coverage:** search a literal pattern across scripts,
   retaining per-collection units and source dependence instead of a pooled count.
3. **Inspect uncertainty:** retrieve native notation unchanged and verify the full
   payload against the exact-ID dossier; consult its source before interpretation.
4. **Reproduce a result:** rebuild local packages twice, check every manifest
   entry, then unpack and replay using the native regression suite.
5. **Prepare expert feedback:** create a bounded, revision-bound request; see the
   validator reject the blank draft as a completed review, then follow the native
   rules for an actual independently attributable response and maintainer check.

## What is still open

This delivers all seven engineering controls for the selected public views. It
**does not mean all scholarly P0/P1 issues are closed**. Current dependencies are
still routed by [the native human-validation matrix](HUMAN-VALIDATION-ROUTE.md),
`p1-human-readiness.json`, the [gap register](fleet-gap-register.json), and each
member's review packet and source/rights registers. Missing editions, permissions,
primary-source attribution/collation, object identity, calibration and independent
expert acceptance cannot be filled with generated data or relabelled as done.

No reviewers were contacted, institutional endorsement obtained, rights granted,
new canonical reading admitted, or empirical LLM performance measured in this
implementation. The deterministic evidence interface is a conservative means of
using the supplied records while those scholarly tasks remain visible.
