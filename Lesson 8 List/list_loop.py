# Accessing elements using loops:
# 1. For Loop
print("For Loop:")
l1=[449,3909,293,583]
for e in l1:
    print(e,id(e)) # id of each element is different

# 2. While Loop
print("While Loop:")
i=0
while i<4:
    print(l1[i],end=' ')
    i+=1

print(id(l1))