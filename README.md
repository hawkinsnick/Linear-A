# Linear A Open Corpus

An open, provenance-first, machine-readable research corpus for Minoan Linear A.

## Project goal

The long-term goal is a comprehensive, reproducible corpus of Linear A evidence that is free to access and reuse by everyone to the maximum extent legally possible.

The corpus distinguishes:
- physical/document observations;
- source transcriptions and classifications;
- normalized representations;
- computationally derived data;
- scholarly interpretations and hypotheses.

It does not assume that Linear B correspondences constitute deciphered Linear A readings.

## Current release

0.3.0-alpha — validated SigLA import foundation

This release expands the project from a Unicode sign inventory into a corpus architecture ready for systematic ingestion of openly licensed upstream data.

## Current files

- data/signs_unicode.csv — Unicode Linear A character inventory.
- data/sites.csv — normalized site identifiers used by the corpus.
- data/inscriptions.csv — document-level schema.
- data/sign_occurrences.csv — individual sign-attestation schema.
- data/bibliography.csv — normalized source bibliography.
- data/provenance.csv — record-level source/provenance schema.
- data/hypotheses.csv — explicit interpretive claims, kept separate from observations.
- DATA-POLICY.md — corpus methodology.
- DATA-LICENSE-MATRIX.md — licensing and attribution policy.
- SOURCE-POLICY.md — upstream-source policy.
- scripts/import_sigla.py — conservative SigLA ingestion scaffold.
- scripts/validate_corpus.py — structural validation.

## SigLA

SigLA is a major upstream source for this project. It describes itself as an open-access database intended to be systematic and exhaustive, and its current site documents documents, signs, sequences, words, and palaeographic/contextual information.

SigLA states that its dataset and drawings are available under CC BY-NC-SA 4.0.

Source: https://sigla.phis.me/

## Licensing philosophy

The project is intended to be free for everyone.

For material we create ourselves, we will use open licensing as far as legally possible. For upstream material, the upstream license remains controlling. We will not redistribute copyrighted or unclearly licensed material merely because it is useful to the project.

See DATA-LICENSE-MATRIX.md.

## Design principles

1. Sign identity is not decipherment.
2. Linear B correspondences are not automatically Linear A readings.
3. Observation and interpretation remain separate.
4. Every external record carries provenance.
5. Uncertainty is preserved.
6. Licensing is tracked at the record/source level.
7. Conflicting scholarly claims remain distinguishable.
8. Releases should be reproducible.
9. Original project contributions should be maximally open.
10. Citation is encouraged without unnecessarily restricting lawful reuse.

## Roadmap

- 0.1.0 — Unicode sign inventory.
- 0.2.0 — corpus architecture, provenance, licensing framework, and SigLA import foundation.
- 0.3.0 — validated SigLA corpus ingestion.
- 0.4.0+ — broader source reconciliation, paleographic normalization, variants, numerals, bibliography expansion, and derived analytical datasets.
- 1.0.0 — reproducible, release-versioned research corpus suitable for general computational and scholarly use.

## Important legal note

This repository is a research project, not legal advice. Always check the license attached to a source or record before redistributing derived material.


## Reproducible SigLA import

SigLA publishes its machine-readable corpus as a JavaScript payload containing OCaml Marshal data. Its published paper describes the underlying architecture as deliberately open and usable outside the web interface. The current payload is an implementation-level serialized representation rather than a documented JSON export.

This repository includes a decoder and importer, but **does not bundle the upstream SigLA payload**.

To obtain and process a current snapshot locally:

\`\`\`bash
python scripts/import_sigla.py --fetch
\`\`\`

The fetched source and generated corpus are stored under \`data/raw/\` and \`data/generated/\`, both of which are gitignored. Generated output retains SigLA provenance and **CC BY-NC-SA 4.0** licensing metadata.

The importer is deliberately opt-in. Running ordinary project validation or analysis does not silently download another research group's corpus.

See [THIRD-PARTY-NOTICES.md](THIRD-PARTY-NOTICES.md) for attribution and upstream-license handling.
