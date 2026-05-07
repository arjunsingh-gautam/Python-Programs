# Error Handling in Python
from pydantic import BaseModel,ValidationError,Field
from datetime import datetime,UTC
import os
import json
from functools import partial
from typing import Literal


class User(BaseModel):
    username:str
    user_id:int
    verified_at:datetime | None = None
    email:str
    bio:str = ""
    is_active:bool = True
    fullname:str|None = None
    

class BlogPost(BaseModel):
    title:str
    content:str
    view_count:int = 0
    is_published:bool = False
    tags:list[str] = Field(default_factory=list)
    created_at:datetime=Field(default_factory=partial(datetime.now,tz=UTC))
    status:Literal["draft","published","archived"]="draft"
    
try:
    post1=BlogPost(title="My First Blog Post",content="This is the content of my first blog post.",view_count=100,is_published=True,tags=["python","pydantic"],status="published")
    print(post1)
except ValidationError as e:
    print(e)
    
