# Writing to a json file using the json module
import json
import os
os.chdir("d:/Desktop/Python_Programs/Lesson 23 File_Handling/json_programs")
with open('states.json', 'r') as file:
    data = json.load(file) # load the data from the file
    for state in data['states']:
        del state['area_codes'] # delete the population key from each state 
with open('states_copy.json', 'w') as file:
    json.dump(data, file, indent=4) # write the data to the file with indentation