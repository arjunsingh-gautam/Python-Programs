# In this module we will implement a decorator with Argument

def argument_function(prefix):
    def decorator_function(original_function):
        def wrapper_function(*args,**kwargs):
            print(f"{prefix}: Before Wrapper")
            result=original_function(*args,**kwargs)
            print(f"{prefix}: After Wrapper")
            return original_function
        return wrapper_function
    return decorator_function


@argument_function("Log")
def greet(name):
    print(f"Hello {name}!")

greet('John')
