# Variable Length Argument
def Average(*num): # *variable_name ---> used to tell interpreter about variable length argument
    a=sum(num)/len(num)
    print(num,type(num))
    return a

print("Average is:",Average(10,20))
print("Average is:",Average(10,20,30))
print("Average is:",Average(10,20.33,23,13))

