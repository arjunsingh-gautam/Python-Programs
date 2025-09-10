class Student:
    def __init__(self,x,y,z):
        self.name=x
        self.rollno=y
        self.marks=z
    def talk(self):
        print("My name is ",self.name)
        print("My roll no is ",self.rollno)
        print("My marks is ",self.marks)

s1=Student("Sunny",138,83) # here a new object is created in Heap Space referred by s1 in namespace
s2=Student("Bunnt",128,92) # here a new object is created in Heap Space referred by s2 in namespace
# When object is created contructor->__init__ method get called simultaneously and variables are being initialised
print("Student-1:",s1.name,s1.rollno,s1.marks)
print("Student-2:",s2.name,s2.rollno,s2.marks)