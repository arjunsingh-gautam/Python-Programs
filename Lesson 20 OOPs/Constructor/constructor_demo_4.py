class Book:
    def __init__(self,name,price): # Parameterised Constructor
        self.name=name
        self.price=price
    def Book(self): # It is possible to have the name of the method same as it's class
        print("Method executed")

b1=Book("Mastery",100)
print(b1.name,id(b1))
b1.__init__("Power",200) # Explicit constructor call to re-initialise instace variable
print(b1.name,id(b1))

b1.Book()