l1=(3,4,5)
l2=(2,3,1)
l3=(1,2,3,4,5,6)
l4=(3,4,5)

print(l1!=l2)
print(l1>l3) # True: because length of the list does not matter comparison is element wise not len wise
print(l1==l4) # because tuples  are immutable there fore l1 and l4 are referenced to same objects unlike list
