# Alternative constructor using class method:
class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

    def __call__(self, *args, **kwds):
        print(f"Employee Name:{self.name}\nEmployee Salary:{self.salary}")
        
    @classmethod # Alternative constructor
    def alternative_constructor(cls,emp_str):
        name,salary=emp_str.split('-')
        return cls(name,salary)
    

e1=Employee('John Doe',50000)
e1()
e2=Employee.alternative_constructor('Corey Macgill-70000')
e2()