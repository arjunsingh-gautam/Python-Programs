# Write a python script which takes a three digit number from the user and displays only its first digit.
num=int(input("Enter a three digit  number:"))
result1=num/100
print(" the first digit of the number is",int(result1))
result2=(int(num/10))%10
print(" the middle digit of the number is",int(result2))
result3=num%10
print(" the last digit of the number is",int(result3))
