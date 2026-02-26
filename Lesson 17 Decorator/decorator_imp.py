# In this we will show pythonic implementation of decorated function

def decorator_function(original_function):
    # It takes original_function as input argument
    def wrapper_function(): # Adds extra functionality to original function
        print(f"wrapper_function executed before {original_function.__name__}")
        return original_function() # calling original function

    return wrapper_function # Return a modified/decorated original function
    

@decorator_function
def display():
    print("original_function get executed") 

# Above expression is same as display=decorator_function(display)

display() 