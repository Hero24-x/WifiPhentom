# main.py
from modules.scanner import scan_networks
from modules.detector import detect_evil_twin
from modules.auto_disconnect import disconnect_suspicious
from telegram.notifier import send_alert
