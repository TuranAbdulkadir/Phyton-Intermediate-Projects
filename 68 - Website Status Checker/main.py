import requests

sites = ["google.com", "facebook.com", "github.com", "olmayansite123.com"]

print("[*] Site Durum Kontrolü Başlıyor...\n")

for site in sites:
    url = f"http://{site}"
    try:
        r = requests.get(url, timeout=3)
        if r.status_code == 200:
            print(f"[+] {site} -> AKTİF")
        else:
            print(f"[-] {site} -> HATA ({r.status_code})")
    except requests.ConnectionError:
        print(f"[!] {site} -> ULAŞILAMIYOR")