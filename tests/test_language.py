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
        detector = mock.patch.object(i18n, "detect_system_language", return_value="en")
        detector.start()
        self.addCleanup(detector.stop)

    def test_all_language_menus_and_notifications(self):
        for language, preferences, refresh in (("en", "Preferences", "Refresh now"),
                                               ("zh-TW", "偏好設定", "立即更新"),
                                               ("ja", "設定", "今すぐ取得")):
            with self.subTest(language=language):
                app = make_app({"language": language})
                menu = app.build_menu(None)
                self.assertIn(refresh, [item.text for item in menu.items])
                prefs = next(item.submenu for item in menu.items if item.text == preferences)
                options = prefs.items[0].submenu.items
                self.assertEqual([item.text for item in options], ["English", "繁體中文", "日本語"])
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

    def test_japanese_notifications_and_status(self):
        i18n.set_language("ja")
        self.assertEqual(hb.low_battery_text("Mouse", 15, False),
                         "Mouse: バッテリー残量 15%。充電してください。")
        self.assertEqual(hb.fully_charged_text("Mouse"), "Mouse の充電が完了しました。")
        self.assertIn("v1.2.3 をダウンロード…", hb.update_text("1.2.3"))
        self.assertEqual(hb.history.format_left(18000), "あと約 5 時間使用できます")
        state = dev()
        state.approx = "about 50% (medium), charging"
        self.assertEqual(hb.device_state(state), "約 50% (中程度)、充電中")
        self.assertEqual(set(i18n.ENGLISH), set(i18n.JAPANESE))
        import string
        for key, translated in i18n.JAPANESE.items():
            fields = lambda text: {field for _, field, _, _ in string.Formatter().parse(text)
                                   if field is not None}
            self.assertEqual(fields(key), fields(translated), key)

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
                for language in ("en", "zh-TW", "ja", "invalid", None, 42):
                    with open(path, "w", encoding="utf-8") as file:
                        json.dump({"language": language}, file)
                    expected = language if language in ("en", "zh-TW", "ja") else i18n.DEFAULT_LANGUAGE
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


class SystemLanguageTests(unittest.TestCase):
    def test_windows_language_mapping(self):
        for code, expected in ((0x0404, "zh-TW"), (0x0C04, "zh-TW"),
                               (0x1404, "zh-TW"), (0x7C04, "zh-TW"),
                               (0x0411, "ja"), (0x0409, "en"), (0x0809, "en"),
                               (0x0804, "en"), (0x0407, "en"), (0, "en")):
            with self.subTest(code=code):
                self.assertEqual(i18n.language_for_windows_id(code), expected)

    def test_windows_ui_api_and_failure_fallback(self):
        import ctypes
        import sys
        fake = mock.Mock(return_value=0x0411)
        with mock.patch.object(sys, "platform", "win32"), \
             mock.patch.object(ctypes, "windll", create=True) as api:
            api.kernel32.GetUserDefaultUILanguage = fake
            self.assertEqual(i18n.detect_system_language(), "ja")
            fake.side_effect = OSError("unavailable")
            self.assertEqual(i18n.detect_system_language(), "en")
        with mock.patch.object(sys, "platform", "linux"):
            self.assertEqual(i18n.detect_system_language(), "en")

    def test_system_default_and_explicit_choice(self):
        with tempfile.TemporaryDirectory() as directory:
            path = os.path.join(directory, "config.json")
            with mock.patch.object(hb, "CONFIG_PATH", path), \
                 mock.patch.object(i18n, "detect_system_language", return_value="ja"):
                self.assertEqual(hb.load_config()["language"], "ja")
                for data, expected in (({}, "ja"), ({"language": "invalid"}, "ja"),
                                       ({"language": "zh-TW"}, "zh-TW"),
                                       ({"language": "en"}, "en")):
                    with open(path, "w", encoding="utf-8") as file:
                        json.dump(data, file)
                    self.assertEqual(hb.load_config()["language"], expected)
