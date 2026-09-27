# Linear A Open Corpus

An open, provenance-first research corpus for Minoan Linear A.

## Initial release: 0.1.0

This release contains the Unicode-encoded Linear A sign inventory only. It is intentionally separated from inscription transcriptions and interpretive glosses.

### Design principles

1. **Sign identity is not decipherment.**
2. Linear B correspondences are stored separately from proposed Linear A readings.
3. Every interpretive claim should carry a source and confidence/provenance.
4. Copyright and licensing are tracked at the dataset level.
5. Raw archaeological observations should remain distinguishable from hypotheses.

### Files

- `data/signs_unicode.csv` — Unicode Linear A characters and GORILA-based identifiers.
- `data/metadata.json` — release metadata and corpus principles.

### Unicode

The Unicode Standard defines Linear A at U+10600–U+1077F and states that its repertoire is broadly based on the GORILA catalog. Unicode character names use GORILA catalog numbers.

Official reference:
https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-8/

### Planned datasets

Future releases may add inscription/document metadata, sign sequences, sign variants and paleography, numerical notation, bibliographic references, proposed readings and competing hypotheses, statistical observations, and analysis scripts.

Inscription data will only be redistributed when its source licensing permits it. Otherwise, the repository will provide scripts/instructions to obtain the source locally.
