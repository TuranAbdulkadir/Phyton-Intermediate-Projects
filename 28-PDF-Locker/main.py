from PyPDF2 import PdfReader, PdfWriter

print("--- PDF KİLİTLEYİCİ ---")
target_pdf = "dosya.pdf"
password = input("Koymak istediğin şifre: ")

try:
    reader = PdfReader(target_pdf)
    writer = PdfWriter()

    # Tüm sayfaları kopyala
    for page in reader.pages:
        writer.add_page(page)

    # Şifrele
    writer.encrypt(password)

    # Kaydet
    with open("kilitli_dosya.pdf", "wb") as f:
        writer.write(f)
    
    print(f"✅ Dosya şifrelendi: kilitli_dosya.pdf")
    print(f"🔑 Şifre: {password}")

except FileNotFoundError:
    print("❌ 'dosya.pdf' bulunamadı!")