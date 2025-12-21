import psutil
import time

print("[*] Sistem Kaynakları İzleniyor (CTRL+C ile durdur)...")

while True:
    cpu_usage = psutil.cpu_percent(interval=1)
    ram_usage = psutil.virtual_memory().percent
    
    if cpu_usage > 80:
        print(f"[!] YÜKSEK CPU KULLANIMI: %{cpu_usage}")
    
    if ram_usage > 90:
        print(f"[!] YÜKSEK RAM KULLANIMI: %{ram_usage}")
        
    print(f"CPU: %{cpu_usage} | RAM: %{ram_usage}")
    time.sleep(1)