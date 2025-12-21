import base64

def encode(text):
    encoded_bytes = base64.b64encode(text.encode("utf-8"))
    return encoded_bytes.decode("utf-8")

def decode(text):
    decoded_bytes = base64.b64decode(text.encode("utf-8"))
    return decoded_bytes.decode("utf-8")

choice = input("1-Şifrele / 2-Çöz: ")
text = input("Metin: ")

if choice == "1":
    print(f"[+] Encoded: {encode(text)}")
elif choice == "2":
    print(f"[+] Decoded: {decode(text)}")