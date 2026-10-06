# Researcher browser and API — 3.0.18

The first implementation tranche exposes the committed public SigLA source layer through a small read-only Python API and a compact browser index.

Run `python scripts/research_api.py documents --text HT --limit 20`, or query `source_words` and `signs`. Stable-ID lookup uses repeated `--id`. JSONL output is available with `--jsonl`.

Run `python scripts/build_researcher_browser.py` to generate `analysis/researcher-browser-index.json`. The index is intentionally compact: it points back to committed source records and does not replace them as authority.

The interface preserves the CC BY-NC-SA 4.0 source-layer boundary. Search results are source-reported evidence, not independent epigraphic verification. Source-defined word groups are not established linguistic words, and displayed sign values must not be promoted into a Linear A decipherment.
