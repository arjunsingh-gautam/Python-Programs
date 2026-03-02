# Better Design:
class Car:
    car_company = "Ferrari"
    car_model = "Ferrari Romero"

    def __init__(self):
        self.owner = input("Enter Owner name:")
        self.engine = None

    def enter_engine_details(self):
        option = input("Enter y to build custom engine else no:")
        if option == 'y':
            self.engine = Car.Car_Engine()

    def get_details(self):
        print(f"Car Owner: {self.owner}")
        print(f"Car Model: {self.car_model}")
        if self.engine:
            print(f"Car Engine Details: {self.engine.engine_spec}")
        else:
            print("No Engine Info")

    class Car_Engine:
        def __init__(self):
            self.engine_spec = input("Enter Engine Description:")