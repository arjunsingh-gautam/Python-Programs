# Write a python script to use IN operator to display the data present in the list
# Write a python script to use NOT IN operator to display the data not present in list
l1=[int(e) for e in range(1,10,1)]
data=int(input("enter a number:"))
if data in l1:
    print("You guess right")
else:
    print("You guess wrong")