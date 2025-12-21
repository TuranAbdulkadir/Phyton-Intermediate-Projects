import whois

domain = input("Domain Girin (google.com): ")

try:
    w = whois.whois(domain)
    print("\n[*] WHOIS BİLGİLERİ:")
    print(f"Kayıt Kuruluşu: {w.registrar}")
    print(f"Oluşturma Tarihi: {w.creation_date}")
    print(f"Bitiş Tarihi: {w.expiration_date}")
    print(f"E-postalar: {w.emails}")
except Exception as e:
    print(e)