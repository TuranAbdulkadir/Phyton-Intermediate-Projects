import socket

def grab_banner(ip, port):
    try:
        s = socket.socket()
        s.settimeout(2)
        s.connect((ip, int(port)))
        banner = s.recv(1024)
        print(f"[+] {ip}:{port} Banner: {banner.decode().strip()}")
    except:
        print(f"[-] {ip}:{port} üzerinden banner alınamadı.")

ip = input("Hedef IP: ")
port = input("Hedef Port: ")
grab_banner(ip, port)