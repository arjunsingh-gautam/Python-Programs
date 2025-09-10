# Write a python script to print greater between two numbers. Print number only once even if the numbers are the same
num1=int(input("Enter number 1:"))
num2=int(input("Enter number 2:"))
if num1>num2:
    print("%d is greater than %d"%(num1,num2))
elif num1==num2:
    print("Both are equal")
else:
    print("%d is less than %d"%(num1,num2))