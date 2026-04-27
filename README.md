# musicBOT_YesMan 🎵

一個 Discord bot，用於保持語音頻道有人狀態，並自動回應 Jockie Music 的喚醒訊息。

## 功能
- 🔊 自動加入並長駐語音頻道
- 💬 偵測到 `hey wake up` 相關訊息時自動回覆 `yes`
- 🔄 被踢出語音頻道後自動重新加入

## 部署環境
- 平台：Railway.app
- 語言：Python 3.12
- 套件：discord.py[voice]、PyNaCl

## 環境變數設定
| 變數名稱 | 說明 |
|----------|------|
| `TOKEN` | Discord Bot Token |
| `VOICE_CHANNEL_ID` | 目標語音頻道 ID |

## 檔案結構
musicBOT_YesMan/
├── bot.py            # 主程式
├── requirements.txt  # Python 套件
├── railway.toml      # Railway 部署設定
└── README.md         # 說明文件

## 本地執行
```bash
pip install -r requirements.txt
export TOKEN=你的token
export VOICE_CHANNEL_ID=你的頻道ID
python bot.py
```