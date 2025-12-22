# Write a program to calculate sum of first n natural numbers:
def f1(n):
    if n==1:
        return 1
    return n+f1(n-1) # recursive call

r=f1(3) # function call
print(r) # Sum of first 3 natural numbers