# How super() is used in case of Multiple Inheritence

class Shape:
    def draw(self):
        print("Draw a shape")

class Rectangle:
    def draw(self):
        print("Draw rectangle")

class Square(Shape,Rectangle): # Here Shape is inherited as 1st Base class therefore super will call it's method
    def draw(self):
        print("Draw Square")
        super().draw() # draw() method from Shape will be called as it is inherited first

        # To call draw() from Rectangle
        Rectangle.draw(self) # Here self must compulsary since we are calling an instance method

s=Square()
s.draw()