#!/usr/bin/env python3
import json, pathlib, sys
root=pathlib.Path(__file__).resolve().parents[1]
reg=json.loads((root/"fleet-gap-register.json").read_text())
required={"repo","evidence_depth","coverage_state","top_gap"}
errors=[]
seen=set()
for i,m in enumerate(reg.get("members",[])):
    miss=required-set(m)
    if miss: errors.append(f"member {i} missing {sorted(miss)}")
    if m.get("repo") in seen: errors.append(f"duplicate repo {m.get('repo')}")
    seen.add(m.get("repo"))
if len(reg.get("members",[]))!=11: errors.append("fleet must contain 11 corpus projects")
if reg.get("rule")!="Parity is rigor and traceability under surviving evidence, never equal row counts.": errors.append("parity rule changed")
if errors:
    print("\n".join(errors)); sys.exit(1)
print(f"PASS: {len(seen)} corpus projects; benchmark register structurally valid")
