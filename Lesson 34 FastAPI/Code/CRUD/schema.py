from pydantic import BaseModel,Field,ConfigDict

class StudentBase(BaseModel):
    name:str=Field(min_length=1,max_length=50)
    
class StudentCreate(StudentBase):
    pass

class StudentRespone(StudentBase):
    id:int