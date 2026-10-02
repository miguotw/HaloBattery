"""Language selection, persistence and live menu updates without hardware."""
import json
import os
import tempfile
import unittest
from unittest import mock
from test_hide_rename import hb, make_app, dev
import i18n


class LanguageTests(unittest.TestCase):
    def setUp(self):
        i18n.set_language("zh-TW")
        self.addCleanup(i18n.set_language, "zh-TW")

    def test_both_menus_and_notifications(self):
        for language, preferences, refresh in (("en", "Preferences", "Refresh now"),
                                               ("zh-TW", "偏好設定", "立即更新")):
            with self.subTest(language=language):
                app = make_app({"language": language})
                menu = app.build_menu(None)
                self.assertIn(refresh, [item.text for item in menu.items])
                prefs = next(item.submenu for item in menu.items if item.text == preferences)
                options = prefs.items[0].submenu.items
                self.assertEqual([item.text for item in options], ["English", "繁體中文"])
                self.assertEqual([item.text for item in options if item.checked],
                                 [dict(i18n.LANGUAGES)[language]])
        i18n.set_language("en")
        self.assertEqual(hb.low_battery_text("Mouse", 15, False),
                         "Mouse: 15% left. Time to charge.")
        self.assertEqual(hb.fully_charged_text("Mouse"), "Mouse is fully charged.")
        self.assertIn("Download v1.2.3…", hb.update_text("1.2.3"))
        self.assertEqual(hb.history.format_left(18000), "about 5 h of use left")
        state = dev()
        state.approx = "about 50% (medium), charging"
        self.assertEqual(hb.device_state(state), state.approx)

    def test_select_language_saves_and_rebuilds_menu_and_tooltip(self):
        app = make_app()
        owner = mock.Mock(status=dev())
        app.icons = {"device": owner}
        app.placeholder = mock.Mock()
        with mock.patch.object(hb, "save_config") as save:
            prefs = next(item.submenu for item in app.build_menu(None).items
                         if item.text == "偏好設定")
            prefs.items[0].submenu.items[0](None)
        save.assert_called_once_with(app.cfg)
        self.assertEqual(app.cfg["language"], "en")
        owner.update.assert_called_once_with(owner.status)
        self.assertIn("Preferences", [item.text for item in owner.icon.menu.items])
        self.assertIn("No devices found", app.placeholder.title)
        self.assertTrue(app.wake.is_set())

    def test_persisted_language_and_invalid_values(self):
        with tempfile.TemporaryDirectory() as directory:
            path = os.path.join(directory, "config.json")
            with mock.patch.object(hb, "CONFIG_PATH", path):
                for language in ("en", "zh-TW", "invalid", None, 42):
                    with open(path, "w", encoding="utf-8") as file:
                        json.dump({"language": language}, file)
                    expected = language if language in ("en", "zh-TW") else i18n.DEFAULT_LANGUAGE
                    self.assertEqual(hb.load_config()["language"], expected)
                cfg = dict(hb.DEFAULTS, language="en")
                hb.save_config(cfg)
                self.assertEqual(hb.load_config()["language"], "en")

    def test_all_ui_strings_have_english_translations(self):
        import ast
        from pathlib import Path
        for filename in ("halo_battery.pyw", "history.py"):
            tree = ast.parse(Path(filename).read_text(encoding="utf-8"))
            for node in ast.walk(tree):
                if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id == "tr":
                    arg = node.args[0]
                    if isinstance(arg, ast.Constant) and any("\u4e00" <= char <= "\u9fff" for char in arg.value):
                        self.assertIn(arg.value, i18n.ENGLISH)
