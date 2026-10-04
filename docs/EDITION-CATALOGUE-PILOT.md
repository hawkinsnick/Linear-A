# Edition locators, captions and counting units

The [comparison table](../research/edition-catalogue-comparison.csv) covers **all 135 acquired GORILA pages**, linked to 222 SigLA source entries. AI visual inspection confirms **220 target headings**; two HT 53 face records point to a page showing HT 52 a/b instead. Their original links remain preserved, their edition headings and parent units stay null, and no replacement route is adopted from a pagination offset alone.

| Review scope | Pages | Meaning |
|---|---:|---|
| Selected caption and metadata review | 43 | Historical labels, dimensions and qualifications where legible; unresolved observations retained |
| Pagination and target-heading review only | 92 | Captions explicitly uncollated, not absent |
| Total acquired-page review | 135 | Does not include the 232 routes without completed acquisitions |

Each row retains printed and viewer pagination, source URL and acquired-image SHA-256. The 220 confirmed source targets group into **167 edition parent units**, not certified physical objects. GO Wc 1a/b share one edition parent; uppercase HT 154 suffixes remain distinct edition entries. Two mismatched HT 53 records contribute no confirmed parent. The 51 distinct non-null caption strings include unassigned dash labels and compound labels: they are not 51 certified accessions.

The reviewed primary pages preserve several distinctions:

- HT 42 [+] 59, HT 62 [+] 73 and HT 79 [+] 83 retain bracketed join notation that source IDs flatten. No physical join is certified.
- ARKH 1 reports three captioned fragment items and four additional separate fragments. Fragment dimensions are not summed into one size or seven certified object identities. ARKH 3/4 b faces retain explicit relations to captions on a, without inventing b captions.
- HT 12 reports HM 2 (moulage), with unknown thickness. Cast metadata is not an independently measured original.
- HT 114's first inventory digit and HT 115's thickness remain unresolved; candidate observations do not become adopted values.
- HT 123's compound HM 1367 + 1371 caption remains an edition report. HT 126's historical absence note does not establish present custody.
- HT 109's proposed join is questioned in the edition. The neighbouring HT 113 ter and HT 67 panels are excluded from the linked entries on those pages.
- HS Zg 1 is captioned as a schist plaque, with a printed scale. No dimensions are inferred from screen pixels.

Inspection was by AI; independent expert review remains pending. Catalogue captions are historical edition reports, not a current museum crosswalk. No sign readings are adjudicated or Raison–Pope joins closed. Primary photographs and drawings remain private. SigLA-derived IDs and routes retain CC BY-NC-SA 4.0 and Ester Salgarella/Simon Castellan attribution via Ryan Pavlicek/pyaegean; primary edition facts are attributed to Godart and Olivier, GORILA, with the volume and page retained per row.

Reproduce the metadata table and accounting:

```sh
python scripts/build_edition_catalogue_pilot.py --check
python scripts/test_edition_catalogue_pilot.py
```

With authorized local images, add `--verify-assets /path/to/gorila-route-assets`. This layer remains separate from the ten-entry [critical pilot](CRITICAL-PILOT.md) and does not extend its amount or transcription coverage. Full caption collation, remaining page acquisition, Raison–Pope reconciliation and independent sign adjudication remain open.
