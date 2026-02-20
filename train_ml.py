import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import classification_report
import joblib # এটি উপরে ইমপোর্ট করে নিন

# ১. ডেটা লোড করা
try:
    df = pd.read_csv('network_log.csv')
    print(f"Dataset loaded successfully with {len(df)} packets.")
except FileNotFoundError:
    print("Error: network_log.csv ফাইলটি পাওয়া যায়নি!")
    exit()

# ২. ফিচার ইঞ্জিনিয়ারিং
le_src = LabelEncoder()
le_dst = LabelEncoder()
le_proto = LabelEncoder()

df['src_id'] = le_src.fit_transform(df['Source IP'])
df['dst_id'] = le_dst.fit_transform(df['Destination IP'])
df['proto_id'] = le_proto.fit_transform(df['Protocol'])

# ৩. টার্গেট লেবেল তৈরি
threshold = 1000
counts = df['Source IP'].value_counts()
df['is_anomaly'] = df['Source IP'].apply(lambda x: 1 if counts[x] > threshold else 0)

# ৪. ফিচার এবং টার্গেট সেট করা
X = df[['src_id', 'dst_id', 'proto_id']]
y = df['is_anomaly']

# ৫. ডেটা ভাগ করা
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# ৬. Random Forest মডেল ট্রেনিং
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# ৭. রেজাল্ট দেখা
accuracy = model.score(X_test, y_test)
print(f"\nMODEL ACCURACY: {accuracy * 100:.2f}%")

# ৮. মডেল এবং এনকোডার সেভ করা (লুপের বাইরে রাখবেন)
joblib.dump(model, 'network_model.pkl')
joblib.dump(le_src, 'le_src.pkl') 
print("Model and Encoder saved successfully!")

# সন্দেহজনক আইপি শনাক্ত করা
suspicious_ips = df[df['is_anomaly'] == 1]['Source IP'].unique()
print(f"\n[ Detected Suspicious IPs ]")
for ip in suspicious_ips:
    print(f"⚠️ {ip}")