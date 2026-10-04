# Downloadable SigLA source layer

Download the [802 source documents](../research/sigla-source-documents.jsonl), [1,401 source editorial groups](../research/sigla-source-groups.jsonl), and [376 source sign entries](../research/sigla-source-signs.jsonl). On GitHub, open a file and select **Raw** to save it. JSONL contains one JSON record per line. Researchers can load these files into their analysis software or AI alongside this guide and the [critical pilot](CRITICAL-PILOT.md).

This is one checksum-authenticated SigLA derivative, attributed to Ester Salgarella and Simon Castellan via Ryan Pavlicek/pyaegean. Retain **CC BY-NC-SA 4.0**, attribution and the provenance fields in every reuse. These source data are not relicensed under the repository software license. No primary-edition images or SigLA drawings are bundled.

All 5,144 source attestation slots survive, including blanks, uncertain labels and undecoded raw flags. Source sign numbers are not account quantities. Editorial groups are not established linguistic words; conventional display values do not establish Linear A phonetics or equivalence with Linear B. Missing sign keys remain missing. These 802 entries do not certify 802 physical objects or exhaustive inscription coverage.

Document fields preserve the authenticated input except the reference URL: volatile `ce` query parameters are removed from public routes. Each original URL has an input hash and JSON pointer; absent and literal `missing` references remain distinguishable. The upstream declared database hash is source metadata, not an independently acquired second witness. The upstream local temporary file path is omitted. Image paths remain source text only.

Verify public files offline with `python scripts/build_public_sigla_layer.py --check`. To reproduce every published byte from the upstream release, download the input identified in [the audit](../analysis/public-sigla-layer-audit.json), then run:

```sh
python scripts/build_public_sigla_layer.py /path/to/sigla-corpus.json --check
```

The checksum is enforced before any export. CI repeats this replay. Readings, dimensions and source classifications retain their source authority; independent object inspection and Raison–Pope entry reconciliation remain open.
