# Serialisation of custom objects in Python using json module
import json
import os
os.chdir("d:/Desktop/Python_Programs/Lesson 23 File_Handling/Code/files")
class Person:
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
person=Person("Alice",30,"Female")
class Animal:
    def __init__(self,name,species):
        self.name=name
        self.species=species
dog=Animal("Buddy","Dog")

# Custom function to convert Person object to a dictionary for JSON serialization
def person_to_dict(obj):
    if isinstance(obj,Person):
        return {'name':obj.name,'age':obj.age,'gender':obj.gender}
    raise TypeError("Object is not JSON serializable")

with open(os.path.abspath('person.json'),'w') as f:  # 'w' for writing, automatically closes file
    json.dump(person,f,default=person_to_dict)  # serialize person object to JSON and write to file 

with open(os.path.abspath('animal.json'),'w') as f:  # 'w' for writing, automatically closes file
    json.dump(dog,f,default=person_to_dict)  # object is not JSON serializable, will raise TypeError and be caught by default handler, which will write null to file