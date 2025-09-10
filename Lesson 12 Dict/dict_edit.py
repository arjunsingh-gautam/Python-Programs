# Editing data values
d1={101:'Abhishek',102:'Arjun',103:'Bhoumik'}
d1[101]="Ashish"
print(d1)

#Editing keyvalues
del d1[102] # step-1 delete element associated with key
print(d1)
d1[104]="Arjun" # step-2 add new element with new key value
print(d1)