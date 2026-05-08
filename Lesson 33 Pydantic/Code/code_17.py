# In this module we will learn about model configuration in  Pydantic

from pydantic import BaseModel, ConfigDict

class User(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
        validate_assignment=True,
        str_strip_whitespace=True
    )
    name:str
    age:int

user=User(name=" John ",age=25)
print(user) 

#user.age="abc" # ValidationError due to validate_assignment=True