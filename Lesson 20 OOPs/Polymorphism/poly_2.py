# In this program we will see how we can use super() to call Parent class original method

class Animal:

    def greet(self): # Original Method of Parent Class
        print("I am an Animal")

class Dog(Animal):
    def greet(self):
        print("I am a Dog") # Method Overriding of Original Parent class Method
        super().greet() # Calls Parent Method 

class Cat(Animal):
    def greet(self): # Method Overriding of Original Parent class Method
        print("I am a Cat")
        super().greet() # Calls Parent Method 


d=Dog()
c=Cat()


d.greet()
c.greet()