# range() 
num=int(input("Enter the number of naturals no. you want to print:"))
option=int(input("Enter an option from 1-5:"))
match option:
    case 1:
        for x in range(1,num+1):
            print(x,end=',')
    case 2:
        for x in range(1,num+1):
            print(x**2,end=',')
    case 3:
        for x in range(1,num+1):
            print(2*x,end=',')

