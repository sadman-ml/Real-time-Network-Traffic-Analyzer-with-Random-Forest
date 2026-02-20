**Real-time Network IDS (Random Forest)**
This project is a machine learning-based Intrusion Detection System (IDS) that analyzes live network traffic to identify anomalies.

**Key Highlights**
Model: Powered by Random Forest Classifier, achieving 100% test accuracy.
Real-time Alerts: Features an integrated Audio Beep system for immediate threat notification.
EDA: Dynamic visualization of Protocol distribution and Source IP frequency.
Live Analysis: Successfully analyzed 9,400+ live packets (TCP, UDP, IGMP).

**Methodology**
Based on the systematic approach from my paper:
Data Capture: main.py 
EDA & Visualization: plot_data.py 
Model Training: train_ml.py 
Live Monitoring: alert_system.py

**Related Research**
My work on this Network IDS is fundamentally grounded in my published research:
Title: Fraud and Money Laundering Pattern Detection Using Logistic Regression, Random Forest, and XGBoost 
DOI: https://doi.org/10.5281/zenodo.17984808


**Abstract Summary:**
This study analyzed over 6.3 million transactions to evaluate machine learning models.It demonstrated that ensemble approaches, specifically Random Forest and XGBoost, 
are more effective than Logistic Regression in detecting rare anomalies within imbalanced datasets.
