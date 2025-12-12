import pyautogui
import time
import random

print("--- AFK BOT (Durdurmak için: CTRL+C) ---")
print("Mouse her 5 saniyede bir hareket edecek.")

try:
    while True:
        x = random.randint(-5, 5)
        y = random.randint(-5, 5)
        pyautogui.moveRel(x, y) # Mouse'u hafifçe oynat
        print(f"Hareket edildi: {x}, {y}")
        time.sleep(5)
except KeyboardInterrupt:
    print("\n✅ Bot durduruldu.")