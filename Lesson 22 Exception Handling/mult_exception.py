# In this we will implement multiple exceptions in single except block


try:
    num1=int(input("Enter a number:")) # Monitor ValueError
    num2=int(input("Enter a number:")) # Monitor ValueError
    result=num1/num2 # Monitor ZeroDivisionError

except (ValueError,ZeroDivisionError):
    print("Incorrect value for typecasting to integer or division by zero which is not defined")

else:
    print(f"{num1}/{num2} is {result}")