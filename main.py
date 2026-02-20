import csv
from scapy.all import sniff, IP

# একটি লিস্টে আমরা ডেটাগুলো রাখব
captured_data = []

def packet_callback(packet):
    if packet.haslayer(IP):
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        proto = packet[IP].proto
        captured_data.append([src_ip, dst_ip, proto])
        print(f"Captured: {src_ip} -> {dst_ip}")

# ৫ সেকেন্ডের জন্য স্নিনিং (Sniffing)
print("Sniffing started...")
sniff(prn=packet_callback, timeout=70)

# ফাইল সেভ করা
with open('network_log.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["Source IP", "Destination IP", "Protocol"])
    writer.writerows(captured_data)

print("Done! Data saved to network_log.csv")