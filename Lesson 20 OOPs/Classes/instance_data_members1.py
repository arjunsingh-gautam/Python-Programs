# In this code we will how we can store instance attributes of an object using object name

class Student:
    pass

s1=Student()
s2=Student()

print('-'*50)
print(f"Address of s1:{id(s1)}")
print(f"Address of s2:{id(s2)}")
print('-'*50)

s1.name="Bhoumik"
s1.age=20


s2.name="Ashish"
s2.age=21

print("s1 Student details:")
print(s1.__dict__)

print('-'*50)
print("s2 Student details:")
print(s2.__dict__) # __dict__ is a dunder attribute : predefined attribute