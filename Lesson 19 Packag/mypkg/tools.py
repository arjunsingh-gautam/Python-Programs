def greet():
    print("Hello from tools")

from .helpers import helper

def greet():
    helper()
    print("Hello from tools")