"""The fork must retain its own release source and four-part update versions."""
import unittest
from halo import updates, icons

class ForkReleaseTests(unittest.TestCase):
    def test_update_endpoints_use_this_fork(self):
        self.assertEqual(updates.REPO, "miguotw/HaloBattery")
        self.assertIn("miguotw/HaloBattery", updates.API_URL)
        self.assertIn("miguotw/HaloBattery", updates.TAG_URL)
        self.assertIn("miguotw/HaloBattery", updates.RELEASES_URL)

    def test_fork_versions_sort_and_match_release_asset(self):
        self.assertTrue(updates.is_newer("1.15.0.1", "1.14.0.1"))
        self.assertTrue(updates.is_newer("1.15.0.2", "1.15.0.1"))
        rel = updates.parse_release({"tag_name": "v1.15.0.1", "assets": [
            {"name": "HaloBattery-1.15.0.1.zip", "browser_download_url": "https://example.com/build.zip",
             "size": 123, "digest": "sha256:" + "a" * 64}]})
        self.assertEqual(rel.version, "1.15.0.1")
        self.assertIn("phone", icons.PICTOS)
        self.assertNotIn("tablet", icons.PICTOS)
