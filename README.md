NetGuard - Unified Network Management Suite

Overview

NetGuard is a Python-based network monitoring and threat detection system designed to identify suspicious network activities, monitor bandwidth usage, detect unauthorized access, and provide centralized alert management through REST APIs and a monitoring dashboard.

The project consists of two major modules:

- Threat Detection Bot
- Network Health API

---

Project Architecture

Threat Detection Bot
↓
Flask REST API
↓
SQLite Database
↓

Dashboard & Swagger UI

---

Technologies Used

- Python
- Flask
- SQLite
- Scapy
- Requests
- Flasgger (Swagger)
- HTML
- CSS

---

  - Threat Detection Bot

Features

- Live Packet Monitoring
- Suspicious Activity Detection
- High Bandwidth Detection
- Unauthorized Access Detection
- Alert Generation
- Threat Logging
- Unit Testing
- API Integration

Project Structure

threat_detection_bot/

├── config/
│   └── config.py
│
├── logs/
│   └── threat_logs.txt
│
├── services/
│   ├── detector.py
│   └── packet_sniffer.py
│
├── tests/
│   └── test_detector.py
│
├── utils/
│   ├── alerts.py
│   └── logger.py
│
└── main.py

Detection Rules

Suspicious Activity

Detects repeated requests from the same IP address.

Condition:

Request Count > MAX_REQUEST_COUNT

High Bandwidth Usage

Detects unusually large packets.

Condition:

Packet Size > MAX_PACKET_SIZE

Unauthorized Access

Detects requests from untrusted IP addresses.

Condition:

IP NOT IN TRUSTED_IPS

---

  - Network Health API

Features

- REST API Development
- SQLite Database Integration
- CRUD Operations
- Search Alerts by IP
- Network Health Summary
- Swagger Documentation
- Monitoring Dashboard

Project Structure

network_health_api/

├── app.py
├── database.py
├── routes.py
├── network_history.db
├── requirements.txt
│
├── templates/
│   └── dashboard.html
│
└── static/
    └── style.css

---

Database Schema

Table Name:

alerts

Columns:

Column| Description
id| Alert ID
ip| Source IP Address
threat_type| Type of Threat
bandwidth| Packet Size
timestamp| Detection Time

---

API Endpoints

Create Alert

POST /alerts

Stores a new alert.

---

Get All Alerts

GET /alerts

Returns all alerts.

---

Get Alert By ID

GET /alerts/<alert_id>

Returns a specific alert.

---

Update Alert

PUT /alerts/<alert_id>

Updates an alert.

---

Delete Alert

DELETE /alerts/<alert_id>

Deletes an alert.

---

Search Alert By IP

GET /alerts/ip/<ip>

Returns alerts matching the given IP address.

---

Network Health Summary

GET /network-health

Returns current network monitoring status.

---

Dashboard

GET /dashboard

Displays alert statistics and threat history.

---

Dashboard Features

- Navigation Bar
- Network Status Indicator
- Total Alerts Counter
- Unauthorized Access Counter
- High Bandwidth Counter
- Suspicious Activity Counter
- Threat Alert History Table

---

Swagger Documentation

Swagger UI is integrated using Flasgger for API testing and documentation.

URL:

http://127.0.0.1:5000/apidocs

---

Installation

Install Dependencies

pip install -r requirements.txt

Create Database

python database.py

Run Network Health API

python app.py

Run Threat Detection Bot

python main.py

Run Unit Tests

python tests/test_detector.py

---

Sample Workflow

1. Network packets are captured.
2. Threat Detection Bot analyzes packets.
3. Suspicious activities are detected.
4. Alerts are generated.
5. Alerts are sent to the REST API.
6. API stores alert data in SQLite.
7. Dashboard displays alert information.
8. Swagger provides API documentation and testing.

---

Future Enhancements

- Real-Time Threat Analytics
- Advanced Search Filters
- Threat Visualization Charts
- CSV Export Functionality
- Authentication and Authorization
- Email Notifications

---

Conclusion

NetGuard provides an end-to-end network monitoring solution that combines packet analysis, threat detection, alert management, API services, database storage, and dashboard visualization into a single unified platform.