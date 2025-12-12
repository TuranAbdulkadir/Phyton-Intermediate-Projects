import pyautogui
import time
import matplotlib.pyplot as plt

print("--- MOUSE TAKİBİ BAŞLADI ---")
print("10 saniye boyunca fareni normal kullan...")

x_pos = []
y_pos = []
start_time = time.time()

try:
    while time.time() - start_time < 10:
        x, y = pyautogui.position()
        x_pos.append(x)
        y_pos.append(y * -1) # Grafikte düzgün dursun diye ters çevirdik
        time.sleep(0.1) # Kayıt sıklığı
        
    print("Süre doldu! Harita oluşturuluyor...")
    
    plt.figure(figsize=(10, 6))
    plt.scatter(x_pos, y_pos, c='red', alpha=0.5, s=10)
    plt.title("Mouse Isı Haritası (Son 10 Sn)")
    plt.xlabel("Ekran X")
    plt.ylabel("Ekran Y")
    plt.grid(True)
    plt.show()

except KeyboardInterrupt:
    print("İptal edildi.")