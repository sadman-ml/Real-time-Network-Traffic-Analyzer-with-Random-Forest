import pandas as pd
import matplotlib.pyplot as plt

# CSV ফাইল লোড করা
filename = 'network_log.csv'

try:
    df = pd.read_csv(filename)
    # প্রোটোকল নম্বর ম্যাপ করা
    df['Protocol'] = df['Protocol'].map({6: 'TCP', 17: 'UDP', 2: 'IGMP'}).fillna('Others')

    # ১. প্রথম চার্ট: প্রোটোকল ডিস্ট্রিবিউশন (Pie Chart)
    fig1 = plt.figure(figsize=(8, 6))
    df['Protocol'].value_counts().plot(kind='pie', autopct='%1.1f%%', colors=['skyblue', 'salmon', 'green'])
    plt.title('Protocol Distribution Analysis')
    plt.ylabel('') # অপ্রয়োজনীয় লেবেল সরানো
    
    # ২. দ্বিতীয় চার্ট: টপ ৫ সোর্স আইপি (Bar Chart)
    fig2 = plt.figure(figsize=(10, 6))
    df['Source IP'].value_counts().head(5).plot(kind='bar', color='orange')
    plt.title('Top 5 Source IPs (Network Traffic)')
    plt.xlabel('IP Address')
    plt.ylabel('Packet Count')
    plt.xticks(rotation=45) # আইপিগুলো পড়ার সুবিধার জন্য বাঁকা করা
    plt.tight_layout()

    # সবশেষে একবারই শো করা
    plt.show()

except Exception as e:
    print(f"Error: {e}")