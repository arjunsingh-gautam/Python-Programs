# Create a generator to produce first n even natural numbers:

def evenGenerator(n):
    a=2
    while n:
        yield a
        a+=2
        n-=1

for e in evenGenerator(int(input("Enter the no. even numbers:"))):
    print(e,end=' ')