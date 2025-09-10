# Here we what happens when we inherit a constructor from parent and child also has it's own constructor

class University: # Super class
    def __init__(self):
        self.uname=input("Enter University Name:")
        self.ulocat=input("Enter University Location")
    
    def disUnidet(self):  
        print("University details:")
        print('-'*50) 
        print(f"University Name:{self.uname}")
        print(f"University Location:{self.ulocat}")
        print('-'*50)
    
class College(University): # College is a child class and University is it's Parent class
    def __init__(self): # Over-rides Parent constructor
        super().__init__()  # Call parent constructor # Implicitly calling Parent constructor
        self.colame=input("Enter College Name:")
        self.collocat=input("Enter College Location")
    
    def disColdet(self):
        self.disUnidet()  
        print("College details:")
        print('-'*50) 
        print(f"College Name:{self.colame}")
        print(f"College Location:{self.collocat}")
        print('-'*50)

c=College()
c.disColdet()