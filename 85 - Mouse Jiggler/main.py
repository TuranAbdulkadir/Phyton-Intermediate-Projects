import pyautogui
import time
import random

print("[*] Mouse Jiggler Aktif. (Durdurmak için fareyi köşeye çekin)")

try:
    while True:
        x = random.randint(-5, 5)
        y = random.randint(-5, 5)
        pyautogui.moveRel(x, y)
        time.sleep(5) # 5 saniyede bir oynat
except KeyboardInterrupt:
    print("\nDurduruldu.")