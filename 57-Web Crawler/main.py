import requests
from bs4 import BeautifulSoup

url = input("Taranacak Site (https://ornek.com): ")

try:
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    print(f"[*] {url} üzerindeki linkler toplanıyor...\n")
    
    for link in soup.find_all('a'):
        href = link.get('href')
        if href and href.startswith('http'):
            print(f"[+] Link: {href}")
            
except Exception as e:
    print(f"Hata: {e}")