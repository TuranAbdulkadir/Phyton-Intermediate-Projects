import requests

target_url = input("Hedef URL (örn: http://google.com): ")
directories = ["admin", "login", "uploads", "backup", "images", "css", "js"]

print(f"[*] {target_url} üzerinde dizinler taranıyor...\n")

for directory in directories:
    url = f"{target_url}/{directory}"
    try:
        r = requests.get(url)
        if r.status_code != 404:
            print(f"[+] BULUNDU ({r.status_code}): {url}")
    except:
        pass