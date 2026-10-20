#!/usr/bin/env python3
"""Replay every registered individual skill plus the separate Egyptian acquisition skill."""
import argparse
import json
from pathlib import Path
import subprocess
import sys
ROOT=Path(__file__).resolve().parents[1]

def validate(checkouts):
    registry=json.loads((ROOT/'combined-ai-skill/registry/corpus-projects.json').read_bytes())['members']
    registered=[m['repository'] for m in registry]
    if len(registered)!=18 or len(set(registered))!=18:
        raise ValueError('unexpected/duplicate factory membership')
    repos=registered+['hawkinsnick/Egyptian-Hieroglyphic-Corpus']
    if 'hawkinsnick/LightroomIsSlow' in repos or 'hawkinsnick/Open-Endurance-Coaching' in repos:
        raise ValueError('unrelated project in skill audit')
    results=[]
    for repository in repos:
        root=Path(checkouts)/repository.split('/')[-1]
        run=subprocess.run([sys.executable,'scripts/validate_ai_skill.py'],cwd=root,
                           capture_output=True,text=True,timeout=180)
        if run.returncode:
            raise ValueError(repository+': '+run.stderr+run.stdout)
        result=json.loads(run.stdout)
        if result['repository']!=repository:raise ValueError('skill resolved to wrong repository')
        result['master_member']=repository in registered
        results.append(result)
    if len({r['skill_name'] for r in results})!=len(repos):raise ValueError('duplicate canonical skill names')
    master=subprocess.run([sys.executable,'combined-ai-skill/scripts/validate.py'],cwd=ROOT,
                          capture_output=True,text=True,timeout=180)
    if master.returncode:raise ValueError('master validation failed: '+master.stdout+master.stderr)
    return {'format':'all-corpus-ai-skills-validation-v1','status':'PASS_SCOPED_FUNCTIONAL_CHECKS',
            'corpus_count':len(repos),'master_member_count':len(registered),
            'independent_project_count':1,'individual_skills':results,
            'master_validation':{'command':'python combined-ai-skill/scripts/validate.py',
                                 'exit_code':master.returncode,'output':master.stdout},
            'master_skill':'hawkinsnick/Linear-A:combined-ai-skill/SKILL.md',
            'empirical_cross_platform_model_accuracy_established':False,
            'scholarly_acceptance_granted':False}

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--checkouts',required=True,type=Path)
    p.add_argument('--output',type=Path);a=p.parse_args()
    try:result=validate(a.checkouts)
    except (ValueError,OSError,subprocess.TimeoutExpired) as error:p.exit(2,str(error)+'\n')
    text=json.dumps(result,ensure_ascii=False,indent=2)+'\n'
    if a.output:a.output.write_text(text,encoding='utf-8')
    else:print(text,end='')
if __name__=='__main__':main()
