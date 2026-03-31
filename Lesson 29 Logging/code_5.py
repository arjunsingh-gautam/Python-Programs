# Adding logging to a Python program using the logging module
import logging
import os
os.chdir(r"d:\Desktop\Python_Programs\Lesson 29 Logging")
logging.basicConfig(filename="demo2.log",level=logging.DEBUG,format='%(name)s:%(asctime)s - %(levelname)s - %(message)s')

class Employee:
    def __init__(self, name, age):
        self._name = name
        self.age = age
        logging.info(f"Employee created: {self.name}, Age: {self.age}")

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value):
        logging.info(f"Changing name from {self._name} to {value}")
        self._name = value
    def work(self):
        logging.info(f"{self.name} is working.")
emp1 = Employee("Alice", 30)
emp1.name = "Alice Smith"
emp1.work()