# Using ValidationInfo in Pydantic to access field and model information during validation for enhanced error handling and custom validation logic.
from pydantic import (BaseModel,ValidationError,Field,EmailStr,HttpUrl,SecretStr,model_validator,field_validator,ValidationInfo)
from datetime import datetime,UTC
from typing import Annotated
from uuid import UUID,uuid4

class User(BaseModel):
    username:Annotated[str,Field(min_length=3,max_length=20)]
    user_id:UUID = Field(default_factory=uuid4)
    verified_at:datetime | None = None
    age:Annotated[int,Field(ge=13,le=130)]
    email:EmailStr
    website:HttpUrl|None=None
    password:SecretStr
    confirm_password:SecretStr
    bio:str = ""
    is_active:bool = True
    fullname:str|None = None
    
    # After Validation hook to ensure username is always stored in lowercase
    @field_validator("username")
    @classmethod
    def validate_username(cls,v:str,info:ValidationInfo)-> str:
        if not v.replace("_","").isalnum():
            raise ValueError("Username must be alphanumeric with optional underscores")
        return v.lower()
    
    # Before Validation hook to add https to website if missing before validating it as HttpUrl
    @field_validator("website",mode="before")
    @classmethod
    def add_https(cls,v:str|None)-> str|None:
        if v is not None and not v.startswith(("http://","https://")):
            return "https://"+v
        return v
    

    # Model level validation to ensure password and confirm_password match
    @field_validator("confirm_password")
    @classmethod
    def check_passwords_match(cls,v,info:ValidationInfo):
        password = info.data.get("password")
        if password is not None and v != password:
            raise ValueError("Passwords do not match")
        return v
    
try:
    user=User(
        username="Arjdev_123",
        email="arj@gmail.com",
        password="secret123",
        age=23,
        confirm_password="secret124"
    )   
    print(user)
except ValidationError as e:    
    print(e)

