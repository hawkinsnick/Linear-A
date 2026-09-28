#!/usr/bin/env python3
"""Build deterministic SHA-256 manifest; excludes itself and VCS metadata."""
import hashlib,json
from pathlib import Path
ROOT=Path(".");OUT=Path("MANIFEST-3.0.0.json")
def main():
 rows=[]
 for p in sorted(x for x in ROOT.rglob("*") if x.is_file()):
  rel=p.as_posix()
  if rel==OUT.as_posix() or rel.startswith(".git/"):continue
  b=p.read_bytes();rows.append({"path":rel,"bytes":len(b),"sha256":hashlib.sha256(b).hexdigest()})
 OUT.write_text(json.dumps({"version":"3.0.0","self_excluded":True,"files":rows},indent=2)+"\n")
 print(f"Wrote {OUT} with {len(rows)} entries")
if __name__=="__main__":main()
