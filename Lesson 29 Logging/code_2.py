# Logging using the logging module

# Logging levels: DEBUG, INFO, WARNING, ERROR, CRITICAL
# Debug: Detailed information, typically of interest only when diagnosing problems.
# Info: Confirmation that things are working as expected.
# Warning: An indication that something unexpected happened, or indicative of some problem in the near future (e.g., ‘disk space low’). The software is still working as expected.
# Error: Due to a more serious problem, the software has not been able to perform some
# Critical: A serious error, indicating that the program itself may be unable to continue running.

import logging

def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    if b == 0:
        logging.error("Division by zero attempted")
        return None
    return a / b

num1 = 10
num2 = 5
logging.info(f"Adding {num1} and {num2}: {add(num1, num2)}")
logging.warning(f"Subtracting {num2} from {num1}: {subtract(num1, num2)}")
logging.debug(f"Multiplying {num1} and {num2}: {multiply(num1, num2)}")
logging.info(f"Dividing {num1} by {num2}: {divide(num1, num2)}")
logging.info(f"Dividing {num1} by 0: {divide(num1, 0)}")    