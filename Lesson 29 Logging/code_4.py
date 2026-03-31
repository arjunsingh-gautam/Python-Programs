# Logging in a file using the logging module
import logging
import os
os.chdir(r"d:\Desktop\Python_Programs\Lesson 29 Logging")
logging.basicConfig(filename='demo.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
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
logging.debug(f"Adding {num1} and {num2}: {add(num1, num2)}")
logging.debug(f"Subtracting {num2} from {num1}: {subtract(num1  , num2)}")
logging.debug(f"Multiplying {num1} and {num2}: {multiply(num1   , num2)}")              
logging.debug(f"Dividing {num1} by {num2}: {divide(num1, num2)}")
logging.debug(f"Dividing {num1} by 0: {divide(num1, 0)}")