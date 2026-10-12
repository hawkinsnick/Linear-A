"""Replay the bounded master dependency register and its published source receipts."""
import argparse
import hashlib
import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXPECTED_SHA = 'e883c5aff6aad132695c79819c8f047d9c0d41d193b5fe5b632eb039d9e4de9f'


def digest(data):
    return hashlib.sha256(json.dumps(data, ensure_ascii=False, sort_keys=True, separators=(',', ':')).encode()).hexdigest()


def pointer(value, path):
    for key in path.strip('/').split('/') if path else []:
        value = value[int(key)] if isinstance(value, list) else value[key.replace('~1', '/').replace('~0', '~')]
    return value


def check(data, checkouts=None):
    if digest(data) != EXPECTED_SHA:
        raise ValueError('audited master dependency register or policy changed')
    if data['physical_identity_certified'] is not False or data['independence_established'] is not False:
        raise ValueError('unsupported identity/independence promotion')
    groups = {group['group_id']: group for group in data['dependency_groups']}
    if len(groups) != len(data['dependency_groups']):
        raise ValueError('duplicate dependency group')
    if checkouts is not None:
        checkouts = Path(checkouts).resolve()
        acquired = {}
        for receipt in data['member_projections']:
            repo = receipt['repository']
            root = checkouts / repo.split('/')[-1]
            origin = subprocess.check_output(['git', 'remote', 'get-url', 'origin'], cwd=root, text=True).strip()
            if not origin.rstrip('/').removesuffix('.git').endswith('/' + repo):
                raise ValueError('wrong member checkout origin')
            blob = subprocess.check_output(['git', 'show', receipt['source_commit'] + ':' + receipt['path']], cwd=root)
            if hashlib.sha256(blob).hexdigest() != receipt['sha256']:
                raise ValueError('published projection digest drift')
            projection = json.loads(blob)
            if projection['repository'] != repo or projection['physical_identity_certified'] is not False or projection['independence_established'] is not False:
                raise ValueError('projection identity or claim mismatch')
            if [group['group_id'] for group in projection['dependency_groups']] != receipt['group_ids']:
                raise ValueError('projection membership mismatch')
            for group in projection['dependency_groups']:
                if groups.get(group['group_id']) != group:
                    raise ValueError('member/master dependency disagreement')
            acquired[repo] = (root, receipt['source_commit'])
        for group in groups.values():
            for participant in group['participants']:
                root, commit = acquired[participant['repository']]
                for evidence in participant['evidence']:
                    path = evidence['path']
                    if Path(path).is_absolute() or '..' in Path(path).parts:
                        raise ValueError('unsafe source evidence path')
                    blob = subprocess.check_output(['git', 'show', commit + ':' + path], cwd=root)
                    if hashlib.sha256(blob).hexdigest() != evidence['sha256']:
                        raise ValueError('source evidence digest mismatch')
                    if pointer(json.loads(blob), evidence['pointer']) != evidence['expected']:
                        raise ValueError('source identifier or URL mismatch')
    return {'status': 'PASS_BOUNDED_MASTER_DEPENDENCIES', 'groups': len(groups), 'published_projections': len(data['member_projections']), 'source_receipts_replayed': checkouts is not None, 'scientific_approval_granted': False}


def screen(data, keys, claim='source_record_count'):
    check(data)
    if claim != 'source_record_count':
        raise ValueError('pooled physical counts, independent witness counts and phonetic transfer are not authorized')
    if len(keys) != len(set(keys)):
        raise ValueError('duplicate requested key')
    registered = {p['repository'] + '::' + p['record_id'] for g in data['dependency_groups'] for p in g['participants']}
    overlap = [g['group_id'] for g in data['dependency_groups'] if len(set(keys) & {p['repository'] + '::' + p['record_id'] for p in g['participants']}) > 1]
    return {'requested_key_count': len(keys), 'source_record_count': len(keys) if set(keys) <= registered else None, 'known_dependency_groups_in_selection': overlap, 'unregistered_keys': sorted(set(keys) - registered), 'physical_object_count': None, 'independent_witness_count': None}


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--checkouts', type=Path)
    parser.add_argument('--records', nargs='*')
    parser.add_argument('--claim', default='source_record_count')
    args = parser.parse_args()
    data = json.loads((ROOT / 'corpus-factory/cross-corpus-dependencies.json').read_text())
    print(json.dumps(screen(data, args.records, args.claim) if args.records is not None else check(data, args.checkouts), indent=2))
