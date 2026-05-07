# Error Handling in Python
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
    

try:
    user_1=User(username=None,user_id="123",email="arj123@gmail.com")
except ValidationError as e:
    print(e)
    
