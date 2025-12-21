import socket
from cryptography.fernet import Fernet

key = input("Sunucunun verdiği anahtarı gir: ").encode()
cipher = Fernet(key)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1", 5555)) # Sunucu IP'si

while True:
    msg = input("Sen: ")
    encrypted_msg = cipher.encrypt(msg.encode())
    client.send(encrypted_msg)