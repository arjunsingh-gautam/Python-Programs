# In this program we will see how we can access name mangled method using a public wrapper

class Account:
    
    def __init__(self):
        self.__accno=22070123043  # Cannot be accessed outside class if Name used are: __acno or acno
        # To accessed name mangled data members outside class you have to use their mangled name 
        # Mangled name: _classname__dataMemberName
        self.cname="Arjun"
        self.__acbalance=394329.19
        self.__acpin=1234
        self.bname="SBI"
    
    def __get_data(self): # Here the method is name mangled using '__'
        print(f"Account No.:{self.__accno}") # Inside Class to access mangled data member we can directly use it's mangled name starting from '__'
        print(f"Customer Name:{self.cname}")
        print(f"Bank Name:{self.bname}")

    def extract_data(self): # Acting as Public wrapper
        self.__get_data() # calling name mangled method 

ac1=Account()

#ac1.__get_data() #AttributeError: 'Account' object has no attribute '__get_data'
#ac1.get_data() #AttributeError: 'Account' object has no attribute 'get_data'

ac1.extract_data() # No AttributeError when Public wrapper is used since method is called internall within the class
