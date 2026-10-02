# Linear A AI Research Skill

A vendor-neutral AI layer for the Linear A Open Corpus.

The corpus remains canonical. This folder teaches an AI how to use it conservatively and reproducibly; it does not create a second corpus and does not grant new rights over upstream material.

## Non-technical use

1. Download the AI-skill release/package.
2. Add the package to your AI system as instructions/knowledge, or upload `SKILL.md` plus the recommended corpus bundle.
3. Ask ordinary research questions such as:
   - "Show every attestation of this sign and separate source facts from derived claims."
   - "Compare these two documents and cite the corpus IDs."
   - "Audit this proposed pattern against the current claim registry and errata."
   - "Export the matching source-defined words as CSV."
4. Require the assistant to retain IDs, provenance, uncertainty and limitations in its answer.

See `QUICKSTART.md` for platform-specific instructions.

## Design

The skill is intentionally thin. It points at the repository's canonical evidence rather than duplicating or rewriting it. Vendor adapters may change; `SKILL.md` and the research contract are the portable core.
