import zipfile

print("--- ZIP PASSWORD CRACKER ---")
zip_file = "test.zip" # Şifreli zip dosyan
wordlist = "wordlist.txt" # Denenecek şifreler listesi (içine 1234, admin vs yaz)

try:
    zip_obj = zipfile.ZipFile(zip_file)
    with open(wordlist, 'r') as pass_file:
        for line in pass_file:
            password = line.strip()
            try:
                zip_obj.extractall(pwd=password.encode())
                print(f"🔥 ŞİFRE BULUNDU: {password}")
                break
            except:
                continue
    print("İşlem bitti.")
except FileNotFoundError:
    print("❌ Dosyalar eksik! (test.zip ve wordlist.txt koymalısın)")