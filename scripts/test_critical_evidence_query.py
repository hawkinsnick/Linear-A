"""Test evidence loss, attribution boundaries, exact joins and source corruption."""
import copy
import json
import tempfile
import unittest
from pathlib import Path
import query_critical_evidence as q


class DossierTests(unittest.TestCase):
    def test_all_entries_preserved_with_attribution(self):
        pilot, pin = q.load()
        for entry in pilot['entries']:
            result = q.dossier(entry['source_record_id'])
            self.assertEqual(result['input']['sha256'], pin)
            self.assertEqual(result['source_witness']['attestations'], entry['source_attestations'])
            self.assertEqual(result['attributed_assertions'], entry['assertions'])
            sources = {p['page_id'] for p in result['source_locators']['edition_pages']}
            sources |= {s['source_id'] for s in result['source_locators']['scholarly_reports']}
            self.assertTrue(all(a['source_id'] in sources for a in result['attributed_assertions']))
            self.assertFalse(result['source_reported_record']['expert_validated'])

    def test_untraced_alternative_and_missing_quantity_stay_distinct(self):
        result = q.dossier('HT 17')
        case = next(c for c in result['legacy_queue_cases'] if c['case_id'] == 'U001')
        self.assertEqual(case['legacy_alternatives'], '37 vs 38')
        self.assertIn('37_ATTRIBUTION_UNTRACED', case['disposition'])
        self.assertEqual(case['authenticated_source_excerpts'], [])
        self.assertIn('NOT_INDIVIDUALLY_SOURCE_COLLATED', result['alternative_reading_status'])
        self.assertTrue(all('quantity' not in a for a in result['source_witness']['attestations']))

    def test_no_fuzzy_record_or_face_merging(self):
        for identity in ['HT17', 'ht 17', 'HT 49', 'HT 49b', 'NONEXISTENT']:
            with self.assertRaisesRegex(ValueError, 'Exact source_record_id absent'):
                q.dossier(identity)

    def test_corrupted_source_is_rejected_before_query(self):
        pilot, _ = q.load()
        pilot = copy.deepcopy(pilot)
        pilot['entries'][0]['expert_validated'] = True
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            for path in ['research/edition-concordance.csv', 'data/unresolved_cases.csv']:
                target = root / path
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_bytes((q.ROOT / path).read_bytes())
            (root / q.INPUT).write_text(json.dumps(pilot))
            with self.assertRaisesRegex(ValueError, 'promotion'):
                q.dossier('HT 15', root)

    def test_committed_coverage_replays(self):
        actual = json.loads((q.ROOT / 'analysis/critical-evidence-coverage-v1.json').read_text())
        self.assertEqual(actual, q.coverage())
        self.assertEqual(actual['record_count'], 10)
        self.assertEqual(actual['source_attestation_slots'], 168)
        self.assertEqual(actual['source_collated_alternative_pairs'], 0)
        self.assertEqual(actual['expert_validated_records'], 0)
        self.assertEqual(actual['total_legacy_case_count'], 15)
        self.assertEqual(actual['joined_legacy_case_count'], 10)
        self.assertEqual(len(actual['unjoined_legacy_cases']), 5)
        self.assertIn('INTERPRETATION_ONLY_NOT_A_DOCUMENT',
                      {c['source_join_status'] for c in actual['unjoined_legacy_cases']})


if __name__ == '__main__':
    unittest.main()
