# Adding Constraints in Data Validation using Pydantic

from pydantic import BaseModel,ValidationError,Field,EmailStr,HttpUrl,SecretStr
from datetime import datetime,UTC
import os
import json
from functools import partial
from typing import Literal,Annotated
from uuid import UUID,uuid4


class User(BaseModel):
    username:Annotated[str,Field(min_length=3,max_length=20)]
    user_id:UUID = Field(default_factory=uuid4)
    verified_at:datetime | None = None
    age:Annotated[int,Field(ge=13,le=130)]
    email:EmailStr
    website:HttpUrl|None=None
    password:SecretStr
    bio:str = ""
    is_active:bool = True
    fullname:str|None = None
    

class BlogPost(BaseModel):
    title:Annotated[str,Field(min_length=1,max_length=200)]
    content:Annotated[str,Field(min_length=10)]
    view_count:int = 0
    is_published:bool = False
    tags:list[str] = Field(default_factory=list)
    created_at:datetime=Field(default_factory=partial(datetime.now,tz=UTC))
    status:Literal["draft","published","archived"]="draft"
    slug:Annotated[str,Field(pattern=r"^[a-z0-9-]+$")]
    
try:
   user=User(
       username="arjdev",
       email="arj12@gmail.com",
       age=38,
       password="secret123"
   )
   print(user)
except ValidationError as e:
    print(e)
    
