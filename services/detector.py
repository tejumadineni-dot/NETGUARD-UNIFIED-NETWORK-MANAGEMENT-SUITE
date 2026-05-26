"""
Threat Detection Module

This module detects suspicious activities,
high bandwidth usage, and unauthorized access.
"""

from utils.logger import save_log
from utils.alerts import generate_alert

from config.config import MAX_PACKET_SIZE
from config.config import MAX_REQUEST_COUNT
from config.config import TRUSTED_IPS


# Store request counts
ip_count = {}



def detect_suspicious_ip(ip, packet_size, protocol, timestamp):

    """
    Detects repeated requests from same IP.
    """

    # Increase request count
    if ip in ip_count:
        ip_count[ip] += 1
    else:
        ip_count[ip] = 1


    # Threshold validation
    if ip_count[ip] > MAX_REQUEST_COUNT:

        threat_type = "Suspicious Activity"

        generate_alert(
            f"{threat_type} detected from IP: {ip}"
        )

        save_log(
            ip,
            packet_size,
            protocol,
            threat_type,
            timestamp
        )



def detect_high_bandwidth(packet_size, ip, protocol, timestamp):

    """
    Detects abnormal bandwidth usage.
    """

    # Check packet size threshold
    if packet_size > MAX_PACKET_SIZE:

        threat_type = "High Bandwidth Usage"

        generate_alert(
            f"{threat_type} detected from IP: {ip}"
        )

        save_log(
            ip,
            packet_size,
            protocol,
            threat_type,
            timestamp
        )



def detect_unauthorized_ip(ip, packet_size, protocol, timestamp):

    """
    Detects unauthorized IP access.
    """

    # Validate trusted IP list
    if ip not in TRUSTED_IPS:

        threat_type = "Unauthorized Access"

        generate_alert(
            f"{threat_type} detected from IP: {ip}"
        )

        save_log(
            ip,
            packet_size,
            protocol,
            threat_type,
            timestamp
        )