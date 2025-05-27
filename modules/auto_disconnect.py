import os

def disconnect_suspicious(ssids):
    print(f"Disconnecting from: {ssids}")
    os.system("nmcli radio wifi off")
