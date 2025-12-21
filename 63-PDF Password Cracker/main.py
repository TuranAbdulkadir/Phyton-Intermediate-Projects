import pikepdf
from tqdm import tqdm # İlerleme çubuğu (pip install tqdm)

pdf_file = input("PDF Dosyası: ")
wordlist = input("Wordlist Dosyası: ")

passwords = [line.strip() for line in open(wordlist)]

for password in tqdm(passwords, "Deneniyor"):
    try:
        with pikepdf.open(pdf_file, password=password) as pdf:
            print(f"\n[+] ŞİFRE BULUNDU: {password}")
            break
    except pikepdf.PasswordError:
        continue