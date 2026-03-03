# In this eg. we will implement repr dunder method:

class Vector:

    def __init__(self,value):
        self.value=value
    
    def __repr__(self):
        print("Calling __repr__:")
        return f"Vector({self.value})"
    
v1=Vector(5)
print(v1)