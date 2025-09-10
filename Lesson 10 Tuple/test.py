# tuple
# class
# immutable
# hashable
# order sequnce

# tuple declaration and initialistion:
# t=10,39,48,39# single element tuple
# print(type(t))

#tuple builtin methods
t=('ram','laxman','bharat','shatrugan')
# print(min(t),max(t),sorted(t),len(t),sep='\n')

#tuple arithmatic
#t1=(3,'true',True,3,3)
# t3=(3+4j,False)
# print(t1+t3)
# print(t3*3)

#tuple method
# print(t1.count(3))
# print(t1.index('true'))

#tuple comparator
# t=('ram',3,'bharat',4)
# t3=('shatrugan',2)
# print(t3>t)

# tuple slicing
# print(t[::-1])
# print(t[:4:2])

#tuple input
t=tuple([z**3 for z in range(5)])
print(t)