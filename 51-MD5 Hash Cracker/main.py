import hashlib

target_hash = input("Kırılacak MD5 Hash'i girin: ")
wordlist = input("Wordlist dosya yolu (örn: sifreler.txt): ")

print("[*] Kırma işlemi başladı...")

try:
    with open(wordlist, "r", encoding='latin-1') as file:
        for line in file:
            word = line.strip()
            # Kelimeyi MD5 yap
            hashed_word = hashlib.md5(word.encode()).hexdigest()
            
            if hashed_word == target_hash:
                print(f"\n[+] ŞİFRE BULUNDU: {word}")
                exit()
    print("\n[-] Şifre listede bulunamadı.")
except FileNotFoundError:
    print("Dosya bulunamadı!")