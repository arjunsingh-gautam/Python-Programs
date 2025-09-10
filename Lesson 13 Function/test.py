#TNRN
# def add():
#     num1=int(input("Enter a no.:"))
#     num2=int(input("Enter a no.:"))
#     print("Sum is {}".format(num1+num2))
# add() # function call

#TNRS
# def add():
#     num1=int(input("Enter a no.:"))
#     num2=int(input("Enter a no.:"))
#     return (num1+num2)
# print("Sum is {}".format(add()))

#TSRN
# def add(a,b):
#     sum=a+b
#     print("Sum is {}".format(sum))

# num1=int(input("Enter a no.:"))
# num2=int(input("Enter a no.:"))
# x = add(num1,num2)
# print(x)

#TSRS
# def add(a,b):
#     return a+b

# num1=int(input("Enter a no.:"))
# num2=int(input("Enter a no.:"))
# print("Sum is {}".format(add(num1,num2)))

# function  always return something--> it returns none



def add(*t):
    a=sum(t)
    print(a,t)   
add(3,4,5,6)
add(1,2,3,4,5,6,7,8,9) 