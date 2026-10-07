from scapy.all import AsyncSniffer, IP, TCP, UDP
from scapy.utils import PcapWriter
import msvcrt
pcap= PcapWriter("capture.pcap",append=False, sync=True)
def process_packet(packet):
    pcap.write(packet)
    if not packet.haslayer(IP):
        return
    if  packet.haslayer(TCP):

        src_ip=packet[IP].src
        dst_ip=packet[IP].dst
        src_port=packet[TCP].sport
        dst_port=packet[TCP].dport
        print(f"[TCP] {src_ip}:{src_port} -> {dst_ip}:{dst_port}")    
    elif packet.haslayer(UDP):
        src_ip=packet[IP].src
        dst_ip=packet[IP].dst
        src_udp_port=packet[UDP].sport
        dst_udp_port=packet[UDP].dport
        print(f"[UDP] {src_ip}:{src_udp_port} -> {dst_ip}:{dst_udp_port}")
    else: 
        return
sniff=AsyncSniffer(prn=process_packet, store=False)
try:
     sniff.start()
     print("Listening to live traffic ")
     msvcrt.getch()
except KeyboardInterrupt:
    pass
finally:
    sniff.stop()
    pcap.close()
    print("\n Capture stopped cleanly")


