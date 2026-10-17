#!/usr/bin/env python3
"""Audit the bounded public SigLA view; never certify scholarly completeness."""
import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
import re

from research_api import FILES, rows, stable_id
from build_source_context import build as contexts, FIELD_MAP

ROOT = Path(__file__).resolve().parents[1]
REPORT = 'analysis/research-readiness.json'


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def build(root=ROOT):
    audit = json.loads((root/'analysis/public-sigla-layer-audit.json').read_text())
    counts = {}
    inputs = []
    datasets = {}
    for resource in ('documents', 'source_words', 'signs'):
        path = FILES[resource]
        raw = (root/path).read_bytes()
        entry = next(e for e in audit['files'] if e['path'] == path)
        if sha(raw) != entry['sha256']:
            raise ValueError('source checksum mismatch: '+path)
        data = list(rows(resource, root))
        ids = [stable_id(resource, row) for row in data]
        if any(not isinstance(i, str) or not i for i in ids) or len(ids) != len(set(ids)):
            raise ValueError('missing/duplicate identifier: '+resource)
        for row in data:
            p = row['provenance']
            if (p['input_sha256'] != audit['input_sha256'] or not re.fullmatch(r'[0-9a-f]{64}', p['input_sha256'])
                    or not p['json_pointer'].startswith('/') or not p['attribution'] or p['license'] != 'CC BY-NC-SA 4.0'):
                raise ValueError('invalid provenance: '+resource)
            if resource == 'documents' and (row['classification'] != 'SOURCE_REPORTED_NOT_INDEPENDENTLY_VERIFIED'
                    or row['physical_object_identity_certified'] is not False):
                raise ValueError('source document promoted to expert evidence')
            if resource == 'source_words' and (row['provenance']['status'] != 'SOURCE_REPORTED_NOT_INDEPENDENTLY_VERIFIED'
                    or row['definition'] != 'SigLA source grouping; not a confirmed linguistic word'):
                raise ValueError('editorial grouping promoted to linguistic word')
            if resource == 'signs' and (row['linear_a_phonetic_value'] is not None
                    or row['linear_b_equivalence_status'] != 'NOT_ESTABLISHED_BY_THIS_SOURCE'):
                raise ValueError('unestablished sign value promoted')
        datasets[resource] = data
        counts[resource] = len(data)
        inputs.append({'path':path, 'sha256':sha(raw), 'records':len(data)})
    docs = {d['source_record_id']:d for d in datasets['documents']}
    for g in datasets['source_words']:
        if g['document_id'] not in docs:
            raise ValueError('orphan source group')
        att = docs[g['document_id']]['source_fields']['attestations']
        for i in g['occurrence_indices']:
            if type(i) is not int or not 0 <= i < len(att) or att[i]['word'] != g['source_word_index']:
                raise ValueError('source grouping alignment drift')
    assertions = contexts(root)
    by = Counter(c['field'] for c in assertions)
    refs = Counter(d['reference_url_status'] for d in docs.values())
    return {
        'format':'linear-a-research-readiness-v1',
        'scope':'Committed public SigLA derivative only; not all Linear A evidence or all language corpora.',
        'p0_engineering_status':'PASS_BOUNDED_PUBLIC_VIEW',
        'scholarly_completeness':'NOT_ESTABLISHED',
        'expert_review_completed':False,
        'counts':dict(counts, attestation_slots=sum(len(d['source_fields']['attestations']) for d in docs.values())),
        'inputs':inputs,
        'context':{'assertions':len(assertions), 'assertions_by_field':{k:by[k] for k in FIELD_MAP},
                   'meaning':'Counts are source-reported nonempty values, not independently verified archaeological facts.'},
        'reference_routes':dict(sorted(refs.items())),
        'unresolved_dependencies':[
            f"{sum(not d.get('public_reference_url') for d in docs.values())} source entries lack a usable public reference route; do not invent publication locators.",
            'A public edition route does not establish permission, primary collation or an attributed competing reading.',
            'Source-reported dates and contexts are not independent object verification.',
            'GORILA structured ingestion remains subject to the recorded EFA refusal.',
            'Independent epigraphic review and known-answer calibration remain open under current gates.',
            'Other corpus members require native audits before this bounded result can be generalized.'
        ]
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    raw = (json.dumps(build(), ensure_ascii=False, indent=2)+'\n').encode()
    target = ROOT/REPORT
    if args.check:
        if target.read_bytes() != raw:
            raise SystemExit('Research-readiness report drift')
    else:
        target.write_bytes(raw)
    print(raw.decode(), end='')


if __name__ == '__main__':
    main()
