# In this code we will see how we can parameterised and default constructor using defaul arguments

class Student:
    def __init__(self,sname='DefaultValue',sno=0):
        self.sname=sname
        self.sno=sno
    
    def get_value(self):
        print('-'*50)
        print("Student Details:")
        print('-'*50)
        print(f"Student Name:{self.sname}")
        print(f"Student PRN:{self.sno}")

s1=Student() # default constructor behavior
s2=Student("Arjun",22070123043) # Parameterised constructor behavior 
s1.get_value()
s2.get_value()