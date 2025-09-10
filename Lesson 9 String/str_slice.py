#slice operator
# M-1
s1="MysirG Education Services"
print(s1[1:10:2])
#M-2
print(s1[:5:-1]) # starts from index 0 by default if not given
 # M-3
print(s1[::-1]) # if end not mentioned it takes end='last index' and also include it. Prints reverse of string
#M-4 
print(s1[::]) # print original string because default step is 1

l1=[5,True,"arjun",5.63,"ashish",6,9.83,False]
print(l1[2::2])