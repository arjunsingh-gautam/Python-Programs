# Reading data from a json file using the json module
import json
import os
os.chdir("d:/Desktop/Python_Programs/Lesson 23 File_Handling/json_programs")
with open('states.json', 'r') as file:
    data = json.load(file) # load the data from the file
    print(data)
    print(type(data)) # check the type of the data

    print(50*'-')
    for state in data['states']:
        print(state)