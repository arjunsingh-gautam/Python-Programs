# In this module we will learn about deserialisation in Python using pickle module
import pickle_1
import pickle
import os
os.chdir("d:/Desktop/Python_Programs/Lesson 23 File_Handling/Code/files")
with open(os.path.abspath('person.pkl'),'rb') as f:  # 'rb' for reading binary, automatically closes file
    p1=pickle.load(f)  # deserialize binary data from file to person object     

print(p1)  # print the deserialized person object
print(type(p1))  # print the type of the deserialized object (should be Person)
print(p1.name)  # access attributes of the deserialized object
print(p1.age)
print(dir(p1))  # print the attributes and methods of the deserialized object
print(p1.__class__)  # print the class of the deserialized object
print(p1.__class__.__name__)  # print the name of the class of the deserialized object
print(pickle_1.Person("Bob",25))  # create a new person object using the Person class from pickle_1 module
