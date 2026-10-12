"""Build a private, lossless research package from explicitly declared native views.

No view is a certified unique-inscription population. Restricted derivatives,
component licenses, competing readings and native context remain separate.
"""
import argparse
import hashlib
import json
import shutil
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXCLUDED = {'hawkinsnick/LightroomIsSlow', 'hawkinsnick/Egyptian-Hieroglyphic-Corpus'}
CONTEXT = ['research/sigla-source-layout.json', 'analysis/sigla-layout-audit.json', 'research/sigla-layout-source-inspection.json', 'docs/SIGLA-SOURCE-LAYOUT.md', 'docs/LINEARA-XYZ-REFERENCE.md', 'research/kn-fp13-object-concordance.json', 'docs/KN-FP13-CONCORDANCE.md', 'research/stele-a-facsimile-ordinal-review.json', 'research/stele-a-type-table.json', 'research/stele-a-type-table-audit.json', 'research/stele-a-facsimile-number-index.json', 'docs/FULL-AVAILABLE-SOURCE-LAYERS.md'] + ['LICENSE', 'LICENSE-CODE', 'LICENSE-CONTENT.md', 'LICENSING.md', 'NOTICE',
           'DATA-LICENSE-MATRIX.md', 'ai-skill/SKILL.md', 'ai-skill/references/authority-profile.json',
           'research/cross-corpus-dependencies.json', 'research/browser-sources.json',
           'research/reference-reconciliation-v2.json', 'research/identity-reconciliation-v2.json',
           'research/record-dossiers.json', 'docs/AI-INTEGRITY.md',
           'research/ediana-list-snapshot.json', 'research/ediana-edition-snapshot.json',
           'research/monumental-link-snapshot.json', 'docs/DIGITAL-ENTRY-DOSSIERS.md',
           'docs/COVERAGE-EXPANSION-2026-10-12.md',
           'research/bbaw-squeeze-identifier-snapshot.json', 'docs/GEOGRAPHIC-EXPANSION.md',
           'research/source-access-delivery-2026-10-12.json',
           'docs/RAISON-POPE-ACCESS-FOLLOWUP.md', 'docs/DUNAND-SOURCE-REQUEST.md',
           'docs/SOURCE-DELIVERY-REQUESTS.md',
           'corpus-factory/SOURCE-DELIVERY-2026-10-12.md',
           'corpus-factory/source-delivery-worklist-2026-10-12.json']


def encode(data):
    return (json.dumps(data, ensure_ascii=False, sort_keys=True, indent=2) + '\n').encode()


def digest(data):
    return hashlib.sha256(data).hexdigest()


def pointer(data, path):
    for key in path.strip('/').split('/') if path else []:
        data = data[int(key)] if isinstance(data, list) else data[key.replace('~1', '/').replace('~0', '~')]
    return data


def safe_path(root, relative, receipt_only=False):
    path = (root / relative).resolve()
    if Path(relative).is_absolute() or not path.is_relative_to(root.resolve()):
        raise ValueError('unsafe native path')
    if not receipt_only and any(word in relative.lower() for word in ['prediction', 'prospective', 'gold', 'gorila', 'outcome']):
        raise ValueError('sealed or prohibited systematic source path')
    return path


def collect(checkouts, registry, include_local=False):
    checkouts = Path(checkouts).resolve()
    members, records, files = [], [], {}
    repos = [m['repository'] for m in registry['members']]
    if len(repos) != len(set(repos)) or set(repos) & EXCLUDED:
        raise ValueError('duplicate or excluded member')
    for member in registry['members']:
        repo = member['repository']
        root = checkouts / repo.split('/')[-1]
        origin = subprocess.check_output(['git', 'remote', 'get-url', 'origin'], cwd=root, text=True).strip()
        if not origin.rstrip('/').removesuffix('.git').endswith('/' + repo):
            raise ValueError('wrong native checkout')
        config_path = root / 'research/collection-readiness-inputs.json'
        config_bytes = config_path.read_bytes()
        config = json.loads(config_bytes)
        if config['repository'] != repo:
            raise ValueError('native collection identity mismatch')
        ledger = json.loads((root / 'research/collection-work-ledger.json').read_bytes())
        if ledger['config_sha256'] != digest(config_bytes) or ledger.get('scientific_approval_granted') is not False:
            raise ValueError('stale native collection configuration or unsupported acceptance')
        for relative, expected in ledger['input_sha256'].items():
            if digest(safe_path(root, relative, receipt_only=True).read_bytes()) != expected:
                raise ValueError('stale native evidence input: ' + repo + '/' + relative)
        component = {'repository': repo, 'checkout_base_commit': subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=root, text=True).strip(),
                     'configuration_sha256': digest(config_bytes), 'views': [], 'context_files': [],
                     'physical_object_count': None, 'independent_witness_count': None,
                     'rights_rule': 'Native component/source terms apply; package formation grants no redistribution permission.'}
        names = set()
        local_context = {}
        for view in config['record_sets']:
            if view['name'] in names:
                raise ValueError('duplicate native view name')
            names.add(view['name'])
            description = {'view': view['name'], 'unit': view['unit'], 'path': view['path'],
                           'pointer': view.get('pointer', ''), 'local_only': view.get('local_only', False)}
            if view.get('local_only') and not include_local:
                description.update(status='LOCAL_VIEW_EXCLUDED', rows=None)
                component['views'].append(description)
                continue
            path = safe_path(root, view['path'])
            if not path.is_file():
                raise ValueError('declared input missing: ' + repo + '/' + view['path'])
            raw = path.read_bytes()
            file_hash = digest(raw)
            data = pointer(json.loads(raw), view.get('pointer', ''))
            rows = [data] if view.get('singleton') else data
            if not isinstance(rows, list):
                raise ValueError('native view is not a list')
            if view.get('local_only'):
                audit = json.loads(safe_path(root, view['count_path']).read_bytes())
                if len(rows) != pointer(audit, view['count_pointer']):
                    raise ValueError('restricted view count differs from authenticated native audit')
                receipts = {entry['file']: entry['sha256'] for entry in audit['local_export_manifest']}
                if receipts.get(path.name) != file_hash:
                    raise ValueError('restricted payload differs from authenticated native audit')
                # Carry the other admitted native export layers as context as well:
                # Linear A occurrences/groupings must not disappear behind metadata rows.
                for entry in audit['local_export_manifest']:
                    auxiliary = safe_path(root, str(Path(view['path']).parent / entry['file']))
                    auxiliary_raw = auxiliary.read_bytes()
                    if digest(auxiliary_raw) != entry['sha256']:
                        raise ValueError('authenticated auxiliary layer digest drift')
                    relative = auxiliary.relative_to(root.resolve()).as_posix()
                    local_context[relative] = auxiliary_raw
            ids = set()
            for index, row in enumerate(rows):
                identity = row.get(view['id_key']) if isinstance(row, dict) else row
                if not isinstance(identity, (str, int)) or isinstance(identity, bool) or not str(identity).strip() or str(identity) in ids:
                    raise ValueError('missing or colliding native view identity')
                ids.add(str(identity))
                row_pointer = view.get('pointer', '') + ('' if view.get('singleton') else '/' + str(index))
                records.append({'record_key': json.dumps([repo, view['name'], str(identity)], ensure_ascii=False, separators=(',', ':')),
                                'repository': repo, 'view': view['name'], 'unit': view['unit'], 'native_id': identity,
                                'source_path': view['path'], 'source_pointer': row_pointer,
                                'source_file_sha256': file_hash, 'native_row_sha256': digest(encode(row)),
                                'local_only': view.get('local_only', False), 'source_record': row,
                                'context_component': repo.split('/')[-1],
                                'acceptance': 'NATIVE_SOURCE_ASSERTION; NO NEW SCIENTIFIC_OR_IDENTITY_ACCEPTANCE'})
            description.update(status='MATERIALIZED_NATIVE_VIEW', rows=len(rows), sha256=file_hash)
            component['views'].append(description)
        context = list(CONTEXT)
        browser = root / 'research/browser-sources.json'
        if browser.exists():
            context += json.loads(browser.read_bytes())['sources']
        for relative in sorted(set(context)):
            path = safe_path(root, relative)
            if not path.is_file():
                continue
            raw = path.read_bytes()
            destination = 'members/' + repo.split('/')[-1] + '/' + relative
            files[destination] = raw
            component['context_files'].append({'path': relative, 'package_path': destination, 'sha256': digest(raw), 'bytes': len(raw)})
        for relative, raw in sorted(local_context.items()):
            destination = 'members/' + repo.split('/')[-1] + '/' + relative
            files[destination] = raw
            component['context_files'].append({'path': relative, 'package_path': destination, 'sha256': digest(raw),
                                               'bytes': len(raw), 'local_only': True,
                                               'role': 'AUTHENTICATED_NATIVE_AUXILIARY_LAYER; NOT_ADDITIONAL_UNIQUE_OBJECTS'})
        members.append(component)
    if len({row['record_key'] for row in records}) != len(records):
        raise ValueError('package key collision')
    payload = b''.join((json.dumps(row, ensure_ascii=False, sort_keys=True, separators=(',', ':')) + '\n').encode() for row in records)
    report = {'format': 'mega-corpus-research-package-v1', 'members': members,
              'registered_members': len(members), 'materialized_members': sum(any(v['status'] == 'MATERIALIZED_NATIVE_VIEW' for v in m['views']) for m in members),
              'record_view_rows': len(records), 'record_payload_sha256': digest(payload),
              'record_rows_are_not_unique_inscription_counts': True, 'physical_object_count': None,
              'independent_witness_count': None, 'scientific_approval_granted': False, 'calibration_executed': False,
              'includes_local_only_payloads': any(row['local_only'] for row in records),
              'redistribution_authorized_by_this_package': False,
              'scope': 'Existing explicitly declared native views and browser context; no new inscriptions, inferred readings or global completeness claim.'}
    files['records.jsonl'] = payload
    files['manifest.json'] = encode(report)
    files['README.md'] = ('# Mega corpus research package\n\n'
        'This private research package materializes the explicitly declared views of the registered language corpora. '
        'Rows retain original fields, native units, source pointers, hashes and component context. '
        'Source-derived linguistic assertions remain separate from accepted readings. '
        'Views overlap and must never be added as unique physical inscriptions or independent witnesses. '
        'Read each member AI skill and reconciliation context before using its records. '
        'All native/source licensing remains controlling; no combined redistribution grant is made. '
        'Restricted local A/B inputs must remain local. This package cannot be used as blind calibration gold.\n').encode()
    return report, files


def write_package(checkouts, output, include_local=False, registry=None):
    output = Path(output).resolve()
    checkouts = Path(checkouts).resolve()
    registry = registry or json.loads((ROOT / 'combined-ai-skill/registry/corpus-projects.json').read_bytes())
    if any(output.is_relative_to(checkouts / m['repository'].split('/')[-1]) for m in registry['members']):
        raise ValueError('private package must be outside corpus repositories')
    if output.exists():
        raise FileExistsError('refusing to overwrite existing research package')
    report, files = collect(checkouts, registry, include_local)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.mkdir(exist_ok=False)
    try:
        for relative, data in files.items():
            path = output / relative
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(data)
    except Exception:
        shutil.rmtree(output)
        raise
    return report


def verify_package(output, expected_manifest_sha256=None):
    output = Path(output).resolve()
    raw = (output / 'manifest.json').read_bytes()
    if expected_manifest_sha256 is not None and digest(raw) != expected_manifest_sha256:
        raise ValueError('external manifest receipt mismatch')
    manifest = json.loads(raw)
    for field in ['scientific_approval_granted', 'calibration_executed', 'redistribution_authorized_by_this_package']:
        if manifest.get(field) is not False:
            raise ValueError('unsupported package approval')
    if manifest.get('physical_object_count') is not None or manifest.get('independent_witness_count') is not None:
        raise ValueError('unsupported pooled population')
    payload = (output / 'records.jsonl').read_bytes()
    if digest(payload) != manifest['record_payload_sha256']:
        raise ValueError('record payload digest drift')
    keys, counts = set(), {}
    views = {(m['repository'], v['view']): v for m in manifest['members'] for v in m['views']}
    for line in payload.splitlines():
        row = json.loads(line)
        key = row['record_key']
        if key in keys or json.loads(key) != [row['repository'], row['view'], str(row['native_id'])]:
            raise ValueError('duplicate or inconsistent row key')
        keys.add(key)
        view_key = (row['repository'], row['view'])
        view = views[view_key]
        if row['unit'] != view['unit'] or row['source_path'] != view['path'] or row['source_file_sha256'] != view['sha256']:
            raise ValueError('native view lineage mismatch')
        if row['native_row_sha256'] != digest(encode(row['source_record'])):
            raise ValueError('native row changed')
        counts[view_key] = counts.get(view_key, 0) + 1
    if len(keys) != manifest['record_view_rows']:
        raise ValueError('package row count mismatch')
    for member in manifest['members']:
        for view in member['views']:
            if view['status'] == 'MATERIALIZED_NATIVE_VIEW' and counts.get((member['repository'], view['view']), 0) != view['rows']:
                raise ValueError('native view coverage loss')
        for entry in member['context_files']:
            path = safe_path(output, entry['package_path'])
            if digest(path.read_bytes()) != entry['sha256']:
                raise ValueError('native qualification or license context changed')
    return {'status': 'PASS_PACKAGE_INTEGRITY', 'record_view_rows': len(keys),
            'manifest_sha256': digest(raw), 'external_receipt_checked': expected_manifest_sha256 is not None,
            'scientific_approval_granted': False}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--checkouts', type=Path)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--include-local', action='store_true', help='explicitly include authenticated, already materialized private A/B derivatives')
    parser.add_argument('--verify', action='store_true')
    parser.add_argument('--expected-manifest-sha256')
    args = parser.parse_args()
    if not args.verify and args.checkouts is None:
        parser.error('--checkouts is required when building')
    print(json.dumps(verify_package(args.output, args.expected_manifest_sha256) if args.verify else write_package(args.checkouts, args.output, args.include_local), indent=2))
