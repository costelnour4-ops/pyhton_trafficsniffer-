from scapy.all import sniff, IP, TCP
def process_packet(packet):
    if packet.haslayer(IP) and packet.haslayer(TCP):
        src_ip=packet[IP].src
        dst_ip=packet[IP].dst
        src_port=packet[TCP].sport
        dst_port=packet[TCP].dport
        print(f"[TCP] {src_ip}:{src_port} -> {dst_ip}:{dst_port}")
print("Listenin to live traffic, press CTRL+C to stop the traffic")
try:
    sniff(prn=process_packet, store=False)
except KeyboardInterrupt:
    print("\n Capture stopped cleanly")