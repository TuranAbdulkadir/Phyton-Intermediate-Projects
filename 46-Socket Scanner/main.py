import socket
from colorama import Fore, init

init()

target = input("Hedef IP Adresini Girin: ")
print(f"{Fore.CYAN}[*] {target} taranıyor...{Fore.RESET}")

try:
    for port in range(1, 1000): # İlk 1000 portu tara
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.5)
        result = s.connect_ex((target, port))
        if result == 0:
            print(f"{Fore.GREEN}[+] Port {port} AÇIK{Fore.RESET}")
        s.close()
except KeyboardInterrupt:
    print("\nÇıkış yapılıyor...")
except socket.gaierror:
    print("Hostname çözülemedi.")
except socket.error:
    print("Sunucuya bağlanılamadı.")