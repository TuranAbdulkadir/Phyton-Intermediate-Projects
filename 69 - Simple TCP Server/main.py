import socket

SERVER_IP = "0.0.0.0" # Tüm arayüzleri dinle
SERVER_PORT = 9999

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((SERVER_IP, SERVER_PORT))
server.listen(1)

print(f"[*] Sunucu dinliyor: {SERVER_PORT}")

client, addr = server.accept()
print(f"[+] Bağlantı geldi: {addr}")

msg = client.recv(1024).decode()
print(f"[>] Mesaj: {msg}")

client.close()
server.close()