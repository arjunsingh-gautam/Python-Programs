# implementing Pydantic 
from pydantic import BaseModel,ValidationError
from datetime import datetime
import os
import json

class User(BaseModel):
    username:str
    user_id:int
    verified_at:datetime | None = None
    email:str
    bio:str = ""
    is_active:bool = True
    fullname:str|None = None
    
user_1=User(username="arjdev",user_id=123,email="arj123@gmail.com")
print(user_1)

print(f"Username:{user_1.username}") 

# Dumping model as dictionary: this serialises the model to dict object
user_dict=user_1.model_dump()
print(user_dict)

# Serialising the model to json and storing the json
os.chdir(r"D:\Desktop\Python_Programs\Lesson 33 Pydantic\Code\data")
print("Writing User to json file")
with open("demo.json","w") as f:
    json.dump(user_1.model_dump_json(indent=2),f)
    
print("Writing Done")
