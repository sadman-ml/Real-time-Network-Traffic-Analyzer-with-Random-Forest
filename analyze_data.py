import csv
from collections import Counter

filename = 'network_log.csv'

try:
    with open(filename) as f:
        data = list(csv.DictReader(f))

    if not data:
        print("The file has no data!")
    else:
        print(f"--- Total Packets: {len(data)} ---")

        # Top Source IPs & Alerts
        src_ips = [row['Source IP'] for row in data]
        ip_counts = Counter(src_ips)

        print("\n[ Security Alerts ]")
        threshold = 100  # Alert if packets exceed this number
        alert_found = False
        for ip, count in ip_counts.items():
            if count > threshold:
                print(f"⚠️ ALERT: Unusual traffic from {ip} (Packets: {count})")
                alert_found = True
        if not alert_found:
            print("No suspicious activity detected.")

        # Protocol summary
        print("\n[ Protocol Summary ]")
        proto_map = {'6': 'TCP', '17': 'UDP', '2': 'IGMP'}
        protocols = [proto_map.get(row['Protocol'], row['Protocol']) for row in data]
        for proto, count in Counter(protocols).items():
            print(f"{proto}: {count} times")

except FileNotFoundError:
    print("Error: 'network_log.csv' not found. Please run main.py first.")
