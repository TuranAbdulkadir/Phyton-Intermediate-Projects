from scapy.all import ARP, Ether, srp

target_ip = input("IP Aralığı (örn: 192.168.1.1/24): ")

# ARP Paketi oluştur
arp = ARP(pdst=target_ip)
ether = Ether(dst="ff:ff:ff:ff:ff:ff")
packet = ether/arp

print("[*] Ağ taranıyor, lütfen bekleyin...")
result = srp(packet, timeout=3, verbose=0)[0]

print("IP Adresi\t\tMAC Adresi")
print("-----------------------------------------")
for sent, received in result:
    print(f"{received.psrc}\t\t{received.hwsrc}")