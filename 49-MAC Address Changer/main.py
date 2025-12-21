import subprocess
import random

def get_random_mac():
    mac = [0x00, 0x16, 0x3e,
           random.randint(0x00, 0x7f),
           random.randint(0x00, 0xff),
           random.randint(0x00, 0xff)]
    return ':'.join(map(lambda x: "%02x" % x, mac))

interface = input("Ağ Arayüzü (örn: eth0 veya wlan0): ")
new_mac = get_random_mac()

print(f"[*] {interface} için MAC adresi değiştiriliyor -> {new_mac}")

# Linux komutlarını çalıştır
subprocess.call(["sudo", "ifconfig", interface, "down"])
subprocess.call(["sudo", "ifconfig", interface, "hw", "ether", new_mac])
subprocess.call(["sudo", "ifconfig", interface, "up"])

print("[+] MAC Adresi başarıyla değiştirildi!")