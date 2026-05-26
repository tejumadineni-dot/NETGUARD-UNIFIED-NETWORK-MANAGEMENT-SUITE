"""
NetGuard - Threat Detection Bot
Main Entry File
"""

from services.packet_sniffer import start_sniffing


print("===================================")
print(" NETGUARD - THREAT DETECTION BOT ")
print("===================================")

print("Initializing System...")
print("Starting Network Monitoring...")
print("-----------------------------------")


# Start live packet monitoring
start_sniffing()