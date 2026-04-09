# 🟢 VAULT-OS – Systemüberwachung im Fallout-Style

> *„Willkommen im Vault. Deine Sicherheit ist unsere Priorität.“*
> – Vault-Tec Corporation

---

## 🧠 Projektübersicht

**VAULT-OS** ist ein modulares Systemüberwachungs-Tool im Fallout-Stil, entwickelt mit Python.
Es überwacht Systemressourcen, erkennt potenzielle Sicherheitsprobleme und informiert dich direkt über Telegram – dein persönlicher **Securitron**. 🤖

---

## ⚙️ Features

🟢 **Live-Systemüberwachung**

* CPU-Auslastung
* RAM-Nutzung
* Festplattenstatus

🛡️ **Security-Checks**

* Letzte Logins
* Fehlgeschlagene Loginversuche
* Verdächtige Prozesse

📡 **Telegram Alerts (SecuritronMK2)**

* Benachrichtigung bei kritischen Systemwerten
* Warnungen direkt aufs Handy

📊 **Vault Dashboard**

* Terminalbasierte Übersicht im Fallout-Design
* Echtzeit-Systemstatus

🧩 **Modulare Architektur**

* Erweiterbar (z. B. GUI, weitere Bots, Cloud-Anbindung)

---

## 🗂️ Projektstruktur

```
Vault_Watcher/
│
├─ Vault_monitor.py      # Systemüberwachung (CPU, RAM, Disk, Security)
├─ Vault_Dashboard.py    # Anzeige im Terminal (Fallout UI)
├─ SecuritronMK2.py      # Telegram-Bot für Alerts
├─ Adapter.py            # Zentrale Datenquelle (optional)
└─ main.py               # Steuerung & Intervall-Logik
```

---

## 🚀 Installation

### 1. Repository klonen

```
git clone https://github.com/NarunaOdinsdottirVault-OS.git
cd Vault-OS
```

### 2. Abhängigkeiten installieren

```
pip install psutil python-telegram-bot
```

---

## 🤖 Telegram Bot einrichten

1. Öffne Telegram und suche nach **@BotFather**
2. Erstelle einen neuen Bot → `/newbot`
3. Kopiere deinen **Bot Token**
4. Hole dir deine **Chat ID** (z. B. über @userinfobot)

Dann in `SecuritronMK2.py` eintragen:

```python
TELEGRAM_TOKEN = "DEIN_TOKEN"
CHAT_ID = "DEINE_CHAT_ID"
```

---

## ▶️ Nutzung

### Dashboard starten

```
python Vault_Dashboard.py
```

### Securitron (Bot) starten

```
python main.py
```

---

## ⚠️ Schwellenwerte anpassen

In `Vault_monitor.py`:

```python
CPU_LIMIT = 80
RAM_LIMIT = 80
DISK_LIMIT = 90
```

---

## 🧪 Roadmap (Vault Expansion geplant)

* [ ] GUI im Pip-Boy Stil
* [ ] Log-Historie & Analyse
* [ ] Mehr Security Checks (Ports, Netzwerk)
* [ ] Remote Monitoring (mehrere Systeme)
* [ ] Integration in dein „Kevin“-System 🤖

---

## ☢️ Lore

> Nach dem Fall der alten Welt entwickelte Vault-Tec ein autonomes Überwachungssystem…
> **VAULT-OS**.
>
> Es schützt die verbleibenden Systeme vor Überlastung, Eindringlingen und… menschlichen Fehlern.

---

## ❤️ Credits

Entwickelt von einem aufstrebenden Tech-Mind auf dem Weg in Richtung **Cybersecurity / DevOps / Robotics**.

---

## 🛑 Haftungsausschluss

Dieses Tool dient zu Lern- und Monitoringzwecken.
Keine Garantie für vollständige Sicherheit.

---

## 🟢 Status

```
SYSTEM STATUS: STABLE
SECURITRON: ACTIVE
VAULT INTEGRITY: 100%
```
