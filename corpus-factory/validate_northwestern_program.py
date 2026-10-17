"""Validate the implementation receipts; never certify scholarly closure."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]


def validate(root=ROOT):
    read=lambda p:json.loads((root/p).read_bytes())
    registry=read('combined-ai-skill/registry/corpus-projects.json')
    expected={m['repository'] for m in registry['members']}
    program=read('corpus-factory/northwestern-work-program.json')
    if program['all_scholarly_p0_p1_closed'] is not False or program['expert_acceptance_added'] is not False:
        raise ValueError('unsupported scholarly closure')
    tasks=program['requirements']
    keys={'P0-provenance','P0-evidence-categories','P0-reproducibility','P1-search','P1-ai-skills','P1-demonstrations','P1-feedback'}
    if len(tasks)!=len(keys) or {t['id'] for t in tasks}!=keys or any(t['implementation_status']!='IMPLEMENTED_AND_LOCALLY_TESTED' for t in tasks):
        raise ValueError('incomplete implementation requirements')
    fleet=read('corpus-factory/research-delivery-fleet.json')
    if len(fleet['members'])!=len(expected) or {m['repository'] for m in fleet['members']}!=expected:
        raise ValueError('delivery membership drift')
    if fleet['all_scholarly_p0_p1_closed'] is not False or fleet['unique_object_count'] is not None:
        raise ValueError('pooled count or scholarly promotion')
    import re
    for m in fleet['members']:
        if m['expert_acceptance_added'] is not False or not m['scholarly_limits']:
            raise ValueError('missing limits or false acceptance')
        for k in ('delivery_report_sha256','profile_sha256'):
            if not re.fullmatch('[0-9a-f]{64}',m[k]):raise ValueError('missing evidence pin')
    exercises=read('corpus-factory/northwestern-exercises.json')
    if len(exercises['exercises'])!=5 or exercises['new_readings']!=0 or exercises['expert_acceptance_added'] is not False:
        raise ValueError('exercise coverage or unsupported reading')
    packages=exercises['exercises'][3]['packages']
    if len(packages)!=len(expected) or {p['repository'] for p in packages}!=expected:
        raise ValueError('missing package exercise')
    receipt=read('corpus-factory/northwestern-validation.json')
    checks=[c for m in receipt['native_commands'] for c in m['checks']]
    if len(checks)!=receipt['native_command_count'] or receipt['native_failures']!=0 or any(c['exit']!=0 for c in checks):
        raise ValueError('native validation failure or count mismatch')
    if {m['repository'] for m in receipt['native_commands']}!=expected:raise ValueError('native validation membership drift')
    return {'status':'PASS_IMPLEMENTATION_RECEIPTS_NOT_SCHOLARLY_CLOSURE','members':len(expected),'requirements':len(keys),'native_commands':len(checks),'expert_acceptance_added':False}

if __name__=='__main__':print(json.dumps(validate()))
