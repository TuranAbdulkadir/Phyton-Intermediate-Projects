import zipfile
import threading

zip_file = input("Zip Dosyası: ")
wordlist = input("Wordlist: ")

def crack(password):
    try:
        with zipfile.ZipFile(zip_file) as z:
            z.extractall(pwd=password.encode())
            print(f"\n[+] ŞİFRE BULUNDU: {password}")
            # Programı sonlandır (basit yöntem)
            import os; os._exit(0)
    except:
        pass

with open(wordlist, "r", encoding="latin-1") as f:
    for line in f:
        password = line.strip()
        t = threading.Thread(target=crack, args=(password,))
        t.start()