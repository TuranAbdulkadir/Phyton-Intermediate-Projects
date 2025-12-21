import requests

domain = input("Hedef Domain (örn: google.com): ")
# Sunum için kısa liste, gerçekte büyük wordlist kullanılır
subdomains = ["www", "mail", "ftp", "admin", "blog", "dev", "test", "shop"] 

print(f"[*] {domain} için alt alan adları taranıyor...\n")

for sub in subdomains:
    url = f"http://{sub}.{domain}"
    try:
        requests.get(url, timeout=2)
        print(f"[+] BULUNDU: {url}")
    except requests.ConnectionError:
        pass # Bulunamazsa ses etme