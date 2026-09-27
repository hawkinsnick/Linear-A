# Data Schema

The corpus uses separate layers for documents, individual sign occurrences, sources, provenance, and hypotheses.

## data/sites.csv

One normalized record per archaeological/site identifier used by the project.

## data/inscriptions.csv

One record per document/object bearing Linear A evidence.

Fields:
- document_id — stable project identifier
- source_id — primary upstream source
- site_id — normalized site identifier
- document_name — source document identifier/name
- document_type — tablet, sealing, roundel, pithos, etc.
- support — object/support category
- material — material
- period — archaeological period as supplied by source
- dimensions — source dimensions, preserved as supplied
- sign_count — source sign count where available
- word_count — source word count where available
- gorila_reference — GORILA cross-reference when documented
- museum_or_repository — current repository if documented
- source_url — upstream record
- source_license — license applying to source-derived fields
- provenance_id — link to provenance record
- notes — controlled/curated notes

## data/sign_occurrences.csv

One record per observed sign occurrence or explicitly grouped/composite occurrence.

Fields:
- occurrence_id — stable occurrence identifier
- document_id — parent document
- sequence_index — position in normalized sign sequence
- line_index — line/row where known
- word_index — word/sequence grouping where known
- sign_id — standardized sign identifier
- sign_variant — graphic/palaeographic variant
- reading_status — observed, doubtful, unreadable, etc.
- function_class — source classification; not assumed to be linguistic meaning
- damage_status — damage/visibility status
- uncertainty — structured uncertainty
- composite — composite/ligature information
- unicode_codepoint — Unicode representation where applicable
- source_id — source
- source_record — source-specific occurrence identifier
- source_license — applicable source license
- provenance_id — provenance record
- notes — notes

## data/provenance.csv

One record per source snapshot/transformation.

## data/bibliography.csv

Normalized bibliographic records and source documentation.

## data/hypotheses.csv

Interpretive claims are not stored as facts. Each hypothesis should identify scope, claim, status, confidence, evidence, counterevidence, sources, and date/author of project entry.

## Source vs normalized fields

Where possible, future versions should preserve both the source representation and the normalized representation. Normalization must be documented so a researcher can reproduce or reverse it.

## Stable identifiers

Identifiers should be stable across releases whenever the underlying object/occurrence remains the same. Changes to identity should be documented rather than silently reusing an ID.
