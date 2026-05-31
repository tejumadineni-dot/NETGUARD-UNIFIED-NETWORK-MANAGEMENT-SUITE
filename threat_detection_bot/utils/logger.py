"""
Logger Module

This module stores threat details
and logs exceptions.
"""

import logging


# Configure logging
logging.basicConfig(

    filename="logs/threat_logs.txt",

    level=logging.ERROR,

    format="%(asctime)s - %(levelname)s - %(message)s"
)



def save_log(ip, packet_size, protocol, threat_type, timestamp):

    """
    Saves detected threat information.
    """

    try:

        with open("logs/threat_logs.txt", "a") as file:

            log_message = (
                f"\nTime: {timestamp}\n"
                f"Threat Type: {threat_type}\n"
                f"IP Address: {ip}\n"
                f"Packet Size: {packet_size}\n"
                f"Protocol: {protocol}\n"
                f"-----------------------------------\n"
            )

            file.write(log_message)


    except Exception as error:

        logging.error(
            f"Error while saving log: {error}"
        )