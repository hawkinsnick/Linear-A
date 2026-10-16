import copy,json,unittest
from validate_p1_refresh import ROOT,validate
class P1RefreshTests(unittest.TestCase):
    def setUp(self):
        self.reg=json.loads((ROOT/'corpus-factory/fleet-gap-register.json').read_text());self.work=json.loads((ROOT/'corpus-factory/p1-current-work.json').read_text())
    def test_current(self):self.assertEqual(validate()['members'],18)
    def test_universal_closure_and_expert_promotion_rejected(self):
        for k in ['all_p1_closed','scientific_acceptance_granted']:
            w=copy.deepcopy(self.work);w[k]=True
            with self.assertRaises(ValueError):validate(work=w)
    def test_omitted_member_or_authority_rejected(self):
        d=copy.deepcopy(self.reg);d['members'].pop()
        with self.assertRaises(ValueError):validate(register=d)
        d=copy.deepcopy(self.reg);d['members'][0]['current_evidence']['artifacts']=[]
        with self.assertRaises(ValueError):validate(register=d)
    def test_tampered_snapshot_and_lost_next_action_rejected(self):
        w=copy.deepcopy(self.work);w['native_followups'][0]['snapshot_sha256']='0'*64
        with self.assertRaises(ValueError):validate(work=w)
        w=copy.deepcopy(self.work);w['remaining_work'][0]['evidence_needed']=''
        with self.assertRaises(ValueError):validate(work=w)
if __name__=='__main__':unittest.main()
