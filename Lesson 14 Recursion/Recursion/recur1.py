# Write a program to calculate sum of square of first n natural numbers:
def f1(n): # step-1 f1(n)--> 1+4+9 _____+n^2
    if n==1: # step-3 Base Case: function should stop when n=1/Termination case of recursive call
        return 1
    return n**2 +f1(n-1) # step-2 Recursive Case: f1(n-1)--> 1+4+9 ------ +(n-1)^2

N=int(input("Enter the value of n: "))
r=f1(N)
print("sum of square of first %d number is %d"%(N,r))