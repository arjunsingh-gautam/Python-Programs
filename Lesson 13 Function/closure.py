# In this code we will understand how closures help us to capture a local variable of function beyond the life time of it's stack frame using cell object and inner function

def outter():
    x=10 # local scope object of x
    def inner():
        return x # Captures x using closure referencing
    return inner

f=outter() # f-->(refernce) to (inner)function object
print(f()) # print(inner()) --> print(x) # Here outter stack frame destroyed but still we are able to capture x beyond it's lifetime using closures
