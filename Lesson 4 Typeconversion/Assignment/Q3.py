option=int(input("Enter an option:"))
match option:
    case 1:
        print("Area of circle")
        r=int(input("Enter radius of circle:"))
        print("Area of circle is:",3.14*r*r)
    case 2:
        print("Square of number")
        num=int(input("Enter number:"))
        print("Square of number is:",num**2)
    case 3:
        print("Area of Triangle")
        b=int(input("Enter base of triangel:"))
        h=int(input("Enter of height of triangle:"))
        print("Area of triangle is:",0.5*b*h)
    case 4:
        print("Simple Interest")
        p=int(input("Enter printciple amount:"))
        rate=int(input("Enter rate of interest:"))
        t=int((input("Enter duration:")))
        result=(p*rate*t)/100
        print("Simple interest is:",result)

