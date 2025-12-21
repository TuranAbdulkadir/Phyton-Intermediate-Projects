import requests

target = input("Hedef Site (https://...): ")
important_headers = ['X-Frame-Options', 'X-XSS-Protection', 'Content-Security-Policy', 'Strict-Transport-Security']

try:
    response = requests.get(target)
    headers = response.headers
    
    print("\n[*] Güvenlik Başlıkları Analizi:")
    for header in important_headers:
        if header in headers:
            print(f"[+] {header}: MEVCUT ({headers[header]})")
        else:
            print(f"[-] {header}: EKSİK! (Riskli)")
            
except:
    print("Siteye bağlanılamadı.")