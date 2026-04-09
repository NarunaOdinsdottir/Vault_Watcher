from report_adapter import get_current_report
from telegram import Bot
from telegram_alert import send_alert
import time

CHECK_INTERVAL = 300  # alle 5 Minuten

while True:
    report = get_current_report()
    if report and report["warnings"]:
        send_alert(report)
    time.sleep(CHECK_INTERVAL)
# Telegram Config
TELEGRAM_TOKEN = "Hier BOT-TOKEN Eintragen"
CHAT_ID = "Hier ID Eintragen"

bot = Bot(token=TELEGRAM_TOKEN)

def send_alert(report):
    msg = f"📊 Vault-OS Alert [{report['timestamp']}]\n"
    msg += f"CPU: {report['cpu']:.1f}% | RAM: {report['ram']:.1f}% | DISK: {report['disk']:.1f}%\n"

    if report["warnings"]:
        msg += "\n🚨 WARNUNGEN:\n"
        for w in report["warnings"]:
            msg += f"{w}\n"
    else:
        msg += "\n✅ Alles stabil.\n"

    if report["suspicious"]:
        msg += "\n⚠️ Verdächtige Prozesse:\n"
        msg += "\n".join(report["suspicious"]) + "\n"

    msg += f"\n👤 Letzter Login:\n{report['last_login']}\n"

    bot.send_message(chat_id=CHAT_ID, text=msg)
