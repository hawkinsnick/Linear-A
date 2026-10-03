"""Reject membership drift and accidental inclusion of separate projects."""
import copy
import json
import unittest
from validate_fleet import ROOT, validate


class FleetTests(unittest.TestCase):
    def setUp(self):
        self.register = json.loads((ROOT / "corpus-factory/fleet-gap-register.json").read_text())
        self.combined = json.loads((ROOT / "combined-ai-skill/registry/corpus-projects.json").read_text())

    def test_current_membership(self):
        self.assertEqual(validate(self.register, self.combined), [])

    def test_missing_and_duplicate_members(self):
        self.register['members'].pop()
        self.assertTrue(any('missing fleet' in e for e in validate(self.register, self.combined)))
        self.register['members'].append(copy.deepcopy(self.register['members'][0]))
        self.assertTrue(any('duplicate repo' in e for e in validate(self.register, self.combined)))

    def test_separate_projects_rejected_even_if_both_registries_change(self):
        for name in ['LightroomIsSlow']:
            register = copy.deepcopy(self.register)
            combined = copy.deepcopy(self.combined)
            row = copy.deepcopy(register['members'][0])
            row['repo'] = name
            register['members'].append(row)
            combined['members'].append({'repository': 'hawkinsnick/' + name})
            self.assertTrue(any('separate projects included' in e for e in validate(register, combined)))

    def test_missing_gap_and_exclusion_reason_rejected(self):
        self.register['members'][0]['top_gap'] = ''
        self.register['excluded_projects'][0]['reason'] = ''
        errors = validate(self.register, self.combined)
        self.assertTrue(any('top_gap' in e for e in errors))
        self.assertTrue(any('exclusions' in e for e in errors))


if __name__ == '__main__':
    unittest.main()
