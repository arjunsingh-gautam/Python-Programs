# In this module we will explore duck typing

class Dog:
    def speak(self):
        print("Woof!")

class Cat:
    def speak(self):
        print("Meow!")

class Human:
    def speak(self):
        print("Hello!")


def make_sound(object): # It doen't check type of the object it checks it's behavior if object can speak then it will execute without exception
    object.speak()

obj1=Dog()
obj2=Cat()
obj3=Human()

make_sound(obj1)
make_sound(obj2)
make_sound(obj3)