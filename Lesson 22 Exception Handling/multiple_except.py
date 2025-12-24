# In this we will implement multiple except:
# Task: Take two input convert them to integer divide them and try to handle exceptions like ValueError or ZeroDivisionError

try:
    num1=int(input("Enter a number:")) # Monitor ValueError
    num2=int(input("Enter a number:")) # Monitor ValueError
    result=num1/num2 # Monitor ZeroDivisionError

except ValueError:
    print("Incorrect value for typecasting to integer")
except ZeroDivisionError:
    print(f"num2={num2} Division by zero is not defined")

else:
    print(f"{num1}/{num2} is {result}")