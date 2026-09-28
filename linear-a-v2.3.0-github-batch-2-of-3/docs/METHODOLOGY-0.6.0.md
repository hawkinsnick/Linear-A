# 0.6.0 Methodology Freeze

## Source words

Word membership is decoded from SigLA's explicit serialized `Word` object list
within each document. It is not reconstructed from `f3`.

The current SigLA help interface independently describes Word View as
highlighting all syllabograms belonging to a word, and the database model
exposes `Document -> Word List`.

Empty serialized Word objects are retained as source observations but excluded
from sequence statistics pending clarification.

## Context

Document type, find-place, and optional period are decoded directly from the
current local SigLA document metadata object. Raw values are preserved.
Dimensions are withheld because float decoding has not yet received an
independent semantic validation.

## Word adjacency null

For each nonempty source word, sign order is independently permuted while word
length and sign inventory are preserved. Five hundred permutations are used.
Candidate directed pairs require observed count >= 4. Empirical upper-tail
p-values use `(ge + 1)/(B + 1)` and are corrected with Benjamini-Hochberg FDR.

A surviving pair is described only as structurally enriched within
SigLA-defined words under this null. This does not establish phonotactics,
morphology, syntax, semantic relation, or decipherment.

## f3

The RC15 evidence-tier policy remains unchanged. `f3` is unresolved and is not
used to define words in 0.6.0.
