import csv
from collections import Counter

filename = 'network_log.csv'

try:
    with open(filename, mode='r') as f:
        reader = csv.DictReader(f)
        data = list(reader)

    if not data:
        print("File e kono data nai!")
    else:
        print(f"--- Total Packets: {len(data)} ---")

        # Top Source IPs ber kora
        src_ips = [row['Source IP'] for row in data]
        ip_counts = Counter(src_ips)

        print("\n[ Security Alerts ]")
        threshold = 100 # 10 er beshi packet pathale alert dibe
        alert_found = False
        for ip, count in ip_counts.items():
            if count > threshold:
                print(f"⚠️ ALERT: Unusual traffic from {ip}! (Packets: {count})")
                alert_found = True
        
        if not alert_found:
            print("No suspicious activity detected.")

        print("\n[ Protocol Summary ]")
        protocols = [row['Protocol'] for row in data]
        for proto, count in Counter(protocols).items():
            p_name = "TCP" if proto == '6' else "UDP" if proto == '17' else proto
            print(f"{p_name}: {count} times")

except FileNotFoundError:
    print("Error: network_log.csv paini. Age main.py run koren.")