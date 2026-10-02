# Generic AI adapter

For an AI system with project/system instructions:
1. load `SKILL.md` as instructions;
2. load `references/research-contract.md`;
3. attach the compact corpus bundle;
4. instruct the model to answer only from supplied evidence for corpus-specific factual claims.

For systems supporting retrieval/RAG, index stable IDs and provenance fields and return the source record with every retrieval result.
