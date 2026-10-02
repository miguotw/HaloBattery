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

**「是」**表示已實際讀到該裝置的電量，驗證來源可能是本專案測試、診斷報告或使用者回報。**「否」**表示依其他工具的程式碼實作，但尚未於實機驗證。**「預期可用」**表示同系列其他型號共用程式邏輯，預期可正常使用，但尚未逐一測試。表格中的連結指向各裝置的[電量讀取協定說明](docs/protocols.md)（英文）。

| 裝置 | 連線方式 | 已於實機驗證 |
|---|---|---|
| [8BitDo Pro 2, Pro 3, SN30 Pro, SF30 Pro （D-input 模式）](docs/protocols.md#8bitdo-pro-2-pro-3-sn30-pro-sf30-pro-in-d-input-mode) | 藍牙或 USB | 否 |
| [AM Infinity 8K (Angry Miao)](docs/protocols.md#am-infinity-8k-angry-miao) | 2.4 GHz 接收器 | 否 |
| [Astro A50 Gen 5 (Logitech 046D:0B1C)](docs/protocols.md#astro-a50-gen-5-logitech-046d0b1c) | 基地台 | 否 |
| ASUS TX Gaming Mouse Mini Miku (`0B05:1C5A`) | 2.4 GHz 接收器 | 是 |
| [ASUS ROG Gladius III Aimpoint 及其他 ROG / TUF 無線滑鼠（清單見 `providers/asus.py`）](docs/protocols.md#asus-rog-gladius-iii-aimpoint-and-other-rog--tuf-wireless-mice) | 2.4 GHz 接收器或 USB 傳輸線 | 否 |
| [Audeze Maxwell](docs/protocols.md#audeze-maxwell) | 2.4 GHz 接收器或 USB-C 傳輸線 | 是 |
| [藍牙裝置，已測試 1MORE SonoFlow 耳機（另有使用者回報 Audio-Technica 與 JBL Tune 760NC 耳機可用）](docs/protocols.md#bluetooth-devices-tested-on-the-1more-sonoflow-headset) | 藍牙（預設啟用，可在選單關閉） | 是 |
| [Corsair Dark Core RGB Pro SE](docs/protocols.md#corsair-dark-core-rgb-pro-se) | 2.4 GHz 接收器 | 否 |
| [Corsair Void v2 Wireless, Virtuoso Max Wireless, HS80 Max Wireless](docs/protocols.md#corsair-void-v2-wireless-virtuoso-max-wireless-hs80-max-wireless) | 無線接收器 | 否 |
| [GameSir G7 Pro; FlyDigi Vader Pro （使用者已測試）](docs/protocols.md#gamesir-g7-pro-flydigi-vader-pro) | 2.4 GHz 接收器（識別為 Xbox 控制器） | 是 |
| [G-Wolves WARG, HTS Plus (Pro), HTXU, Lycan, Fenrir Pro / Asym, HTX Mini](docs/protocols.md#g-wolves-warg-hts-plus-pro-htxu-lycan-fenrir-pro--asym-htx-mini) | 8K 接收器或 USB 傳輸線 | 否 |
| [Hitscan Hyperlight](docs/protocols.md#hitscan-hyperlight) | 2.4 GHz 接收器或 USB 傳輸線 | 否 |
| [HyperX Cloud Alpha 2](docs/protocols.md#hyperx-cloud-alpha-2) | 2.4 GHz 基地台 | 是 |
| [HyperX Cloud II Wireless](docs/protocols.md#hyperx-cloud-ii-wireless) | 2.4 GHz 接收器 | 否 |
| [HyperX Cloud III Wireless](docs/protocols.md#hyperx-cloud-iii-wireless) | 2.4 GHz 接收器 | 否 |
| [JBL Quantum 910 Wireless](docs/protocols.md#jbl-quantum-910-wireless) | 2.4 GHz 接收器 | 是 |
| [Keychron Ultra-Link 8K, Keychron M5](docs/protocols.md#keychron-ultra-link-8k-keychron-m5) | 2.4 GHz 接收器與 USB 傳輸線 | 否 |
| [LAMZU Maya X](docs/protocols.md#lamzu-maya-x) | 8K 接收器或 USB 傳輸線 | 是 |
| [Lofree Hyzen](docs/protocols.md#lofree-hyzen) | 2.4 GHz 接收器 | 否 |
| [Logitech G502 LIGHTSPEED, G502 X PLUS](docs/protocols.md#logitech-g502-lightspeed-g502-x-plus) | Lightspeed 接收器 | 是 |
| [Logitech （其他 HID++ 2.0 裝置與 G 系列耳機）](docs/protocols.md#logitech-more-hid-20-devices-and-g-series-headsets) | Lightspeed、Unifying 或 Bolt 接收器 | 預期可用 |
| [MCHOSE A7 V2 Ultra](docs/protocols.md#mchose-a7-v2-ultra) | 2.4 GHz 接收器 | 否 |
| [MCHOSE G7](docs/protocols.md#mchose-g7) | USB（晶片為「YJX-CHIP」） | 是 |
| [MCHOSE M7 Ultra](docs/protocols.md#mchose-m7-ultra) | 2.4 GHz 接收器 | 是 |
| [Nintendo Switch Pro Controller, Joy-Con (L) / (R)](docs/protocols.md#nintendo-switch-pro-controller-joy-con-l--r) | 藍牙 | 否 |
| [Pulsar X2 V2 Mini, ATK VXE R1 SE+, VXE R1 Pro Max](docs/protocols.md#pulsar-x2-v2-mini-atk-vxe-r1-se-vxe-r1-pro-max) | 2.4 GHz 接收器與 USB 傳輸線 | 是 |
| [Razer Barracuda Pro (2.4 GHz)](docs/protocols.md#razer-barracuda-pro-24-ghz) | 2.4 GHz 接收器 | 是 |
| [Razer Basilisk V3 Pro, Razer Basilisk Ultimate （使用者已測試）](docs/protocols.md#razer-basilisk-v3-pro-razer-basilisk-ultimate) | 2.4 GHz 接收器 | 是 |
| [Razer BlackShark V2 Pro (2023)](docs/protocols.md#razer-blackshark-v2-pro-2023) | 2.4 GHz 接收器 | 是 |
| [Razer BlackWidow V3 Pro](docs/protocols.md#razer-blackwidow-v3-pro) | 2.4 GHz 接收器或 USB 傳輸線 | 否 |
| [Razer DeathAdder V4 Pro](docs/protocols.md#razer-deathadder-v4-pro) | 2.4 GHz 接收器 | 是 |
| [Razer 無線滑鼠 （其他 OpenRazer 型號）](docs/protocols.md#razer-wireless-mice-other-openrazer-models) | 2.4 GHz 接收器或 USB 傳輸線 | 預期可用 |
| [Sony DualSense (PS5)](docs/protocols.md#sony-dualsense-ps5) | USB 或藍牙 | 是 |
| [Sony DualShock 4 (PS4)](docs/protocols.md#sony-dualshock-4-ps4) | USB 傳輸線與藍牙 | 是 |
| [SteelSeries Aerox 3 Wireless](docs/protocols.md#steelseries-aerox-3-wireless) | 2.4 GHz 接收器 | 否 |
| [SteelSeries Arctis and GameBuds （其他型號）](docs/protocols.md#steelseries-arctis-and-gamebuds-other-models) | 無線基地台或接收器 | 預期可用 |
| [SteelSeries Arctis Nova 7](docs/protocols.md#steelseries-arctis-nova-7) | 2.4 GHz 接收器 | 是 |
| [SteelSeries Arctis Nova Pro Wireless (`1038:12E0`, `1038:12E5` X)](docs/protocols.md#steelseries-arctis-nova-pro-wireless-103812e0-103812e5-x) | 無線基地台，介面 3 或 4 | 否 |
| [SteelSeries Rival 3 Wireless](docs/protocols.md#steelseries-rival-3-wireless) | 2.4 GHz 接收器 | 否 |
| [WLmouse Beast X and Beast X Mini Pro](docs/protocols.md#wlmouse-beast-x-and-beast-x-mini-pro) | 8K 或 1K 接收器，或 USB 傳輸線 | 預期可用 |
| [WLmouse Beast X Max](docs/protocols.md#wlmouse-beast-x-max) | 8K 接收器與 USB 傳輸線 | 是 |
| [Xbox 相容控制器 （其他型號）](docs/protocols.md#xbox-compatible-controllers-other-models) | USB 或 Xbox 無線接收器 | 預期可用 |

**透過藍牙連接的 PlayStation 控制器：** DualShock 4 與 DualSense 只有在「完整回報」模式下，才會透過藍牙提供電量。切換至此模式會使使用 DirectInput 的遊戲無法辨識控制器，直到控制器關閉後重新開啟（#96）。因此程式預設不會切換模式：當 Steam 或遊戲已將控制器切換至此模式時會顯示電量，否則只顯示控制器圖示。如果你不使用受影響的遊戲，可啟用「偏好設定 → PlayStation 完整模式（藍牙）」以持續讀取電量。透過 USB 連接時可正常顯示電量。

**D-input 模式下的 8BitDo 控制器：** 電量只包含在控制器的增強回報中。切換至此模式會讓 DirectInput 遊戲無法辨識控制器，直到關閉後重新開啟（#101 的回報者已驗證）。程式不會主動切換：只有在 Steam 或遊戲已切換模式時顯示電量，否則只顯示圖示。XInput 模式下可正常顯示電量。

標示為「預期可用」的裝置包含 OpenRazer 支援的其他 Razer 型號、其他 WLmouse 型號、更多 Logitech HID++ 2.0 裝置與 G 系列耳機、其他 Arctis Nova 與較舊的 Arctis 型號，以及其他 Xbox 相容控制器；它們使用同一套讀取邏輯。

不保證其他裝置都能使用。新裝置支援會依使用者回饋與診斷紀錄加入；如果裝置未被偵測或電量不正確，請建立 Issue 並附上診斷報告，詳見下方「疑難排解」。

## 安裝

### 方式一：下載已建置的 EXE（建議）

1. 從本分支的 [Releases](https://github.com/miguotw/HaloBattery/releases/latest) 下載 `HaloBattery-<版本>.zip`。
2. 解壓縮至固定資料夾，例如 `C:Tools`，讓執行檔位於 `C:ToolsHaloBatteryHaloBattery.exe`，再執行 `HaloBattery.exe`。請保留完整的 `HaloBattery` 資料夾：EXE 必須與 `_internal` 資料夾放在一起。
3. 在系統匣圖示上按右鍵，選擇「偏好設定 → 隨 Windows 啟動」。

首次啟動時會依 Windows 使用者的介面語言自動選擇；不支援的語言或讀取失敗時使用 English。你可以在「偏好設定 → 語言」選擇 **English**、**繁體中文** 或 **日本語**，切換後立即生效，並記住選擇供下次啟動使用。

程式每天檢查一次新版，有更新時選單會出現「下載 vX.Y.Z.N…」。更新前先在系統匣選單選擇「結束」，再替換完整資料夾；「隨 Windows 啟動」會在新版執行後指向新的位置。如果先前使用的是單一檔案版 `HaloBattery.exe`，請移除舊檔。

由於程式未經程式碼簽署，首次執行時 Windows SmartScreen 可能顯示無法辨識應用程式的提示，可選擇「其他資訊 → 仍要執行」。部分防毒軟體也可能誤判未簽署的 Python 應用程式，通常顯示通用的 `!ml` 偵測名稱。Release 由 GitHub Actions 直接從此儲存庫建置，建置紀錄公開；你也可以使用下方的原始碼執行方式。

### 方式二：從原始碼執行

1. 安裝 [Python 3.10 以上版本](https://www.python.org/downloads/)，並勾選 **Add python.exe to PATH**。
2. 將本儲存庫下載或複製至固定資料夾，例如 `C:ToolsHaloBattery`。
3. 執行 `install_and_run.bat`，再於系統匣圖示按右鍵，選擇「偏好設定 → 隨 Windows 啟動」。

執行 `build_exe.bat` 可自行建置，輸出位於 `distHaloBattery`。發布流程由 `.github/workflows/release.yml` 管理：推送如 `v1.13.0.1` 的 tag 後，GitHub Actions 會建置程式並將 ZIP 附加至 Release。tag 必須符合 `version.py` 產生的版本，且 `CHANGELOG.md` 必須有對應的版本說明。

## 圖示說明

- **中央圖案**：耳機、滑鼠、鍵盤（帶有 K 字母的按鍵）、Xbox 或 PlayStation 控制器、iPhone 外觀的手機，或藍牙標誌；可在選單中關閉裝置圖案。
- **顏色**：跟隨工作列主題，深色工作列顯示白色，淺色工作列顯示黑色。執行 [MyDockFinder](https://store.steampowered.com/app/1787090/MyDockFinder/) 時，會跟隨其頂端選單列。使用透明工作列（例如 TranslucentTB）時，可在「偏好設定 → 圖示顏色」手動選擇「白色」或「黑色」。
- **琥珀色**：接近低電量提醒門檻。**紅色**：電量低於或等於門檻。
- **綠色呼吸效果**：正在充電。關閉充電動畫後會保留一般綠色圓弧。
- **半透明**：滑鼠進入休眠，程式最多保留上次電量 5 分鐘。關閉裝置後，其圖示會離開系統匣，再次開啟時重新出現。

低電量通知只會觸發一次，待裝置充電後才會再次觸發。

## 系統匣選單

在裝置圖示按右鍵即可開啟選單。選單採用 Windows 11 風格（壓克力背景、圓角及深／淺色主題），並支援顯示縮放。如果在你的電腦上無法正常使用，可在 `%APPDATA%HaloBatteryconfig.json` 設定 `"fluent_menu": false`，改回傳統 Windows 選單。

### 裝置操作

- **重新命名…**：為裝置取自己的名稱，例如區分兩支同名控制器。「重設名稱」可還原裝置原始名稱。新版選單可點選名稱右側的鉛筆圖示，傳統選單則顯示「重新命名…」。
- **圖示**：為此裝置選擇「自動、滑鼠、鍵盤、耳機、控制器、手機、藍牙」。例如透過藍牙連接而顯示藍牙圖案的控制器，可自行改為控制器圖案。手機圖示採用 iPhone 外觀。
- **低電量提醒門檻**：僅設定此裝置的提醒門檻，可選擇「關閉」或 10–30%；選擇「預設」則依偏好設定的門檻。電量環變紅的門檻也會跟隨此設定。
- **隱藏此裝置**：移除裝置圖示，例如隱藏始終回報 100% 的控制器。
- **立即更新**：立即重新讀取電量。

### 偏好設定

- **語言**：選擇 English、繁體中文或日本語。選單、電量提示及通知會立即切換，並儲存選擇。未設定時依 Windows 介面語言選擇，不支援時使用 English；手動選擇會優先保留。
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

## 致謝

- WLmouse 協定：@len0c（[incconutwo/mouse-battery-tray](https://github.com/incconutwo/mouse-battery-tray)，MIT）。
- MCHOSE 協定：@alexfrih 的說明（[alexfrih/mchose-linux](https://github.com/alexfrih/mchose-linux)，從 MCHOSE 自家的網頁驅動程式還原）；G7 的支援來自 @kek353 的監測工具，以及 [#8](https://github.com/HeyOkay/HaloBattery/issues/8) 的資料擷取。
- Hitscan Hyperlight 協定：@sopparus（[sopparus/hitscan-battery](https://github.com/sopparus/hitscan-battery)），透過廠商應用程式的 USB 通訊分析，並於 [libratbag 討論](https://github.com/libratbag/libratbag/issues/1893) 確認。
- AM Infinity 8K 協定：AJAZZ Control Center 專案（[Aiacos/ajazz-control-center](https://github.com/Aiacos/ajazz-control-center)，GPL-3.0），其 AJ159 APEX 裝置使用相同 USB 識別碼。
- BlackShark V2 Pro 2023：OpenRazer 驅動程式（[PR #2862](https://github.com/openrazer/openrazer/pull/2862)）。Razer PID 與交易識別碼參考 OpenRazer 與 [RazerBatteryTaskbar](https://github.com/Tekk-Know/RazerBatteryTaskbar)。
- 各裝置參考的實作，包括 HeadsetControl、rivalcfg、Solaar、G-Helper、HyperHeadset、mouse.xyz、[`@openmouse/protocol`](https://github.com/OpenMouse-Project/openmouse)、keychron-battery-dkms、JBL_Baterry_Monitor 等，均在 [docs/protocols.md](docs/protocols.md) 中對應裝置的段落註明。

## 授權

採用 MIT 授權，詳見 [LICENSE](LICENSE)。
