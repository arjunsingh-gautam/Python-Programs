# In this code we will understand complete boilerplate of a class with a simple eg.

class Student:

    school_name="DPS" # class attribute

    def __init__(self,name,grade): # Constructor Initialises instance variables when object is created ,no need to call explicitly
        self.name=name
        self.grade=grade

    def show_grade(self): # Instance Method
        print(f"{self.name} is in grade:{self.grade}")

    @classmethod # class method
    def get_school_name(cls):
        print(f"School name is {cls.school_name}")
    
    @staticmethod # static method
    def greet():
        print("Hello")

    def __del__(self): # Destructor
        print(f"Destroy object with name:{self.name}")


s1=Student("Arjun",10)  
s1.show_grade()
Student.get_school_name()
Student.greet()