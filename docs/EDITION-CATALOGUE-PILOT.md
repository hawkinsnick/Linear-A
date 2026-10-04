# Edition labels and counting units: GORILA II pilot

The [comparison table](../research/edition-catalogue-comparison.csv) records **20 source entries** on four inspected primary-edition pages. Each row supplies the printed page, viewer page, stable source URL, acquired image digest, exact edition heading/panel and historical catalogue caption. Inspection was by AI; independent expert review remains pending.

| GORILA II printed page | Viewer page | Source entries | Edition presentation |
|---|---:|---|---|
| 2 | 64 | GO Wc 1a, GO Wc 1b | One heading GO Wc 1, two panels a/b; HM 83 caption below a |
| 4 | 66 | HT Wa 1001–1005 | Five individually numbered panels and captions |
| 5 | 67 | HT Wa 1006–1013 | Eight individually numbered panels; Haghia Triada nodules section heading |
| 6 | 68 | HT Wa 1014–1018 | Five individually numbered panels and captions |

The source entries comprise **19 edition parent units**. This is an edition-level grouping, not a count of certified physical objects. GO Wc 1a/b retain distinct source IDs while sharing the printed parent heading and caption. Its caption dimensions, 3,50 × 3,50 × 1,00 cm, apply at that parent-caption level; they are not separate measurements of both panels. The HT prefix is inherited from the section/source attribution: it is not printed beside every Wa heading.

Historical captions include HM numbers and Pigorini 5. These are edition-reported labels, not a verified modern museum accession crosswalk. No sign readings are adjudicated, catalogue labels promoted to certified object identities, or Raison–Pope joins closed. Drawings and photographs remain private. All SigLA-derived IDs and routes retain CC BY-NC-SA 4.0 and Ester Salgarella/Simon Castellan attribution via Ryan Pavlicek/pyaegean; edition caption facts are attributed to Godart and Olivier, GORILA II (1979).

Reproduce the table and its unit accounting with:

```sh
python scripts/build_edition_catalogue_pilot.py --check
python scripts/test_edition_catalogue_pilot.py
```

With authorized local images, add `--verify-assets /path/to/gorila-route-assets`. This metadata pilot is separate from the ten-entry [critical pilot](CRITICAL-PILOT.md) and does not extend its amount or transcription coverage. The larger acquired collection still requires target-specific inspection.
