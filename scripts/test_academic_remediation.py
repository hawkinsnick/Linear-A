"""Regression tests for wrong-route reuse and false legacy-pair admission."""
import json
import tempfile
import unittest
from pathlib import Path
import academic_remediation as m
from evidence_query import Evidence

class RemediationTests(unittest.TestCase):
    def test_known_wrong_targets_rejected_in_actual_retrieval(self):
        e=Evidence()
        for sid in ('HT 53a','HT 53b'):
            d=e.dossier(sid,'source-documents')
            q=[x['native_record'] for x in d['explicitly_linked_records'] if x['collection']=='edition-route-decisions']
            self.assertEqual(len(q),1)
            self.assertTrue(q[0]['rejected_for_target'])
            self.assertIsNone(q[0]['usable_confirmed_target_url'])
            self.assertIn('sp=136',q[0]['historical_source_url'])
            self.assertFalse(q[0]['replacement_verified'])

    def test_supported_and_uninspected_routes_not_conflated(self):
        rows=m.build()['route_decisions']
        self.assertEqual(sum(x['target_heading_supported'] is True for x in rows),220)
        self.assertEqual(sum(x['rejected_for_target'] for x in rows),2)
        for r in rows:
            if r['target_heading_supported'] is not True:
                self.assertIsNone(r['usable_confirmed_target_url'])
            self.assertFalse(r['reading_verified'])
            self.assertFalse(r['physical_identity_certified'])

    def test_five_cases_are_explicitly_disposed_without_reading_admission(self):
        e=Evidence()
        for cid in ('U010','U012','U013','U014','U015'):
            d=e.dossier(cid,'legacy-cases')
            q=next(x['native_record'] for x in d['explicitly_linked_records'] if x['collection']=='case-dispositions')
            self.assertFalse(q['alternative_pair_admitted'])
            self.assertFalse(q['physical_join_certified'])
            self.assertFalse(q['reading_adjudicated'])
            if cid=='U010':
                self.assertEqual(q['source_record_ids'],['HT Zd 157','HT Zd 156'])
                self.assertEqual(q['disposition'],'EXCLUDE_COMBINED_READING_COMPONENT_POINTERS_ONLY')
            elif cid=='U015':
                self.assertEqual(q['disposition'],'ROUTE_TO_INTERPRETATION_DOSSIER_NOT_INSCRIPTION')
            else:
                self.assertEqual(q['source_record_ids'],[])
                self.assertIn('KEEP_SNAPSHOT_GAP',q['disposition'])

    def test_source_route_misjoin_cannot_be_generated(self):
        with tempfile.TemporaryDirectory() as d:
            root=Path(d)
            for name in m.INPUTS:
                p=root/name;p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes((m.ROOT/name).read_bytes())
            p=root/m.INPUTS[1];v=json.loads(p.read_text());v['pages'][0]['page_url']+='&wrong=1';p.write_text(json.dumps(v))
            with self.assertRaisesRegex(AssertionError,'route'):
                m.build(root)

    def test_false_pair_admission_in_source_evidence_stops_builder(self):
        with tempfile.TemporaryDirectory() as d:
            root=Path(d)
            for name in m.INPUTS:
                p=root/name;p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes((m.ROOT/name).read_bytes())
            p=root/m.INPUTS[3];v=json.loads(p.read_text());v['same_locus_competing_pairs_established']=1;p.write_text(json.dumps(v))
            with self.assertRaises(AssertionError):
                m.build(root)

if __name__=='__main__':unittest.main()
