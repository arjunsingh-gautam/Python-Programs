# Checking if a number is positive, negative, or zero using nested if-else statements

num = float(input("Enter a number: "))  # Taking input from the user

if num > 0:
    print("The number is positive.")
else:
    if num < 0:
        print("The number is negative.")
    else:
        print("The number is zero.")
