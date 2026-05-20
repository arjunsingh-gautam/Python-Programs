from pydantic import BaseModel,Field,ConfigDict

class UserBase(BaseModel):
    id:int
    name:str=Field(min_length=1,max_length=50)
    
class UserResponse(UserBase):
    pass

class UserCreate(UserBase):
    pass