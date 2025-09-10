# making this program to understand how to use match statement

print("""         Press '1' for addition
         Press '2' for subtraction
         Press '3' for multiplication
         Press '4' for division""")
option=int(input("Enter your chosen option:"))
match option:
    case 1:
        num_1=float(input("Enter your first number:"))
        num_2=float(input("Enter your second number:"))
        Result= num_1+num_2
        print("Sum is %f"%Result)
    case 2:
        num_1=float(input("Enter your first number:"))
        num_2=float(input("Enter your second number:"))
        Result= num_1-num_2
        print("Subtraction is %f"%Result)
    case 3:
        num_1=float(input("Enter your first number:"))
        num_2=float(input("Enter your second number:"))
        Result= num_1*num_2
        print("Product is %f"%Result)
    case 4:
        num_1=float(input("Enter your first number:"))
        num_2=float(input("Enter your second number:"))
        Result= num_1/num_2
        print("Resul is %f"%Result)
    case _:
        print("Please enter correct option")