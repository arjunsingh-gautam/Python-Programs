# Fixing the issue of using root logger by creating a custom logger in each module and using that instead of the root logger

import logging
import os
import code_5 # Importing code_5 to show that it uses a different logger and does not interfere with the logging in this module
os.chdir(r"d:\Desktop\Python_Programs\Lesson 29 Logging")

# Create a custom logger for this module
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
# Create a file handler for this logger
file_handler = logging.FileHandler('demo3.log')
# Create a formatter and set it for the file handler
formatter = logging.Formatter('%(name)s:%(asctime)s -%(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
# Add the file handler to the logger    
logger.addHandler(file_handler)

def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    if b == 0:
        logger.error("Division by zero attempted")
        return None
    return a / b
num1 = 10
num2 = 5
logger.debug(f"Adding {num1} and {num2}: {add(num1, num2)}")
logger.debug(f"Subtracting {num2} from {num1}: {subtract(num1, num2)}")
logger.debug(f"Multiplying {num1} and {num2}: {multiply(num1, num2)}")
logger.debug(f"Dividing {num1} by {num2}: {divide(num1, num2)}")
logger.debug(f"Dividing {num1} by 0: {divide(num1, 0)}")