# In this program we will see that class cannot be encapsulated

class __Account:
    def __init__(self):
        self.accno=22070123043  
        self.cname="Arjun"
        self.acbalance=394329.19
        self.acpin=1234
        self.bname="SBI"

#ac1=Account() #NameError: name 'Account' is not defined. Did you mean: '__Account'?
ac2=__Account() # __Account Name is working outside it is not Name mangled
print("Account details ac2:")
print('-'*50)
print(ac2.__dict__)

# Only data members and methods can be encapsulate using name mangling
