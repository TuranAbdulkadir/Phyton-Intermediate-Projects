import subprocess
import re

# Kayıtlı profilleri al
output = subprocess.getoutput("netsh wlan show profiles")
profiles = re.findall(r"All User Profile\s*:\s(.*)", output)

print(f"[*] {len(profiles)} ağ bulundu. Şifreler çekiliyor...\n")

for profile in profiles:
    profile = profile.strip()
    try:
        results = subprocess.getoutput(f'netsh wlan show profile name="{profile}" key=clear')
        password = re.search(r"Key Content\s*:\s(.*)", results).group(1)
        print(f"AĞ: {profile:<20} | ŞİFRE: {password}")
    except AttributeError:
        print(f"AĞ: {profile:<20} | ŞİFRE: [Açık Ağ veya Hata]")