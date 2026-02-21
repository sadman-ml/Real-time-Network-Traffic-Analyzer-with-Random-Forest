"""Network Intrusion Detection Project
Student Version.
Steps:
1. Load Data
2. Clean Data
3. Encode Categorical Features
4. Create Anomaly Label
5. Prepare Data (Train-Test Split)
6. Train Random Forest Model
7. Evaluate Model
8. Save Model
9. Display Suspicious IPs
"""

import pandas as pd
import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import classification_report, confusion_matrix

# =========================
# 1. Load Dataset
# =========================

try:
    df = pd.read_csv("network_log.csv")
    print("Dataset loaded successfully☺️.")
except FileNotFoundError:
    print("File not found⚠️")
    exit()

# =========================
# 2. Data Cleaning
# =========================
# Remove rows with missing important values.

df = df.dropna(subset=["Source IP", "Destination IP", "Protocol"])
df = df.reset_index(drop=True)

print("Data cleaned successfully.")

# =========================
# 3. Feature Engineering
# =========================
# Machine learning models cannot understand text,
# so we convert IP addresses and protocol into numbers.

le_source = LabelEncoder()
le_destination = LabelEncoder()
le_protocol = LabelEncoder()

df["source_id"] = le_source.fit_transform(df["Source IP"])
df["destination_id"] = le_destination.fit_transform(df["Destination IP"])
df["protocol_id"] = le_protocol.fit_transform(df["Protocol"])

print("Feature encoding completed.")

# =========================
# 4. Create Target Label
# =========================
# If a source IP appears more than 1000 times,
# we consider it suspicious.

THRESHOLD = 1000
ip_counts = df["Source IP"].value_counts()

df["is_anomaly"] = df["Source IP"].map(
    lambda ip: 1 if ip_counts[ip] > THRESHOLD else 0
)

print("Anomaly labels created.")

# Check class distribution
print("\nClass Distribution:")
print(df["is_anomaly"].value_counts())

# =========================
# 5. Prepare Data
# =========================

X = df[["source_id", "destination_id", "protocol_id"]]
y = df["is_anomaly"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# =========================
# 6. Train Model
# =========================

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42,
    class_weight="balanced"
)

model.fit(X_train, y_train)
print("Model training completed.")

# =========================
# 7. Evaluate Model
# =========================
y_pred = model.predict(X_test)

accuracy = model.score(X_test, y_test)

print("\nModel Evaluation:")
print(f"Accuracy: {accuracy * 100:.2f}%")

print("\nClassification Report:")
print(classification_report(y_test, y_pred))


print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

print("\nNote: High recall for anomaly class is critical in Intrusion Detection.")

# =========================
# Feature Importance
# =========================

print("\nFeature Importance:")
for name, importance in zip(X.columns, model.feature_importances_):
    print(f"{name}: {importance:.4f}")
    
# =========================
# 8. Save Model
# =========================
joblib.dump(model, "network_model.pkl")
print("Model saved successfully.")

# =========================
# 9. Show Suspicious IPs
# =========================
suspicious_ips = df[df["is_anomaly"] == 1]["Source IP"].unique()

print("\nDetected Suspicious IPs:")
for ip in suspicious_ips:
    print(f"⚠️ {ip}")
