import copy
import json
import unittest
from check_cross_corpus_dependencies import ROOT, check, screen


class MasterDependenciesTests(unittest.TestCase):
    def setUp(self):
        self.data = json.loads((ROOT / 'corpus-factory/cross-corpus-dependencies.json').read_text())

    def test_restored_published_groups(self):
        self.assertEqual(check(self.data)['groups'], 15)
        self.assertEqual(check(self.data)['published_projections'], 17)

    def test_malia_shared_evidence(self):
        result = screen(self.data, ['hawkinsnick/Cretan-hieroglyphs::CHIC-328', 'hawkinsnick/Aegean-anomalous::MALIA-ALTAR-STONE'])
        self.assertEqual(result['source_record_count'], 2)
        self.assertIn('CHIC-MALIA-328', result['known_dependency_groups_in_selection'])
        self.assertIsNone(result['physical_object_count'])
        self.assertIsNone(result['independent_witness_count'])

    def test_unknown_is_not_independent(self):
        self.assertIsNone(screen(self.data, ['unregistered::record'])['source_record_count'])

    def test_erasure_and_certification_rejected(self):
        for key, value in [('dependency_groups', []), ('independence_established', True), ('physical_identity_certified', True)]:
            bad = copy.deepcopy(self.data)
            bad[key] = value
            with self.assertRaises(ValueError):
                check(bad)

    def test_forbidden_claims(self):
        for claim in ['physical_object_count', 'independent_witness_count', 'phonetic_transfer']:
            with self.assertRaises(ValueError):
                screen(self.data, [], claim)

    def test_duplicate_selection(self):
        with self.assertRaises(ValueError):
            screen(self.data, ['x::y', 'x::y'])
