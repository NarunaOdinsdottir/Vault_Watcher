import time
from Vault_monitor import get_report
from SecuritronMK2 import send_alert

CHECK_INTERVAL = 300  # alle 5 Minuten

if __name__ == "__main__":
    print("🚀 Vault-Securitron gestartet...")
    while True:
        report = get_report()
        if report["warnings"]:  # nur bei Warnungen
            send_alert(report)
        time.sleep(CHECK_INTERVAL)
