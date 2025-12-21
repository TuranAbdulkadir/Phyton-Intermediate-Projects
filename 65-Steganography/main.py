def hide_message(file_path, message):
    with open(file_path, "a") as f:
        f.write(f"") # HTML yorumu gibi gizle
    print("[+] Mesaj dosyaya gizlendi.")

def read_message(file_path):
    with open(file_path, "r") as f:
        content = f.read()
        if "')[0]}")
        else:
            print("[-] Mesaj bulunamadı.")

choice = input("1-Gizle / 2-Oku: ")
file = input("Dosya Adı: ")

if choice == "1":
    msg = input("Mesajınız: ")
    hide_message(file, msg)
elif choice == "2":
    read_message(file)