# In this we will see the concept of alias of exception objects:
# Task: Accessing list element using the user input index value and handle IndexError

user_list=[1,2,3,4,5,6,7,8,9]
index=int(input("Enter an integer value for indexing:"))
try:
    value=user_list[index]
except IndexError as i:
    print(f"Invalid index value-{index} reason:{i}")
else:
    print(f"Value at Index-{index} is:{value}")