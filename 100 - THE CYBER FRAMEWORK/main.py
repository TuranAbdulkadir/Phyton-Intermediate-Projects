import os
from colorama import Fore, init

init()

def banner():
    print(Fore.GREEN + """
    =========================================
       CYBER SECURITY FRAMEWORK v1.0
       [100 Projects Completed]
    =========================================
    """ + Fore.RESET)

def main():
    while True:
        banner()
        print("1. Port Scanner")
        print("2. WiFi Deauth Attack")
        print("3. Password Generator")
        print("4. Hash Cracker")
        print("5. Subdomain Finder")
        print("99. Çıkış")
        
        choice = input(Fore.YELLOW + "\nSeçiminiz: " + Fore.RESET)
        
        if choice == "1":
            os.system("python port_scanner.py")
        elif choice == "2":
            os.system("sudo python wifi_kicker.py")
        elif choice == "3":
            os.system("python pass_gen.py")
        elif choice == "4":
            os.system("python hash_cracker.py")
        elif choice == "5":
            os.system("python subdomain_finder.py")
        elif choice == "99":
            print("Güle güle...")
            break
        else:
            print("Geçersiz seçim!")

if __name__ == "__main__":
    main()