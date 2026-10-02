#!/usr/bin/env python3
import hashlib,json,re,sys
from pathlib import Path
R=Path(__file__).resolve().parents[2]; A=R/"ai-skill"; errors=[]
bundle=json.loads((A/"generated"/"research-bundle-index.json").read_text())
manifest=json.loads((A/"manifest.json").read_text())
profile=json.loads((A/"references"/"authority-profile.json").read_text())
skill=(A/"SKILL.md").read_text()
m=re.search(r"^version:\s*([^\s]+)",skill,re.M); declared=m.group(1) if m else None
expected=str(manifest.get("skill_version") or manifest.get("version"))
if declared!=expected: errors.append(f"SKILL version {declared} != manifest {expected}")
if bundle.get("skill_version")!=expected: errors.append(f"bundle skill version {bundle.get('skill_version')} != manifest {expected}")
if bundle.get("schema_version")!=manifest.get("bundle_schema"): errors.append("bundle schema mismatch")
indexed={x.get("path"):x for x in bundle.get("artifacts",[])}
for req in profile.get("required_authorities",[]):
 p=R/req["path"]
 if req.get("required") and not p.is_file(): errors.append("missing authority "+req["path"]); continue
 if p.is_file():
  digest=hashlib.sha256(p.read_bytes()).hexdigest()
  item=indexed.get(req["path"])
  if not item: errors.append("authority not indexed "+req["path"])
  elif item.get("sha256")!=digest: errors.append("authority hash mismatch "+req["path"])
if not bundle.get("source_commit"): errors.append("missing source commit")
if errors: print("\n".join(errors));sys.exit(1)
print(f"{profile['corpus']} AI integration validation PASS")
