# Linear A: joined legacy-case attribution pass

All10 exact joined legacy cases from the critical pilot; five unjoined cases remain outside this attribution pass. Bounded source-history and publication checks, not exhaustive literature search or new epigraphic collation.

All ten cases now have an explicit attribution disposition and remaining evidence gap. None has two attributed readings aligned to the same locus. The old queue and historical registers remain unchanged; this audit qualifies their unsupported claims rather than silently rewriting history.

## Findings

- HT17: the authenticated SigLA export has no account-quantity field. A sign identifier numbered37 is not the account quantity37. The old attribution of37 to that export is unsupported; its actual origin remains untraced.
- KH8: A567 and A510 occur at different source slots. The RC2 and original queue do not identify one aligned locus. Do not treat these identifiers as interchangeable alternatives.
- MA10b: the identified Consani2002 passage supports a related vessel-sign discussion, not the full legacy pair. The early register gives no precise Consani publication or locator.
- KNZc6: Flouda’s punctuation report is attributable. Its correspondence to the queued before-IZU break, linguistic function and independent physical adjudication remain unestablished. An old project status saying a physical feature was resolved does not establish these claims.

## Case-by-case ledger

| Case | Source record | Disposition | Remaining evidence needed |
|---|---|---|---|
| U001 | HT 17 | QUANTITY_ATTRIBUTION_GAP | Recover an attributed source and exact account locus for37. The claimed conflict needs two source-specific numerical assertions at the same locus; do not use sign-number37 or recopy restricted editions. |
| U002 | HT 15 | ONE_SOURCE_COMPONENT_RELATED_OTHER_UNTRACED | Find the specific publication and locus for the L4L4 reading and establish how each author renders the compound. Do not infer a fraction value or correct a sign from typographical resemblance. |
| U003 | HT 17 | ENCODING_AND_VARIANT_ATTRIBUTION_GAP | Recover the literal private-use code point, font/sign chart, named author and occurrence locator; recover the source of the suffixA before testing identity. |
| U004 | HT 34 | ONE_SOURCE_SEQUENCE_RELATED_OTHER_UNTRACED | Recover the author, exact notation and locus for SII, then compare the same position while preserving uncertain composition. A numeral-style sign identifier is not a word reading. |
| U005 | HT 34 | BOTH_LEGACY_WORD_READINGS_UNTRACED | Locate a named source and precise occurrence for each claimed word reading. Establish the same locus before treating different composite-sign slots as variants of a word. |
| U006 | HT 49a | SOURCE_SEQUENCE_WITH_UNTRACED_DAMAGE_ALTERNATIVE | Recover the source behind SU + VESST or SU-[damaged], including the original editorial abbreviation and position; do not turn an editorial vestigia/damage label into a sign or a modern lexical token. |
| U007 | KH 74 | COMPOSITE_NOTATION_WITH_UNTRACED_805 | Recover the named source, notation system and same-locus evidence for805; determine whether the legacy301MI rendering is a decomposition convention rather than a different physical sign. |
| U008 | KH 8 | LEGACY_LOCUS_CONFLATION_IDENTIFIED | Resolve whether the legacy case targets slot11, slot14 or another locus. Recover the source of QA2PU and its notation before comparing it to either identifier. |
| U009 | MA 10b | PARTIAL_SCHOLARLY_CONTEXT_NOT_LEGACY_PAIR | Identify the source of each complete legacy string, its notation and locus. Distinguish adjacent vessel compounds from alternative readings of one occurrence; do not infer new GORILA-derived structured readings from the discussion. |
| U011 | KN Zc 6 | PUNCTUATION_REPORT_RECOVERED_WORD_BREAK_UNALIGNED | Map the claimed before-IZU locus to the same spatial positions as the author’s punctuation statement, using permissible original evidence. Separate a punctuation observation from the hypothesis that it divides linguistic words. |

## Identified scholarly context

- **CONSANI2002**: Carlo Consani (2002), “Double writings” in Minoan Linear A, Collectanea Philologica 4, 15–25. Printed p.16, last portion of §1; PDF ordinal 2. Consultation: Repository PDF, printed page visually inspected. [Source](https://dspace.uni.lodz.pl/xmlui/bitstream/handle/11089/51333/Consani_15-25.pdf?isAllowed=y&sequence=1).
- **SALGARELLA2022**: Ester Salgarella (2022), Mix and Match: A Combinatory (Re-)Classification of Linear A Signs, TALANTA 54, 31–52; accepted manuscript DOI 10.17863/CAM.75845. Accepted DOCX word/document.xml, zero-based paragraph54, A605 example; not journal pagination. Consultation: Author accepted DOCX, paragraph text inspected. [Source](https://api.repository.cam.ac.uk/server/api/core/bitstreams/70a9babb-6286-4a27-a52f-44f2f04bd389/content).
- **FLOUDA2013_REPRINT**: Georgia Flouda (2013), Materiality of Minoan Writing: Modes of display and perception, in Writing as Material Practice, 143–174; DOI 10.5334/bai.h. LibreTexts §Alignment and Directionality, paragraph beginning “The readability”; zero-based HTML p index38, section_3. Consultation: Scholarly reprint HTML inspected; original PDF not acquired. [Source](https://socialsci.libretexts.org/Bookshelves/Anthropology/Archaeology/Book:_Writing_as_Material_Practice_-_Substance_Surface_and_Medium_(Piquette_et_al.)/08:_Materiality_of_Minoan_Writing-_Modes_of_Display_and_Perception_(Georgia_Flouda)/8.04:_Linear_A_-_The_social_and_cultural_construction_of_Neopalatial_literacy).

These are three qualified publication contexts across three cases: one general sign-class discussion, one related vessel-sign discussion and one punctuation report. They are not three recovered alternative pairs. Accepted DOCX paragraph numbers do not establish final journal pagination. The original PDFs/HTML/DOCX and images are not redistributed.

## Project history

The earliest observed Git archive `b06c90ca15907b085375e5270bae104c418abe2d` contains `linear-a-v2.3.0-github-batch-2-of-3/data/unresolved_cases.csv`. Its queue bytes match the normalized current CSV. All15 rows entered together without per-reading scholar/publication/locator columns. This identifies project ingress, not the source or authorship before upload. GitHub account authorship is not scholarly attribution.

## Query and verification

```sh
python scripts/legacy_case_attribution.py --summary
python scripts/legacy_case_attribution.py --case U008
python scripts/legacy_case_attribution.py --check
python scripts/test_legacy_case_attribution.py
```

`query_critical_evidence.py --record` returns this attribution overlay beside the unchanged historical cases. The corpus-native evidence profile also exposes an `attribution-audit` collection. Consult this audit before interpreting the old RC2, visual-evidence and branch labels as sourced scholarly disputes.

## Boundaries and next evidence

Source-specific terms remain applicable. SigLA-derived identifiers/fields retain CC BY-NC-SA4.0 and Salgarella/Castellan attribution through pyaegean. Original audit notes and bibliographic references are not a licence grant over the modern publications. Historical GORILA inspection records are referenced only as existing audit history; no new restricted reading is extracted.

The historic GORILA quantity assertion is referenced only as existing audit history. No new GORILA-derived transcription or restricted downstream payload was acquired or reconstructed. A failed URL or unsuccessful search is not a finding that a publication or reading does not exist. The finite attribution pass is complete; scholarly resolution, occurrence alignment and expert review are not.
