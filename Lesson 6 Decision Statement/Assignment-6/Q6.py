#Write a python script to check whether a given number is a three digit number or not.
num=int(input("Enter a number:"))
if 100<=num<=999:
    print("%d is three digit number"%(num))
else:
    print("%d is not a three digit number"%(num))