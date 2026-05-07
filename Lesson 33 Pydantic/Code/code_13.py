# Defining model_validators in Pydantic
# Used generally for cross field validation or validation that requires access to multiple fields of the model

from pydantic import (BaseModel,ValidationError,Field,EmailStr,HttpUrl,SecretStr,model_validator,field_validator,ValidationInfo)
from datetime import datetime,UTC

class Order(BaseModel):
    price:float
    discount:float
    @model_validator(mode="after")
    def check_discount(self):
        if self.discount >= self.price:
            raise ValueError("Discount cannot be greater than or equal to price")
        return self
    
try:    
    order=Order(price=100,discount=150)
    print(order)
except ValidationError as e:
    print(e)