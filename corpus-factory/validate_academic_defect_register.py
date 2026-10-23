#!/usr/bin/env python3
"""Resolve the register's observations against pinned git blobs, not current files."""
import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
import subprocess


def validate(register, checkouts):
    r = json.loads(register.read_text())
    items = r['items']
    ids = [x['id'] for x in items]
    assert len(ids) == len(set(ids))
    assert ids == [f'ACD-{i:03}' for i in range(1, len(items) + 1)]
    revisions = {x['repository']: x['commit'] for x in r['revisions']}
    assert len(revisions) == 19
    assert r['exhaustive'] is False
    c = r['counts']
    assert c['total'] == len(items)
    assert c['open'] == sum(x['status'] == 'OPEN' for x in items)
    assert c['resolved_bounded'] == sum(x['status'] == 'RESOLVED_BOUNDED' for x in items)
    assert c['by_record_type'] == dict(Counter(x['record_type'] for x in items))
    assert c['open_by_priority'] == dict(Counter(x['priority'] for x in items if x['status'] == 'OPEN'))
    cache = {}
    assertions = 0
    for item in items:
        for key in ('finding', 'required_action', 'closure_criteria', 'claim_blocked_or_limited'):
            assert item[key].strip(), (item['id'], key)
        assert item['evidence']
        assert set(item['dependencies']) <= set(ids)
        for e in item['evidence']:
            assert revisions[e['repository']] == e['commit']
            key = (e['repository'], e['commit'], e['path'])
            if key not in cache:
                repo = checkouts / e['repository'].split('/')[-1]
                cache[key] = subprocess.check_output(['git', 'show', f"{e['commit']}:{e['path']}"], cwd=repo)
            b = cache[key]
            assert hashlib.sha256(b).hexdigest() == e['sha256'], (item['id'], e['path'])
            if e['locator_type'] == 'json_pointer':
                obj = json.loads(b)
                for raw in e['locator'].split('/')[1:]:
                    k = raw.replace('~1', '/').replace('~0', '~')
                    obj = obj[int(k)] if isinstance(obj, list) else obj[k]
            else:
                assert e['locator_type'] == 'text_contains'
                obj = [[i + 1, line] for i, line in enumerate(b.decode().splitlines()) if e['locator'] in line]
                assert obj
            if 'observed' in e:
                assert obj == e['observed'], (item['id'], e['path'], e['locator'])
            if 'observed_sha256' in e:
                canonical = json.dumps(obj, ensure_ascii=False, sort_keys=True, separators=(',', ':')).encode()
                assert hashlib.sha256(canonical).hexdigest() == e['observed_sha256']
            assertions += 1
    return {'status': 'PASS_EVIDENCE_BINDING_NOT_SCHOLARLY_ACCEPTANCE', 'items': len(items), 'open': c['open'], 'bounded': c['resolved_bounded'], 'unique_pinned_files': len(cache), 'evidence_observations_resolved': assertions, 'scope': 'Checks hashes, pointers, stored observations, counts and dependency IDs; does not establish ancient-reading correctness or close any scholarly gate.'}

if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument('--register', type=Path, default=Path(__file__).with_name('academic-defect-register-2026-10-22.json'))
    p.add_argument('--checkouts', type=Path, required=True)
    a = p.parse_args()
    print(json.dumps(validate(a.register, a.checkouts), indent=2))
