"""Reject promotion through stale, missing or edited readiness evidence."""
import copy
import json
import unittest
from readiness_overview import ROOT, SNAPSHOT, OUTPUT, validate, render


class ReadinessTests(unittest.TestCase):
    def setUp(self):
        self.snapshot = json.loads(SNAPSHOT.read_text())

    def test_committed_projection(self):
        validate(ROOT, self.snapshot)
        self.assertEqual(OUTPUT.read_text(), render(self.snapshot))

    def test_missing_member_rejected(self):
        self.snapshot['members'].pop()
        with self.assertRaises(ValueError):
            validate(ROOT, self.snapshot)

    def test_duplicate_member_rejected(self):
        self.snapshot['members'][-1] = copy.deepcopy(self.snapshot['members'][0])
        with self.assertRaises(ValueError):
            validate(ROOT, self.snapshot)

    def test_native_byte_tampering_rejected(self):
        self.snapshot['members'][0]['native_status_json'] = '{"calibration_executed": true}'
        with self.assertRaisesRegex(ValueError, 'bytes changed'):
            validate(ROOT, self.snapshot)

    def test_stale_register_rejected(self):
        self.snapshot['input_sha256']['corpus-factory/fleet-gap-register.json'] = '0' * 64
        with self.assertRaisesRegex(ValueError, 'input changed'):
            validate(ROOT, self.snapshot)

    def test_readiness_promotion_rejected(self):
        self.snapshot['members'][0]['remaining_source_and_review_work'] = 'Expert review only; all sources verified'
        with self.assertRaisesRegex(ValueError, 'statement changed'):
            validate(ROOT, self.snapshot)


if __name__ == '__main__':
    unittest.main()
