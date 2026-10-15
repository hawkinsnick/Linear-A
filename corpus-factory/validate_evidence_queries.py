"""Validate the recorded native-query rollout, preserving distinct native units."""
import hashlib
import json
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]


def validate(root=ROOT):
    registry = json.loads((root/'combined-ai-skill/registry/corpus-projects.json').read_text())
    rollout = json.loads((root/'corpus-factory/evidence-query-rollout.json').read_text())
    members = rollout['members']
    expected = {m['repository'] for m in registry['members']}
    if len(members) != len(expected) or {m['repository'] for m in members} != expected:
        raise ValueError('query rollout member mismatch')
    implementation = hashlib.sha256((root/'scripts/evidence_query.py').read_bytes()).hexdigest()
    for member in members:
        path = (root/member['snapshot_path']).resolve()
        if not path.is_relative_to(root.resolve()):
            raise ValueError('unsafe snapshot path')
        report = json.loads(path.read_text())
        if report['repository'] != member['repository'] or report['profile_sha256'] != member['profile_sha256']:
            raise ValueError('snapshot identity/profile mismatch')
        if report['implementation_sha256'] != member['implementation_sha256'] or member['implementation_sha256'] != implementation:
            raise ValueError('query implementation drift')
        if report['alternative_pair_count'] is not None or report['independent_witness_count'] is not None:
            raise ValueError('unknown scholarly counts promoted')
        if len({c['name'] for c in report['collections']}) != len(report['collections']):
            raise ValueError('duplicate native view')
        if any(c['record_count'] < 0 or not c['native_unit'] or not c['scope'] for c in report['collections']):
            raise ValueError('invalid native view')
    if rollout['unique_inscription_total'] is not None or rollout['new_verified_readings'] != 0 or rollout['expert_acceptance_added'] is not False:
        raise ValueError('unsupported scholarly promotion')
    return {'status':'PASS_RECORDED_NATIVE_QUERY_ROLLOUT','members':len(members),'scientific_acceptance_added':False}


if __name__ == '__main__':
    print(json.dumps(validate()))
