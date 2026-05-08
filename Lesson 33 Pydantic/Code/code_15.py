# In this module we will learn about computed fields in Pydantic
# Computed fields help us to dynamically computer derived data from other fields
from __future__ import annotations
from pydantic import(
    BaseModel,
    Field,
    computed_field
    
)


class Employee(BaseModel):
    firstname:str
    lastname:str
    monthly_salary:float=0.0
    
    @computed_field
    @property
    def fullname(self:Employee)->str:
        return f"{self.firstname} {self.lastname}"
    
    @computed_field
    @property
    def annual_salary(self:Employee)->float:
        return self.monthly_salary*12
    

e1=Employee(firstname="John",lastname="Doe",monthly_salary=10000)
e1_info=e1.model_dump()
print(e1_info)
    
    