#!/usr/bin/env python3
import json,re,sys
from pathlib import Path
R=Path(__file__).resolve().parents[1]
errors=[]
reg=json.loads((R/"registry"/"corpus-projects.json").read_text())
tests=json.loads((R/"tests"/"adversarial-cases.json").read_text())
manifest=json.loads((R/"manifest.json").read_text())
skill=(R/"SKILL.md").read_text()
members=reg.get("members",[])
if reg.get("registry_version")!="1.6.0": errors.append("registry version must be 1.6.0")
if len(members)!=manifest.get("member_count"): errors.append("registry and manifest member counts differ")
repos=[m.get("repository") for m in members]
if len(repos)!=len(set(repos)): errors.append("duplicate repository in registry")
required=("repository","label","individual_skill_path","bundle_index_path","required_contract","required_skill_version","authority_profile_path","validation_path")
for member in members:
    for key in required:
        if not member.get(key): errors.append("missing "+key+" for "+str(member.get("repository")))
    if member.get("repository") not in {"hawkinsnick/Anatolian-Hieroglyphic","hawkinsnick/Archanes-Script","hawkinsnick/Aegean-anomalous"} and member.get("required_skill_version")!="0.3.1":
        errors.append("legacy member not pinned to hardened skill 0.3.1: "+str(member.get("repository")))
pre=[m for m in members if m.get("pre_expert_maximum_path")]
if len(pre)<8: errors.append("pre-expert maximum coverage unexpectedly low")
for member in pre:
    if not member.get("current_gate") or "PRE_EXPERT_MAXIMUM" not in member.get("current_gate",""):
        errors.append("pre-expert member missing explicit current gate: "+str(member.get("repository")))
cases=tests.get("cases",[])
ids=[c.get("id") for c in cases]
if len(cases)<12: errors.append("adversarial suite too small")
if len(ids)!=len(set(ids)): errors.append("duplicate adversarial test id")
match=re.search(r"^version:\s*([^\s]+)",skill,re.M)
if (match.group(1) if match else None)!=manifest.get("version"): errors.append("combined SKILL and manifest versions differ")
if errors:
    print("\n".join(errors)); sys.exit(1)
print(f"Combined integration contract PASS: {len(members)} corpus projects validated; {len(cases)} adversarial cases")
