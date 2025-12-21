from faker import Faker

fake = Faker() # 'tr_TR' ekleyerek Türkçe yapabilirsin

print("[*] SAHTE KİMLİK OLUŞTURULUYOR...\n")

print(f"Ad Soyad: {fake.name()}")
print(f"Adres: {fake.address()}")
print(f"Email: {fake.email()}")
print(f"İş: {fake.job()}")
print(f"Kredi Kartı (Test): {fake.credit_card_number()}")