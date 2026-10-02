"""Fork languages retain manual choices and precise Windows language matching."""
import ctypes
import json
import os
import tempfile
import unittest
from unittest import mock
import i18n
from test_hide_rename import hb, make_app

class ForkLanguageTests(unittest.TestCase):
    def test_windows_language_mapping(self):
        for code, expected in ((0x0404, "zh-TW"), (0x0C04, "zh-TW"),
                               (0x1404, "zh-TW"), (0x7C04, "zh-TW"),
                               (0x0411, "ja"), (0x0409, "en"), (0x0809, "en"),
                               (0x0804, "zh-CN"), (0x1004, "zh-CN"),
                               (0x0004, "zh-CN"), (0x7804, "zh-CN"), (0x0407, "en"), (0x040C, "fr")):
            with self.subTest(code=code), mock.patch.object(i18n.sys, "platform", "win32"), \
                 mock.patch.object(ctypes, "windll", create=True) as api:
                api.kernel32.GetUserDefaultUILanguage.return_value = code
                self.assertEqual(i18n.detect_language(), expected)

    def test_saved_language_survives_system_language_change(self):
        with tempfile.TemporaryDirectory() as directory:
            path = os.path.join(directory, "config.json")
            with mock.patch.object(hb, "CONFIG_PATH", path), \
                 mock.patch.object(i18n, "detect_language", return_value="fr") as detect:
                for language in ("en", "zh-TW", "zh-CN", "ja", "fr"):
                    with open(path, "w", encoding="utf-8") as file:
                        json.dump({"language": language}, file)
                    self.assertEqual(hb.load_config(initialize_language=True)["language"], language)
                detect.assert_not_called()

    def test_app_languages_are_independent(self):
        chinese = make_app({"language": "zh-TW"})
        simplified = make_app({"language": "zh-CN"})
        self.assertEqual(simplified.tr("menu.preferences"), "首选项")
        self.assertEqual(simplified.tr("icon.phone"), "手机")
        japanese = make_app({"language": "ja"})
        self.assertEqual(chinese.tr("menu.preferences"), "偏好設定")
        self.assertEqual(japanese.tr("menu.preferences"), "設定")
        self.assertEqual(chinese.tr("icon.phone"), "手機")
        self.assertEqual(japanese.tr("icon.phone"), "スマートフォン")
        self.assertEqual(i18n.translate("menu.preferences"), "Preferences")

    def test_asian_languages_have_no_singular_distinction(self):
        for language in ("zh-TW", "zh-CN", "ja"):
            for count in (0, 1, 2, 5):
                self.assertEqual(i18n.LANGUAGES[language].plural_rule(count), "other")
                self.assertIn(str(count), i18n.translate("duration.hours", language=language, count=count))
