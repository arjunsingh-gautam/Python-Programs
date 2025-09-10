# In this code we will learn about static method in Python

class Student:
    def get_std_data(self):
        self.name=input("Enter Student Name:")
        self.prn=int(input("Enter Student PRN:"))

class Employee:
    def get_emp_data(self):
        self.empname=input("Enter Employee Name:")
        self.empid=int(input("Enter Employee ID:"))

class Disp:
    @staticmethod # staticmethod
    def display(obj,objinfo):
        print("-"*50)   
        print(f"{objinfo} Information:")
        for k,v in obj.__dict__.items():
            print(f"{objinfo} {k}:{v}")

s= Student()
e=Employee()
s.get_std_data()
e.get_emp_data()

Disp.display(s,"Student")

d=Disp()
d.display(e,"Employee")