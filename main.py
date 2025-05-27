# main.py
from modules.scanner import scan_networks
from modules.detector import detect_evil_twin
from modules.auto_disconnect import disconnect_suspicious
from telegram.notifier import send_alert

if __name__ == "__main__":
    print("\n[+] WiFiPhantom Starting...\n")
    networks = scan_networks()
    rogue = detect_evil_twin(networks)
    if rogue:
        send_alert(rogue)
        disconnect_suspicious(rogue)
      
