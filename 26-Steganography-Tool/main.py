from stegano import lsb
import os

print("--- GİZLİ AJAN ARACI (Steganography) ---")
print("1: Mesaj Gizle (Hide)")
print("2: Mesajı Oku (Reveal)")

choice = input("Seçiminiz (1/2): ")

if choice == '1':
    if os.path.exists("input.png"):
        secret_text = input("Gizlenecek Mesajı Yaz: ")
        secret = lsb.hide("input.png", secret_text)
        secret.save("gizli_resim.png")
        print("✅ Mesaj başarıyla 'gizli_resim.png' içine saklandı!")
    else:
        print("❌ Hata: Klasörde 'input.png' bulunamadı.")

elif choice == '2':
    filename = input("Okunacak resim (örn: gizli_resim.png): ")
    try:
        clear_message = lsb.reveal(filename)
        print(f"🔓 GİZLİ MESAJ: {clear_message}")
    except:
        print("❌ Bu resimde gizli mesaj yok veya dosya bozuk.")    