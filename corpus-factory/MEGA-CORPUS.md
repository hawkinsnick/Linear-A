> Current evidence-growth checkpoint: **18 members / 10,527 heterogeneous view rows**. Earlier totals below are historical. [Scope and source boundaries](AVAILABLE-EVIDENCE-GROWTH-2026-10-12.md).

# Mega corpus research package

The expanded package materializes **18 language corpora and 9,562 native view rows**. The original 9,116-row build remains a historical baseline. It includes the existing source-bound readings and browser context, reconciliation apparatus where supplied, individual AI instructions and licensing information. These rows include catalogue entries, source records, groups, sentences and text rows; they overlap and are not a unique-inscription total. No new ancient evidence or expert acceptance is claimed.

This is a reproducible private research package. The public repository supplies the builders and aggregate verification receipts; it does not redistribute restricted A/B derivatives or grant new rights over other components.

## Native view coverage

| Repository | Declared materialized views (rows) |
|---|---|
| Linear-A | authenticated-records: 802 |
| Cypro-Minoan | catalogue-slots: 254; rich-records: 21 |
| Linear-B | authenticated-records: 5932 |
| Cretan-hieroglyphs | CHIC-spine: 331 |
| Phaistos-Disc | disc-object: 1; disc-groups: 61 |
| Byblos-syllabary | catalogue: 39 |
| Cypriot-syllabic-Greek | IGXV1-entries: 592; BBAW legacy syllabic squeeze identifiers: 210 |
| Eteocypriot | IGXV1-candidates: 25 |
| Eteocretan | attributed-readings: 12; coverage-objects: 11 |
| Lycian-and-Carian | ediana-reference: 453 |
| Phrygian | canonical: 0; ud-reference: 203; k01-catalogue: 8 |
| Anatolian-Hieroglyphic | full eDiAna digital-entry dossiers: 287 |
| Archanes-Script | Decorte-baseline: 16 |
| Aegean-anomalous | quarantine-candidates: 2 |
| Lydian | ediana-records: 118 |
| Sidetic | ediana-records: 11 |
| Pisidian | ediana-records: 54 |
| Milyan-Lycian-B | provisional-bibliography: 3; ediana-reference-records: 2; ediana-reference-text-rows: 114 |

## Build and use

1. Download/check out the 18 members listed in `combined-ai-skill/CORPUS-DOWNLOADS.md` into one parent directory. Keep repository names and origins intact.
2. For private Linear A/B views, materialize the exact admitted source snapshots with each native `scripts/build_pre_expert_audit.py`. The native source audit gives their SHA-256 and local export hashes. Do not acquire protected GORILA images or perform new GORILA extraction.
3. Run `python corpus-factory/build_mega_corpus.py --checkouts /path/to/checkouts --output /path/outside/repos/mega-corpus --include-local` in Linear A. Omit `--include-local` for the declared public-view subset; it explicitly reports the two omitted private views.
4. Run `python corpus-factory/build_mega_corpus.py --output /path/to/mega-corpus --verify --expected-manifest-sha256 HASH_FROM_YOUR_BUILD_RECEIPT`.
5. Search with `python corpus-factory/query_mega_corpus.py /path/to/mega-corpus --repository hawkinsnick/Cretan-hieroglyphs --text CHIC-328 --limit 5`.

Each result preserves its native payload and links to its component context. The package key namespaces repository, view and native ID; it is not a physical identity join. Read the original member skill, source roles, rights and reconciliation context before interpreting a match. Comparisons may retrieve conflicting assertions; retrieval does not adjudicate them. Missing links mean unknown, and member views are not pooled as independent witnesses.

## Growth and calibration

This package is the materialized baseline for continued breadth and depth work, not a claim that the mega corpus is maximal. Expand explicit native populations and source-qualified readings first, rebuild the package when inputs change, and preserve source-dependent alternatives. Independent expert acceptance follows the largest lawful and machine-reconciled evidence package. Source access and component permissions necessarily run alongside growth because they govern what can be included.

Linear B has a separate answer-free observation package of 5,932 records. Source word-ID alignment, linguistic annotations and certified graphical occurrences remain missing. Never substitute this mixed research package for blind linguistic gold. It contains attributed interpretation layers and should not be exposed to a blinded experiment as observations.

The builder refuses missing declared inputs, hash drift, identity collisions, sealed/prohibited data paths and an existing output directory. Verification checks payloads, context and licenses; hostile tests cover uncertainty loss, source drift and false acceptance. The package grants no redistribution permission and performs no decipherment or scientific calibration.

A CI workflow rebuilds the actual full 18-member package from exact A/B input bytes and native repositories, validates it, and publishes only aggregate receipts. Corpus source payloads are not uploaded as CI artifacts.

The actual local build and package SHA-256 are recorded in `mega-corpus-build-2026-10-12.json`. This is a historical source-bound receipt; later native source changes require a new package and manifest, not silent reuse of old hashes.

The authenticated private A/B auxiliary exports also travel with the package, under their own native hashes. In particular, Linear A's 5,144 source occurrence slots and 1,401 source-defined word groups are retained; they are not newly admitted readings, linguistic words or additional independent witnesses. Native export metadata and attribution remain attached.

## Geographic and dossier expansion — 2026-10-12

All 287 Anatolian digital-entry dossiers replace the previous overlapping 19-ID/32-portable-row views. This integrates existing reconciled evidence: 280 entries have principal-reference fields, 32 explicit class assertions and 255 unknown classes; no new reading is admitted. The full bibliography, source notices and period candidates remain qualified. Cypriot Greek adds 210 source-identifier rows from BBAW's legacy syllabic squeeze catalogue, including 138 Rantidi labels. Casts, fragments and uncertain geographic labels remain intact; language and IG/object joins remain unadjudicated. Its 170 admitted source-interpreted Greek entries and existing frequency population are unchanged.

The net increase of 446 is a change in heterogeneous indexed rows, not 446 new inscriptions or independent witnesses. See [the expansion report](COVERAGE-EXPANSION-2026-10-12.md) and its source-bound actual package receipt. Neither integration nor discovery enumeration completes direct edition collation.
