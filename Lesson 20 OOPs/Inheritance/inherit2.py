# In this eg. we will se single inheritence
# In Single inheritence ther is :
    #- One Base class
    #- One child class: Inherit only from a single base class

class C1: # Base Class/ Parent Class
    def getA(self):
        self.a=int(input("Enter value of a:"))

class C2(C1): # Derived class/ Child Class having single super class
    def getB(self):
        self.b=int(input("Enter value of b:"))
    def add(self):
        self.sum=self.a+self.b
        print(f"Sum({self.a},{self.b})={self.sum}")

o=C2()
o.getA()
print(f"Attributes of o are:{o.__dict__}")
print('-'*50)
o.getB()
print(f"Attributes of o are:{o.__dict__}")
print('-'*50)
o.add()
print(f"Attributes of o are:{o.__dict__}")
