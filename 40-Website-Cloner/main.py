import requests

url = input("Kopyalanacak Site URL (https:// dahil): ")
filename = "cloned_site.html"

headers = {'User-Agent': 'Mozilla/5.0'} # Tarayıcı taklidi yap

try:
    print("Bağlanılıyor...")
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        with open(filename, "w", encoding="utf-8") as f:
            f.write(response.text)
        print(f"✅ Site kopyalandı! '{filename}' dosyasını açabilirsin.")
    else:
        print(f"❌ Hata: {response.status_code}")
except Exception as e:
    print(f"Bağlantı hatası: {e}")