import csv
from scapy.all import sniff, IP
captured_data = []

# Callback function for each packet
def packet_callback(packet):
    if packet.haslayer(IP):
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        proto = packet[IP].proto
        captured_data.append([src_ip, dst_ip, proto])
        print(f"Captured: {src_ip} -> {dst_ip}")

# Sniffing for 5 seconds
print("Sniffing started...")
sniff(prn=packet_callback, timeout=70)

# file saved
with open('network_log.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["Source IP", "Destination IP", "Protocol"])
    writer.writerows(captured_data)

print("Done! Data saved to network_log.csv")
