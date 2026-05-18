from datetime import datetime
from pydantic import BaseModel,ConfigDict,EmailStr,Field

class UserBase(BaseModel):
    username:str=Field(min_length=1,max_length=50)
    email:EmailStr=Field(min_length=1,max_length=120)
    
class UserCreate(UserBase):
    pass

class UserResponse(UserBase):
    model_config=ConfigDict(from_attributes=True)
    id:int
    
class NoteBase(BaseModel):
    content:str=Field(min_length=1)
    title:str=Field(min_length=1,max_length=50)
    
    
class NoteCreate(NoteBase):
    user_id:int

class NoteResponse(NoteBase):
    model_config=ConfigDict(from_attributes=True)
    id:int
    user_id:int
    date_posted:datetime
    author:UserResponse