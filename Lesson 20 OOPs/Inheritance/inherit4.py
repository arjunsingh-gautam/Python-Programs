# In this code we will see Multi-Level Inheritence

class University: # University is also a Base class
    def getUnidet(self):
        self.uname=input("Enter University Name:")
        self.ulocat=input("Enter University Location")
    
    def disUnidet(self):  
        print("University details:")
        print('-'*50) 
        print(f"University Name:{self.uname}")
        print(f"University Location:{self.ulocat}")
        print('-'*50)
    
class College(): # College is a Base class
    def getColdet(self):
        self.colame=input("Enter College Name:")
        self.collocat=input("Enter College Location")
    
    def disColdet(self): 
        print("College details:")
        print('-'*50) 
        print(f"College Name:{self.colame}")
        print(f"College Location:{self.collocat}")
        print('-'*50)

class Student(University,College): # Here College and University both are independent base classes and Student is derived class having properties of both base classes
    
    def getStddet(self):
        self.getUnidet()
        self.getColdet()
        self.stdame=input("Enter Student Name:")
        self.stdlocat=input("Enter Student Location")
    
    def disStddet(self):
        self.disUnidet()
        self.disColdet() 
        print("Student details:")
        print('-'*50) 
        print(f"Student Name:{self.stdame}")
        print(f"Student Location:{self.stdlocat}")
        print('-'*50)

s=Student()
s.getStddet()
s.disStddet()