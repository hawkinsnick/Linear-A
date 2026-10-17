# Linear A research pilot: reproduce a bounded sequence concordance

The research question is: **where does the exact source-label sequence KU RO occur within one source-defined group in this selected collection?** This supports source tracing before interpretation. It establishes no pronunciation, meaning, morphology or decipherment. Named academics have not requested, reviewed or endorsed the pilot.

## Inspect the executed result

1. Open [the saved concordance](../analysis/task-pilot-example.json).
2. Read `pilot`: 25 source-document entries reporting `Haghia Triada`, selected in the frozen public JSONL order. The exact IDs are explicit. This convenience sample is not the complete site corpus or 25 certified unique tablets.
3. Read `summary`: seven matches occur in seven selected source-document entries.
4. The matching IDs are **HT 100, HT 102, HT 104, HT 109, HT 110a, HT 116b and HT 117a**. Inspect each hit's literal source attestations, raw flags, source provenance and indices.
5. The method requires contiguous `sign` labels equal to `KU`, `RO` and the same non-null source `word` label. It does not collapse groups, fill blanks, strip notation or infer boundaries from raw flags. The labels are source conventions; a source-defined group is not an independently adjudicated linguistic word.
6. A pointer such as `/…/source_fields/attestations` identifies a zero-based row in the nonempty JSONL sequence; `attestation_indices` identifies the exact array slots within it. It is not an edition line or a physical sign position.
7. `collated_competing_pairs` and `meanings_established` remain null. The raw flags are retained, not interpreted as a secure/doubtful-reading classifier.

## Reproduce

Download and extract the repository's ZIP. Open a terminal in its root and use Python 3.12:

```sh
python scripts/evidence_query.py --check
python scripts/task_pilot.py --check
python scripts/test_task_pilot.py
```

The source, frozen specification and script hashes are in the saved result. Source mutations fail closed; inspect a changed edition/version rather than changing the hash merely to make a check pass. `--write` regenerates the result after an intentional, reviewed change.

For a different question, develop a separately versioned selection/query specification and preserve both results. Do not silently revise this teaching sample or describe its count as a whole-corpus frequency. Use the existing research API and sequence tools for exploration; attach their source/view coverage and method to any result.

## Compare readings only after establishing their source and locus

Use the existing attribution audit as a second, separate worked task:

```sh
python scripts/evidence_query.py --record U008 --collection attribution-audit
```

Read [the step-by-step U008 example](../combined-ai-skill/WORKED-EXAMPLES.md#example-2--can-two-recorded-alternatives-really-be-compared). Its legacy alternatives are not two established editions at a shared locus. It is not an alternative reading of this KU RO concordance. Recover attributable same-locus witnesses before claiming a completed critical comparison. GORILA remains excluded under the recorded EFA restriction; no protected content is reconstructed here.

## Try with AI and request review

Supply the individual skill and saved concordance, then ask:

> List the seven matching source entries and exact attestation-array slots. Explain the source-group inclusion rule and preserve every raw flag and attribution. Distinguish a recurring source-label sequence from a phonetic or linguistic claim. Identify what this file cannot establish.

Expected: seven matches in seven selected entries, no translation, no competing pair or source-independence claim. This is a proposed response criterion, not a captured LLM test.

The bounded review question is: “Does this concordance faithfully reproduce the declared source labels and group boundaries, and what evidence would permit interpretation?” Record the reviewer's sources, expertise/conflicts, reasoning and dissent. Status remains PREPARED_NOT_REVIEWED. Automated reproduction is not expert acceptance.

## Attribution and rights

The existing SigLA-derived public source and derived concordance retain CC BY-NC-SA 4.0. Attribute Ester Salgarella and Simon Castellan, SigLA; derivative by Ryan Pavlicek/pyaegean. Preserve the [license matrix](../DATA-LICENSE-MATRIX.md), source provenance and component notices. No raw upstream drawings, GORILA content or sealed prospective outcomes are added.
