"""Validate the four selected documentary checkpoints without granting acceptance."""
import hashlib
import json
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
EXPECTED = {'hawkinsnick/'+n for n in ['Cypro-Minoan','Lydian','Sidetic','Pisidian']}


def validate(root=ROOT):
    root = Path(root)
    d = json.loads((root/'corpus-factory/source-collation-2026-10-15.json').read_text())
    reg = json.loads((root/'combined-ai-skill/registry/corpus-projects.json').read_text())
    if len(d['members']) != 4 or {m['repository'] for m in d['members']} != EXPECTED:
        raise ValueError('selected member mismatch')
    if not EXPECTED <= {m['repository'] for m in reg['members']}:
        raise ValueError('member absent from registry')
    count = pages = corrections = 0
    for m in d['members']:
        p = (root/m['snapshot_path']).resolve()
        if not p.is_relative_to(root.resolve()):
            raise ValueError('unsafe snapshot')
        raw = p.read_bytes()
        if hashlib.sha256(raw).hexdigest() != m['snapshot_sha256']:
            raise ValueError('stale source collation snapshot')
        r = json.loads(raw)
        if r['repository'] != m['repository'] or r['packet_sha256'] != m['packet_sha256']:
            raise ValueError('snapshot identity mismatch')
        if r['accepted_readings_added'] != 0 or r['independent_reviews_added'] != 0 or r['frozen_readings_changed'] is not False or r['source_files_redistributed'] is not False:
            raise ValueError('unsupported scholarly promotion')
        if r['alternative_pair_total'] is not None or r['independent_witness_total'] is not None or r['literature_exhaustive'] is not False:
            raise ValueError('unsupported completeness or witness count')
        count += r['comparison_tasks']
        pages += r['rendered_page_inspections']
        corrections += r['project_representation_corrections']
    if (count,pages,corrections) != (d['selected_comparison_tasks'],d['rendered_page_inspections'],d['project_representation_corrections']):
        raise ValueError('documentary accounting mismatch')
    if d['accepted_readings_added'] != 0 or d['independent_reviews_added'] != 0 or d['frozen_readings_changed'] is not False or d['source_files_redistributed'] is not False or d['literature_exhaustive'] is not False:
        raise ValueError('unsupported master promotion')
    return {'status':'PASS_FOUR_MEMBER_DOCUMENTARY_SNAPSHOTS', 'members':4,
            'selected_comparison_tasks':count, 'rendered_page_inspections':pages,
            'project_representation_corrections':corrections, 'scholarly_acceptance_added':False}


if __name__ == '__main__':
    print(json.dumps(validate()))
