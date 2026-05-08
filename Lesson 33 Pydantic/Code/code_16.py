# In this module we will learn about Nested Models
# Nested Models help us to write go Modular code and avoid flat validation model which are hard to maintain
from __future__ import annotations
from pydantic import(
    BaseModel,
    Field
)
from typing import Annotated

class Address(BaseModel):
    city:str
    country:str
    
class Person(BaseModel):
    name:str
    age:Annotated[int,Field(ge=0,le=120)]
    address:Address # Nested 
    
p1=Person(name="John Doe",age=23,address={"city":"Queens","country":"USA"})
    
print(p1.model_dump())