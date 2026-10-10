#!/usr/bin/env python3
"""Validate fleet admission against each registered repository's current main tree."""
import hashlib, json, os, subprocess, sys, tempfile, urllib.error, urllib.request, urllib.parse
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
registry=json.loads((ROOT/"combined-ai-skill/registry/corpus-projects.json").read_text())
errors=[]
required_license={"LICENSE","LICENSE-CODE","LICENSE-CONTENT.md","LICENSING.md","NOTICE"}
def github_json(url):
    """Read public repository metadata; retry without an unusable workflow token.

    The GITHUB_TOKEN can be scoped to this repository and return 403 for other
    public corpus repositories. Never interpret a failed request as PASS.
    """
    headers={"Accept":"application/vnd.github+json","User-Agent":"combined-corpus-admission-validator"}
    token=os.environ.get("GITHUB_TOKEN")
    if token: headers["Authorization"]=f"Bearer {token}"
    try:
        with urllib.request.urlopen(urllib.request.Request(url,headers=headers),timeout=30) as response:
            return json.load(response)
    except urllib.error.HTTPError as exc:
        if exc.code != 403 or not token:
            raise
        # Public corpus repos can be inspected anonymously if token scope blocks them.
        headers.pop("Authorization",None)
        with urllib.request.urlopen(urllib.request.Request(url,headers=headers),timeout=30) as response:
            return json.load(response)
HEADS={}
def tree(repo):
    try:
        ref=github_json(f"https://api.github.com/repos/{repo}/git/ref/heads/main")
        HEADS[repo]=ref["object"]["sha"]
        payload=github_json(f"https://api.github.com/repos/{repo}/git/trees/{HEADS[repo]}?recursive=1")
        if payload.get("truncated"): raise RuntimeError(f"Git tree truncated for {repo}")
        return {x.get("path"): {"type":x.get("type"),"sha":x.get("sha")} for x in payload.get("tree",[])}
    except urllib.error.HTTPError as exc:
        if exc.code not in (403,429): raise
        # Public Git transport is an independent, exact-tree acquisition route.
        # A rate/scope error never becomes PASS and no files are executed.
        with tempfile.TemporaryDirectory(prefix="corpus-admission-") as folder:
            subprocess.run(["git","clone","--quiet","--bare","--depth=1","--branch=main",f"https://github.com/{repo}.git",folder],check=True,capture_output=True,timeout=120)
            HEADS[repo]=subprocess.check_output(["git","-C",folder,"rev-parse","HEAD"],text=True).strip()
            output=subprocess.check_output(["git","-C",folder,"ls-tree","-r","-t","-z","HEAD"])
            result={}
            for item in output.split(b"\0"):
                if not item:continue
                metadata,path=item.decode().split("\t",1);mode,kind,sha=metadata.split()
                result[path]={"type":kind,"sha":sha}
            print(f"{repo}: API unavailable; exact public Git tree acquired at {HEADS[repo]}",flush=True)
            return result

def raw_bytes(repo, path):
    url=f"https://raw.githubusercontent.com/{repo}/{HEADS[repo]}/{urllib.parse.quote(path)}"
    with urllib.request.urlopen(urllib.request.Request(url,headers={"User-Agent":"combined-corpus-admission-validator"}),timeout=30) as response:
        return response.read()

def validate_adapter(repo, member):
    path=member.get('contract_adapter_path')
    if not path:return
    index=json.loads(raw_bytes(repo,path))
    gates={'corpus_is_authoritative','missing_means_unknown','cross_corpus_equivalence_requires_explicit_evidence','preserve_uncertainty','preserve_source_independence','preserve_rights'}
    if index.get('schema_version')!='0.3.1' or index.get('repository')!=repo:raise ValueError('adapter identity/version mismatch')
    if set(index.get('contract',{}))!=gates or any(v is not True for v in index['contract'].values()):raise ValueError('disabled behavioral contract')
    if index.get('scientific_approval_granted') is not False:raise ValueError('adapter falsely grants scientific approval')
    artifacts=index.get('artifacts',[]);seen=set();contents={}
    with ThreadPoolExecutor(max_workers=4) as pool:
        acquired=list(pool.map(lambda item: raw_bytes(repo,item['path']),artifacts))
    for item,data in zip(artifacts,acquired):
        rel=item['path']
        if rel in seen or rel.startswith('/') or '..' in rel.split('/'):raise ValueError('duplicate or unsafe adapter path')
        seen.add(rel);contents[rel]=data
        if hashlib.sha256(data).hexdigest()!=item['sha256'] or len(data)!=item['bytes']:raise ValueError('stale adapter authority: '+rel)
    required=required_license|{member['individual_skill_path'],member['authority_profile_path'],member['bundle_index_path'],'ai-skill/manifest.json','ai-skill/references/fleet-contract.json','ai-skill/references/corpus-project-contract.md','ai-skill/scripts/fleet_contract.py',member['validation_path']}
    if not required<=seen:raise ValueError('adapter omits required authorities')
    manifest=json.loads(contents['ai-skill/manifest.json'])
    if manifest.get('master_contract_0_3_1')!='IMPLEMENTED' or manifest.get('skill_version')!=member['required_skill_version']:raise ValueError('member contract/version declaration mismatch')
    authority=json.loads(contents[member['authority_profile_path']]);native=json.loads(contents[member['bundle_index_path']])
    required.update(a['path'] for a in authority.get('required_authorities',[]) if a.get('required'))
    required.update(native.get('authoritative_inputs',[]));required.update(native.get('files',[]));required.update(a['path'] for a in native.get('artifacts',[]))
    if authority.get('canonical_dataset'):required.add(authority['canonical_dataset'])
    if not required<=seen:raise ValueError('adapter omits native corpus evidence')
    print(f"{repo}: immutable authority replay PASS at {HEADS[repo]}")

def validate_member(member):
    repo=member.get("repository"); admission=member.get("admission",{})
    if admission.get("status")=="PENDING":
        if not admission.get("reason"): errors.append(f"{repo}: pending candidate missing documented admission blocker")
        if admission.get("master_ai_member") is not False: errors.append(f"{repo}: pending candidate must not claim certified master membership")
        # A registered candidate is discoverable but NOT admitted; do not certify rights or skill compliance.
        return
    if admission.get("status")!="PASS": errors.append(f"{repo}: invalid admission status")
    if admission.get("contract")!="corpus-factory/CORPUS-ADMISSION-CONTRACT.md": errors.append(f"{repo}: missing admission contract declaration")
    if set(admission.get("licensing_paths",[])) != required_license: errors.append(f"{repo}: licensing path declaration differs from required architecture")
    skill_paths={member.get("individual_skill_path"),member.get("bundle_index_path"),member.get("authority_profile_path"),member.get("validation_path")}
    if None in skill_paths or "" in skill_paths:
        errors.append(f"{repo}: incomplete individual AI skill declaration"); return
    for key in ["review_directory_path","review_manifest_path","review_packets_path","source_checks_path","source_worklist_path","review_validator_path"]:
        if member.get(key):skill_paths.add(member[key])
    try: paths=tree(repo)
    except Exception as exc:
        errors.append(f"{repo}: cannot inspect main tree: {exc}"); return
    required_files=required_license|skill_paths-{member.get("review_directory_path")}
    missing=sorted(p for p in required_files if not paths.get(p) or paths[p].get("type")!="blob")
    review_dir=member.get("review_directory_path")
    if review_dir and (not paths.get(review_dir) or paths[review_dir].get("type")!="tree"): missing.append(review_dir+" [directory]")
    if missing:
        errors.append(f"{repo}: missing required admission paths: {', '.join(missing)}")
        return
    try:
        with ThreadPoolExecutor(max_workers=4) as pool:
            names=sorted(required_license)
            data=list(pool.map(lambda name: raw_bytes(repo,name).decode("utf-8"),names))
        license_text=dict(zip(names,data))
    except Exception as exc:
        errors.append(f"{repo}: licensing acquisition failed: {exc}"); return
    semantic_checks=[
        ("LICENSE","polyform noncommercial"),
        ("LICENSE","cc by-nc 4.0"),
        ("LICENSE-CODE","polyform noncommercial"),
        ("LICENSE-CONTENT.md","noncommercial"),
        ("LICENSE-CONTENT.md","attribution"),
        ("LICENSING.md","commercial"),
    ]
    for name,phrase in semantic_checks:
        if phrase not in license_text[name].lower():
            errors.append(f"{repo}: {name} missing expected licensing marker: {phrase}")
    try: validate_adapter(repo,member)
    except Exception as exc: errors.append(f"{repo}: adapter validation failed: {exc}")
    notice=license_text["NOTICE"].lower()
    if not any(marker in notice for marker in ("third-party","upstream","public-domain","public domain","source attribution","component rights","component licences","component licenses","reference source","retain cc","redistributed under cc")):
        errors.append(f"{repo}: NOTICE does not visibly preserve source/upstream rights context")
with ThreadPoolExecutor(max_workers=4) as pool:
    list(pool.map(validate_member,registry.get("members",[])))

if errors:
    print("\n".join(errors)); sys.exit(1)
print(f"Fleet admission validation PASS: {sum(m.get('admission',{}).get('status')=='PASS' for m in registry.get('members',[]))} admitted corpora checked; {sum(m.get('admission',{}).get('status')=='PENDING' for m in registry.get('members',[]))} explicitly pending and NOT certified.")
