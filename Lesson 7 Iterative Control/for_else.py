"""Print all the elements in a string but stop printing if 'r' appeared in the sequence.If all the characters successfully printed then print the message : All the characters processed """
input_string=input("Enter the string:")
for x in input_string:
    if x=='r':
        print(f"All character are not processed\nCharacter proccessed till: {x}")
        break
    print(x)
else:
    print("All the characters processed")