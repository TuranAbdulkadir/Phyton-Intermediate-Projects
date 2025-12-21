import requests

target = input("Hedef URL (http://site.com): ")
paths = ["admin", "test", "dev", "api", "backup", "db", "conf"]

print("[*] Fuzzing Başlıyor...\n")

for path in paths:
    url = f"{target}/{path}"
    r = requests.get(url)
    
    if r.status_code == 200:
        print(f"[+] {url} -> 200 OK (Mevcut)")
    elif r.status_code == 403:
        print(f"[!] {url} -> 403 Forbidden (Yasaklı ama var)")
    elif r.status_code == 500:
        print(f"[!] {url} -> 500 Server Error (Hata bulundu!)")