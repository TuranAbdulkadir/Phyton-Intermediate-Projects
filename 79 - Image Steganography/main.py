from stegano import lsb

choice = input("1-Gizle / 2-Çöz: ")

if choice == "1":
    img = input("Resim Yolu: ")
    msg = input("Gizlenecek Mesaj: ")
    secret = lsb.hide(img, msg)
    secret.save("secret_image.png")
    print("[+] Mesaj gizlendi -> secret_image.png")

elif choice == "2":
    img = input("Gizli Resim Yolu: ")
    try:
        clear_message = lsb.reveal(img)
        print(f"[+] Gizli Mesaj: {clear_message}")
    except:
        print("[-] Mesaj bulunamadı.")