#split() --> returns list of str type elements
s1="MysirG Education Services"
l1=s1.split(' ')
l2=s1.split('e')
print(l1)
print(l2)

# number list from user
print("Enter numbers separated by commas:")
l3=[int(e) for e in input().split(',')]
print(l3)

