a=5
b=6
print(a,b) # Use default sep=' '(space)
print(a) #print automatically changes line after printing the argument # use default end='\n' (new-line)
print(b)
"""-> Output : a
               b   """


print(a,end=' , ') 
print(b)
#using the 'end' parameter to change the default behavior of the print function.

# % -> used as place holder
x=20
print("My age is %d"%x)

# use of `sep`
print(a,b,sep=' and ')
print("my age is",a," and b is",b)
# String formatting
print("a = %d and b = %d"%(a,b)) #M1
print("a = {} and b = {}".format(a,b)) #M2
print(f"a = {a} and b = {b}") #M3
print("a={1} and b={0}".format(a,b)) #M4
print("a={x} and b={y}".format(x=b,y=a)) #M5
