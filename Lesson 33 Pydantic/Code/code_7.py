# basic data validation using Pydantic

from pydantic import BaseModel,Field

class User(BaseModel):
    name:str
    age:int
    
user_1=User(name="John",age=18)
user_2=User(name="Annie",age="25") # Here Pydanctic itself implicitly convert age "25" to integer
#user_3=User(name="Max",age="old") # ValidationError

print(user_1)
print(user_2)
#print(user_3)