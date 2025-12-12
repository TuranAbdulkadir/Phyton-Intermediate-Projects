import os
from colorama import Fore, Style, init

init() # Renkleri başlat

def list_files(startpath):
    print(f"\n📂 {Fore.YELLOW}{startpath}{Style.RESET_ALL}")
    
    for root, dirs, files in os.walk(startpath):
        level = root.replace(startpath, '').count(os.sep)
        indent = ' ' * 4 * (level)
        
        # Klasör adı
        print(f"{indent}{Fore.BLUE}📁 {os.path.basename(root)}/{Style.RESET_ALL}")
        
        subindent = ' ' * 4 * (level + 1)
        # Dosya adları
        for f in files:
            print(f"{subindent}{Fore.GREEN}📄 {f}{Style.RESET_ALL}")

# Çalıştığı klasörü listele
current_dir = os.getcwd()
list_files(current_dir)

input("\nÇıkmak için Enter...")