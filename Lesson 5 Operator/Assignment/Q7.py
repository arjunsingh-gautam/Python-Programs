#Write a python script to use IS operator to display if both variables are the same object or not?
a=int(input("Enter a number:"))
b=int(input("Enter a number:"))
if a is b:
    print("Pointting same objects id of a is",id(a),"and id of b is",id(b),"is same")
else:
    print("Not pointing same object")