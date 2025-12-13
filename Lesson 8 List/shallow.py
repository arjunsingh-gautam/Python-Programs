# In this code we will learn about shallow copy
import copy
l1=[[1,2],[3,4]] # original
l2=copy.copy(l1) # shallow copy --> inner iterable / objects are referenced not made a separate copy only outter list is copied and is represent a separate object
print(f"ID of l1:{id(l1)}\nID of l2:{id(l2)}")
print(f"l1:{l1}\nl2:{l2}")
l2[0][1]=82 # make changes to both original and copy since inner objects are only referred not copied
print(f"ID of l1:{id(l1)}\nID of l2:{id(l2)}")
print(f"l1:{l1}\nl2:{l2}")
