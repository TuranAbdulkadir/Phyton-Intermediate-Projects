import zipfile

zip_file = input("Zip Dosyası Adı: ")
wordlist = input("Wordlist Dosyası Adı: ")

zip_obj = zipfile.ZipFile(zip_file)
found = False

with open(wordlist, "rb") as file:
    for line in file:
        password = line.strip()
        try:
            zip_obj.extractall(pwd=password)
            print(f"\n[+] ŞİFRE KIRILDI: {password.decode()}")
            found = True
            break
        except:
            continue

if not found:
    print("[-] Şifre bulunamadı.")