# NetGuard – Threat Detection Bot

## Project Overview

NetGuard is a Python-based Threat Detection Bot developed as part of the Unified Network Management Suite. The system monitors live network traffic, captures packets, analyzes traffic behavior, detects suspicious activities, generates alerts, and stores threat logs for security analysis.

---

# Features

- Real-time packet sniffing
- Source and destination IP extraction
- Protocol identification
- Packet size monitoring
- Suspicious IP detection
- High bandwidth detection
- Unauthorized IP detection
- Alert generation
- Threat logging
- Modular architecture

---

# Technologies Used

- Python
- Scapy
- File Handling
- Modular Programming

---

# Project Structure

```plaintext
NetGuard/
│
├── main.py
├── packet_sniffer.py
├── detector.py
├── alerts.py
├── logger.py
├── config.py
├── threat_logs.txt
└── README.md
```

---

# Module Description

## main.py
Starts the application and initializes packet monitoring.

## packet_sniffer.py
Captures live network packets and extracts:
- Source IP
- Destination IP
- Packet Size
- Protocol
- Timestamp

## detector.py
Performs threat analysis and threat detection.

### Detection Features
- Suspicious IP Detection
- High Bandwidth Detection
- Unauthorized IP Detection

## alerts.py
Generates alert messages for detected threats.

## logger.py
Stores threat logs into `threat_logs.txt`.

## config.py
Stores threshold values and trusted IP configurations.

---

# Detection Logic

## Test Case 1 – Suspicious IP Detection
If the same IP sends repeated packets more than the configured threshold, the system generates an alert.

## Test Case 2 – High Bandwidth Detection
If packet size exceeds the configured threshold, the system identifies abnormal traffic behavior.

## Test Case 3 – Unauthorized IP Detection
If traffic is detected from an unknown IP address, the system generates an unauthorized access alert.

---

# How to Run the Project

## Step 1
Install required library:

```bash
pip install scapy
```

## Step 2
Run the project:

```bash
python main.py
```

---

# Sample Output

```plaintext
Time: 2026-05-19 19:10:20
Source IP: 192.168.55.103
Destination IP: 142.x.x.x
Packet Size: 1200
Protocol: TCP

[ALERT] High bandwidth usage detected from IP: 192.168.55.103
```

---

# Threat Log Example

```plaintext
2026-05-19 19:10:20 - Threat detected from IP: 192.168.55.103
```

---

# Future Enhancements

- GUI dashboard integration
- Email alert notifications
- Database log storage
- Machine learning-based anomaly detection
- Real-time monitoring dashboard

---

# Conclusion

NetGuard provides a lightweight and modular threat detection system capable of monitoring live network traffic and identifying suspicious activities in real time.