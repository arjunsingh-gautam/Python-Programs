# Implementing Non Data Descriptor:

class NonData:
    def __get__(self,instance,owner):
        return 10
    
class A:
    x=NonData()

a=A()
print(a.x) # Read Operation #10

a.x=50 # Write Operation in instance __dict__
print(a.x) # Now for non data-descriptor instance __dict__ reading is given priority over __get__