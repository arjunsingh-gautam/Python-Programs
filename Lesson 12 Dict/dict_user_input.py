n=int(input("How many student data you want to store:"))
dict={}
for k in range(n):
    keys=input("Enter Roll no.:")
    values=input("Enter names:")
    dict[keys]=values
print(dict)