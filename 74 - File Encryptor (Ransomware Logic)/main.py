from cryptography.fernet import Fernet

# Anahtar oluştur ve kaydet
key = Fernet.generate_key()
with open("secret.key", "wb") as key_file:
    key_file.write(key)

file_name = input("Şifrelenecek Dosya Adı: ")

# Dosyayı oku
with open(file_name, "rb") as file:
    file_data = file.read()

# Şifrele
f = Fernet(key)
encrypted_data = f.encrypt(file_data)

# Kaydet
with open(file_name, "wb") as file:
    file.write(encrypted_data)

print(f"[+] Dosya şifrelendi! Anahtar: secret.key")