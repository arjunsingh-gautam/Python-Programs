# here we check how eval() works
x=eval(input("Enter a option:"))
match x:
    case 2.14:
        print(x,type(x),sep='\n')
    case "-3":
        print(x,type(x),sep='\n')
    case True:
        print(x,type(x),sep='\n')


# eval() evaluate a string as string if provided as input in double qoutes ""