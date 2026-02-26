 # In this we will implement decorator using class

class decorator_class:
    def __init__(self,original_function):
        self.original_function=original_function
    
    def __call__(self):# Allows class instance to be called like a function objec
        print(f"wrapper_function executed before {self.original_function.__name__}")
        return self.original_function()
    
@decorator_class
def display():
    print("original_function executed")

display()