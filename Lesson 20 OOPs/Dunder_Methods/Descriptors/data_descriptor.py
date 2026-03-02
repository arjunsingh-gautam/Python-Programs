# Implementing Data Descriptor:

class DataDescriptor:
    
    def __get__(self,instance,owner):
        print("Getter Executed...")
        return instance._value
    
    def __set__(self,instance,value):
        print("Setter Executed...")
        instance._value=value

class A:
    x=DataDescriptor()

b=A()
b.x=10
print(b.x) # Value set by __set__