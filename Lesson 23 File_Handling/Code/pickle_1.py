# In this module we will learn about serialisation in Python using pickle module
import pickle
import os
os.chdir("d:/Desktop/Python_Programs/Lesson 23 File_Handling/Code/files")
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):
        return f"Person(name={self.name}, age={self.age})"
    
p1=Person("Alice",30)
with open(os.path.abspath('person.pkl'),'wb') as f:  # 'wb' for writing binary, automatically closes file
    pickle.dump(p1,f)  # serialize person object to binary and write to file
