from scapy.all import *
from texttable import Texttable

# Function to parse packet
def parse_packet(packet):
    # Check for IP layer
    if packet.haslayer(IP):
        src_ip = packet[IP].src
        dest_ip = packet[IP].dst
        protocol = packet[IP].proto
    else:
        src_ip = dest_ip = protocol = None

    # Check for TCP or UDP layer
    if packet.haslayer(TCP):
        source_port = packet[TCP].sport
        dest_port = packet[TCP].dport
        payload_data = packet[TCP].payload.load[:8].hex()  # First 8 bytes of the payload
        protocol_name = "TCP"
    elif packet.haslayer(UDP):
        source_port = packet[UDP].sport
        dest_port = packet[UDP].dport
        payload_data = packet[UDP].payload.load[:8].hex()  # First 8 bytes of the payload
        protocol_name = "UDP"
    elif packet.haslayer(ICMP):
        source_port = dest_port = None
        payload_data = packet[ICMP].payload.load[:8].hex()  # First 8 bytes of the payload
        protocol_name = "ICMP"
    else:
        return  # Unknown or unsupported protocol, skip packet

    # Print packet info in table format
    print_packet_info(src_ip, dest_ip, protocol_name, source_port, dest_port, payload_data)

# Function to print packet information in a table format
def print_packet_info(src_ip, dest_ip, protocol, source_port, dest_port, payload_data):
    t = Texttable()
    t.add_row(["Source IP", "Destination IP", "Protocol", "Source Port", "Destination Port", "Payload"])
    t.add_row([src_ip, dest_ip, protocol, source_port, dest_port, payload_data])
    print(t.draw())

# Function to start sniffing
def capture_packets():
    print("Starting packet sniffer...")
    sniff(prn=parse_packet, store=0)  # Capture packets and call `parse_packet` for each

# Run the sniffer
if __name__ == "__main__":
    capture_packets()
