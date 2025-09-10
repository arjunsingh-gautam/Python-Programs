# In this code we will se how we will create a multiplication table using oops

class Table:
    def __init__(self):
        self.num=int(input("Enter the no.:"))

    def get_value(self):
        print(f"Table of:{self.num}")

    def get_table(self):
        print("Table of {} is:".format(self.num))
        for x in range(1,11):
            print(f"{self.num} x {x} = {self.num*x}")

t1=Table()
t1.get_table()
t1.get_value()