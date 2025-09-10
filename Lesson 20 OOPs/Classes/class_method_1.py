# In this program we will learn about class method in Python

class Employee:
    company_name="IBM" # class attribute

    def __init__(self,objinfo):
        self.objinfo=objinfo
        self.emp_name=''
        self.emp_dept=''
        self.emp_id=''
    
    @classmethod # class method
    def branch_details(cls):
        cls.branch_city="Bangalore" # class attribute created using cls
        Employee.branch_country="India" # class attribute created using class_name

    @classmethod # class method
    def get_branch_details(cls,obj):
        cls.branch_details()
        print('*'*50)
        print(f"{obj.objinfo} Employee Branch Details:")
        print(f"Company Name:{Employee.company_name}")
        print(f"Branch City:{cls.branch_city}")
        print(f"Branch Country:{Employee.branch_country}")
        print('*'*50)

    def emp_details(self):
        self.emp_name=input(f"Enter {self.objinfo} Employee name:")
        self.emp_dept=input(f"Enter {self.objinfo} Employee Department:")
        self.emp_id=int(input(f"Enter {self.objinfo} Employee ID:"))

    def get_emp_details(self):
        print('-'*50)
        print(f"Enter {self.objinfo} Employee Name:{self.emp_name}")
        print(f"Enter {self.objinfo} Employee Department:{self.emp_dept}")
        print(f"Enter {self.objinfo} Employee ID:{self.emp_id}")
        print('-'*50)

    def get_details(self,obj): # instance method
        # Employee.get_branch_details(obj)  # Class Method called using class_name
        # Above can also be called in following ways
        self.get_branch_details(obj) # Class Method called using self in instance method
        self.get_emp_details()

        
e1=Employee("First")
e2=Employee("Second")

e1.emp_details()
e2.emp_details()

e1.get_details(e1)
e2.get_details(e2)
    
