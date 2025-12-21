import hashlib

file_path = input("Dosya Yolu: ")

def calculate_hash(file_path):
    sha256_hash = hashlib.sha256()
    with open(file_path, "rb") as f:
        # Dosyayı parça parça oku (Büyük dosyalar için)
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()

try:
    print(f"SHA256 Hash: {calculate_hash(file_path)}")
except FileNotFoundError:
    print("Dosya bulunamadı.")