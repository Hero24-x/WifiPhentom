import json

def detect_evil_twin(current_ssids):
    with open('config/safe_ssids.json') as f:
        safe = json.load(f)["trusted_ssids"]
    suspicious = [ssid for ssid in current_ssids if ssid in safe and current_ssids.count(ssid) > 1]
    return suspicious
