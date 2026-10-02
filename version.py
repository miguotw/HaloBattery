"""Release version: upstream base plus this fork's revision.

After merging an upstream release, update UPSTREAM_VERSION and reset FORK_REVISION to 1.
Increment FORK_REVISION for subsequent releases based on the same upstream version.
"""
UPSTREAM_VERSION = "1.13.0"
FORK_REVISION = 1
VERSION = f"{UPSTREAM_VERSION}.{FORK_REVISION}"
