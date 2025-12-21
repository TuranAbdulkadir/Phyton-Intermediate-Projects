import requests

url = "http://httpbin.org/user-agent" # Test sitesi

# Kendimizi iPhone gibi gösterelim
headers = {
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X)'
}

print("[*] İstek gönderiliyor...")
r = requests.get(url, headers=headers)

print(f"[+] Sunucunun Gördüğü: {r.text}")