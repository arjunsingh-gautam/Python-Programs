# Through this user defined module we will understand the concept of reloading

"""This module contains maths utils like definitions of polygon area calculation and other standard mathematical values"""
PI=3.14
E=2.78
def circle(radius):
    return PI*pow(radius,2) 

def rectangle(length,breadth):
    return length*breadth

def square(side):
    return side**2
# change made later
def triangle(base,height):
    return 0.5*base*height
def cube(side):
    return side**3