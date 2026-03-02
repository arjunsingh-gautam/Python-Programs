# Implementing getter,setter,deleter using property

class BankAccount:

    def __init__(self):
        self._balance=None

    @property
    def balance(self):
        print(100*'-')
        print('Getter called')
        return self._balance
    
    #inforce validation of data before assignment no negative value can be assign to balance
    @balance.setter 
    def balance(self,value):
        print(100*'-')
        print("Setter Called")
        if value<0:
            raise ValueError("Negative Amount")
        self._balance=value

    @balance.deleter
    def balance(self):
        print(100*'-')
        print("Deleter called:")


b=BankAccount()
print(b.balance)
b.balance=2000
print(b.balance)
del b.balance