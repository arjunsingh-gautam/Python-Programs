# Module Naming Conflicts

# Program-1
# from module1 import *
# from module2 import *
# add(10,20) # This function is called from Module2 which is imported latter

# Program-2
# from module1 import*
# from module2 import*
# def add(a,b):
#     print("current module add function")
#     print("The sum is:",a+b)
# add(10,20)

# Note: incase of naming conflicts python call the recent copy of that variable or function
# To solve this we can you Aliasing concept