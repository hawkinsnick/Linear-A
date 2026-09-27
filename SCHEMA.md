# Data Schema

## `data/signs_unicode.csv`

| Field | Meaning |
|---|---|
| `unicode_codepoint` | Unicode scalar value |
| `glyph` | Rendered Unicode character |
| `unicode_name` | Official Unicode character name |
| `gorila_identifier` | GORILA-based identifier represented by the Unicode name |
| `sign_class` | Later classification such as syllabic sign, logogram, fraction, etc. |
| `linear_b_correspondence` | Corresponding Linear B sign/value, where documented |
| `proposed_linear_a_value` | Proposed phonetic value for Linear A; never assume it from Linear B |
| `proposed_semantic_value` | Proposed meaning/gloss |
| `confidence` | Evidence status |
| `variant_or_composite` | Variant/composite relationship |
| `notes` | Free-form research notes |
| `sources` | Source/provenance identifiers |

## Future tables

`inscriptions.csv` should contain document-level metadata.

`sign_occurrences.csv` should contain individual sign/group observations.

`hypotheses.csv` should contain explicit claims, evidence, counterevidence, source, and confidence.

`bibliography.csv` should normalize references so claims can be traced back to publications or databases.
