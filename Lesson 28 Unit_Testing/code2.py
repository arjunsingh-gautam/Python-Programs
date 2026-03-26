# Creating an Employee class and testing its methods
class Employee:
    raise_amount = 1.05 # class variable
    def __init__(self,first_name,last_name,salary):
        self.first_name=first_name
        self.last_name=last_name
        self.salary=salary

    @property
    def email(self):
        return f"{self.first_name.lower()}.{self.last_name.lower()}@company.com"
    
    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def apply_raise(self):
        self.salary=int(self.salary*self.raise_amount)
    