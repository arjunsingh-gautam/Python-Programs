# Generate a 6 digit random number to used as OTP
from random import*
OTP=str(randint(0,9))+str(randint(0,9))+str(randint(0,9))+str(randint(0,9))+str(randint(0,9))+str(randint(0,9))
print(f"The OTP:{(OTP)}")

# Generate 6 char password in which 2,4,6 are alphabets
Password=str(randint(0,9))+choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")+str(randint(0,9))+choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")+str(randint(0,9))+choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
print("The Password:",Password)