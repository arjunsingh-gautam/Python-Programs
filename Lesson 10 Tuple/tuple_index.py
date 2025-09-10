#Accessing tuple elements
# Using Indexing only
i=int(input("Enter index value:"))
t3=(7,"sam",True,8.83,7+6j)
print(t3[i],type(t3[i]))
print()
# Using while loop
i=0
while i<len(t3):
    print(t3[i],type(t3[i]))
    i+=1
print()
# Using for loop
for e in t3:
    print(e)



