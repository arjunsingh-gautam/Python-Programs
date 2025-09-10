class Test:
    def __init__(self):
        print("Constructor with 0 argument")
    def __init__(self,x): # This constructor will be considered by PVM while calling
        print("Constructor with 1 argument")
    def m1(self): 
        print("method get executed")
    def m1(self,x): # This method will be considered by PVM while calling
        print(f"method {x} got executed")

#t=Test() # will give error since PVM will consider the recent constructor which requires 1 arg
t=Test(10) # valid
t.m1('t')
# In Pyhton Constructor/Method Overloading is not possible
# Whenever two or more constructor or method of same name are declared inside a class PVM will consider only the last declared constructor/method