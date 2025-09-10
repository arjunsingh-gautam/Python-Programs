# In this program we will se how to implement Polymorphism in Python

# For method overriding Inheritence is necessary
class Animal:

    def greet(self): # Original Method of Parent Class
        print("I am an Animal")

class Dog(Animal):
    def greet(self):
        print("I am a Dog") # Method Overriding of Original Parent class Method

class Cat(Animal):
    def greet(self): # Method Overriding of Original Parent class Method

        print("I am a Cat")

a=Animal()
d=Dog()
c=Cat()

a.greet()
d.greet()
c.greet()