# In this program we will demonstrate an eg. of Non-Inheritance

class C1:
    def disp1(self):
        print("Object of C1 class")

class C2:
    def disp2(self):
        print("Object of C2 class")

class C3:
    def disp3(self):
        print("Object of C3 class")

o1=C1()
o2=C2()
o3=C3()
# More memory space get utilised as we have to create object 3 times to use functionalities all classes
o1.disp1()
o2.disp2()
o3.disp3()
        