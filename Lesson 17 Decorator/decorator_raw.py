# In this code I will implement decorator function in it's raw form and  understand how it works

# Decorator function add extra functionality to a function without alter it's source code

# Raw implementation

def decorator_function(original_function):
    # It takes original_function as input argument
    def wrapper_function(): # Adds extra functionality to original function
        print(f"wrapper_function executed before {original_function.__name__}")
        return original_function()

    return wrapper_function
    

# Original Function:
def display():
    print("original_function get executed")

decorated_display=decorator_function(display)

decorated_display()
