# In this we will implement raise keyword:

balance=int(input("Enter your balance:"))

def check_balance(balance):
    if balance<0:
        raise ValueError
    else: 
        print(f"Your balance is:{balance}")

try:
    check_balance(balance)
except ValueError:
    print(f"Your balance:{balance} is less than zero")