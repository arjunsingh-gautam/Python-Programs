# Global Variables
x = 42
y = "hello"

def my_function():
    # Local Variables
    a = 10
    b = 20
    print("Local Namespace inside function:", locals())  # List local variables

# Listing all names in the global namespace
print("All Names in Global Namespace:", dir())

# Listing only user-defined names (excluding built-ins)
user_defined = [name for name in dir() if not name.startswith("__")]
print("User-Defined Names:", user_defined)

# Listing all global variables and their values
print("Global Namespace Variables:", globals())

# Calling function to check local namespace
my_function()

# Listing all built-in functions and variables
#eprint("Built-in Functions and Variables:", dir(__builtins__))
