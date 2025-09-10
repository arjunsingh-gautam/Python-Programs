# Write a program to count 'a' in a give string using for loop
input_string=input("Enter a string:")
count=0
for x in input_string:
    if x=='a':
        count+=1
print(count)