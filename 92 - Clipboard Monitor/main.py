import pyperclip
import time

print("[*] Pano izleniyor...")

previous_data = ""

while True:
    current_data = pyperclip.paste()
    if current_data != previous_data:
        print(f"[+] Kopyalanan Veri Yakalandı: {current_data}")
        previous_data = current_data
        
        # Burada veriyi log dosyasına kaydedebilirsin
        with open("clipboard_log.txt", "a") as f:
            f.write(current_data + "\n")
            
    time.sleep(1)