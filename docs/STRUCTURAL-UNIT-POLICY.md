# Structural Unit Policy — 0.5.0

The corpus now distinguishes multiple kinds of sequence unit.

- `source_word`: membership explicitly supplied by a source as a word/sequence.
- `source_sign_group`: a source-explicit grouping that is not necessarily a word.
- `physical_line`: signs grouped by a documented physical line.
- `physical_separator_group`: grouping supported by visible/documented separators.
- `candidate_f3_group`: the unresolved RC10–RC15 f3 grouping hypothesis.
- `analytical_window`: a computational construction only.

No unit is promoted across these categories without provenance-bearing evidence.
In particular, `candidate_f3_group` is not a synonym for `source_word`.
