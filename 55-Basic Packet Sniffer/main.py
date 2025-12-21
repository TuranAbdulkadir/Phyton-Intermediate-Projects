from scapy.all import sniff

def packet_callback(packet):
    if packet.haslayer("IP"):
        src = packet["IP"].src
        dst = packet["IP"].dst
        print(f"[+] Paket Yakalandı: {src} -> {dst}")

print("[*] Ağ dinleniyor... (CTRL+C ile durdur)")
# count=10 -> 10 paket yakalayıp durur
sniff(prn=packet_callback, count=20)