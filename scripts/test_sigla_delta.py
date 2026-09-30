#!/usr/bin/env python3
import hashlib,json,pathlib,subprocess,sys,tempfile
R=pathlib.Path(__file__).resolve().parents[1]
with tempfile.TemporaryDirectory() as td:
    d=pathlib.Path(td);old=d/'old.json';new=d/'new.json';out=d/'out.json'
    old.write_text(json.dumps({'documents':[{'id':'A','attestations':[]}]}));new.write_text(json.dumps({'documents':[{'id':'A','attestations':[]},{'id':'B','attestations':[]}]}))
    def run(*args):return subprocess.run([sys.executable,str(R/'scripts/compare_sigla_snapshots_2_4_1.py'),str(old),str(new),'--out',str(out),*args],capture_output=True,text=True)
    assert run('--expected-old-sha256',hashlib.sha256(old.read_bytes()).hexdigest()).returncode==0
    result=json.loads(out.read_text());assert result['documents']['added']==['B'] and result['candidate_outcomes_evaluated'] is False
    assert run('--expected-old-sha256','bad').returncode!=0
    assert run('--expected-current-sha256','bad').returncode!=0
    old.write_text(json.dumps({'source':'database.js'}));assert run().returncode!=0
    old.write_text(json.dumps({'documents':[{'id':'A','attestations':[]},{'id':'A','attestations':[]}]}));assert run().returncode!=0
print('PASS: descriptive delta, both digest guards, source-envelope and duplicate-ID refusal')
