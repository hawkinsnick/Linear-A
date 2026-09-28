#!/usr/bin/env python3
"""3.0 claim-registry guardrails."""
import csv,json
from pathlib import Path
PROHIBITED=("deciphered","translation established","morpheme established","linear b calibration successful")
def main():
 rows=list(csv.DictReader(Path("release/CLAIM-REGISTRY.csv").open(encoding="utf-8")))
 errs=[]
 ids=[r["claim_id"] for r in rows]
 if len(ids)!=len(set(ids)):errs.append("duplicate claim_id")
 for r in rows:
  low=r["claim"].lower()
  for p in PROHIBITED:
   if p in low:errs.append(f'{r["claim_id"]}: prohibited unsupported phrase: {p}')
 status=json.loads(Path("analysis/2.5.0_status.json").read_text())
 if status.get("known_answer_calibration_result") is not None:errs.append("unexpected known-answer result")
 if status.get("sigla_2026_prospective_result") is not None:errs.append("unexpected prospective SigLA result")
 if errs:
  print("\n".join("ERROR: "+x for x in errs));return 1
 print(f"Claim audit passed: {len(rows)} registered claims; unresolved gates preserved.");return 0
if __name__=="__main__":raise SystemExit(main())
