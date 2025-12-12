import browser_history
from datetime import datetime

print("--- TARAYICI GEÇMİŞİ ANALİZİ ---")
print("Veriler çekiliyor, biraz sürebilir...")

try:
    # Tüm tarayıcıların geçmişini birleştir
    history = browser_history.get_history()
    
    # Son 20 siteyi yazdır
    print(f"\n{'ZAMAN':<25} | {'WEB SİTESİ'}")
    print("-" * 60)
    
    # Listeyi ters çevir (En yeniden eskiye)
    for entry in reversed(history.histories[-20:]):
        date = entry[0].strftime("%d.%m.%Y %H:%M")
        url = entry[1]
        # URL çok uzunsa kısalt
        if len(url) > 50: url = url[:47] + "..."
        
        print(f"{date:<25} | {url}")

    # Dosyaya kaydet
    with open("history_log.txt", "w", encoding="utf-8") as f:
        for entry in history.histories:
            f.write(f"{entry[0]} - {entry[1]}\n")
            
    print("\n✅ Tüm geçmiş 'history_log.txt' dosyasına kaydedildi!")

except Exception as e:
    print(f"Hata: {e}")