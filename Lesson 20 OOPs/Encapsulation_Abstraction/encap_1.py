# In this program we can see how we can implement encapsulation by name mangling using '__'

class Account:
    def __init__(self):
        self.__accno=22070123043  # Cannot be accessed outside class if Name used are: __acno or acno
        # To accessed name mangled data members outside class you have to use their mangled name 
        # Mangled name: _classname__dataMemberName
        self.cname="Arjun"
        self.__acbalance=394329.19
        self.__acpin=1234
        self.bname="SBI"


ac1=Account()

print("Account details of ac1:")
print('-'*50)
#print(f"Account No.:{ac1.__accno}") #AttributeError: 'Account' object has no attribute 'accno'
#print(f"Account No.:{ac1.accno}") #AttributeError: 'Account' object has no attribute 'accno'
print(f"Customer Name:{ac1.cname}")
print(f"Bank Name:{ac1.bname}")
print(f"Account No.:{ac1._Account__accno}") # No AttributeError since Mangled name is used to access it

# If we know the mangled name we can still access the mangled data member
