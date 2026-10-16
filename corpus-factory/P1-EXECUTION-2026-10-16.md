# P1 execution checkpoint — 16 October 2026

Requested order: refresh the central register, investigate attribution/identity gaps, then continue primary-edition comparison. The register refresh is complete across all18 members. The source work made bounded progress; it does not close every P1 or certify scholarly acceptance.

## Register reconciliation

`fleet-gap-register.json` now pins each member's native authority paths, exact Git revision and SHA-256 values. The39 pinned authority blobs were replayed from local Git objects. CM's stale16-occurrence/nine-record summary is replaced by28 encoded occurrences on13 of21 rich records; eight remain without encoded occurrences. These are occurrence/record units, not physical-object counts. TL55 documentary flag accounting and historical count-voice reconciliation are complete within their declared scope. TL44 has105 page/label routes, not105 sign collations. The supplied LW40 and Sidetic2025 PDF checks are recorded as completed consultation rather than missing acquisition.

## Attribution and source work

| Member | Executed work | Retained boundary |
|---|---|---|
| Phrygian | Reacquired both registered publication PDFs; visually checked four printed pages. Two source-role/restoration dispositions now link to exact UD reference records in native queries. | General formula does not support an object-fragment reading. Conditional longer restoration remains attributed. Both TM catalogue routes returned502; external identity and upstream intent remain open. |
| Eteocypriot | Reacquired entry150 XML, replayed parse failure and exact historical byte identity. Added a queryable quarantine disposition. | HTTP200 is not valid parsed evidence; no raw repair, language decision or record admission. |
| Sidetic | Acquired and visually consulted all12 leaves of Darga's early Seleukeia publication, including its plates. Added four source-qualified comparisons, linked to the exact S6 digital record. | Historical numbering and source-date conflicts remain distinct. No present-location certification, object autopsy or phonetic-value adoption. Brixhe–Neumann1988 itself remains unconsulted. |

The seven new disposition records and16 rendered-page consultations are documentary work units, not inscriptions, independent witnesses or accepted readings. The3 native packets, query profiles, required AI authorities and guides are synchronized. Source PDFs/images are excluded from GitHub. Ordinary public consultation supplies no general reuse permission.

## Remaining work

`p1-current-work.json` lists the residual evidence for every follow-up and each member's broader native frontier. Immediate acquisition targets include Olivier2007 source pages, the two modern TL44 articles, direct Brixhe–Neumann1988 consultation and the other2025 Abydos edition. A publisher PDF request for the latter returned an empty202 response, not an acquired article. Existing permission refusals, protected images/RTI and independent-review gates remain controlling. No messages, purchases or institutional access requests were sent.

CH material conflicts, CM positional/identity alternatives, Eteocypriot item-level joins, wider edition coverage and other native source work remain open. The source-access and judgment requirements are explicitly retained; they are not renamed completed expert review. The next pass should use those exact native worklists, not repeat completed TL55 documentary accounting or supplied-PDF typography checks.

## Replay

Run `python corpus-factory/validate_p1_refresh.py --checkouts /path/to/checkouts` to replay immutable authority and follow-up packet bytes. Fetch the recorded revisions first if checkouts are shallow. Run `python -m unittest discover -s corpus-factory -p test_p1_refresh.py` for rejection tests. In each changed member, run `python scripts/p1_source_followup.py`, its native-query replay, tests and AI validator. Optional `--verify-source SOURCE_ID /path/to/local/file` checks a lawfully acquired source against its recorded bytes; byte identity does not prove epigraphic truth.

Validation command receipts and explicit skipped/excluded scopes are in `p1-validation-2026-10-16.json`. Native full unittest discovery:60/54/55 cases across Phrygian/Eteocypriot/Sidetic, with two upstream-dependent skips total. Central corpus-factory tests:46 passed; master package tests:19 passed. No browser or new pinned upstream EpiDoc run is claimed.
