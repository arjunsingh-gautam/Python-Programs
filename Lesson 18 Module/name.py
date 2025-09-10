# Here we understan application of __name__:
def f1():
    print("f1 function")

def f2():
    print("f2 function")

def f3():
    print("f3 function")

def f4():
    print("f4 function")

if __name__=="__main__": # Prevent indirect execution of this function when imported somewhere else
    f1()
    f2()
    f3()
    f4()