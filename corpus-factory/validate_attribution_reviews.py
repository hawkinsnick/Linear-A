"""Validate bounded per-member documentary snapshots without pooling corpus units."""
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def validate(root=ROOT):
    root = Path(root)
    registry = json.loads((root/'combined-ai-skill/registry/corpus-projects.json').read_text())
    data = json.loads((root/'corpus-factory/attribution-review-rollout.json').read_text())
    expected = {m['repository'] for m in registry['members']}
    members = data['members']
    if len(members) != len(expected) or {m['repository'] for m in members} != expected:
        raise ValueError('attribution member mismatch')
    count = 0
    engine = hashlib.sha256((root/'scripts/attribution_review.py').read_bytes()).hexdigest()
    for member in members:
        path = (root/member['snapshot_path']).resolve()
        if not path.is_relative_to(root.resolve()):
            raise ValueError('unsafe attribution snapshot')
        raw = path.read_bytes()
        if hashlib.sha256(raw).hexdigest() != member['snapshot_sha256']:
            raise ValueError('snapshot digest mismatch')
        report = json.loads(raw)
        if report['repository'] != member['repository'] or report['manifest_sha256'] != member['review_manifest_sha256']:
            raise ValueError('snapshot identity mismatch')
        if report['implementation_sha256'] != engine:
            raise ValueError('attribution implementation drift')
        if report['consultation_this_pass'] != 'PINNED_REPOSITORY_EVIDENCE_ONLY':
            raise ValueError('unsupported consultation claim')
        if report['alternative_pair_count'] is not None or report['independent_witness_count'] is not None:
            raise ValueError('unknown scholarly count promoted')
        if report['new_readings_admitted'] != 0 or report['independent_reviews_added'] != 0 or report['literature_exhaustive'] is not False:
            raise ValueError('unsupported scholarly promotion')
        if sum(report['case_classes'].values()) != report['review_case_count'] or sum(report['pair_attribution_states'].values()) != report['review_case_count']:
            raise ValueError('review task accounting mismatch')
        count += report['review_case_count']
    if count != data['review_tasks']:
        raise ValueError('review task total mismatch')
    if data['alternative_pair_count'] is not None or data['independent_witness_count'] is not None or data['new_readings_admitted'] != 0 or data['independent_reviews_added'] != 0 or data['literature_exhaustive'] is not False:
        raise ValueError('unsupported fleet promotion')
    return {'status':'PASS_BOUNDED_ATTRIBUTION_REVIEW_SNAPSHOTS', 'members':len(members), 'documentary_review_tasks':count, 'scholarly_acceptance_added':False}


if __name__ == '__main__':
    print(json.dumps(validate()))
