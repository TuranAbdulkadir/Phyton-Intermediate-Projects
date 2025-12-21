import socket

TARGET_IP = "127.0.0.1" # Kendi bilgisayarın
TARGET_PORT = 9999

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    client.connect((TARGET_IP, TARGET_PORT))
    message = input("Gönderilecek Mesaj: ")
    client.send(message.encode())
    print("[+] Mesaj gönderildi!")
    client.close()
except ConnectionRefusedError:
    print("[-] Hedef sunucu kapalı.")