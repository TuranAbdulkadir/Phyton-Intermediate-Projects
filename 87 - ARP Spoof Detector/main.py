from scapy.all import sniff, ARP

def process_packet(packet):
    if packet.haslayer(ARP) and packet[ARP].op == 2: # ARP Response
        try:
            real_mac = get_mac(packet[ARP].psrc)
            response_mac = packet[ARP].hwsrc

            if real_mac != response_mac:
                print(f"[!!!] ARP SPOOFING TESPİT EDİLDİ! IP: {packet[ARP].psrc}")
        except:
            pass

print("[*] ARP Saldırıları İzleniyor...")
sniff(store=False, prn=process_packet)