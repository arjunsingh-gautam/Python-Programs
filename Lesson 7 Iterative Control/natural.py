# Write a program to print 10 natural numbers
# using while loop.
i=1
while i<11:
    print(i)
    i+=1
print("Condition become false at:",i)
print()
# Write a program to print 10 natural numbers in reverse order
# Method-1
i=1
while i<11:
    print(11-i)
    i+=1
print("Condition become false at:",i)
print()
# Method-2
i=10
while i>0:
    print(i)
    i-=1
print("condition become false at:",i)
print()
#Method-3
i=10
while i:
    print(i)
    i-=1
print("condition become false at:",i)  #at i=0 it becomes'False'
print()