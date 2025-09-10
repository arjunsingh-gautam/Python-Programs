# Write a python script to print greater among three numbers. Print number only once even if the numbers are the same.
a=int(input("Enter num-1:"))
b=int(input("Enter num-2:"))
c=int(input("Enter num-3:"))
max=0
if a>b and a>c:
    max=a
    print("Maximum is %d"%a)
elif b>a and b>c:
    max=b
    print("Maximum is %d"%b)
else:
    max=c
    print("Maximum is %d"%c)