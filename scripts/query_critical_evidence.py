"""Query existing critical-pilot evidence without adjudicating or adding readings."""
import argparse
import copy
import hashlib
import json
from pathlib import Path
from build_critical_pilot import ROOT, INPUT, validate

BOUNDARY = ('A bounded, problem-selected Linear A pilot, not representative corpus coverage. '
            'Legacy alternatives are project queue labels, not two attributed scholarly readings. '
            'Source agreement is not independent confirmation. No new readings or expert acceptance.')


def load(root=ROOT):
    root = Path(root)
    raw = (root / INPUT).read_bytes()
    pilot = json.loads(raw)
    validate(pilot, root)
    if any('not individually source-collated witness readings' not in c['legacy_provenance'] for c in pilot['cases']):
        raise ValueError('Alternative attribution model changed; reassess pair coverage')
    return pilot, hashlib.sha256(raw).hexdigest()


def dossier(record_id, root=ROOT):
    pilot, pin = load(root)
    entry = next((e for e in pilot['entries'] if e['source_record_id'] == record_id), None)
    if entry is None:
        raise ValueError('Exact source_record_id absent from pilot: ' + record_id)
    # Preserve complete assertions, uncertainty strings and source-level qualification.
    entry = copy.deepcopy(entry)
    assertions = entry.pop('assertions')
    witness = entry.pop('source_attestations')
    cases = [copy.deepcopy(c) for c in pilot['cases'] if c['source_record_id'] == record_id]
    page_ids = set(entry['gorila_page_ids'])
    scholar_ids = {a['source_id'] for a in assertions} - page_ids
    return {
        'format': 'linear-a-evidence-dossier-v1',
        'input': {'path': INPUT, 'sha256': pin, 'checked_in_source': pilot['checked']},
        'source_record_id': record_id,
        'source_reported_record': entry,
        'source_witness': {'attribution': pilot['source_attribution'], 'url': pilot['source_url'],
                           'sha256': pilot['source_sha256'], 'pointer': entry['source_pointer'],
                           'license': pilot['source_derived_metadata_license'], 'attestations': witness},
        'attributed_assertions': assertions,
        'source_locators': {
            'edition_pages': [copy.deepcopy(p) for p in pilot['pages'] if p['page_id'] in page_ids],
            'scholarly_reports': [copy.deepcopy(s) for s in pilot['scholarly_sources'] if s['source_id'] in scholar_ids]},
        'legacy_queue_cases': cases,
        'alternative_reading_status': 'LEGACY_QUEUE_LABELS_NOT_INDIVIDUALLY_SOURCE_COLLATED',
        'rights': pilot['rights'], 'boundary': BOUNDARY,
    }


def coverage(root=ROOT):
    pilot, pin = load(root)
    rows = []
    for entry in pilot['entries']:
        cases = [c for c in pilot['cases'] if c['source_record_id'] == entry['source_record_id']]
        rows.append({'source_record_id': entry['source_record_id'],
                     'source_attestation_slots': entry['source_attestation_count'],
                     'attributed_assertions': len(entry['assertions']),
                     'legacy_case_ids': [c['case_id'] for c in cases],
                     'source_collated_alternative_pairs': 0,
                     'expert_validated': entry['expert_validated']})
    return {'format': 'linear-a-evidence-dossier-coverage-v1', 'input_path': INPUT,
            'input_sha256': pin, 'selection_reason': pilot['selection_reason'],
            'records': rows, 'record_count': len(rows),
            'attributed_assertion_count': sum(r['attributed_assertions'] for r in rows),
            'source_attestation_slots': sum(r['source_attestation_slots'] for r in rows),
            'joined_legacy_case_count': sum(len(r['legacy_case_ids']) for r in rows),
            'total_legacy_case_count': len(pilot['cases']),
            'unjoined_legacy_cases': [copy.deepcopy(c) for c in pilot['cases']
                                     if c['source_record_id'] not in pilot['declared_source_ids']],
            'source_collated_alternative_pairs': 0,
            'alternative_pair_count_basis': 'Every pilot case explicitly labels its alternatives as legacy project queue strings, not individually source-collated witness readings.',
            'expert_validated_records': sum(r['expert_validated'] for r in rows),
            'boundary': BOUNDARY}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--record', help='Exact source ID, e.g. "HT 17"; no fuzzy joins')
    parser.add_argument('--coverage', action='store_true')
    args = parser.parse_args()
    if bool(args.record) == args.coverage:
        parser.error('choose exactly one of --record or --coverage')
    try:
        result = coverage() if args.coverage else dossier(args.record)
    except ValueError as error:
        parser.exit(2, str(error) + '\n')
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
