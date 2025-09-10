s1={1,95,22} # order of insertion is not preserve
s2={10,338,929,47,19,19,838,10,338}
s3={}  # creates empty dict
s4=set() # creates empty set
s5=set([10,94,929])
s6={3.3,4,True,"arj",3+4j} # can have heterogenous elements
#s7={[10,30,93],[38,28,19]} #--> gives error can't stor unhashable class and list is unhashable
s8={(10,393,38,93),(818,38,919)} # ---> no error since tuple is hashable
print(s1,type(s1))
print(s2,type(s2))
print(s3,type(s3))
print(s4,type(s4))
print(s5,type(s5))
print(s6,type(s6))
# print(s7,type(s7))
print(s8,type(s8))