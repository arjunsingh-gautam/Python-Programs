# Serialisation in Python using json module
import json
import os
os.chdir("d:/Desktop/Python_Programs/Lesson 23 File_Handling/Code/files")
data={'name':'Alice','age':30,'city':'New York'}    
with open(os.path.abspath('data.json'),'w') as f:  # 'w' for writing, automatically closes file
    json.dump(data,f)  # serialize data to JSON and write to file