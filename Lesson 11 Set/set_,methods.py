s1={'a',1,3+4j,True}
s2={1,2,39,49,20,93,100,20}
s3={2,49,20,199,200}
s4={49,20,2}

#add()
s1.add((10,20))
print(s1) #Output:{1,'a',(10,20),(3+4j)}  here True is considered equivalent to 1

#update()
s1.update("arj",[10,20])
print(s1)

#discard()
s1.discard(3+4j)
print(s1)

#remove()
s1.remove('a')
print(s1)

#intersection()
print(s2.intersection(s3))

#union()
print(s2.union(s3))

#issubset()
print(s4.issubset(s2))

#issuperset()
print(s2.issuperset(s4))

#clear()
(s1.clear())
print(s1)

#pop()
print(s2.pop())