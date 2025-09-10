class Teacher:
    '''This a class used for demo''' #doc string
    def __init__(self): # constructor
        print("Constructor executed...")
        self.name ="Durga" # variables
        self.id="A-101"
        self.salary=20000
    def intro(self): # method->function defined inside a class
        print("My name is ",self.name)
        print("My id is ",self.id)
        print("My salary is ",self.salary)

t1=Teacher() #t(reference variable)--> Object
""" print(t.__doc__)
print(t.name)
print(t.id)
print(t.salary)
t.intro() """ # Class method calling
t2=Teacher()
print(f"id of t1: {id(t1)} type of t1:{type(t1)}")
print(f"id of t2: {id(t2)} type of t2:{type(t2)}")

""" class Teacher has:
1. 3 variable
2. 2 methods out of which one is __init__ method
3. We have two instances of class t1 and t2 """