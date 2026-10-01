import copy,json,unittest
from audit_prospective_independence import audit,R
class AuditTests(unittest.TestCase):
    def setUp(self):self.source=json.loads((R/'analysis/sigla-cohort-input-membership.json').read_text())
    def test_known_membership_and_seal(self):
        r=audit(self.source)
        self.assertEqual(r['membership_counts'],{'ABSENT_FROM_V3_PRESENT_IN_V4':17,'PRESENT_IN_V3':7})
        self.assertFalse(r['entire_cohort_unseen_relative_to_v3'])
        self.assertFalse(r['prospective_scoring_allowed'])
    def test_report_replay(self):self.assertEqual(audit(self.source),json.loads((R/'analysis/prospective-independence-audit-v1.json').read_text()))
    def test_invalid_membership_rejected(self):
        for mutation in ['drop','duplicate','state','outcomes']:
            bad=copy.deepcopy(self.source)
            if mutation=='drop':bad['rows'].pop()
            elif mutation=='duplicate':bad['rows'][1]=bad['rows'][0]
            elif mutation=='state':bad['rows'][0]['state']='ABSENT_FROM_V3_PRESENT_IN_V4'
            else:bad['candidate_outcomes_evaluated']=True
            with self.subTest(mutation=mutation),self.assertRaises(ValueError):audit(bad)
if __name__=='__main__':unittest.main()
