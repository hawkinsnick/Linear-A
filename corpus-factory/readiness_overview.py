#!/usr/bin/env python3
"""Render a bounded readiness entry point; never infer scholarly acceptance."""
import argparse
import hashlib
import json
from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parents[1]
SNAPSHOT = ROOT / 'corpus-factory/readiness-snapshot.json'
OUTPUT = ROOT / 'corpus-factory/CURRENT-READINESS.md'
INPUTS = ['combined-ai-skill/registry/corpus-projects.json',
          'corpus-factory/fleet-gap-register.json']


def digest(data):
    return hashlib.sha256(data).hexdigest()


def capture(root, checkouts):
    registry = json.loads((root / INPUTS[0]).read_text())
    gaps = json.loads((root / INPUTS[1]).read_text())
    members = []
    gap_map = {m['repo']: m for m in gaps['members']}
    expected = {m['repository'].split('/')[1] for m in registry['members']}
    if set(gap_map) != expected or len(gaps['members']) != len(expected):
        raise ValueError('fleet and registry membership differ or contain duplicates')
    for m in registry['members']:
        repo = m['repository']
        checkout = checkouts / repo.split('/')[1]
        commit = subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=checkout, text=True).strip()
        # Different members use different native status models. Never substitute
        # a missing common field with a zero or flatten all counts into records.
        candidates = ['analysis/current-status.json', 'exports/audit.json',
                      'research/reference-manifest.json', 'project.json']
        native = next((p for p in candidates if (checkout / p).is_file()), None)
        if native is None:
            raise ValueError('no native status authority for ' + repo)
        data = (checkout / native).read_bytes()
        # Refuse uncommitted inputs: the immutable link must identify these bytes.
        pinned = subprocess.check_output(['git', 'show', commit + ':' + native], cwd=checkout)
        if data != pinned:
            raise ValueError('uncommitted status authority for ' + repo)
        gap = gap_map[repo.split('/')[1]]
        members.append({'repository': repo, 'commit': commit,
                        'status_path': native, 'status_sha256': digest(data),
                        'native_status_json': data.decode('utf-8'),
                        'coverage_statement': gap['coverage_state'],
                        'remaining_source_and_review_work': gap['top_gap']})
    return {'format': 'corpus-readiness-snapshot-v1',
            'scope': 'Pinned repository status assertions; not independent source verification.',
            'input_sha256': {p: digest((root / p).read_bytes()) for p in INPUTS},
            'members': members}


def validate(root, snapshot):
    for path in INPUTS:
        if digest((root / path).read_bytes()) != snapshot['input_sha256'].get(path):
            raise ValueError('readiness input changed; refresh snapshot: ' + path)
    registry = json.loads((root / INPUTS[0]).read_text())
    expected = [m['repository'] for m in registry['members']]
    actual = [m['repository'] for m in snapshot['members']]
    if actual != expected or len(actual) != len(set(actual)):
        raise ValueError('snapshot membership/order differs from registry')
    gaps = {m['repo']: m for m in json.loads((root / INPUTS[1]).read_text())['members']}
    for m in snapshot['members']:
        gap = gaps[m['repository'].split('/')[1]]
        if m['coverage_statement'] != gap['coverage_state'] or m['remaining_source_and_review_work'] != gap['top_gap']:
            raise ValueError('coverage or remaining-work statement changed')
        if len(m['commit']) != 40 or any(c not in '0123456789abcdef' for c in m['commit']):
            raise ValueError('invalid revision')
        if len(m['status_sha256']) != 64:
            raise ValueError('missing native authority digest')
        if digest(m['native_status_json'].encode('utf-8')) != m['status_sha256']:
            raise ValueError('native status snapshot bytes changed')
        json.loads(m['native_status_json'])


def render(snapshot):
    lines = ['# Current collection readiness', '',
             'This is the researcher entry point for the 18-member language collection. '
             'It describes pinned repository assertions, with native units retained. '
             'It does not certify primary-source completeness or independent scholarly acceptance.', '',
             '## Choose the claim you need', '',
             '| Question | Required evidence |',
             '|---|---|',
             '| Can I search or export this layer? | Native tooling and its admitted source scope. |',
             '| Is the transcription source-checked? | Exact edition/page/locus comparison in the native record. A catalogue identity alone is insufficient. |',
             '| Is the reading independently accepted? | Attributable specialist judgment admitted under native rules. A passed test or AI answer is insufficient. |',
             '| Is an inference calibrated? | Executed known-answer evaluation on admissible aligned inputs. Linear B calibration remains unexecuted at this checkpoint. |', '',
             '## Coverage and remaining work by corpus', '',
             'Coverage statements and remaining work below are projections of the fleet gap register. '
             'The pinned native status links and captured native JSON in '
             '[readiness-snapshot.json](readiness-snapshot.json) retain each member’s own model. '
             'The fleet summary can lag a native update: if they conflict, use the native evidence and refresh this view. '
             'No fleet-wide unique-inscription total or completion percentage is computed.', '',
             '| Corpus / pinned native status | Coverage in the declared layer | Remaining source and review work |',
             '|---|---|---|']
    def cell(s):
        return s.replace('|', '\\|').replace('\n', ' ')
    for m in snapshot['members']:
        name = m['repository'].split('/')[1]
        url = f"https://github.com/{m['repository']}/blob/{m['commit']}/{m['status_path']}"
        lines.append(f"| [{name}]({url}) | {cell(m['coverage_statement'])} | {cell(m['remaining_source_and_review_work'])} |")
    lines += ['', '## How to interpret readiness', '',
              '“Pre-expert maximum” is a scoped work-boundary label. It does not certify that '
              'all remaining work requires an expert. Source acquisition, permission, record joins, '
              'primary collation, calibration and expert adjudication remain distinct dependencies. '
              'Use the member’s current ledger and selected review packet before handing off a task.', '',
              'Native fields that are absent or use another unit mean unknown or differently scoped; '
              'they must not become zero verified objects, zero unresolved issues, or inferred acceptance. '
              'Source-derived metadata and multiple dependent editions remain attributed assertions.', '',
              'The [20 October audit](VALIDITY-AUDIT-2026-10-20.md) passed 163 scoped commands and '
              'checked 1,095 indexed artifact hashes at its recorded revisions. It did not establish '
              'empirical AI accuracy, independent source truth, browser execution or live Actions success. '
              'These historical check counts are not a live validation badge.', '',
              '## Refresh and check', '',
              'Refresh from clean, fetched member checkouts with '
              '`python corpus-factory/readiness_overview.py --checkouts /path/to/checkouts --write`. '
              'Run `python corpus-factory/readiness_overview.py --check` to verify the committed '
              'projection and its registry/gap inputs. This offline check does not contact upstream '
              'repositories or assert that pinned revisions are still their latest heads.', '']
    return '\n'.join(lines)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--checkouts', type=Path)
    parser.add_argument('--write', action='store_true')
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    if args.write:
        if args.checkouts is None:
            parser.error('--write requires --checkouts')
        snapshot = capture(ROOT, args.checkouts.resolve())
        validate(ROOT, snapshot)
        SNAPSHOT.write_text(json.dumps(snapshot, ensure_ascii=False, indent=2) + '\n')
        OUTPUT.write_text(render(snapshot))
    else:
        snapshot = json.loads(SNAPSHOT.read_text())
        validate(ROOT, snapshot)
        if OUTPUT.read_text() != render(snapshot):
            raise ValueError('stale or edited readiness output')
    print('PASS: 18-member bounded readiness projection; scientific acceptance unchanged')


if __name__ == '__main__':
    main()
