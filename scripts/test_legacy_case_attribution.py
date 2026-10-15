"""Test literal preservation, source binding and rejection of scholarly overclaims."""
import copy
import json
import shutil
import tempfile
import unittest
from pathlib import Path
import legacy_case_attribution as a


class AttributionTests(unittest.TestCase):
    def setUp(self):self.audit=a.load()
    def reject(self,change,pattern):
        value=copy.deepcopy(self.audit);change(value)
        with self.assertRaisesRegex(ValueError,pattern):a.validate(value)
    def test_replay_and_bounded_scope(self):
        self.assertEqual(json.loads((a.ROOT/a.REPORT).read_text()),a.summary())
        self.assertEqual((a.ROOT/a.GUIDE).read_text(),a.guide())
        report=a.summary()
        self.assertEqual(report['joined_cases_examined'],10)
        self.assertEqual(report['alternatives_preserved'],20)
        self.assertEqual(report['qualified_published_contexts'],3)
        self.assertEqual(report['same_locus_competing_pairs_established'],0)
    def test_unjoined_cases_cannot_be_claimed_as_reviewed(self):
        with self.assertRaisesRegex(ValueError,'outside joined'):a.case('U010')
        self.reject(lambda v:v['cases'].pop(),'coverage drift')
    def test_literal_and_document_identity_preserved(self):
        self.reject(lambda v:v['cases'][0].update(legacy_alternatives='37 vs 39'),'literal drift')
        self.reject(lambda v:v['cases'][0].update(source_record_id='HT 15'),'identity/literal')
        self.reject(lambda v:v['cases'][0]['alternatives'][0].update(literal='38'),'literal changed')
    def test_account_quantity_not_inferred_from_sign_number(self):
        self.assertEqual(a.case('U001')['alternatives'][0]['attribution_status'],'UNTRACED_ACCOUNT_QUANTITY')
        self.reject(lambda v:v['cases'][0]['alternatives'][0].update(attribution_status='SIGLA_NUMERAL_37'),'account quantity')
    def test_source_and_locus_misjoins_rejected(self):
        self.reject(lambda v:v['cases'][0]['source_evidence'][0].update(pointer='/entries/0/source_attestations/2'),'misjoin')
        self.reject(lambda v:v['cases'][0]['source_evidence'][0].update(pointer='/entries/1/source_context'),'misjoin')
        self.reject(lambda v:v['cases'][-1]['published_contexts'][0].update(source_id='UNNAMED'),'unbound')
    def test_distinct_kh8_positions_cannot_collapse(self):
        index=next(i for i,c in enumerate(self.audit['cases']) if c['case_id']=='U008')
        self.reject(lambda v:v['cases'][index]['source_evidence'][1].update(pointer=v['cases'][index]['source_evidence'][0]['pointer']),'distinct-locus')
    def test_scholarly_and_rights_promotions_rejected(self):
        for field in ['same_locus_competing_pair_established','independent_witnesses_established','canonical_reading_changed','expert_review_granted']:
            self.reject(lambda v:v['cases'][0].update({field:True}),'promotion')
        self.reject(lambda v:v['sources'][0].update(independence_established=True),'promotion')
        self.reject(lambda v:v['sources'][0].update(full_source_redistributed=True),'promotion')
        self.reject(lambda v:v.update(source_collated_competing_pairs_added=1),'promotion')
    def test_stale_inputs_fail_closed(self):
        with tempfile.TemporaryDirectory() as td:
            root=Path(td)
            for item in self.audit['inputs']:
                p=root/item['path'];p.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(a.ROOT/item['path'],p)
            (root/'data/unresolved_cases.csv').write_text('changed')
            with self.assertRaisesRegex(ValueError,'pin mismatch'):a.validate(self.audit,root)
    def test_archive_history_is_not_scholarly_authorship(self):
        self.reject(lambda v:v['project_ingress'].update(archive_csv_sha256='0'*64),'archived queue')
        self.assertIn('before upload',self.audit['project_ingress']['finding'])
    def test_queries_expose_corrections_beside_unchanged_queue(self):
        from query_critical_evidence import dossier
        result=dossier('KH 8')
        self.assertEqual(result['legacy_queue_cases'][0]['legacy_alternatives'],'QA2PU vs *510')
        self.assertEqual(result['current_attribution_audit'][0]['attribution_disposition'],'LEGACY_LOCUS_CONFLATION_IDENTIFIED')
        self.assertFalse(result['current_attribution_audit'][0]['same_locus_competing_pair_established'])


if __name__=='__main__':unittest.main()
