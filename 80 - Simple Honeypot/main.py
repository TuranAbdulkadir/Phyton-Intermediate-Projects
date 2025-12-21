import socket
import datetime

def start_honeypot(port=23): # 23 = Telnet Portu (Sık saldırılır)
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("0.0.0.0", port))
    server.listen(5)
    
    print(f"[*] Honeypot {port} portunda aktif...")
    
    while True:
        client, addr = server.accept()
        log = f"[{datetime.datetime.now()}] SALDIRI TESPİT EDİLDİ: {addr[0]}"
        print(log)
        
        # Log dosyasına yaz
        with open("honeypot.log", "a") as f:
            f.write(log + "\n")
            
        client.send(b"Access Denied.\n")
        client.close()

try:
    start_honeypot()
except PermissionError:
    print("Lütfen sudo ile çalıştırın (Düşük portlar yetki ister).")