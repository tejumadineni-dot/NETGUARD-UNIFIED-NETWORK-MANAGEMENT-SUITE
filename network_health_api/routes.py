# Import required Flask modules
from flask import Blueprint, request, jsonify, render_template

# Import SQLite database library
import sqlite3


# Create Blueprint
api_routes = Blueprint('api_routes', __name__)


# Database file name
DB_NAME = "network_history.db"


# =====================================================
# CREATE ALERT
# =====================================================
@api_routes.route('/alerts', methods=['POST'])
def create_alert():

    """
    Create a new alert
    ---
    tags:
      - Alerts
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            ip:
              type: string
            threat_type:
              type: string
            bandwidth:
              type: string
            timestamp:
              type: string
    responses:
      200:
        description: Alert stored successfully
    """

    # Get JSON request data
    data = request.json

    # Connect to database
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    # Insert alert record
    cursor.execute("""
        INSERT INTO alerts(
            ip,
            threat_type,
            bandwidth,
            timestamp
        )
        VALUES (?, ?, ?, ?)
    """, (
        data['ip'],
        data['threat_type'],
        data['bandwidth'],
        data['timestamp']
    ))

    # Save changes
    conn.commit()

    # Close connection
    conn.close()

    return jsonify({
        "message": "Alert Stored Successfully"
    })


# =====================================================
# GET ALL ALERTS
# =====================================================
@api_routes.route('/alerts', methods=['GET'])
def get_alerts():

    """
    Get all alerts
    ---
    tags:
      - Alerts
    responses:
      200:
        description: List of all alerts
    """

    # Connect database
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    # Fetch all alerts
    cursor.execute("SELECT * FROM alerts")

    rows = cursor.fetchall()

    conn.close()

    return jsonify(rows)


# =====================================================
# GET SINGLE ALERT
# =====================================================
@api_routes.route('/alerts/<int:alert_id>', methods=['GET'])
def get_single_alert(alert_id):

    """
    Get single alert by ID
    ---
    tags:
      - Alerts
    parameters:
      - name: alert_id
        in: path
        type: integer
        required: true
    responses:
      200:
        description: Single alert details
    """

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    # Fetch alert by ID
    cursor.execute(
        "SELECT * FROM alerts WHERE id=?",
        (alert_id,)
    )

    row = cursor.fetchone()

    conn.close()

    return jsonify(row)


# =====================================================
# UPDATE ALERT
# =====================================================
@api_routes.route('/alerts/<int:alert_id>', methods=['PUT'])
def update_alert(alert_id):

    """
    Update alert by ID
    ---
    tags:
      - Alerts
    parameters:
      - name: alert_id
        in: path
        type: integer
        required: true
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            ip:
              type: string
            threat_type:
              type: string
            bandwidth:
              type: string
            timestamp:
              type: string
    responses:
      200:
        description: Alert updated successfully
    """

    # Read request data
    data = request.json

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    # Update alert record
    cursor.execute("""
        UPDATE alerts
        SET
            ip=?,
            threat_type=?,
            bandwidth=?,
            timestamp=?
        WHERE id=?
    """, (
        data['ip'],
        data['threat_type'],
        data['bandwidth'],
        data['timestamp'],
        alert_id
    ))

    conn.commit()
    conn.close()

    return jsonify({
        "message": "Alert Updated Successfully"
    })


# =====================================================
# DELETE ALERT
# =====================================================
@api_routes.route('/alerts/<int:alert_id>', methods=['DELETE'])
def delete_alert(alert_id):

    """
    Delete alert by ID
    ---
    tags:
      - Alerts
    parameters:
      - name: alert_id
        in: path
        type: integer
        required: true
    responses:
      200:
        description: Alert deleted successfully
    """

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    # Delete alert
    cursor.execute(
        "DELETE FROM alerts WHERE id=?",
        (alert_id,)
    )

    conn.commit()
    conn.close()

    return jsonify({
        "message": "Alert Deleted Successfully"
    })


# =====================================================
# SEARCH ALERTS BY IP
# =====================================================
@api_routes.route('/alerts/ip/<ip>', methods=['GET'])
def search_by_ip(ip):

    """
    Search alerts by IP
    ---
    tags:
      - Alerts
    parameters:
      - name: ip
        in: path
        type: string
        required: true
    responses:
      200:
        description: Matching alerts
    """

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    # Search alerts using IP
    cursor.execute(
        "SELECT * FROM alerts WHERE ip=?",
        (ip,)
    )

    rows = cursor.fetchall()

    conn.close()

    return jsonify(rows)


# =====================================================
# NETWORK HEALTH SUMMARY
# =====================================================
@api_routes.route('/network-health', methods=['GET'])
def network_health():

    """
    Get network health summary
    ---
    tags:
      - Network Health
    responses:
      200:
        description: Network health summary
    """

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    # Count total alerts
    cursor.execute("SELECT COUNT(*) FROM alerts")
    total_alerts = cursor.fetchone()[0]

    conn.close()

    return jsonify({
        "total_alerts": total_alerts,
        "status": "Network Monitoring Active"
    })


# =====================================================
# DASHBOARD UI
# =====================================================
@api_routes.route('/dashboard')
def dashboard():

    # Connect database
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    # Get all alerts
    cursor.execute("SELECT * FROM alerts")
    alerts = cursor.fetchall()

    # Total alerts count
    cursor.execute("SELECT COUNT(*) FROM alerts")
    total_alerts = cursor.fetchone()[0]

    # Unauthorized access count
    cursor.execute(
        "SELECT COUNT(*) FROM alerts WHERE threat_type='Unauthorized Access'"
    )
    unauthorized_count = cursor.fetchone()[0]

    # High bandwidth count
    cursor.execute(
        "SELECT COUNT(*) FROM alerts WHERE threat_type='High Bandwidth Usage'"
    )
    high_bandwidth_count = cursor.fetchone()[0]

    # Suspicious activity count
    cursor.execute(
        "SELECT COUNT(*) FROM alerts WHERE threat_type='Suspicious Activity'"
    )
    suspicious_count = cursor.fetchone()[0]

    conn.close()

    # Load dashboard page
    return render_template(
        "dashboard.html",
        alerts=alerts,
        total_alerts=total_alerts,
        unauthorized_count=unauthorized_count,
        high_bandwidth_count=high_bandwidth_count,
        suspicious_count=suspicious_count
    )


# =====================================================
# SEARCH ALERTS FOR DASHBOARD
# =====================================================
@api_routes.route('/search/<ip>')
def search_dashboard(ip):

    # Connect database
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    # Search by IP
    cursor.execute(
        "SELECT * FROM alerts WHERE ip=?",
        (ip,)
    )

    alerts = cursor.fetchall()

    conn.close()

    return jsonify(alerts)