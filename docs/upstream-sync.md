# Upstream synchronization

The fork checks `HeyOkay/HaloBattery` main daily at 01:17 UTC (09:17 Asia/Taipei).
GitHub may delay scheduled runs and disables schedules on public repositories
without activity for 60 days. Run **Actions > Sync upstream > Run workflow** to
check manually. The schedule runs only in `miguotw/HaloBattery`.

Updates are merged into `codex/sync-upstream` with merge commits, and one PR is
created or updated against the fork's main. Main is never pushed by this workflow.
Existing synchronization-branch edits are preserved; ordinary pushes reject races
rather than force-overwriting another contributor's work.

The same run validates the exact candidate SHA on Windows: full unit tests with
isolated APPDATA, a probe and a PyInstaller folder build. A separate validation
workflow also covers PRs and main pushes. Its build artifacts expire after seven
days and are test builds, not releases. Bot-created PR checks may need approval;
the synchronization run still performs validation without waiting for those checks.
Review the diff, candidate SHA and linked Actions result before merging manually.
No automatic approval, merge, version bump, tag or Release is configured.

## Setup and permissions

In **Settings > Actions > General > Workflow permissions**, enable **Allow GitHub
Actions to create and approve pull requests**. Keep the default token read-only.
Only the preparation job requests contents and pull-request write permission;
the Windows validation job has read-only access and receives no custom secrets.
This implementation uses the built-in GITHUB_TOKEN and does not require a PAT.
The permission enables PR creation; this workflow never approves a PR.

## Conflicts and failures

A merge conflict aborts preparation before pushing. Actions reports the conflicting
files. If a sync branch already exists, its remote contents remain unchanged.
If a new branch cannot be merged, there is no candidate PR until the conflict is
resolved manually.

To resolve, use a clean checkout and fetch both remotes. Start from the existing
`origin/codex/sync-upstream`, or create that branch from `origin/main` if it does
not exist. Merge `origin/main`, then merge upstream main, resolve the listed files,
commit and push `codex/sync-upstream` normally. Rerun **Sync upstream** to create or
update the PR and validate the resolved commit. Do not force-push this branch.

If tests or the build fail, the PR remains available for fixes and manual review.
Fix the synchronization branch, push and rerun the workflow. A rejected push means
someone updated the branch concurrently; rerun to fetch their changes.
An explicitly closed unmerged PR can be recreated on a later run while upstream
is still ahead; pause the schedule in Actions if you do not want further proposals.

Fork-specific language catalogs, update URLs, icons and versioning need review
when upstream modifies the same behavior, even when Git can merge automatically.
Release publication remains a separate manual decision.
