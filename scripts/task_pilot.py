#!/usr/bin/env python3
"""A bounded, source-located Linear A sequence concordance."""
import argparse
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def match_slots(atts, sequence):
    if not sequence or any(not isinstance(s, str) or not s for s in sequence):
        raise ValueError('nonempty exact source sign labels required')
    n = len(sequence)
    matches = []
    for start in range(len(atts) - n + 1):
        span = atts[start:start + n]
        labels = [a.get('sign') for a in span]
        group = span[0].get('word')
        if labels == sequence and group is not None and all(a.get('word') == group for a in span):
            matches.append(start)
    return matches


def build(root=ROOT):
    root = Path(root)
    spec_raw = (root / 'research/task-pilot.json').read_bytes()
    spec = json.loads(spec_raw)
    raw = (root / spec['source_path']).read_bytes()
    if sha(raw) != spec['source_sha256']:
        raise ValueError('source checksum differs')
    rows = [json.loads(line) for line in raw.splitlines() if line.strip()]
    if len(rows) != spec['source_records']:
        raise ValueError('source count differs')
    ids = [r['source_record_id'] for r in rows]
    if len(set(ids)) != len(ids):
        raise ValueError('duplicate source document IDs')
    selected = [(i, r) for i, r in enumerate(rows) if r['source_fields'].get('site') == spec['site_literal']][:25]
    if len(selected) != 25 or [r['source_record_id'] for _, r in selected] != spec['document_ids']:
        raise ValueError('selection differs')
    hits = []
    for index, row in selected:
        atts = row['source_fields']['attestations']
        for start in match_slots(atts, spec['sequence']):
            n = len(spec['sequence'])
            hits.append({'source_record_id': row['source_record_id'],
                         'attestation_indices': list(range(start, start + n)),
                         'source_attestations': atts[start:start + n],
                         'source_provenance': row['provenance'],
                         'source_pointer': f'/{index}/source_fields/attestations',
                         'locator_scope': 'JSONL row and zero-based source-array slots, not physical lines or graphical coordinates.'})
    return {
        'format': 'linear-a-task-result-v1', 'pilot': spec,
        'reproduction': {'source_sha256': sha(raw), 'spec_sha256': sha(spec_raw),
                         'code_sha256': sha(Path(__file__).read_bytes())},
        'summary': {'selected_source_documents': len(selected), 'source_sequence_matches': len(hits),
                    'matching_source_documents': len({h['source_record_id'] for h in hits}),
                    'collated_competing_pairs': None, 'meanings_established': None},
        'hits': hits,
        'uncertainty': 'Retain every raw flag literally. Do not infer f3 semantics or secure-reading status from this search. A source-defined group is not an independently adjudicated linguistic word.',
        'alternative_comparison_route': {'case': 'U008', 'collection': 'attribution-audit',
            'command': 'python scripts/evidence_query.py --record U008 --collection attribution-audit',
            'limit': 'Separate attribution/locus audit; not a competing edition of the queried sequence.'},
        'scientific_status': 'SOURCE_LABEL_CONCORDANCE_NOT_DECIPHERMENT_OR_EXPERT_ACCEPTANCE',
    }


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--write', action='store_true')
    p.add_argument('--check', action='store_true')
    a = p.parse_args()
    result = build()
    out = ROOT / 'analysis/task-pilot-example.json'
    if a.check and json.loads(out.read_bytes()) != result:
        raise SystemExit('task pilot result differs')
    if a.write:
        out.write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps(result['summary'], indent=2))


if __name__ == '__main__':
    main()
