# In this we will implement user-defined Exception class:

class AgeError(Exception): # Inherit Exception class
    pass
age=int(input("Enter your age:"))
try:
    if age<18:
        raise AgeError("Age is less than 18")
except AgeError as e:
    print(f"age:{age}- {e}")

else:
    print(f"age:{age}- Eligible to vote")