# Deserialisation in Python using json module
import json
import os
os.chdir("d:/Desktop/Python_Programs/Lesson 23 File_Handling/Code/files")
with open(os.path.abspath('data.json'),'r') as f:  # 'r' for reading, automatically closes file
    data=json.load(f)  # deserialize JSON from file to Python object
print(data)  # print the deserialized data
print(type(data))  # print the type of the deserialized data (should be dict)