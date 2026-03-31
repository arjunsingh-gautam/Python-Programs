# Creating a logger in a module and using it in another module by importing the first module into the second module

import logging
import os
os.chdir(r"d:\Desktop\Python_Programs\Lesson 29 Logging")
# Create a logger for this module
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
# Create a file handler for this logger
file_handler = logging.FileHandler('demo4.log') 
# Create a formatter and set it for the file handler
formatter = logging.Formatter('%(name)s:%(asctime)s - %(levelname)s - %(message)s')
file_handler.setLevel(logging.ERROR)
file_handler.setFormatter(formatter)   
# Add the file handler to the logger
logger.addHandler(file_handler) 
# Creating a stream handler to also log to the console
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.DEBUG)
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)

def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        logger.exception("Division by zero attempted")
        
num1 = 10
num2 = 5
logger.debug(f"Adding {num1} and {num2}: {add(num1, num2)}")
logger.debug(f"Subtracting {num2} from {num1}: {subtract(num1, num2)}")
logger.debug(f"Multiplying {num1} and {num2}: {multiply(num1, num2)}")
logger.debug(f"Dividing {num1} by {num2}: {divide(num1, num2)}")
logger.debug(f"Dividing {num1} by 0: {divide(num1, 0)}")