import dns.resolver

domain = input("Domain (google.com): ")

print(f"\n[*] {domain} için Mail Güvenliği Taranıyor...")

try:
    # SPF Kaydı Kontrolü
    answers = dns.resolver.resolve(domain, 'TXT')
    spf_found = False
    for rdata in answers:
        if "v=spf1" in str(rdata):
            print(f"[+] SPF Kaydı: {rdata}")
            spf_found = True
    if not spf_found:
        print("[-] SPF Kaydı YOK! (Spoofing Riski)")

except Exception as e:
    print(f"[-] Hata: {e}")