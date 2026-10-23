#!/usr/bin/env python3
"""Apply existing source/identity qualifications to executable retrieval views."""
import argparse
import csv
import hashlib
import io
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = 'research/academic-remediation.json'
INPUTS = ['research/edition-concordance.csv', 'research/edition-catalogue-pilot.json',
          'analysis/case-source-membership.json', 'analysis/legacy-case-attribution-audit.json']

def sha(b):
    return hashlib.sha256(b).hexdigest()

def build(root=ROOT):
    files = {p: (root/p).read_bytes() for p in INPUTS}
    routes = list(csv.DictReader(io.StringIO(files[INPUTS[0]].decode())))
    pilot = json.loads(files[INPUTS[1]])
    pages = {p['route_id']: p for p in pilot['pages']}
    inspected = {r['source_record_id']: r for r in pilot['entries']}
    assert len(inspected) == len(pilot['entries'])
    assert len(routes) == len({r['source_record_id'] for r in routes}) == 802
    decisions = []
    for row in routes:
        identity = row['source_record_id']
        check = inspected.get(identity)
        raw_url = row['gorila_source_url'] or None
        status = 'SOURCE_REPORTED_LOCATOR_NOT_TARGET_CONFIRMED' if raw_url else 'NO_EXACT_GORILA_ROUTE'
        usable = None
        locator = None
        evidence = None
        if check:
            page = pages[check['route_id']]
            assert raw_url == page['page_url'], 'Inspected route and attributed route disagree'
            status = check['locator_status']
            usable = status == 'TARGET_HEADING_VISUALLY_CONFIRMED'
            assert status in ('TARGET_HEADING_VISUALLY_CONFIRMED', 'SOURCE_ROUTE_TARGET_MISMATCH')
            if usable:
                locator = raw_url
            evidence = {'path': INPUTS[1], 'pointer': '/entries/'+str(pilot['entries'].index(check)),
                        'page_image_sha256': page['image_sha256'], 'edition_heading': check['edition_heading']}
        decisions.append({'source_record_id': identity, 'status': status,
                          'target_heading_supported': usable,
                          'usable_confirmed_target_url': locator,
                          'historical_source_url': raw_url,
                          'rejected_for_target': usable is False,
                          'replacement_verified': False,
                          'evidence': evidence,
                          'reading_verified': False, 'physical_identity_certified': False})
    memberships = json.loads(files[INPUTS[2]])['cases']
    pairs = json.loads(files[INPUTS[3]])
    assert pairs['same_locus_competing_pairs_established'] == 0
    disposition = {
        'EXACT_SOURCE_ID': 'SOURCE_MEMBERSHIP_ONLY_NOT_AN_ADMITTED_READING_PAIR',
        'COMPOSITE_CASE_SEPARATE_SOURCE_RECORDS_NO_COMBINED_ID': 'EXCLUDE_COMBINED_READING_COMPONENT_POINTERS_ONLY',
        'NO_EXACT_ID_IN_PINNED_SNAPSHOT': 'EXCLUDE_FROM_EXACT_SOURCE_PILOT_KEEP_SNAPSHOT_GAP',
        'INTERPRETATION_NOT_DOCUMENT': 'ROUTE_TO_INTERPRETATION_DOSSIER_NOT_INSCRIPTION',
    }
    cases = [{**r, 'disposition': disposition[r['membership_status']],
              'alternative_pair_admitted': False,
              'alternatives_evidence_status': 'QUARANTINED_LEGACY_QUEUE_STRINGS',
              'source_membership_is_reading_validation': False} for r in memberships]
    assert len(cases) == len({r['case_id'] for r in cases}) == 15
    return {'format': 'linear-a-academic-remediation-v1',
            'inputs': [{'path': p, 'sha256': sha(b)} for p,b in files.items()],
            'route_decisions': decisions, 'case_dispositions': cases,
            'counts': {'source_records': 802, 'confirmed_target_routes': sum(r['target_heading_supported'] is True for r in decisions),
                       'rejected_target_routes': sum(r['rejected_for_target'] for r in decisions),
                       'case_dispositions': len(cases), 'admitted_alternative_pairs': 0},
            'boundary': 'Existing inspected-source and membership evidence only. Rejected URLs remain historical source assertions, never usable confirmed targets. Null means unestablished. No replacement URL, reading, join or scholarly acceptance is inferred.',
            'source_derived_terms': 'Preserve CC BY-NC-SA 4.0 attribution to Ester Salgarella and Simon Castellan, SigLA, via Ryan Pavlicek/pyaegean; GORILA edition facts attributed to Godart and Olivier. No images or protected text redistributed.'}

def main():
    p = argparse.ArgumentParser(); p.add_argument('--check', action='store_true'); a=p.parse_args()
    text=json.dumps(build(),ensure_ascii=False,indent=2)+'\n'
    if a.check:
        assert (ROOT/OUT).read_text() == text, 'Academic remediation view drift'
    else:
        (ROOT/OUT).write_text(text)
    print('PASS: 802 route decisions; known wrong targets rejected; 15 legacy cases explicitly qualified.')

if __name__ == '__main__':
    main()
