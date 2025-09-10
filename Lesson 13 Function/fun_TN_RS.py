# Function that takes nothing and returns something
def Add():  # Here return keyword is used is used therefore function is returning the value of when it is called
    print("Enter two numbers:")
    a=int(input())
    b=int(input())
    c=a+b
    return c

s=Add()  # Here balue of c is returned when called and stored in s
print("Sum is:",s)