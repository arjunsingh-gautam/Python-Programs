# How to implement decorator function which can take function with any no of positional or key-word argument

def decorator_function(original_function):
    def wrapper_function(*args,**kwargs):
        print(f"wrapper_function executed before {original_function.__name__}")
        return original_function(*args,**kwargs)
    return wrapper_function
@decorator_function
def display():
    print("display() executed having 0 arguments")

@decorator_function
def display_2(a,b):
    print(f"display2() executed with 2 positional arguments:{a} and {b}")

display()

display_2('John',24)