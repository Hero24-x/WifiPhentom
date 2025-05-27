import requests

def send_alert(ssids):
    msg = f"ALERT! Rogue WiFi Detected: {ssids}"
    token = "YOUR_BOT_TOKEN"
    chat_id = "YOUR_CHAT_ID"
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    data = {"chat_id": chat_id, "text": msg}
    requests.post(url, data=data)
