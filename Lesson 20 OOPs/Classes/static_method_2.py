# In this program we will see one of the method to access static method using self inside instance method

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
    
    def call_static(self,obj,objinfo):
        self.display(obj,objinfo) # calling static method wrt. self

s= Student()
e=Employee()
s.get_std_data()
e.get_emp_data()


d1=Disp()
d2=Disp()
d1.call_static(e,"Employee") # calling static method wrt instance_method
d2.call_static(s,"Student")
