"""Exercise synchronization against local Git repositories, without GitHub access."""
import subprocess
import tempfile
import unittest
from pathlib import Path

from tools.sync_upstream import BRANCH, MergeConflict, git, prepare


class SyncUpstreamTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="halo_sync_")
        self.addCleanup(self.temp.cleanup)
        root = Path(self.temp.name)
        self.upstream, self.origin, self.work = root/"upstream", root/"origin.git", root/"work"
        self.upstream.mkdir()
        git(self.upstream, "init", "-b", "main")
        git(self.upstream, "config", "user.name", "Test")
        git(self.upstream, "config", "user.email", "test@example.invalid")
        self.commit(self.upstream, "shared.txt", "original\n")
        self.command(root, "clone", "--bare", str(self.upstream), str(self.origin))
        self.command(root, "clone", str(self.origin), str(self.work))
        git(self.work, "config", "user.name", "Test")
        git(self.work, "config", "user.email", "test@example.invalid")
        self.commit(self.work, "fork.txt", "fork feature\n")
        git(self.work, "push", "origin", "main")
        self.main_sha = git(self.work, "rev-parse", "HEAD").stdout.strip()

    def command(self, root, *args):
        result = subprocess.run(["git", *args], cwd=root, capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)

    def commit(self, repo, filename, text):
        (repo/filename).write_text(text, encoding="utf-8")
        git(repo, "add", filename)
        git(repo, "commit", "-m", "Update " + filename)

    def prepare(self):
        return prepare(self.work, str(self.upstream))

    def remote_main(self):
        return git(self.work, "ls-remote", "origin", "refs/heads/main").stdout.split()[0]

    def test_no_upstream_changes_create_no_branch(self):
        self.assertIsNone(self.prepare())
        self.assertEqual(git(self.work, "branch", "--show-current").stdout.strip(), "main")
        self.assertEqual(self.remote_main(), self.main_sha)

    def test_clean_merge_preserves_fork_and_upstream_history(self):
        self.commit(self.upstream, "upstream.txt", "new upstream feature\n")
        upstream_sha = git(self.upstream, "rev-parse", "HEAD").stdout.strip()
        sha = self.prepare()
        self.assertEqual((self.work/"fork.txt").read_text(), "fork feature\n")
        self.assertEqual((self.work/"upstream.txt").read_text(), "new upstream feature\n")
        parents = git(self.work, "show", "-s", "--format=%P", sha).stdout.split()
        self.assertEqual(parents, [self.main_sha, upstream_sha])
        self.assertEqual(self.remote_main(), self.main_sha)

    def test_conflict_aborts_without_pushing_or_leaving_merge_state(self):
        self.commit(self.work, "shared.txt", "fork value\n")
        git(self.work, "push", "origin", "main")
        before = self.remote_main()
        self.commit(self.upstream, "shared.txt", "upstream value\n")
        with self.assertRaises(MergeConflict) as error:
            self.prepare()
        self.assertEqual(error.exception.files, ["shared.txt"])
        self.assertEqual(self.remote_main(), before)
        self.assertEqual(git(self.work, "status", "--porcelain").stdout, "")
        self.assertFalse((self.work/".git/MERGE_HEAD").exists())

    def test_existing_sync_branch_keeps_manual_edits_and_new_main_changes(self):
        self.commit(self.upstream, "upstream.txt", "upstream one\n")
        self.prepare()
        self.commit(self.work, "manual.txt", "manual resolution\n")
        manual_sha = git(self.work, "rev-parse", "HEAD").stdout.strip()
        git(self.work, "push", "origin", f"HEAD:refs/heads/{BRANCH}")
        git(self.work, "checkout", "main")
        self.commit(self.work, "fork.txt", "fork feature two\n")
        git(self.work, "push", "origin", "main")
        self.commit(self.upstream, "upstream.txt", "upstream two\n")
        sha = self.prepare()
        self.assertEqual((self.work/"manual.txt").read_text(), "manual resolution\n")
        self.assertEqual((self.work/"fork.txt").read_text(), "fork feature two\n")
        self.assertEqual((self.work/"upstream.txt").read_text(), "upstream two\n")
        git(self.work, "merge-base", "--is-ancestor", manual_sha, sha)

    def test_dirty_checkout_is_rejected_without_losing_changes(self):
        (self.work/"fork.txt").write_text("unsaved\n")
        with self.assertRaisesRegex(RuntimeError, "clean checkout"):
            self.prepare()
        self.assertEqual((self.work/"fork.txt").read_text(), "unsaved\n")
        self.assertEqual(self.remote_main(), self.main_sha)

    def test_main_already_contains_upstream_creates_no_pr_candidate(self):
        self.commit(self.upstream, "upstream.txt", "update\n")
        self.prepare()
        git(self.work, "push", "origin", "HEAD:refs/heads/main")
        self.assertIsNone(self.prepare())
