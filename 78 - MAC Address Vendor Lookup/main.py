import requests

mac_address = input("MAC Adresi (örn: 44:38:39:ff:ef:57): ")
url = f"https://api.macvendors.com/{mac_address}"

try:
    response = requests.get(url)
    if response.status_code == 200:
        print(f"\n[+] Üretici Firma: {response.text}")
    else:
        print("[-] Bulunamadı.")
except:
    print("Bağlantı hatası.")