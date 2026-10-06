# Halo Battery

**繁體中文** | [English](README.en.md)

這是 miguotw 維護的分支版本。發布版本採用「上游主版本.次版本.修訂版本.分支修訂號」，例如 `1.13.0.1`；上游基礎版本與分支修訂號分別在 `version.py` 維護。程式會從本分支的 Releases 檢查更新。

在 Windows 系統匣顯示無線滑鼠、鍵盤、耳機與控制器的電量，每個裝置有自己的圖示，無須安裝廠商軟體。

![各種圖示狀態](docs/icons.png)

充電時，電量圓弧會緩慢呈現呼吸效果：

![充電動畫](docs/charging.gif)

每個裝置都有獨立的系統匣圖示：中央是裝置圖案，外側是電量環。圓弧從頂端順時針填滿；接近低電量提醒門檻時變成琥珀色，低於或等於門檻時變成紅色，充電時則以綠色呈現呼吸效果。將游標移到圖示上可查看電量百分比，按右鍵可重新命名、隱藏裝置、調整偏好設定或產生診斷報告。

程式透過 USB/HID（無線接收器或傳輸線）、Xbox 類型控制器的回報，以及 Windows 提供的藍牙裝置資訊讀取電量。

## 支援的裝置

完整清單、連線方式與實機驗證狀態見[支援裝置清單（英文）](docs/devices.md)，協定來源見[技術說明（英文）](docs/protocols.md)。本分支另提供 ASUS TX Gaming Mouse Mini Miku (`0B05:1C5A`) 的 2.4 GHz 接收器支援。

## 安裝

### 方式一：下載已建置的 EXE（建議）

1. 從本分支的 [Releases](https://github.com/miguotw/HaloBattery/releases/latest) 下載 `HaloBattery-<版本>.zip`。
2. 解壓縮至固定資料夾，例如 `C:\Tools`，讓執行檔位於 `C:\Tools\HaloBattery\HaloBattery.exe`，再執行 `HaloBattery.exe`。請保留完整的 `HaloBattery` 資料夾：EXE 必須與 `_internal` 資料夾放在一起。
3. 在系統匣圖示上按右鍵，選擇「偏好設定 → 隨 Windows 啟動」。

首次啟動時會依 Windows 使用者的介面語言自動選擇；不支援的語言或讀取失敗時使用 English。你可以在「偏好設定 → 語言」選擇 **English**、**繁體中文**、**简体中文**、**日本語** 或 **Français**，切換後立即生效，並記住選擇供下次啟動使用。

程式每天檢查一次新版，有更新時選單會出現「下載 vX.Y.Z.N…」。更新前先在系統匣選單選擇「結束」，再替換完整資料夾；「隨 Windows 啟動」會在新版執行後指向新的位置。如果先前使用的是單一檔案版 `HaloBattery.exe`，請移除舊檔。

由於程式未經程式碼簽署，首次執行時 Windows SmartScreen 可能顯示無法辨識應用程式的提示，可選擇「其他資訊 → 仍要執行」。部分防毒軟體也可能誤判未簽署的 Python 應用程式，通常顯示通用的 `!ml` 偵測名稱。Release 由 GitHub Actions 直接從此儲存庫建置，建置紀錄公開；你也可以使用下方的原始碼執行方式。

### 方式二：從原始碼執行

1. 安裝 [Python 3.10 以上版本](https://www.python.org/downloads/)，並勾選 **Add python.exe to PATH**。
2. 將本儲存庫下載或複製至固定資料夾，例如 `C:\Tools\HaloBattery`。
3. 執行 `install_and_run.bat`，再於系統匣圖示按右鍵，選擇「偏好設定 → 隨 Windows 啟動」。

執行 `build_exe.bat` 可自行建置，輸出位於 `dist\HaloBattery`。發布流程由 `.github/workflows/release.yml` 管理：推送如 `v1.13.0.1` 的 tag 後，GitHub Actions 會建置程式並將 ZIP 附加至 Release。tag 必須符合 `version.py` 產生的版本，且 `CHANGELOG.md` 必須有對應的版本說明。

### 可攜模式

在 `HaloBattery.exe`（原始碼版為 `halo_battery.pyw`）旁建立空白 `portable.txt` 後重新啟動，即可將設定、紀錄、電量歷史、狀態檔及診斷報告放在程式資料夾。資料夾必須可寫入；否則退回 `%APPDATA%\HaloBattery` 並記錄原因。設定不會自動搬移，可自行複製原有 `config.json`。「隨 Windows 啟動」仍會使用目前使用者的登錄設定。

## 圖示說明

- **中央圖案**：耳機、滑鼠、鍵盤（帶有 K 字母的按鍵）、Xbox 或 PlayStation 控制器、iPhone 外觀的手機，或藍牙標誌；可在選單中關閉裝置圖案。
- **顏色**：跟隨工作列主題，深色工作列顯示白色，淺色工作列顯示黑色。執行 [MyDockFinder](https://store.steampowered.com/app/1787090/MyDockFinder/) 時，會跟隨其頂端選單列。使用透明工作列（例如 TranslucentTB）時，可在「偏好設定 → 圖示顏色」手動選擇「白色」或「黑色」。
- **琥珀色**：接近低電量提醒門檻。**紅色**：電量低於或等於門檻。
- **綠色呼吸效果**：正在充電。關閉充電動畫後會保留一般綠色圓弧。
- **半透明**：滑鼠進入休眠，程式最多保留上次電量 5 分鐘。關閉裝置後，其圖示會離開系統匣，再次開啟時重新出現。

低電量通知只會觸發一次，待裝置充電後才會再次觸發。

## 系統匣選單

在裝置圖示按右鍵即可開啟選單。選單採用 Windows 11 風格（壓克力背景、圓角及深／淺色主題），並支援顯示縮放。如果在你的電腦上無法正常使用，可在 `%APPDATA%\HaloBattery\config.json` 設定 `"fluent_menu": false`，改回傳統 Windows 選單。

### 裝置操作

- **重新命名…**：為裝置取自己的名稱，例如區分兩支同名控制器。「重設名稱」可還原裝置原始名稱。新版選單可點選名稱右側的鉛筆圖示，傳統選單則顯示「重新命名…」。
- **圖示**：為此裝置選擇「自動、滑鼠、鍵盤、耳機、控制器、手機、藍牙」。例如透過藍牙連接而顯示藍牙圖案的控制器，可自行改為控制器圖案。手機圖示採用 iPhone 外觀。
- **低電量提醒門檻**：僅設定此裝置的提醒門檻，可選擇「關閉」或 10–30%；選擇「預設」則依偏好設定的門檻。電量環變紅的門檻也會跟隨此設定。
- **隱藏此裝置**：移除裝置圖示，例如隱藏始終回報 100% 的控制器。
- **立即更新**：立即重新讀取電量。

### 偏好設定

- **低電量提醒時播放音效**：預設關閉；裝置清醒、低電量且未充電時播放 Windows 音效，每 5 分鐘重播。

- **語言**：選擇 English、繁體中文、简体中文、日本語或 Français。選單、電量提示及通知會立即切換，並儲存選擇。未設定時依 Windows 介面語言選擇，不支援時使用 English；手動選擇會優先保留。
- **更新間隔**與**低電量提醒**：更新間隔可設為 15 秒至 5 分鐘；低電量提醒可關閉或設為 10–30%。可用 −／＋ 按鈕或滑鼠滾輪調整，選單會保持開啟。
- **充飽電時通知**：每次充電完成後通知一次。預設啟用。
- **預估剩餘使用時間**：在提示中顯示「約可再使用 5 小時」等資訊，依上次充電後的耗電速度估算。只計入裝置清醒且使用電池的時間；累積使用 30 分鐘、電量下降至少 3% 後才提供估算。紀錄儲存在 `%APPDATA%HaloBatteryhistory.json`。
- **遊戲時保持安靜**：預設啟用。遊戲或其他應用程式全螢幕時，通知會暫存，結束全螢幕後再顯示，每個裝置保留各類通知的最新一則。如果裝置期間已接上充電器，會取消過時的低電量通知。此時每 5 分鐘才查詢一次裝置，以減少通訊；插入裝置仍會立即更新。
- **Windows 藍牙裝置**：啟用或停用 Windows 提供的藍牙電量讀取。
- **裝置圖案**：顯示或隱藏電量環中央的圖案。
- **在圖示中顯示百分比**：以數字取代中央圖案，低電量時數字也會變為琥珀色或紅色。
- **充電動畫**：開啟或關閉綠色呼吸效果。
- **PlayStation 完整模式（藍牙）**：預設關閉。啟用後可持續讀取 PS4／PS5 控制器的藍牙電量，但部分遊戲可能無法辨識控制器，直到控制器關閉後重新開啟。
- **供其他應用程式使用的狀態檔**：預設關閉。每次查詢後寫入 `%APPDATA%HaloBatterystatus.json`，可供 Rainmeter、Stream Deck 外掛或腳本使用。每個裝置包含 `name`、`level`、`charging`、`online`、`kind`、`seconds_left` 與提示文字 `text`；程式結束時 `running` 變為 false，`updated_unix` 表示資料更新時間。關閉此功能會刪除狀態檔。
- **裝置類型**：停用特定品牌或裝置系列；停用後程式不會開啟或查詢其裝置。
- **圖示顏色**：可選「自動」（Windows 主題，或執行中的 MyDockFinder 選單列主題）、「白色」或「黑色」。
- **隨 Windows 啟動**：透過目前使用者的登錄機碼設定，不需要系統管理員權限。
- **檢查更新**：預設啟用，每天檢查本分支的 Releases 一次。有新版時會通知，並顯示「下載 vX.Y.Z.N…」。

### 其他操作

- **隱藏的裝置**：只有隱藏過裝置時才出現，點選裝置可讓它重新顯示。
- **診斷報告…**：產生詳細報告並開啟。
- **結束**：關閉程式。

## 疑難排解

1. 關閉 Synapse、WLmouse 網頁驅動程式與其他電量工具，它們可能占用接收器。
2. 移動滑鼠，讓它離開休眠狀態。
3. 執行 `probe.bat`，或在系統匣選單選擇「診斷報告…」。報告會列出所有 HID 裝置與原始協定回覆。請附在本儲存庫的 Issue 中，以協助加入新裝置支援。報告包含藍牙 MAC 位址與裝置序號，發布前可先遮蔽這些資訊。[CONTRIBUTING.md](CONTRIBUTING.md)（英文）說明需要附上哪些資料、如何擷取尚未支援裝置的 USB 通訊，以及如何提交 Pull Request。
4. 若出現 **「python312.dll was not found」**，或「隨 Windows 啟動」提示程式正從暫存資料夾執行，通常是直接從 ZIP 啟動，或只複製了 `HaloBattery.exe`。請將整個 ZIP 解壓縮至獨立資料夾，保留 EXE 旁的 `_internal` 資料夾，再從該位置啟動程式。

設定、執行紀錄與診斷報告位於 `%APPDATA%HaloBattery`。

## 同步上游

每天約台灣時間 09:17 檢查上游，建立或更新同步 PR，執行完整測試與 Windows 建置；合併由人工確認，版本發布另行處理。[維護說明](docs/upstream-sync.md)。

## 致謝

- WLmouse 協定：@len0c（[incconutwo/mouse-battery-tray](https://github.com/incconutwo/mouse-battery-tray)，MIT）。
- MCHOSE 協定：@alexfrih 的說明（[alexfrih/mchose-linux](https://github.com/alexfrih/mchose-linux)，從 MCHOSE 自家的網頁驅動程式還原）；G7 的支援來自 @kek353 的監測工具，以及 [#8](https://github.com/HeyOkay/HaloBattery/issues/8) 的資料擷取。
- Hitscan Hyperlight 協定：@sopparus（[sopparus/hitscan-battery](https://github.com/sopparus/hitscan-battery)），透過廠商應用程式的 USB 通訊分析，並於 [libratbag 討論](https://github.com/libratbag/libratbag/issues/1893) 確認。
- AM Infinity 8K 協定：AJAZZ Control Center 專案（[Aiacos/ajazz-control-center](https://github.com/Aiacos/ajazz-control-center)，GPL-3.0），其 AJ159 APEX 裝置使用相同 USB 識別碼。
- BlackShark V2 Pro 2023：OpenRazer 驅動程式（[PR #2862](https://github.com/openrazer/openrazer/pull/2862)）。Razer PID 與交易識別碼參考 OpenRazer 與 [RazerBatteryTaskbar](https://github.com/Tekk-Know/RazerBatteryTaskbar)。
- 各裝置參考的實作，包括 HeadsetControl、rivalcfg、Solaar、G-Helper、HyperHeadset、mouse.xyz、[`@openmouse/protocol`](https://github.com/OpenMouse-Project/openmouse)、keychron-battery-dkms、JBL_Baterry_Monitor 等，均在 [docs/protocols.md](docs/protocols.md) 中對應裝置的段落註明。

## 授權

採用 MIT 授權，詳見 [LICENSE](LICENSE)。
