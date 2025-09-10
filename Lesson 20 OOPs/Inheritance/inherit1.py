# In this program we will see how inheritance works

class C1:
    def disp1(self):
        print("Object of C1 class")

# C2: Is an intermediate Base Class
class C2(C1): # Here C2 is a child class of C1 class
    def disp2(self):
        print("Object of C2 class")

class C3(C2): # Here C3 is a child class of C2 class
    def disp3(self):
        print("Object of C3 class")

o=C3() # Less Memory is consumed since we are using only a single object to use utilities of all classes
o.disp1()
o.disp2()
o.disp3()