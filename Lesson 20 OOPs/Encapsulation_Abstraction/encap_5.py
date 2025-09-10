# In this program we will see how we encapsulate data using @property decorator

class Account:

    def __init__(self):
        self._accno=22070123043
        self._accpin=1234

    @property
    def value(self):
        return self._accno,self._accpin
    
    #@value.setter
    #def value(self,data):
        #self._accno, self._accpin = data

ac1=Account()
acc_details=ac1.value
print(f"Account Details:{acc_details}")

ac1._accno=22070123004 # You can still set values outside function even if setter is commented
ac1._accpin=5743
acc_details=ac1.value
print(f"Account Details:{acc_details}")

#ac1.value=22070123030,3345 #AttributeError: property 'value' of 'Account' object has no setter
# When comment the setter there cannot be change outside only accessed outside using getter
#acc_details=ac1.value
#print(f"Account Details:{acc_details}")