import requests

ip = input("Sorgulanacak IP Adresi: ")
url = f"http://ip-api.com/json/{ip}"

response = requests.get(url).json()

if response['status'] == 'success':
    print("\n[*] KONUM BİLGİLERİ:")
    print(f"Ülke: {response['country']}")
    print(f"Şehir: {response['city']}")
    print(f"ISP: {response['isp']}")
    print(f"Koordinatlar: {response['lat']}, {response['lon']}")
else:
    print("[-] IP bulunamadı.")