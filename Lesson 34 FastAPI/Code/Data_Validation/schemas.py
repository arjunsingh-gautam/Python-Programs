# Schema for API request and response
from pydantic import BaseModel,Field,ConfigDict

class StudentCreate(BaseModel):
    name:str=Field(min_length=1,max_length=50)
    branch:str=Field(min_length=1,max_length=3)
    
class StudentResponse(StudentCreate):
    model_config=ConfigDict(from_attributes=True)
    id:int
    