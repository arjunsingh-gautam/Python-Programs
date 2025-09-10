class Test:
    def __init__(self):
        print("Address pointed by self is:",id(self))

t=Test()
print("Address pointed by t is:",id(t))
print("new object creation")
t2=Test() # now self refers to this new object 
# When object is created self points to current instance of Class i.e the object created