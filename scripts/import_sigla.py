#!/usr/bin/env python3
"""License-aware SigLA import scaffold.

Fetches the upstream SigLA machine-readable database, records a source
manifest, and leaves normalization to a later validated importer stage.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import urllib.request
from datetime import date
from pathlib import Path

DEFAULT_URL = "https://sigla.phis.me/database.js"


def fetch(url: str) -> bytes:
    request = urllib.request.Request(
        url,
        headers={"User-Agent": "Linear-A-Open-Corpus/0.2.0"},
    )
    with urllib.request.urlopen(request, timeout=60) as response:
        return response.read()


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", default=DEFAULT_URL)
    parser.add_argument("--raw-dir", default="data/raw/sigla")
    args = parser.parse_args()

    raw_dir = Path(args.raw_dir)
    raw_dir.mkdir(parents=True, exist_ok=True)

    payload = fetch(args.url)
    raw_path = raw_dir / "database.js"
    raw_path.write_bytes(payload)

    manifest = {
        "source_id": "SIGLA",
        "source_url": args.url,
        "retrieved_date": date.today().isoformat(),
        "sha256": sha256(payload),
        "license": "CC BY-NC-SA 4.0",
        "status": "raw source snapshot; parser validation required",
    }
    (raw_dir / "source-manifest.json").write_text(
        json.dumps(manifest, indent=2) + "\n", encoding="utf-8"
    )

    print(f"Fetched {len(payload)} bytes from {args.url}")
    print(f"SHA-256: {sha256(payload)}")
    print("Parser/normalizer is deliberately not executed automatically yet.")


if __name__ == "__main__":
    main()
