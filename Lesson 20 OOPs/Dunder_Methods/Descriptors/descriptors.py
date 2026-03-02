# Implementation of descriptors 

class PositiveNumber:

    def __get__(self,instance,owner):
        print("Getter getting executed...")
        return instance._value
    
    def __set__(self,instance,value):
        print("Setter getting executed...")
        if value<0:
            raise ValueError("Negative number not allowed")
        instance._value=value

class Product:
    price=PositiveNumber()

    def __init__(self,price):
        self.price=price

print(Product.__dict__)
print(100*'-')
p=Product(100)
print(100*'-')
print(p.price)
print(100*'-')
print(p.__dict__)
