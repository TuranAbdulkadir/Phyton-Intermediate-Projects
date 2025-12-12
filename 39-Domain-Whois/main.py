import whois

domain = input("Sorgulanacak Domain (örn: google.com): ")

print("\n--- WHOIS BİLGİLERİ ---")
print("Sorgulanıyor...\n")

try:
    info = whois.whois(domain)
    
    print(f"Domain: {info.domain_name}")
    print(f"Kayıt Eden: {info.registrar}")
    print(f"Oluşturma Tarihi: {info.creation_date}")
    print(f"Bitiş Tarihi: {info.expiration_date}")
    print(f"Sunucular: {info.name_servers}")
    print(f"Ülke: {info.country}")
    
except Exception as e:
    print(f"Hata: {e}")