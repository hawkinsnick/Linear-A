# Northwestern research readiness: Linear A pilot

This audit covers the committed public SigLA derivative: 802 source-document
entries, 5,144 attestation slots, 1,401 editorial groups and 376 sign entries.
These units overlap and are not unique physical-object totals. It does not
certify scholarly completeness, independent evidence or expert acceptance.

## P0 acceptance criteria and results

| Requirement | Executable criterion | Scope/result |
|---|---|---|
| Evidence provenance | Every native record has a unique ID, source hash, source pointer, attribution and license; source-group references resolve | Public derivative passes; publication routes remain unavailable for 23 document entries |
| Facts and hypotheses | Source documents remain unverified; editorial groups are not promoted to linguistic words; unestablished phonetic values stay null | Public derivative passes; historical hypotheses and unresolved alternatives retain their existing separate registers |
| Reproducibility | Source/output/generator hashes; exact full-record round trips for JSON, CSV, JSON-LD and TEI; deterministic package and offline rebuild | Automated regression suite covers all 12 resource/format combinations |

The machine-readable authority is `analysis/research-readiness.json`. Run its
validator instead of treating this prose as a fresh execution receipt.

## Repairs

The context extractor previously ignored source fields `typology` and
`dimensions_cm`. They now map to document type and dimensions, retain centimetre
units, attribution and input hash, and cite the exact source-field pointer.
Missing source values remain missing. This is source-field recovery, not a new
archaeological assessment. `analysis/evidence-population-coverage.json` reports
nonempty source values rather than inferred context.

Export manifests now identify the exact source file and upstream input hashes,
the generator script hash, output hash/size and scientific qualifications.
JSON-LD identifiers are opaque URNs, not advertised resolving inscription pages.
The TEI export preserves records as JSON notes; it is **not validated EpiDoc** or
a full semantic mapping. Round-trip equality does not establish interoperability
with external epigraphic software.

## Reproduce locally

From a checkout, using Python 3.12 and the standard library:

```sh
python scripts/research_readiness.py --check
python scripts/test_research_readiness.py
python scripts/build_research_package.py /tmp/linear-a-research.zip
```

The package contains the three public source views, 12 exports and manifests,
replay scripts, this guide and applicable rights notices. It includes no raw
SigLA payload, drawings, GORILA plates, private source PDFs or sealed experiments.
The ZIP stores fixed timestamps and ordered uncompressed entries, allowing exact
replay across zlib versions. Unpack it and run:

```sh
python scripts/research_readiness.py --check
python scripts/build_research_package.py replay.zip
```

Compare the resulting SHA-256 with the original package checksum. The internal
manifest covers every member except itself; the separate ZIP checksum binds the
manifest too. Hashes establish byte identity, not authenticity without a trusted
repository revision. Preserve the GitHub commit from which you obtained it.

GitHub Actions runs the checks on pushes and pull requests and attaches the
package plus checksum as run artifacts. Download the artifact for the exact
commit under review; run artifacts are not permanent DOI releases.

## Remaining scholarly and fleet work

A public source-page route is neither completed primary-edition collation nor
permission to ingest edition content. The 23 unavailable reference routes remain
explicit gaps. Source-reported dates, find contexts and bibliographic routes
require source assessment; no new bibliography, reading or expert agreement is
invented. The recorded EFA/GORILA refusal remains binding. Independent epigraphic
review, source access and known-answer calibration retain their existing gates.

This completes a bounded engineering implementation of the three P0 controls
for this public Linear A view. It does not close corpus-wide provenance research
or establish that other corpus members pass. Apply each member's native evidence
model and repeat the audit before propagating a readiness claim.
