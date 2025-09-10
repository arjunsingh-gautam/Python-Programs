# In this eg. we will see Hierarchial inheritance
class Animal: # Parent Class
    def greet(self):
        print("I am an Animal")

class Dog(Animal): # Child class of Parent class Animal
    def woof(self):
        self.greet()
        print("I am a Dog")
        print("woof!")

class Cat(Animal): # Child class of Parent class Animal
    def meow(self):
        self.greet()
        print("I am a cat")
        print("meow!")

d1=Dog()
c1=Cat()
d1.woof()
c1.meow()