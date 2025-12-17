# In this code we will learn about fromkeys dictionary method:
# .fromkeys dictionary method is used to create dictionary having key value taken from an iterable and all keys assigned same object
# Precaution: All keys point to same object there cautious use with mutable objects

# Eg.

d=dict.fromkeys([1,2,3,4],0)
print(d)

d1=dict.fromkeys([1,2,3],[])
d1[1].append("Arjun") # affect values of all keys since all keys are pointing same list object when created through fromkeys method
print(d1)