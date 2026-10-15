import hashlib
import json
import tempfile
import unittest
from pathlib import Path
from validate_attribution_reviews import ROOT, validate


class FleetAttributionTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.rollout = 'corpus-factory/attribution-review-rollout.json'
        self.data = json.loads((ROOT/self.rollout).read_text())
        paths = [self.rollout, 'combined-ai-skill/registry/corpus-projects.json', 'scripts/attribution_review.py'] + [m['snapshot_path'] for m in self.data['members']]
        for path in paths:
            p = self.root/path
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_bytes((ROOT/path).read_bytes())

    def save(self):
        (self.root/self.rollout).write_text(json.dumps(self.data))

    def test_current(self):
        self.assertEqual(validate()['members'], 18)

    def test_membership(self):
        self.data['members'].pop()
        self.save()
        with self.assertRaisesRegex(ValueError, 'member mismatch'):
            validate(self.root)

    def test_changed_snapshot(self):
        p = self.root/self.data['members'][0]['snapshot_path']
        p.write_text(p.read_text()+'\n')
        with self.assertRaisesRegex(ValueError, 'digest'):
            validate(self.root)

    def test_count_is_not_pairs(self):
        self.data['alternative_pair_count'] = self.data['review_tasks']
        self.save()
        with self.assertRaisesRegex(ValueError, 'promotion'):
            validate(self.root)

    def test_no_fake_primary_consultation(self):
        item = self.data['members'][0]
        p = self.root/item['snapshot_path']
        report = json.loads(p.read_text())
        report['consultation_this_pass'] = 'ALL_ORIGINALS_INSPECTED'
        p.write_text(json.dumps(report))
        item['snapshot_sha256'] = hashlib.sha256(p.read_bytes()).hexdigest()
        self.save()
        with self.assertRaisesRegex(ValueError, 'consultation'):
            validate(self.root)


if __name__ == '__main__':
    unittest.main()
