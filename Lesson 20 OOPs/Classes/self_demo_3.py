# It is not necessary to use self to refer an instance you can use any other name but by standard convention using self is recommended
#using 'mai' instead of 'self'

class Dog:
    def __init__(mai, name, breed):
        mai.name = name  # Instance variable name
        mai.breed = breed  # Instance variable breed

    def bark(mai):
        return f"{mai.name} says Woof!"

    def description(mai):
        return f"{mai.name} is a {mai.breed}."

# Creating an instance of Dog
my_dog = Dog("Buddy", "Golden Retriever")

# Calling methods on the instance
print(my_dog.bark())  # Output: Buddy says Woof!
print(my_dog.description())  # Output: Buddy is a Golden Retriever.