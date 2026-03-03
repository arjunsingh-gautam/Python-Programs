# In this module we understand how abstract classes work:

from abc import ABC,abstractmethod

class Payment(ABC): # abstract class-> Creates a contract between subclass that it must implement all abstract classes

    def __init__(self,payment):
        self.payment_method=payment

    @abstractmethod # This method must be implemented in subclasses otherwise no instantiation allowed
    def pay(self,amount):
        pass
    
# We cannot instantiate an object of Payment class since it's abstractmethod set is always non empty and for instantiation it must be empty set():
print(Payment.__abstractmethods__) # non-empty
print("Payment class object can't be instantiated...")  
print()
class UPIPayment(Payment):
    def __init__(self,payment):
        super().__init__(payment)

    def pay(self,amount):
        print(f"UPI Payment of {amount} is successful!")


print(UPIPayment.__abstractmethods__) # empty set  therefore can be instantiated UPIPayment agrees the contract and implement all abstractmethods
print("UPIPayment class object can be instantiated...")
print()

payment=UPIPayment("UPI")
payment.pay(1000)
