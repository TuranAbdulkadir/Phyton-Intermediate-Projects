from cryptography.fernet import Fernet

file_name = input("Çözülecek Dosya Adı: ")

# Anahtarı yükle
with open("secret.key", "rb") as key_file:
    key = key_file.read()

f = Fernet(key)

# Şifreli dosyayı oku
with open(file_name, "rb") as file:
    encrypted_data = file.read()

try:
    # Çöz
    decrypted_data = f.decrypt(encrypted_data)

    # Geri yaz
    with open(file_name, "wb") as file:
        file.write(decrypted_data)
    print("[+] Dosya başarıyla çözüldü ve eski haline döndü.")
except:
    print("[-] Hatalı Anahtar!")