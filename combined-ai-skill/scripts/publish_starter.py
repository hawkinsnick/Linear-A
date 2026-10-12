"""Publish generated starter files only on their validated source parent."""
import argparse
import os
import re
import subprocess
from pathlib import Path

from build_starter import ROOT, build


def git(root, *args):
    return subprocess.check_output(['git', *args], cwd=root, text=True).strip()


def publish(root, expected, before_push=None, builder=build):
    root = Path(root)
    if not re.fullmatch('[0-9a-f]{40}', expected or '') or git(root, 'rev-parse', 'HEAD') != expected:
        raise ValueError('checkout is not the expected source revision')
    files, _, _ = builder(root)
    allowed = set(files)
    for path, data in files.items():
        if (root / path).read_bytes() != data:
            raise ValueError('stale starter output: ' + path)
    changes = git(root, 'diff', '--name-only', 'HEAD').splitlines() + git(root, 'ls-files', '--others', '--exclude-standard').splitlines()
    if any(path not in allowed for path in changes):
        raise ValueError('source or unrelated changes cannot be published as generated downloads')
    subprocess.run(['git', 'fetch', '--no-tags', 'origin', 'main'], cwd=root, check=True, stdout=subprocess.DEVNULL)
    if git(root, 'rev-parse', 'refs/remotes/origin/main') != expected:
        return {'status': 'SKIPPED_SOURCE_ADVANCED', 'published': False, 'source_commit': expected}
    subprocess.run(['git', 'add', '--', *sorted(allowed)], cwd=root, check=True)
    staged = git(root, 'diff', '--cached', '--name-only').splitlines()
    if any(path not in allowed for path in staged):
        raise ValueError('unrelated staged change')
    if not staged:
        return {'status': 'NO_GENERATED_CHANGES', 'published': False, 'source_commit': expected}
    subprocess.run(['git', 'commit', '-m', 'Refresh validated researcher starter downloads'], cwd=root, check=True, stdout=subprocess.DEVNULL)
    if git(root, 'rev-parse', 'HEAD^') != expected:
        raise ValueError('starter commit does not descend directly from checked source')
    if before_push:
        before_push()
    subprocess.run(['git', 'push', 'origin', 'HEAD:refs/heads/main'], cwd=root, check=True, stdout=subprocess.DEVNULL)
    return {'status': 'PUBLISHED_EXACT_SOURCE_PARENT', 'published': True, 'source_commit': expected, 'bundle_commit': git(root, 'rev-parse', 'HEAD')}


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--source', default=os.environ.get('SOURCE_COMMIT') or os.environ.get('GITHUB_SHA'))
    args = parser.parse_args()
    print(publish(ROOT, args.source))
