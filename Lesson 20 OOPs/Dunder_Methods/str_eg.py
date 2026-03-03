# Implementing __str__ dunder method:

class Vector:

    def __init__(self,value):
        self.value=value
    
    def __str__(self):
        print("Calling __str__")
        return f"Vector value is {self.value}"
    
v1=Vector(23)
print(v1)