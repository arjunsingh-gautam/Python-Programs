l1=[1,2,3,4,5] # will be used as iterable for map
def square(a):
    return a**2
l2=list(map(square,l1))
print("The square of each element of l1:",l2)


