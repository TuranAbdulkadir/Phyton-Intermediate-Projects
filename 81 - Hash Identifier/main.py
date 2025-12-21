hash_input = input("Hash Girin: ").strip()
length = len(hash_input)

print(f"\n[*] Hash Uzunluğu: {length}")

if length == 32:
    print("[+] Tahmin: MD5")
elif length == 40:
    print("[+] Tahmin: SHA-1")
elif length == 64:
    print("[+] Tahmin: SHA-256")
elif length == 128:
    print("[+] Tahmin: SHA-512")
else:
    print("[-] Bilinmeyen veya desteklenmeyen hash türü.")