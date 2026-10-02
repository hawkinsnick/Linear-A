#!/usr/bin/env python3
"""Academic-scrutiny regression tests for the Linear A AI research package."""
import json, re, sys
from pathlib import Path
R=Path(__file__).resolve().parents[2]
errors=[]
skill=(R/"ai-skill/SKILL.md").read_text()
status=json.loads((R/"analysis/current-status.json").read_text())
required=["analysis/current-status.json","release/CLAIM-REGISTRY.csv","DATA-LICENSE-MATRIX.md","THIRD-PARTY-NOTICES.md"]
for p in required:
 if not (R/p).is_file(): errors.append("missing required authority: "+p)
for phrase in ["not a decipherment","Never invent","SigLA-derived"]:
 if phrase.lower() not in skill.lower(): errors.append("guardrail absent: "+phrase)
if status["scientific_results"].get("calibration_executed") is not False: errors.append("unexpected calibration state")
if status["scientific_results"].get("multiverse_2_5")!="QUARANTINED": errors.append("quarantined analysis state lost")
if errors: print("\n".join(errors));sys.exit(1)
print("Linear A academic-scrutiny AI regression PASS")
