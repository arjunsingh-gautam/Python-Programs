# continue statement demonstration
i=1
while i<11:
    if i%2==0: # prints odd numbers and skip even numbers
        i+=1
        continue
    print(i)
    i+=1
print("loop terminates at:",i)