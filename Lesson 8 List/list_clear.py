l1=[1,2,3,4,5,6]
l1.clear()
"""Here after above line all reference to stored objects are deleted but the object still exist in memory until garbage collector removes them. """
print(l1)

# l1[0] will cause IndexError
