# Research API contract v1

The 3.0 platform API is a stable **read contract**, not a server requirement. JSON/CSV clients may expose documents, source-defined words, evidence instances, witness assertions, disagreements, claims and experiment states.

Every response must preserve provenance/warnings. There is deliberately no endpoint called "correct transcription", "translation", "morpheme" or "decipherment".

Native source representations remain authoritative inputs to adapters. API stability applies to the interchange contract, not to speculative interpretation.
