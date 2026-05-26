"""
Packet Sniffer Module

This module captures live network packets
and extracts packet information.
"""

from scapy.all import sniff
from scapy.layers.inet import IP

from services.detector import detect_suspicious_ip
from services.detector import detect_high_bandwidth
from services.detector import detect_unauthorized_ip

from datetime import datetime

import logging


# Configure logging
logging.basicConfig(

    filename="logs/threat_logs.txt",

    level=logging.ERROR,

    format="%(asctime)s - %(levelname)s - %(message)s"
)



def get_protocol_name(protocol_number):

    """
    Converts protocol number into readable protocol name.
    """

    if protocol_number == 6:
        return "TCP"

    elif protocol_number == 17:
        return "UDP"

    else:
        return "OTHER"



def process_packet(packet):

    """
    Processes captured packets.
    """

    try:

        # Check IP layer
        if packet.haslayer(IP):

            # Extract IP addresses
            source_ip = packet[IP].src
            destination_ip = packet[IP].dst

            # Packet size
            packet_size = len(packet)

            # Protocol number
            protocol_number = packet[IP].proto

            # Convert protocol number
            protocol = get_protocol_name(protocol_number)

            # Current timestamp
            current_time = datetime.now()

            # Display packet details
            print(f"Time: {current_time}")
            print(f"Source IP: {source_ip}")
            print(f"Destination IP: {destination_ip}")
            print(f"Packet Size: {packet_size}")
            print(f"Protocol: {protocol}")
            print("-----------------------------------")


            # Detect suspicious requests
            detect_suspicious_ip(
                source_ip,
                packet_size,
                protocol,
                current_time
            )

            # Detect high bandwidth
            detect_high_bandwidth(
                packet_size,
                source_ip,
                protocol,
                current_time
            )

            # Detect unauthorized access
            detect_unauthorized_ip(
                source_ip,
                packet_size,
                protocol,
                current_time
            )


    except Exception as error:

        logging.error(
            f"Packet processing error: {error}"
        )



def start_sniffing():

    """
    Starts live packet sniffing.
    """

    sniff(prn=process_packet, count=20)