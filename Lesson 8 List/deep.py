# In this program we will represent the concept of deep copy 
# In deep outter object and it's inner object are recursively copied and represent a new object in memory

import copy
l1=[[1,2],[3,4]] # original
l2=copy.deepcopy(l1) # deep copy --> inner iterable / objects are copied along with outter list and  represent a separate object
print(f"ID of l1:{id(l1)}\nID of l2:{id(l2)}")
print(f"l1:{l1}\nl2:{l2}")
l2[0][1]=82 # make changes to only deep copied objects 
print(f"ID of l1:{id(l1)}\nID of l2:{id(l2)}")
print(f"l1:{l1}\nl2:{l2}")


# More about Deep vs Shallow Copy:
# Deep Copy: Recursively inner iterables as distinct objects
# Shallow Copy: Don't recursively copies
import copy
l1=[[1,2],[3,4]]
l2=copy.deepcopy(l1)
l3=l1.copy() # shallow copy inner object does not have separate id
print(id(l1),id(l2),id(l3))
for x in range(len(l1)):
    print(l1[x],id(l1[x]))
    print(l2[x],id(l2[x]))
    print(l3[x],id(l3[x]))