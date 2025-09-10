# This program demostrates object interning in small integers:
a = 256
b = 256
print(id(a) == id(b))  # True (Same object due to interning)

x = 257
y = 257
print(id(x) == id(y)) 
 # False (Different objects) should return False but due to code optimisation and memory optimisation in VS-Code return True

 # When run in Python shell return False

