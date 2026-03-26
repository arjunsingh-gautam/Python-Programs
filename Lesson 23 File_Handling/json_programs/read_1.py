# Reading a json string using the json module
import json
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
print(data)

for person in data['people']:
    print(person)

for person in data['people']:
    print(person['name'], person['age'], person['city'])