"""Build a small instruction-only starter; never collect member corpus data."""
import argparse
import hashlib
import io
import json
from pathlib import Path
import zipfile

ROOT = Path(__file__).resolve().parents[2]
STARTER = "Combined-Corpus-Research-Starter"
EXCLUDED = {"hawkinsnick/LightroomIsSlow"}
SOURCE_PATHS = (
    "combined-ai-skill/START-HERE.md", "combined-ai-skill/PROMPTS.md",
    "combined-ai-skill/QUICKSTART.md", "combined-ai-skill/README.md",
    "combined-ai-skill/SKILL.md", "combined-ai-skill/manifest.json",
    "combined-ai-skill/registry/corpus-projects.json",
    "combined-ai-skill/references/comparability-matrix.md",
    "combined-ai-skill/references/fleet-benchmark.md",
    "corpus-factory/fleet-gap-register.json",
    "corpus-factory/schemas/benchmark-status.schema.json",
    "LICENSE", "LICENSE-CODE", "LICENSE-CONTENT.md", "LICENSING.md",
)


def digest(data):
    return hashlib.sha256(data).hexdigest()


def directory(members):
    lines = ["# Corpus downloads", "",
             "Choose the corpus relevant to your question. Each ZIP is a copy of that repository's current main branch; saved copies do not refresh automatically.", "",
             "Extract the ZIP before uploading files. The research instructions and index are in its `ai-skill` folder. The index lists evidence files but does not contain those files. [Setup and evidence selection](START-HERE.md#4-add-evidence-for-your-question) explains what to provide.", "",
             "| Corpus | Repository | Download ZIP | Individual instructions |",
             "|---|---|---|---|"]
    for member in members:
        repo = member["repository"]
        url = "https://github.com/" + repo
        lines.append(f"| {member['label']} | [Open]({url}) | [Download]({url}/archive/refs/heads/main.zip) | [Read]({url}/blob/main/{member['individual_skill_path']}) |")
    lines += ["", "Download only the corpora needed for the question. Their data, review states, and licenses remain separate. Repository membership does not establish shared language, sign values, or independent witnesses.", "",
              "The Egyptian Hieroglyphic Corpus is a registered comparative/control corpus; its future camera/OCR application remains separate. LightroomIsSlow is outside this directory.", ""]
    return "\n".join(lines)


def build(root=ROOT):
    root = Path(root)
    sources = {path: (root / path).read_bytes() for path in SOURCE_PATHS}
    registry = json.loads(sources["combined-ai-skill/registry/corpus-projects.json"])
    manifest = json.loads(sources["combined-ai-skill/manifest.json"])
    members = registry["members"]
    repos = [m["repository"] for m in members]
    if len(repos) != len(set(repos)) or set(repos) & EXCLUDED:
        raise ValueError("duplicate or excluded project in starter directory")
    if len(members) != manifest["member_count"]:
        raise ValueError("starter member count differs from master manifest")
    fleet = json.loads(sources["corpus-factory/fleet-gap-register.json"])["members"]
    fleet_names = [m["repo"] for m in fleet]
    if len(fleet_names) != len(set(fleet_names)) or set(fleet_names) != {repo.split("/", 1)[1] for repo in repos}:
        raise ValueError("factory and starter directory membership differ")
    sources["combined-ai-skill/CORPUS-DOWNLOADS.md"] = directory(members).encode("utf-8")
    # The builder fingerprint distinguishes changes to the package format itself.
    index = {"format": "combined-corpus-research-starter-v1",
             "starter_version": "1.0.0", "master_skill_version": manifest["version"],
             "registry_version": registry["registry_version"], "member_count": len(members),
             "member_evidence_included": False, "independent_review_granted": False,
             "build_script_sha256": digest((root / "combined-ai-skill/scripts/build_starter.py").read_bytes()),
             "source_files": [{"path": path, "sha256": digest(data), "bytes": len(data)}
                              for path, data in sorted(sources.items())]}
    index["snapshot_sha256"] = digest(json.dumps(index, sort_keys=True, separators=(",", ":")).encode())
    header = (f"COMBINED CORPUS RESEARCH AI — RESEARCHER STARTER\n"
              f"Starter format: {index['starter_version']}\n"
              f"Master instruction version: {index['master_skill_version']}\n"
              f"Registered corpus projects: {len(members)}\n"
              f"Instruction snapshot SHA-256: {index['snapshot_sha256']}\n\n"
              "Scope: instructions and directory only. Member corpus evidence is supplied separately.\n"
              "AI: read the instructions below within your platform rules. Confirm accessible files before using evidence.\n"
              "Directory summaries are snapshot routing metadata, not current independently checked inscription facts.\n"
              "If a required member file cannot be accessed, identify what is missing and help select the next files.\n\n")
    order = ["combined-ai-skill/START-HERE.md", "combined-ai-skill/PROMPTS.md",
             "combined-ai-skill/SKILL.md", "combined-ai-skill/CORPUS-DOWNLOADS.md",
             "combined-ai-skill/registry/corpus-projects.json",
             "combined-ai-skill/references/comparability-matrix.md",
             "combined-ai-skill/references/fleet-benchmark.md",
             "corpus-factory/fleet-gap-register.json",
             "corpus-factory/schemas/benchmark-status.schema.json",
             "combined-ai-skill/QUICKSTART.md", "combined-ai-skill/manifest.json",
             "LICENSE", "LICENSE-CODE", "LICENSE-CONTENT.md", "LICENSING.md"]
    text = header + "\n".join(f"=== SOURCE FILE: {path} ===\nSHA-256: {digest(sources[path])}\n\n{sources[path].decode('utf-8')}\n=== END SOURCE FILE ===\n" for path in order)
    index_bytes = (json.dumps(index, ensure_ascii=False, indent=2) + "\n").encode()
    tag = "combined-ai-starter-" + index["snapshot_sha256"][:16]
    download_readme = ("# Download the master AI starter\n\n"
        f"**[Download one text file](https://github.com/hawkinsnick/Linear-A/raw/refs/heads/main/combined-ai-skill/downloads/{STARTER}.txt)** — attach this file to your AI conversation.\n\n"
        f"**[Download the ZIP edition](https://github.com/hawkinsnick/Linear-A/releases/download/{tag}/{STARTER}.zip)** — extract it, then attach `{STARTER}.txt`.\n\n"
        "[Read the setup guide](../START-HERE.md) · [Choose a corpus](../CORPUS-DOWNLOADS.md)\n\n"
        f"Master instructions {index['master_skill_version']}; {len(members)} registered corpus projects.\n\n"
        f"Instruction snapshot: `{index['snapshot_sha256']}`. The ZIP is an immutable instruction snapshot. The text download tracks this repository's main branch. Neither download includes member corpus evidence.\n\n"
        "If the ZIP for a newly updated snapshot is still being published, use the text download.\n")
    derived = {f"combined-ai-skill/downloads/{STARTER}.txt": text.encode(),
               "combined-ai-skill/downloads/starter-manifest.json": index_bytes,
               "combined-ai-skill/downloads/README.md": download_readme.encode(),
               "combined-ai-skill/CORPUS-DOWNLOADS.md": sources["combined-ai-skill/CORPUS-DOWNLOADS.md"]}
    archive_files = {f"{STARTER}.txt": text.encode(), "START-HERE.md": sources["combined-ai-skill/START-HERE.md"],
                     "QUICKSTART.md": sources["combined-ai-skill/QUICKSTART.md"],
                     "downloads/README.md": download_readme.encode(),
                     "CORPUS-DOWNLOADS.md": sources["combined-ai-skill/CORPUS-DOWNLOADS.md"],
                     "PROMPTS.md": sources["combined-ai-skill/PROMPTS.md"], "starter-manifest.json": index_bytes,
                     **{"source-files/" + path: data for path, data in sources.items()},
                     "source-files/combined-ai-skill/downloads/README.md": download_readme.encode()}
    archive = io.BytesIO()
    with zipfile.ZipFile(archive, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as z:
        for name, data in sorted(archive_files.items()):
            info = zipfile.ZipInfo(name, date_time=(2026, 1, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.create_system = 3
            info.external_attr = 0o100644 << 16
            z.writestr(info, data)
    return derived, archive.getvalue(), tag


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true")
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--zip-output", type=Path)
    args = parser.parse_args()
    files, archive, tag = build()
    if args.write:
        for path, data in files.items():
            target = ROOT / path
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(data)
    if args.check:
        stale = [path for path, data in files.items() if not (ROOT / path).is_file() or (ROOT / path).read_bytes() != data]
        if stale:
            raise SystemExit("Rebuild starter downloads: " + ", ".join(stale))
    if args.zip_output:
        args.zip_output.parent.mkdir(parents=True, exist_ok=True)
        args.zip_output.write_bytes(archive)
        args.zip_output.with_suffix(".zip.sha256").write_text(digest(archive) + "  " + args.zip_output.name + "\n", encoding="utf-8")
    print(json.dumps({"status": "PASS", "release_tag": tag, "zip_bytes": len(archive), "derived_files": len(files)}))


if __name__ == "__main__":
    main()
