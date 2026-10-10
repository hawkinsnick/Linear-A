"""Negative tests for cross-repository authority replay, without network access."""
import ast, copy, hashlib, json, unittest
from pathlib import Path
SOURCE=Path(__file__).resolve().parents[1]/'scripts/validate_fleet_admission.py'
LICENSES={'LICENSE','LICENSE-CODE','LICENSE-CONTENT.md','LICENSING.md','NOTICE'}
GATES={'corpus_is_authoritative','missing_means_unknown','cross_corpus_equivalence_requires_explicit_evidence','preserve_uncertainty','preserve_source_independence','preserve_rights'}
class AdapterTests(unittest.TestCase):
    def setUp(self):
        self.member={'contract_adapter_path':'adapter.json','individual_skill_path':'ai-skill/SKILL.md','authority_profile_path':'authority.json','bundle_index_path':'native.json','validation_path':'validator.py','required_skill_version':'0.3.1'}
        paths=LICENSES|{'ai-skill/SKILL.md','authority.json','native.json','ai-skill/manifest.json','ai-skill/references/fleet-contract.json','ai-skill/references/corpus-project-contract.md','ai-skill/scripts/fleet_contract.py','validator.py','data/input.json'}
        self.files={p:b'{}' for p in paths}
        self.files['ai-skill/manifest.json']=json.dumps({'master_contract_0_3_1':'IMPLEMENTED','skill_version':'0.3.1'}).encode()
        self.files['native.json']=json.dumps({'authoritative_inputs':['data/input.json']}).encode()
        self.index={'schema_version':'0.3.1','repository':'owner/repo','contract':dict.fromkeys(GATES,True),'scientific_approval_granted':False,'artifacts':[{'path':p,'sha256':hashlib.sha256(v).hexdigest(),'bytes':len(v)} for p,v in sorted(self.files.items())]}
        node=next(n for n in ast.parse(SOURCE.read_text()).body if isinstance(n,ast.FunctionDef) and n.name=='validate_adapter')
        env={'json':json,'hashlib':hashlib,'required_license':LICENSES,'HEADS':{'owner/repo':'immutable'},'raw_bytes':lambda repo,path:self.files[path]}
        exec(compile(ast.Module(body=[node],type_ignores=[]),str(SOURCE),'exec'),env)
        self.validate=env['validate_adapter']
    def run_adapter(self):
        self.files['adapter.json']=json.dumps(self.index).encode();self.validate('owner/repo',self.member)
    def test_complete_adapter(self):self.run_adapter()
    def test_stale_authority(self):
        self.files['data/input.json']=b'{"changed":true}'
        with self.assertRaisesRegex(ValueError,'stale adapter authority'):self.run_adapter()
    def test_native_input_cannot_be_omitted(self):
        self.index['artifacts']=[a for a in self.index['artifacts'] if a['path']!='data/input.json']
        with self.assertRaisesRegex(ValueError,'omits native corpus evidence'):self.run_adapter()
    def test_rights_and_independence_cannot_be_disabled(self):
        for gate in ('preserve_rights','preserve_source_independence'):
            self.index['contract'][gate]=False
            with self.assertRaisesRegex(ValueError,'disabled behavioral contract'):self.run_adapter()
            self.index['contract'][gate]=True
    def test_no_scientific_promotion(self):
        self.index['scientific_approval_granted']=True
        with self.assertRaisesRegex(ValueError,'falsely grants scientific approval'):self.run_adapter()
if __name__=='__main__':unittest.main()
