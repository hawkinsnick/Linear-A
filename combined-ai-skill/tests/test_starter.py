"""Check reproducibility, preserved instructions, scoped content and snapshot pins."""
import copy
import hashlib
import importlib.util
import io
import json
import posixpath
from pathlib import Path
import re
import shutil
import tempfile
import unittest
import zipfile

ROOT = Path(__file__).resolve().parents[2]
spec = importlib.util.spec_from_file_location("starter", ROOT / "combined-ai-skill/scripts/build_starter.py")
starter = importlib.util.module_from_spec(spec)
spec.loader.exec_module(starter)


class StarterTests(unittest.TestCase):
    def test_repeat_build_and_committed_downloads(self):
        a = starter.build(ROOT)
        self.assertEqual(a, starter.build(ROOT))
        for path, data in a[0].items():
            self.assertEqual((ROOT / path).read_bytes(), data, path)

    def test_archive_preserves_sources_and_has_no_member_data(self):
        files, data, tag = starter.build(ROOT)
        with zipfile.ZipFile(io.BytesIO(data)) as z:
            manifest = json.loads(z.read("starter-manifest.json"))
            self.assertFalse(manifest["member_evidence_included"])
            self.assertFalse(manifest["independent_review_granted"])
            self.assertEqual(z.read(starter.STARTER + ".txt"), files[f"combined-ai-skill/downloads/{starter.STARTER}.txt"])
            for source in manifest["source_files"]:
                raw = z.read("source-files/" + source["path"])
                self.assertEqual(hashlib.sha256(raw).hexdigest(), source["sha256"])
            self.assertEqual(z.read("source-files/combined-ai-skill/SKILL.md"), (ROOT / "combined-ai-skill/SKILL.md").read_bytes())
            self.assertFalse(any(n.endswith((".pdf", ".jpg", ".png")) or "/data/" in n or "/imports/" in n for n in z.namelist()))
            self.assertEqual(len(z.namelist()), len(set(z.namelist())))
            self.assertTrue(all(not Path(n).is_absolute() and ".." not in Path(n).parts for n in z.namelist()))
            self.assertIn(manifest["snapshot_sha256"][:16], tag)

    def test_packaged_setup_links_resolve(self):
        _, data, _ = starter.build(ROOT)
        with zipfile.ZipFile(io.BytesIO(data)) as z:
            for path in ["START-HERE.md", "QUICKSTART.md", "CORPUS-DOWNLOADS.md", "downloads/README.md"]:
                text = z.read(path).decode()
                for href in re.findall(r'\]\(([^)]+)\)', text):
                    if href.startswith(("https://", "http://", "#")):
                        continue
                    destination = posixpath.normpath(posixpath.join(posixpath.dirname(path), href.split("#", 1)[0]))
                    self.assertIn(destination, z.namelist(), (path, href))

    def test_source_change_changes_download_and_release_identity(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            for path in (*starter.SOURCE_PATHS, "combined-ai-skill/scripts/build_starter.py"):
                target = root / path
                target.parent.mkdir(parents=True, exist_ok=True)
                shutil.copyfile(ROOT / path, target)
            before = starter.build(root)
            p = root / "combined-ai-skill/SKILL.md"
            p.write_bytes(p.read_bytes() + b"\nTEST ONLY: preserve uncertain readings.\n")
            after = starter.build(root)
            self.assertNotEqual(before[2], after[2])
            self.assertNotEqual(before[1], after[1])

    def test_excluded_project_cannot_enter_starter(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            for path in (*starter.SOURCE_PATHS, "combined-ai-skill/scripts/build_starter.py"):
                target = root / path
                target.parent.mkdir(parents=True, exist_ok=True)
                shutil.copyfile(ROOT / path, target)
            path = root / "combined-ai-skill/registry/corpus-projects.json"
            registry = json.loads(path.read_text())
            bad = copy.deepcopy(registry["members"][0])
            bad["repository"] = "hawkinsnick/Egyptian-Hieroglyphic-Corpus"
            registry["members"][0] = bad
            path.write_text(json.dumps(registry))
            with self.assertRaisesRegex(ValueError, "excluded"):
                starter.build(root)

    def test_factory_mismatch_cannot_be_published(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            for path in (*starter.SOURCE_PATHS, "combined-ai-skill/scripts/build_starter.py"):
                target = root / path
                target.parent.mkdir(parents=True, exist_ok=True)
                shutil.copyfile(ROOT / path, target)
            path = root / "corpus-factory/fleet-gap-register.json"
            register = json.loads(path.read_text())
            register["members"].pop()
            path.write_text(json.dumps(register))
            with self.assertRaisesRegex(ValueError, "membership differ"):
                starter.build(root)


if __name__ == "__main__":
    unittest.main()
