"""Prepare an upstream merge on a dedicated branch; never push or merge main."""
from __future__ import annotations

import argparse
import os
from pathlib import Path
import subprocess

BRANCH = "codex/sync-upstream"
UPSTREAM = "https://github.com/HeyOkay/HaloBattery.git"


class MergeConflict(RuntimeError):
    def __init__(self, target, files):
        self.target, self.files = target, files
        super().__init__(f"Merge conflict with {target}: " + ", ".join(files))


def git(repo, *args, check=True):
    result = subprocess.run(["git", *args], cwd=repo, text=True, encoding="utf-8",
                            stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if check and result.returncode:
        raise RuntimeError(result.stderr.strip() or result.stdout.strip())
    return result


def merge(repo, target):
    result = git(repo, "merge", "--no-ff", "--no-edit", target, check=False)
    if result.returncode:
        files = git(repo, "diff", "--name-only", "--diff-filter=U").stdout.splitlines()
        if files:
            git(repo, "merge", "--abort")
            raise MergeConflict(target, files)
        raise RuntimeError(result.stderr.strip() or result.stdout.strip())


def prepare(repo, upstream_url=UPSTREAM):
    if git(repo, "status", "--porcelain").stdout.strip():
        raise RuntimeError("A clean checkout is required; local changes were not touched.")
    git(repo, "fetch", "--no-tags", "origin", "+refs/heads/main:refs/remotes/origin/main")
    git(repo, "fetch", "--no-tags", upstream_url,
        "+refs/heads/main:refs/remotes/upstream/main")
    ancestor = git(repo, "merge-base", "--is-ancestor", "upstream/main", "origin/main", check=False)
    if ancestor.returncode == 0:
        return None
    if ancestor.returncode != 1:
        raise RuntimeError(ancestor.stderr.strip())
    remote = git(repo, "ls-remote", "--exit-code", "--heads", "origin",
                 f"refs/heads/{BRANCH}", check=False)
    if remote.returncode not in (0, 2):
        raise RuntimeError(remote.stderr.strip())
    git(repo, "config", "user.name", "github-actions[bot]")
    git(repo, "config", "user.email", "41898282+github-actions[bot]@users.noreply.github.com")
    if remote.returncode == 0:
        git(repo, "fetch", "--no-tags", "origin",
            f"+refs/heads/{BRANCH}:refs/remotes/origin/{BRANCH}")
        git(repo, "checkout", "-B", BRANCH, f"origin/{BRANCH}")
        merge(repo, "origin/main")
    else:
        git(repo, "checkout", "-B", BRANCH, "origin/main")
    merge(repo, "upstream/main")
    return git(repo, "rev-parse", "HEAD").stdout.strip()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repository", default=".")
    args = parser.parse_args()
    try:
        sha = prepare(Path(args.repository))
    except RuntimeError as error:
        text = f"## Upstream synchronization requires attention\n\n{error}\n\nNo changes were pushed to main. Resolve conflicts on `{BRANCH}` and rerun.\n"
        print(text)
        if os.environ.get("GITHUB_STEP_SUMMARY"):
            with open(os.environ["GITHUB_STEP_SUMMARY"], "a", encoding="utf-8") as stream:
                stream.write(text)
        return 1
    outputs = f"changed={'true' if sha else 'false'}\nsha={sha or ''}\n"
    print(outputs, end="")
    if os.environ.get("GITHUB_OUTPUT"):
        with open(os.environ["GITHUB_OUTPUT"], "a", encoding="utf-8") as stream:
            stream.write(outputs)
    if not sha and os.environ.get("GITHUB_STEP_SUMMARY"):
        with open(os.environ["GITHUB_STEP_SUMMARY"], "a", encoding="utf-8") as stream:
            stream.write("Upstream main is already included. No synchronization PR is needed.\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
