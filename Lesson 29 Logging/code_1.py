# Logging using in Print Statements

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        print("Error: Division by zero")
        return None
    return a / b

# Example usage
num1 = 10
num2 = 5

print(f"Adding {num1} and {num2}: {add(num1, num2)}")
print(f"Subtracting {num2} from {num1}: {subtract(num1,
    num2)}")
print(f"Multiplying {num1} and {num2}: {multiply(num1, num2)}")
print(f"Dividing {num1} by {num2}: {divide(num1, num2)}")
print(f"Dividing {num1} by 0: {divide(num1, 0)}")