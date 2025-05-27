# ⚡ WiFiPhantom — Evil Twin Detector & Defender

> 🎯 Protect your device from fake WiFi traps with zero-root Python power  
> 🛡️ Built with passion by [HansdaTechs](https://github.com/HansdaTechs) | Shibnath Hansda

---

## 🧠 What is WiFiPhantom?

**WiFiPhantom** is a powerful tool that helps ethical hackers and security researchers detect **Evil Twin WiFi attacks** — fake access points that mimic legit ones to steal data.  
It scans nearby SSIDs, detects duplicates, compares MACs, and **auto-disconnects** from suspicious APs. Ideal for **Termux** or **Linux** use — no root required.

---

## 🔥 Key Features

- 🔎 Real-time SSID scanner
- 🚨 Evil Twin Detection based on:
  - SSID Duplication
  - MAC Spoof Check
  - Signal fluctuation anomaly
- 🛡️ Auto-Disconnect from rogue networks
- 📟 Safe SSID Whitelist (`config/safe_ssids.json`)
- 🤖 Telegram Alert Bot Integration
- 🧾 Real-time logging (`logs/wifi_logs.txt`)

---

## 📁 Folder Structure

WiFiPhantom/
├── README.md
├── LICENSE
├── requirements.txt
├── main.py
├── config/
│ └── safe_ssids.json
├── modules/
│ ├── scanner.py
│ ├── detector.py
│ └── auto_disconnect.py
├── logs/
│ └── wifi_logs.txt
├── assets/
│ └── banner.txt
└── telegram/
└── notifier.py
---

---

## 🧪 Installation (Termux/Linux)

```bash
# Step 1: Clone the repo
git clone https://github.com/HansdaTechs/WiFiPhantom.git
cd WiFiPhantom

# Step 2: Install requirements
pip install -r requirements.txt

# Step 3: Run the tool
python main.py
---

🛠 Configuration
Safe SSIDs List:
Edit config/safe_ssids.json to add your trusted WiFi names.
---
#json
{
  "trusted_ssids": ["Home_WiFi", "CollegeNet", "HansdaHQ"]
}
---
📲 Telegram Alerts (Optional)
Want to get a ping if an Evil Twin is nearby?
Set up your Telegram Bot Token and Chat ID in telegram/notifier.py.
---

🔐 Ethical Usage
This tool is meant for educational and ethical hacking purposes only.
Do not use on networks without permission. Stay clean. Stay legendary.

✍️ Author
🧠 Made with 💻 by HansdaTechs
🧑‍💻 Founder: Shibnath Hansda
🌐 GitHub | 🛡️ Cybersecurity Company in the Making

📜 License
MIT License – Free to use, modify, and learn.

💬 Support & Community
Got questions or want to contribute?
Telegram Group: t.me/HansdaTechsCommunity

GitHub Discussions: Coming soon...
🚀 Future Upgrades (V2 Roadmap)
 •GUI Version with Tkinter/WebView
 •Auto MAC detection of rogue APs
 •Machine Learning-based signal analysis
 •Mobile version (Kivy)











