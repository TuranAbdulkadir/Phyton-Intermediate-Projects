import psutil
import time
from plyer import notification

print("--- USB CİHAZ TAKİBİ ---")
print("USB takılmasını bekliyorum... (Çıkış: Ctrl+C)")

# Başlangıçtaki diskleri kaydet
drives_before = set(p.device for p in psutil.disk_partitions())

try:
    while True:
        time.sleep(2)
        drives_now = set(p.device for p in psutil.disk_partitions())
        
        # Yeni takılan var mı?
        added = drives_now - drives_before
        # Çıkarılan var mı?
        removed = drives_before - drives_now
        
        if added:
            msg = f"YENİ CİHAZ: {', '.join(added)}"
            print("🚨 " + msg)
            notification.notify(title="USB Tespit Edildi", message=msg, timeout=5)
            
        if removed:
            print(f"🔻 Cihaz Çıkarıldı: {', '.join(removed)}")
            
        drives_before = drives_now

except KeyboardInterrupt:
    print("Takip durduruldu.")