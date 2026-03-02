# Module show how to use @property
# @property helps you access a method like an attribute

class Person:
    def __init__(self,age):
        self._age=age #internal variable
    
    @property
    def age(self):
        return self._age
    
p1=Person(24)
age=p1.age # Using age instance method like an attribute but internally it behave like function
print("Age of person is:{}".format(age))
print(p1.__dict__)

