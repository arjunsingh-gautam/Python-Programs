# Write a program to print first n natural numbers:
def f1(n):
    if n>0:
        f1(n-1)
        print(n,end=',')
    

N=int(input("Enter value of n: "))
r=f1(N)
