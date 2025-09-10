# # # # # # # # if statement

# # num=int(input("Enter a number:"))
# # # # # # # if num%2==0:
# # # # # # #     print(num**2)
# # # # # # # if num%2!=0:
# # # # # # #     print(num**3)

# # # # # # # if else --> jab condition mutually exclusive ho
# # # # # # if num%2==0:   
# # # # # #     print(num**2)
# # # # # # else:
# # # # # #      print(num**3)

# # # # # # if elif else:  enter no div 2 3 
# # # # # #--> control flow will shift to other elif iff the elif or if is false
# # # # # if num%2==0:
# # # # #     print("Enter {} is divisible by 2".format(num))
# # # # # elif num%3==0:
# # # # #      print("Enter {} is divisible by 3".format(num))
# # # # # else: 
# # # # #      print("{} is neither divisible by 2 or 3".format(num))

# # # # # nested if : citizenship & vote eligible
# # # # country=input("Enter name of your country:")
# # # # COUNTRY="india"
# # # # if (country==COUNTRY):
# # # #     age=int(input("Enter your age:"))
# # # #     if age>=18:
# # # #         print("You are eligible to Vote")
# # # # print(id(country))
# # # # print(id(COUNTRY))

# # # # match statement
# # # num=int(input("Enter a number:"))
# # # match num%2:
# # #     case 0: 
# # #         print(f"{num} is even")
# # #     case _:
# # #         print(f"{num} is odd")

# # #eval()
# i=input("Enter :")
# match (i):
#     case True:
#         print("T",type(i))
#     case "a":
#         print("S",type(i))
#     case True:
#         print(id(i))
# #    case 5:
# # #         print("N",type(i))

# # # single line if else

# # print(f"{num} is even") if num%2==0 else print(f"{num} is odd")