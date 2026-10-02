"""User interface translations for English, Traditional Chinese and Japanese."""
LANGUAGES = (("en", "English"), ("zh-TW", "繁體中文"), ("ja", "日本語"))
DEFAULT_LANGUAGE = "zh-TW"
_language = DEFAULT_LANGUAGE


def set_language(language):
    global _language
    _language = language if language in dict(LANGUAGES) else DEFAULT_LANGUAGE


def get_language():
    return _language


def tr(text):
    translations = {"en": ENGLISH, "ja": JAPANESE}.get(_language, {})
    return translations.get(text, text)


ENGLISH = {'手機': 'Phone', 'ASUS ROG / TUF 滑鼠': 'ASUS ROG / TUF mice',
 'Corsair 耳機': 'Corsair headsets',
 'G-Wolves 滑鼠': 'G-Wolves mice',
 'LAMZU 滑鼠': 'LAMZU mice',
 'Lofree 鍵盤': 'Lofree keyboards',
 'MCHOSE 滑鼠': 'MCHOSE mice',
 'Nintendo Switch 控制器': 'Nintendo Switch controllers',
 'PlayStation 控制器': 'PlayStation controllers',
 'Pulsar / ATK VXE 滑鼠': 'Pulsar / ATK VXE mice',
 'Razer 滑鼠與耳機': 'Razer mice and headsets',
 'Xbox 相容控制器': 'Xbox-compatible controllers',
 '隨 Windows 啟動': 'Start with Windows',
 '電量不足': 'Low battery',
 '剩餘電量 {level}%': '{level}% left',
 '{name}: {left}。請充電。': '{name}: {left}. Time to charge.',
 '{name} 已充飽電。': '{name} is fully charged.',
 '圖示': 'Icon',
 '自動': 'Automatic',
 '滑鼠': 'Mouse',
 '鍵盤': 'Keyboard',
 '耳機': 'Headset',
 '控制器': 'Controller',
 '藍牙': 'Bluetooth',
 '未連線（已關機或休眠）': 'no link (off or asleep)',
 '，充電中': ', charging',
 '（上次記錄的電量，裝置休眠中）': ' (last known value, device asleep)',
 '找不到裝置': 'No devices found',
 '沒有顯示的裝置（已隱藏 {hidden} 個）': 'No devices shown ({hidden} hidden)',
 '15 秒': '15 s',
 '30 秒': '30 s',
 '1 分鐘': '1 min',
 '2 分鐘': '2 min',
 '5 分鐘': '5 min',
 '白色': 'White',
 '黑色': 'Black',
 '關閉': 'Off',
 '下載更新…': 'Download update…',
 '預設（{low}%）': 'Default ({low}%)',
 '預設（關閉）': 'Default (off)',
 '顯示 {name}': 'Show {name}',
 '重新命名…': 'Rename…',
 '重設名稱': 'Reset name',
 '低電量提醒門檻': 'Low battery alert at',
 '隱藏此裝置': 'Hide this device',
 '更新間隔': 'Poll interval',
 '低電量提醒': 'Low battery alert',
 '充飽電時通知': 'Alert when fully charged',
 '預估剩餘使用時間': 'Estimated time left',
 '遊戲時保持安靜': 'Quiet while gaming',
 'Windows 藍牙裝置': 'Windows Bluetooth devices',
 'PlayStation 完整模式（藍牙）': 'PlayStation full mode (Bluetooth)',
 '裝置類型': 'Device types',
 '裝置圖案': 'Device pictogram',
 '在圖示中顯示百分比': 'Percentage in the icon',
 '充電動畫': 'Charging animation',
 '圖示顏色': 'Icon colour',
 '供其他應用程式使用的狀態檔': 'Status file for other apps',
 '檢查更新': 'Check for updates',
 '立即更新': 'Refresh now',
 '偏好設定': 'Preferences',
 '隱藏的裝置': 'Hidden devices',
 '診斷報告…': 'Diagnostics…',
 '結束（v{VERSION}）': 'Exit (v{VERSION})',
 '已充飽電': 'Fully charged',
 '{APP_TITLE} 更新': '{APP_TITLE} update',
 '剩餘使用時間不到 1 小時': 'less than 1 h of use left',
 '語言': 'Language',
 '已連線，尚未回報電量': 'connected, battery level not reported yet',
 '已接上充電線': 'on cable',
 '上次記錄的電量': 'last known value',
 '充電中': 'charging',
 '極低': 'critical',
 '中等': 'medium',
 '已耗盡': 'empty',
 '滿電': 'full',
 '充足': 'good',
 '偏低': 'low',
 '約 ': 'about ',
 '，': ', ',
 'Halo Battery 正從暫存資料夾執行（直接從 ZIP 開啟）。請先將 ZIP 解壓縮至獨立資料夾，再從該資料夾執行 HaloBattery.exe，接著啟用「隨 Windows 啟動」。': 'Halo '
                                                                                                      'Battery '
                                                                                                      'is '
                                                                                                      'running '
                                                                                                      'from '
                                                                                                      'a '
                                                                                                      'temporary '
                                                                                                      'folder '
                                                                                                      '(straight '
                                                                                                      'from '
                                                                                                      'the '
                                                                                                      'ZIP). '
                                                                                                      'Extract '
                                                                                                      'the '
                                                                                                      'ZIP '
                                                                                                      'to '
                                                                                                      'a '
                                                                                                      'folder '
                                                                                                      'of '
                                                                                                      'its '
                                                                                                      'own, '
                                                                                                      'run '
                                                                                                      'HaloBattery.exe '
                                                                                                      'from '
                                                                                                      'there, '
                                                                                                      'then '
                                                                                                      'turn '
                                                                                                      'on '
                                                                                                      'Start '
                                                                                                      'with '
                                                                                                      'Windows.',
 '請輸入此裝置的新名稱：': 'New name for this device:',
 'Halo Battery - 重新命名': 'Halo Battery - Rename',
 '，{left}': ', {left}',
 '已有新版本 {latest}。請在電量圖示上按右鍵，選擇「下載 v{latest}…」。': 'Version {latest} is available. Right-click a '
                                                 'battery icon and choose "Download v{latest}…".',
 '下載 v{version}…': 'Download v{version}…',
 '約可再使用 {hours} 小時': 'about {hours} h of use left',
 '約可再使用 {days} 天': 'about {days} days of use left'}


JAPANESE = {
    '手機': 'スマートフォン',
    'ASUS ROG / TUF 滑鼠': 'ASUS ROG / TUF マウス',
    'Corsair 耳機': 'Corsair ヘッドセット',
    'G-Wolves 滑鼠': 'G-Wolves マウス',
    'LAMZU 滑鼠': 'LAMZU マウス',
    'Lofree 鍵盤': 'Lofree キーボード',
    'MCHOSE 滑鼠': 'MCHOSE マウス',
    'Nintendo Switch 控制器': 'Nintendo Switch コントローラー',
    'PlayStation 控制器': 'PlayStation コントローラー',
    'Pulsar / ATK VXE 滑鼠': 'Pulsar / ATK VXE マウス',
    'Razer 滑鼠與耳機': 'Razer マウスとヘッドセット',
    'Xbox 相容控制器': 'Xbox 互換コントローラー',
    '隨 Windows 啟動': 'Windows 起動時に実行',
    '電量不足': 'バッテリー残量低下',
    '剩餘電量 {level}%': 'バッテリー残量 {level}%',
    '{name}: {left}。請充電。': '{name}: {left}。充電してください。',
    '{name} 已充飽電。': '{name} の充電が完了しました。',
    '圖示': 'アイコン',
    '自動': '自動',
    '滑鼠': 'マウス',
    '鍵盤': 'キーボード',
    '耳機': 'ヘッドセット',
    '控制器': 'コントローラー',
    '藍牙': 'Bluetooth',
    '未連線（已關機或休眠）': '未接続（電源オフまたはスリープ）',
    '，充電中': '、充電中',
    '（上次記錄的電量，裝置休眠中）': '（前回の残量、デバイスはスリープ中）',
    '找不到裝置': 'デバイスが見つかりません',
    '沒有顯示的裝置（已隱藏 {hidden} 個）': '表示中のデバイスなし（{hidden} 台を非表示）',
    '15 秒': '15 秒',
    '30 秒': '30 秒',
    '1 分鐘': '1 分',
    '2 分鐘': '2 分',
    '5 分鐘': '5 分',
    '白色': '白',
    '黑色': '黒',
    '關閉': 'オフ',
    '下載更新…': '更新をダウンロード…',
    '預設（{low}%）': '既定（{low}%）',
    '預設（關閉）': '既定（オフ）',
    '顯示 {name}': '{name} を表示',
    '重新命名…': '名前を変更…',
    '重設名稱': '名前をリセット',
    '低電量提醒門檻': '低残量通知のしきい値',
    '隱藏此裝置': 'このデバイスを非表示',
    '更新間隔': '取得間隔',
    '低電量提醒': '低残量通知',
    '充飽電時通知': '充電完了時に通知',
    '預估剩餘使用時間': '推定残り使用時間',
    '遊戲時保持安靜': 'ゲーム中は通知を抑制',
    'Windows 藍牙裝置': 'Windows の Bluetooth デバイス',
    'PlayStation 完整模式（藍牙）': 'PlayStation フルモード（Bluetooth）',
    '裝置類型': 'デバイスの種類',
    '裝置圖案': 'デバイスの絵柄',
    '在圖示中顯示百分比': 'アイコンに残量を表示',
    '充電動畫': '充電アニメーション',
    '圖示顏色': 'アイコンの色',
    '供其他應用程式使用的狀態檔': '他のアプリ用の状態ファイル',
    '檢查更新': '更新を確認',
    '立即更新': '今すぐ取得',
    '偏好設定': '設定',
    '隱藏的裝置': '非表示のデバイス',
    '診斷報告…': '診断レポート…',
    '結束（v{VERSION}）': '終了（v{VERSION}）',
    '已充飽電': '充電完了',
    '{APP_TITLE} 更新': '{APP_TITLE} の更新',
    '剩餘使用時間不到 1 小時': '残り使用時間は 1 時間未満',
    '語言': '言語',
    '已連線，尚未回報電量': '接続済み、バッテリー残量は未報告',
    '已接上充電線': '充電ケーブル接続中',
    '上次記錄的電量': '前回の残量',
    '充電中': '充電中',
    '極低': '残量わずか',
    '中等': '中程度',
    '已耗盡': '空',
    '滿電': '満充電',
    '充足': '十分',
    '偏低': '低下',
    '約 ': '約 ',
    '，': '、',
    'Halo Battery 正從暫存資料夾執行（直接從 ZIP 開啟）。請先將 ZIP 解壓縮至獨立資料夾，再從該資料夾執行 HaloBattery.exe，接著啟用「隨 Windows 啟動」。': 'Halo Battery は一時フォルダーから実行されています（ZIP から直接起動）。ZIP を専用フォルダーに展開し、そこから HaloBattery.exe を実行してから「Windows 起動時に実行」を有効にしてください。',
    '請輸入此裝置的新名稱：': 'このデバイスの新しい名前を入力してください：',
    'Halo Battery - 重新命名': 'Halo Battery - 名前を変更',
    '，{left}': '、{left}',
    '已有新版本 {latest}。請在電量圖示上按右鍵，選擇「下載 v{latest}…」。': '新しいバージョン {latest} が利用できます。バッテリーアイコンを右クリックして「v{latest} をダウンロード…」を選択してください。',
    '下載 v{version}…': 'v{version} をダウンロード…',
    '約可再使用 {hours} 小時': 'あと約 {hours} 時間使用できます',
    '約可再使用 {days} 天': 'あと約 {days} 日使用できます',
}
