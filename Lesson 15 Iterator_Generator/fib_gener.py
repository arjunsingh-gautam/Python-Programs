# Write a program to creaste generator for fibonacci numbers:
def fib(n):
    a,b=0,1
    while n:
        yield a
        a,b=b,a+b
        n-=1

for e in fib(int(input("Enter value of fibonacci numbers:"))):
    print(e,end=' ')