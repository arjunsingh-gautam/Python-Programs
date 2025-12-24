# Implementing Basic Try Except in Python
# Task: Take two numbers divide them Handle ZeroDivisionError Exception

num1=int(input("Enter a number:"))
num2=int(input("Enter a number:"))
try:
    result=num1/num2
except ZeroDivisionError:
    print(f"num2=0 and division by zero is not defined")

else: # This run when no exception occurs inside try block
    print(f"{num1}/{num2} is {result}")