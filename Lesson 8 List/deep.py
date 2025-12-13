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
