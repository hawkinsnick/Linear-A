#!/usr/bin/env python3
"""Integration tests over explicit local native checkouts; no fake corpus fixtures."""
import argparse
import copy
import json
from pathlib import Path
import tempfile
import unittest
import federated_research as f

CHECKOUTS=None

class Federation(unittest.TestCase):
    def setUp(self):
        if CHECKOUTS is None:
            self.skipTest("Integration requires explicit --checkouts; run the dedicated fleet workflow.")

    def test_all_members_are_bound_and_scoped(self):
        r=f.audit(CHECKOUTS)
        self.assertEqual(len(r['members']),18)
        self.assertFalse(r['all_scholarly_p0_p1_closed']);self.assertIsNone(r['unique_object_count'])
        self.assertEqual(len({m['repository'] for m in r['members']}),18)

    def test_exact_id_query_preserves_payload_and_namespace(self):
        repo,root,_=f.members(CHECKOUTS)[0]
        e=f.native.Evidence(root);name=next(n for n,c in e.collections.items() if c['records']);row=e.collections[name]['records'][0]
        q=f.query(CHECKOUTS,identity=row['id'],repository=repo,collection=name)
        self.assertEqual(len(q['records']),1)
        hit=q['records'][0]
        self.assertEqual(hit['key'],[repo,name,row['id']]);self.assertEqual(hit['native_record'],row['value'])
        self.assertEqual(hit['provenance'],e.provenance(e.collections[name]['spec']['path'],row['pointer']))
        self.assertFalse(q['physical_identity_join_performed'])

    def test_empty_search_limit_and_missing_identity(self):
        q=f.query(CHECKOUTS,limit=1)
        self.assertEqual(q['returned_view_rows'],1);self.assertTrue(q['truncated'])
        self.assertEqual(f.query(CHECKOUTS,identity='ABSENT_TEST_ID_000')['records'],[])
        for limit in (0,1001):
            with self.assertRaises(ValueError):f.query(CHECKOUTS,limit=limit)
        for repository in ('hawkinsnick/LightroomIsSlow','hawkinsnick/Egyptian-Hieroglyphic-Corpus','invented'):
            with self.assertRaises(ValueError):f.query(CHECKOUTS,repository=repository)

    def test_unknown_adapter_is_rejected(self):
        with tempfile.TemporaryDirectory() as td:
            root=Path(td);target=root/'Linear-A/scripts';target.mkdir(parents=True)
            (target/'evidence_query.py').write_text('malicious replacement')
            with self.assertRaisesRegex(ValueError,'adapter version mismatch'):f.members(root)

    def test_five_exercises_reproduce(self):
        r=f.exercises(CHECKOUTS)
        self.assertEqual(len(r['exercises']),5)
        self.assertEqual(len(r['exercises'][3]['packages']),18)
        self.assertFalse(r['expert_acceptance_added']);self.assertEqual(r['new_readings'],0)

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--checkouts',required=True,type=Path);a,remaining=p.parse_known_args()
    CHECKOUTS=a.checkouts
    unittest.main(argv=['test_federated_research.py']+remaining)
