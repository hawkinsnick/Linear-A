#!/usr/bin/env python3
"""Basic structural validation for Linear A Open Corpus CSV data."""

from __future__ import annotations

import csv
from pathlib import Path

REQUIRED = {
    "data/inscriptions.csv": ["document_id", "source_id"],
    "data/sign_occurrences.csv": ["occurrence_id", "document_id", "sign_id"],
    "data/sites.csv": ["site_id", "site_name"],
    "data/bibliography.csv": ["source_id"],
    "data/provenance.csv": ["provenance_id", "source_id"],
    "data/hypotheses.csv": ["hypothesis_id", "scope_id"],
}


def main() -> int:
    errors = []
    for filename, fields in REQUIRED.items():
        path = Path(filename)
        if not path.exists():
            errors.append(f"missing file: {filename}")
            continue
        with path.open(newline="", encoding="utf-8") as handle:
            reader = csv.DictReader(handle)
            missing = [field for field in fields if field not in (reader.fieldnames or [])]
            if missing:
                errors.append(f"{filename}: missing columns: {', '.join(missing)}")

    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1

    print("Structural validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
