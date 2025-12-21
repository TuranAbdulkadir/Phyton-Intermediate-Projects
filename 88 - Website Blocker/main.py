import os

# Windows: C:\Windows\System32\drivers\etc\hosts
# Linux: /etc/hosts
hosts_path = "/etc/hosts" 
redirect = "127.0.0.1"
website_list = ["www.facebook.com", "facebook.com", "www.twitter.com"]

print("[*] Siteler Engelleniyor...")

try:
    with open(hosts_path, "r+") as file:
        content = file.read()
        for site in website_list:
            if site in content:
                pass
            else:
                file.write(redirect + " " + site + "\n")
    print("[+] Başarılı! Siteler engellendi.")
except PermissionError:
    print("[-] Yönetici (Sudo) yetkisi gerekli.")