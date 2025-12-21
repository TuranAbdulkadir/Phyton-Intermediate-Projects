import pyautogui
import time
import os

if not os.path.exists("screenshots"):
    os.makedirs("screenshots")

print("[*] Ekran takibi başladı (Her 5 saniyede bir)...")

counter = 0
try:
    while True:
        screenshot = pyautogui.screenshot()
        filename = f"screenshots/screen_{counter}.png"
        screenshot.save(filename)
        print(f"[+] Kaydedildi: {filename}")
        counter += 1
        time.sleep(5)
except KeyboardInterrupt:
    print("Durduruldu.")