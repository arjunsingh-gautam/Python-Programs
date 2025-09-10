# print factorial of n using Lambda Expression:
f= lambda n: 1 if n==1 else n*f(n-1)
N=int(input("Enter value of n: "))
print("Factorial of",N,"is:",f(N))