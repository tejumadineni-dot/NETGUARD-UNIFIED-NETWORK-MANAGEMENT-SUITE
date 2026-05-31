"""
Unit Test Module

This file tests threat detection scenarios.
"""

import sys
import os


# Add project root path
sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), '..')
    )
)


from services.detector import detect_suspicious_ip
from services.detector import detect_high_bandwidth
from services.detector import detect_unauthorized_ip

from datetime import datetime


print("===================================")
print(" RUNNING UNIT TEST CASES ")
print("===================================")


# Common test values
test_time = datetime.now()

test_protocol = "TCP"



# -----------------------------------
# Test Case 1
# Suspicious Activity Detection
# -----------------------------------

print("\nTest Case 1 - Suspicious Activity Detection")


# Calling method multiple times
for i in range(7):

    detect_suspicious_ip(
        "192.168.1.100",
        500,
        test_protocol,
        test_time
    )

print("Test Case 1 Completed")



# -----------------------------------
# Test Case 2
# High Bandwidth Detection
# -----------------------------------

print("\nTest Case 2 - High Bandwidth Detection")


detect_high_bandwidth(
    2000,
    "192.168.1.101",
    test_protocol,
    test_time
)

print("Test Case 2 Completed")



# -----------------------------------
# Test Case 3
# Unauthorized Access Detection
# -----------------------------------

print("\nTest Case 3 - Unauthorized Access Detection")


detect_unauthorized_ip(
    "10.10.10.10",
    700,
    test_protocol,
    test_time
)

print("Test Case 3 Completed")



print("\n===================================")
print(" ALL TEST CASES EXECUTED ")
print("===================================")