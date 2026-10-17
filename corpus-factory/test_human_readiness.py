import copy,json,unittest
from validate_human_readiness import ROOT,validate
class RoutingTests(unittest.TestCase):
    def setUp(self):self.d=json.loads((ROOT/'corpus-factory/p1-human-readiness.json').read_text())
    def test_current(self):self.assertEqual(validate()['members'],18)
    def test_unperformed_review_and_source_exhaustion_rejected(self):
        for key in ['human_validation_performed','all_source_work_complete','all_p1_closed']:
            d=copy.deepcopy(self.d);d[key]=True
            with self.assertRaises(ValueError):validate(data=d)
    def test_omitted_member_and_native_gate_bypass_rejected(self):
        d=copy.deepcopy(self.d);d['members'].pop()
        with self.assertRaises(ValueError):validate(data=d)
        d=copy.deepcopy(self.d);d['members'][0]['native_acceptance_controls_remain_required']=False
        with self.assertRaises(ValueError):validate(data=d)
    def test_documentary_count_cannot_be_readings_or_missing_prerequisites(self):
        d=copy.deepcopy(self.d);d['new_documentary_work']['new_accepted_readings']=47
        with self.assertRaises(ValueError):validate(data=d)
        d=copy.deepcopy(self.d);d['members'][0]['native_prerequisites']=''
        with self.assertRaises(ValueError):validate(data=d)
if __name__=='__main__':unittest.main()
