# In this we will implement default except block which cathches all exceptions:
try:
    num1=int(input("Enter a number:")) # Monitor ValueError
    num2=int(input("Enter a number:")) # Monitor ValueError
    result=num1/num2 # Monitor ZeroDivisionError

except: # default except catches all exceptions
    print("Something went wrong...")

else:
    print(f"{num1}/{num2} is {result}")