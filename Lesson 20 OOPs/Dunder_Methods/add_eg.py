# Implementing __add__ dunder method:

class Vector:

    def __init__(self,value):
        self.value=value

    def __add__(self,other):
        print("__add__ called:")
        if isinstance(other,Vector):
            return Vector(self.value+other.value)
        return NotImplemented
    
    def __radd__(self,other):
        print("__radd__ called:")
        if isinstance(other,int):
            return Vector(self.value+other)
        return NotImplemented
        
    def __repr__(self):
        print("__repr__ called")
        return f"Vector({self.value})"
        
v1=Vector(3)
v2=Vector(5)
v3=v1+v2
print(v3)