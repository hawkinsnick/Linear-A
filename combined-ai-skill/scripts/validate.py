#!/usr/bin/env python3
import json,sys
from pathlib import Path
R=Path(__file__).resolve().parents[1]
reg=json.loads((R/"registry"/"corpus-projects.json").read_text())
tests=json.loads((R/"tests"/"adversarial-cases.json").read_text())
errors=[]
members=reg.get("members",[])
if reg.get("registry_version")!="1.0.0": errors.append("registry version must be 1.0.0")
if len(members)<11: errors.append("expected at least 11 registered corpus projects")
repos=[m.get("repository") for m in members]
if len(repos)!=len(set(repos)): errors.append("duplicate repository in registry")
for m in members:
 for k in ("repository","label","individual_skill_path","bundle_index_path","required_contract"):
  if not m.get(k): errors.append(f"missing {k}: {m}")
if len(tests.get("cases",[]))<12: errors.append("adversarial suite too small")
ids=[c.get("id") for c in tests.get("cases",[])]
if len(ids)!=len(set(ids)): errors.append("duplicate adversarial test id")
if errors:
 print("\n".join(errors));sys.exit(1)
print(f"Combined skill 1.0 structural validation PASS: {len(members)} corpus projects, {len(ids)} adversarial cases")
