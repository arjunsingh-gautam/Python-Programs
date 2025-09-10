# Method-1
s1="{}, Welcome"
print(s1.format("Arjun"))
print(s1)

#Method-2
a=4
b=7.9
s2="here a is {} and b is {}"
print(s2.format(a,b))
print(s2)

#Method-3
s3="here a is not {1} and b is not {0}"
print(s3.format(a,b))  # here a refers 0 kwarg and b refers 1 kwarg

#Method-4
print("Addn is {} subtraction is {} multiplication is {}".format(a+b,a-b,a*4))