# In thise we will demonstrate Nested classes in Python

class Car:
    car_company='Ferrari'
    car_model='Ferrari Romero'

    def __init__(self):
        self.owner=input("Enter Owner name:")

    def enter_engine_details(self):
        option=input("Enter y to build custom engine else no:")
        if option=='y':
            obj=Car.Car_Engine()
            return obj
            
    def get_engine_details(self):
        obj=self.enter_engine_details()
        for k in obj.__dict__.keys():
            self.__dict__[k]=obj.__dict__[k]
            

    def get_details(self):
        print(f"Car Owner:{self.owner}")
        print(f"Car Model:{self.car_model}")
        print(f"Car Engine Details:{self.engine_spec}")

    class Car_Engine:
        
        def __init__(self):
            self.engine_spec=input("Enter Engine Description:")

        
c1=Car()
print(c1.__dict__)
print(c1.__class__)
c1.get_engine_details()
print(c1.__dict__)
print(c1.__class__)
c1.get_details()