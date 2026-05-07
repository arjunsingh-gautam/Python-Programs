# Implementing dataclasses in Python

from dataclasses import dataclass

@dataclass
class User:
    name:str
    age:int
    email:str

user_1=User("John",23,"john@email.com")
user_2=User("Annie",12,"annie@yahoo.com")
print(user_1)
print(user_2)