# In this eg. we will Multi-level inheritence

class University: # Super class
    def getUnidet(self):
        self.uname=input("Enter University Name:")
        self.ulocat=input("Enter University Location")
    
    def disUnidet(self):  
        print("University details:")
        print('-'*50) 
        print(f"University Name:{self.uname}")
        print(f"University Location:{self.ulocat}")
        print('-'*50)
    
class College(University): # College is a child class and University is it's Parent class
    def getColdet(self):
        self.getUnidet()
        self.colame=input("Enter College Name:")
        self.collocat=input("Enter College Location")
    
    def disColdet(self):
        self.disUnidet()  
        print("College details:")
        print('-'*50) 
        print(f"College Name:{self.colame}")
        print(f"College Location:{self.collocat}")
        print('-'*50)

class Student(College): # Here College is base class and Student is derived class
    # Since College itself is child class of University ,University is a super class for Student
    def getStddet(self):
        self.getColdet()
        self.stdame=input("Enter Student Name:")
        self.stdlocat=input("Enter Student Location")
    
    def disStddet(self):
        self.disColdet() 
        print("Student details:")
        print('-'*50) 
        print(f"Student Name:{self.stdame}")
        print(f"Student Location:{self.stdlocat}")
        print('-'*50)

s=Student()
s.getStddet()
s.disStddet()