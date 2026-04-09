import psutil
from datetime import datetime
import subprocess

# Schwellenwerte (eventuell später anpassen)
CPU_LIMIT = 80
RAM_LIMIT = 80
DISK_LIMIT = 90

def check_logins():
    last = subprocess.getoutput("last -n 1")
    return last

def get_failed_logins():
    try:
        output = subprocess.getoutput("journalctl -u ssh -n 20 --no-pager 2>/dev/null | grep 'Failed password'")
        if output:
            return output.split("\n")[-3:]  # nur letzte 3 anzeigen
        return []
    except:
        return []
    
def get_suspicious_processes():
    try:
        output = subprocess.getoutput("ps aux --sort=-%cpu | head -n 6")
        lines = output.split("\n")[1:]
        
        suspicious = []
        for line in lines:
            if "root" in line:
                suspicious.append(line)

        return suspicious[:3]
    except:
        return []
    
def get_system_stats():
    cpu = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent
    
    # Absicherung für Logs
    cpu = cpu if cpu is not None else 0.0
    ram = ram if ram is not None else 0.0
    disk = disk if disk is not None else 0.0
    
    return cpu, ram, disk

def check_limits(cpu, ram, disk):
    warnings = []

    if cpu > CPU_LIMIT:
        warnings.append(f"⚠️ CPU kritisch: {cpu}%")

    if ram > RAM_LIMIT:
        warnings.append(f"⚠️ RAM kritisch: {ram}%")

    if disk > DISK_LIMIT:
        warnings.append(f"⚠️ Speicher kritisch: {disk}%")

    return warnings

def get_report():
    cpu, ram, disk = get_system_stats()
    warnings = check_limits(cpu, ram, disk)

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    return {
        "timestamp": timestamp,
        "cpu": cpu,
        "ram": ram,
        "disk": disk,
        "warnings": warnings,
        "last_login": check_logins(),
        "failed_logins": get_failed_logins(),
        "suspicious": get_suspicious_processes()
    }
    
def main():
    cpu, ram, disk = get_system_stats()
    warnings = check_limits(cpu, ram, disk)

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    print(f"\n📊 Vault Status Report [{timestamp}]")
    print(f"CPU: {cpu}% | RAM: {ram}% | DISK: {disk}%")

    if warnings:
        print("\n🚨 WARNUNG:")
        for w in warnings:
            print(w)
    else:
        print("\n✅ Alles stabil im Vault.")

if __name__ == "__main__":
    main()
