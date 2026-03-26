# Writing a python object to json string using the json module
import json
import os
os.chdir("d:/Desktop/Python_Programs/Lesson 23 File_Handling/json_programs")
json_string = '''
{
    "people":[
        {"name": "John", "age": 30, "city": "New York"
        },
        {"name": "Jane", "age": 25, "city": "Los Angeles"
        }
    ]
}
'''
data = json.loads(json_string)

for person in data['people']:
    del person['age'] # delete the age key from the person dictionary

new_json_string = json.dumps(data, indent=4) # convert the python object back to a json string with indentation
print(new_json_string)