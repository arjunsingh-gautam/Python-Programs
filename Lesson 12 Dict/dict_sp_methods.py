# item()
d1={101:'Abhishek',102:'Arjun',103:'Bhoumik'}
print(d1.items(),type(d1.items()))

for k in d1.items():
    print(k)

for k,v in d1.items():
    print(k,v)

# keys()
print(d1.keys(),type(d1.keys()))

# values()
print(d1.values(),type(d1.values()))
