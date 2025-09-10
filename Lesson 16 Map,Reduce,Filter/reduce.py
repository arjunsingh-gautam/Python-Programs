from functools import reduce
l1=[1,2,3,4]
def multiply(a,b):
    return a*b
r= reduce(multiply,l1)
print("The value of reduce is:",r)