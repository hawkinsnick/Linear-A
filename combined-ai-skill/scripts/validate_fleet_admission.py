#!/usr/bin/env python3
"""Validate fleet admission against each registered repository's current main tree."""
import base64, json, os, sys, urllib.request
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
registry=json.loads((ROOT/"combined-ai-skill/registry/corpus-projects.json").read_text())
errors=[]
required_license={"LICENSE","LICENSE-CODE","LICENSE-CONTENT.md","LICENSING.md","NOTICE"}
def tree(repo):
    url=f"https://api.github.com/repos/{repo}/git/trees/main?recursive=1"
    headers={"Accept":"application/vnd.github+json","User-Agent":"combined-corpus-admission-validator"}
    token=os.environ.get("GITHUB_TOKEN")
    if token: headers["Authorization"]=f"Bearer {token}"
    req=urllib.request.Request(url,headers=headers)
    with urllib.request.urlopen(req,timeout=30) as r: payload=json.load(r)
    if payload.get("truncated"): raise RuntimeError(f"Git tree truncated for {repo}")
    return {x.get("path"): {"type":x.get("type"),"sha":x.get("sha")} for x in payload.get("tree",[])}

def blob_text(repo, sha):
    url=f"https://api.github.com/repos/{repo}/git/blobs/{sha}"
    headers={"Accept":"application/vnd.github+json","User-Agent":"combined-corpus-admission-validator"}
    token=os.environ.get("GITHUB_TOKEN")
    if token: headers["Authorization"]=f"Bearer {token}"
    req=urllib.request.Request(url,headers=headers)
    with urllib.request.urlopen(req,timeout=30) as r: payload=json.load(r)
    if payload.get("encoding")!="base64": raise RuntimeError(f"unexpected blob encoding for {repo}")
    return base64.b64decode(payload["content"]).decode("utf-8","replace")
for member in registry.get("members",[]):
    repo=member.get("repository"); admission=member.get("admission",{})
    if admission.get("contract")!="corpus-factory/CORPUS-ADMISSION-CONTRACT.md": errors.append(f"{repo}: missing admission contract declaration")
    if admission.get("status")!="PASS": errors.append(f"{repo}: admission status is not PASS")
    if set(admission.get("licensing_paths",[])) != required_license: errors.append(f"{repo}: licensing path declaration differs from required architecture")
    skill_paths={member.get("individual_skill_path"),member.get("bundle_index_path"),member.get("authority_profile_path"),member.get("validation_path")}
    if None in skill_paths or "" in skill_paths:
        errors.append(f"{repo}: incomplete individual AI skill declaration"); continue
    for key in ["review_directory_path","review_manifest_path","review_packets_path","source_checks_path","source_worklist_path","review_validator_path"]:
        if member.get(key):skill_paths.add(member[key])
    try: paths=tree(repo)
    except Exception as exc:
        errors.append(f"{repo}: cannot inspect main tree: {exc}"); continue
    required_files=required_license|skill_paths-{member.get("review_directory_path")}
    missing=sorted(p for p in required_files if not paths.get(p) or paths[p].get("type")!="blob")
    review_dir=member.get("review_directory_path")
    if review_dir and (not paths.get(review_dir) or paths[review_dir].get("type")!="tree"): missing.append(review_dir+" [directory]")
    if missing:
        errors.append(f"{repo}: missing required admission paths: {', '.join(missing)}")
        continue
    license_text={name:blob_text(repo,paths[name]["sha"]) for name in required_license}
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
    notice=license_text["NOTICE"].lower()
    if not any(marker in notice for marker in ("third-party","upstream","public-domain","public domain","source attribution","component rights","component licences","component licenses","reference source","retain cc","redistributed under cc")):
        errors.append(f"{repo}: NOTICE does not visibly preserve source/upstream rights context")
if errors:
    print("\n".join(errors)); sys.exit(1)
print(f"Fleet admission PASS: {len(registry.get('members',[]))} registered corpora have licensing architecture, individual AI skill paths, and master membership.")
