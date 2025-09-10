# Write a python script to check whether a given quadratic equation has two real & distinct roots, real & equal roots or imaginary roots
import math
print("Quadratic number is of the form ax^2+bx+c")
a=int(input("Coefficient of x^2:"))
b=int(input("Coefficient of x:"))
c=int(input("Constant value is:"))
D=b**2-4*a*c
if (D)>0:
    print("Roots are real and unequal")
elif D==0:
    print("Roots are real and equal")
else:
    print("Roots are imaginary")
