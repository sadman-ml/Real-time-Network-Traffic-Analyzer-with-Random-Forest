# Network Traffic Visualization.
# 1. Protocol distribution (Pie Chart)
# 2. Top 5 Source IPs (Bar Chart)

import pandas as pd
import matplotlib.pyplot as plt

# CSV file loaded.
filename = 'network_log.csv'

try:
    df = pd.read_csv(filename)
    print(f"Dataset loaded with {len(df)} rows.")

    # =========================
    # Map has been used for showing protocol's name.
    # =========================
    protocol_map = {6: 'TCP', 17: 'UDP', 2: 'IGMP'}
    df['Protocol'] = df['Protocol'].map(protocol_map).fillna('Others')

    # =========================
    # 1. Pie Chart: Protocol Distribution
    # =========================
    plt.figure(figsize=(8,6))
    df['Protocol'].value_counts().plot(
        kind='pie',
        autopct='%1.1f%%',
        colors=['skyblue', 'salmon', 'green', 'lightgrey'],
        startangle=140
    )
    plt.title('Protocol Distribution')
    plt.ylabel('')  # y-axis label.
    plt.tight_layout()

    # =========================
    # 2. Bar Chart: Top 5 Source IPs
    # =========================
    plt.figure(figsize=(10,6))
    top_ips = df['Source IP'].value_counts().head(5)
    top_ips.plot(kind='bar', color='orange')
    plt.title('Top 5 Source IPs (Packet Count)')
    plt.xlabel('IP Address')
    plt.ylabel('Number of Packets')
    plt.xticks(rotation=45)
    plt.tight_layout()

    # =========================
    # Show all plots
    # =========================
    plt.show()

except FileNotFoundError:
    print(f"Error: '{filename}' file not found!!")
except Exception as e:
    print(f"Error: {e}")
