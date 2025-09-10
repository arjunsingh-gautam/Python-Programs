class Dog:
    def __init__(self, name, breed): #constructor:the first argument to constructor is alsway self
        self.name = name  # Instance variable name
        self.breed = breed  # Instance variable breed
        print("ID of self:",id(self))

    def bark(self): #instance method-> the first to the instance method is always self
        print( f"{self.name} says Woof!")
        print("ID of self:",id(self))

    def description(self):
        print(f"{self.name} is a {self.breed}.")
        print("ID of self:",id(self))

# Creating an instance of Dog
print("Object Creation")
my_dog = Dog("Buddy", "Golden Retriever")
print("ID of object:",id(my_dog))

# Calling methods on the instance
my_dog.bark()  # Output: Buddy says Woof!
my_dog.description()  # Output: Buddy is a Golden Retriever.

# Creating an instance of Dog
print("Object Creation")
neighbour_dog = Dog("Happy", "German Shephard")
print("ID of object:",id(neighbour_dog))

# Calling methods on the instance
neighbour_dog.bark() # Output: Happy says Woof!
neighbour_dog.description()  # Output: Happy is a German Shephard.

""" How self Works:
__init__ Method:

When my_dog = Dog("Buddy", "Golden Retriever") is executed, the __init__ method is called, with self referring to the new instance being created (my_dog). The attributes self.name and self.breed are set to "Buddy" and "Golden Retriever", respectively.
Instance Methods:

When you call my_dog.bark(), Python automatically passes the my_dog instance as the first argument to the bark method, so self inside bark refers to my_dog. """