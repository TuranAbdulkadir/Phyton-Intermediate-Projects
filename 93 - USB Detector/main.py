import psutil
import time

print("[*] USB Girişleri İzleniyor...")

base_drives = [d.device for d in psutil.disk_partitions()]

while True:
    current_drives = [d.device for d in psutil.disk_partitions()]
    
    # Farkı bul (Yeni takılanlar)
    new_drives = set(current_drives) - set(base_drives)
    
    if new_drives:
        for drive in new_drives:
            print(f"[!] YENİ USB AYGITI TESPİT EDİLDİ: {drive}")
        base_drives = current_drives
        
    time.sleep(2)