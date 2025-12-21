import socket
from cryptography.fernet import Fernet

# Anahtar (İki tarafta da aynı olmalı)
key = Fernet.generate_key()
cipher = Fernet(key)
print(f"[*] GÜVENLİK ANAHTARI (Bunu Client'a ver): {key.decode()}")

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("0.0.0.0", 5555))
server.listen(1)

print("[*] Sohbet Sunucusu Bekliyor...")
client, addr = server.accept()
print(f"[+] Bağlantı: {addr}")

while True:
    encrypted_msg = client.recv(1024)
    if not encrypted_msg: break
    msg = cipher.decrypt(encrypted_msg).decode()
    print(f"Client: {msg}")