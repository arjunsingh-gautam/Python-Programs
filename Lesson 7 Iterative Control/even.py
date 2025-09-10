# Write a program to print n even natural numbers
n=int(input("Enter the value for n:"))
i=1
while i<n+1:
    print(2*i)
    i+=1
print("Condition becomes false at:",i)
print()