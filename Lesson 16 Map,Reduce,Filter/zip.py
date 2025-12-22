# In this we will learn about zip() inbuilt function in Python
l1=["Arjun","Bhoumik","Ashish"]
l2=[43,34,30]
print(list(zip(l1,l2)))

print("a\tb\t")
print(30*"*")
for a,b in zip(l1,l2):
    print(f"{a}\t{b}\t")

# Unzipping
name,roll=zip(*list(zip(l1,l2)))
print(name)
print(roll)