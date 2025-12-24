# In this we will understand the concept of re-raising:

def f1():
    f2() # calling f2

def f2():
    try:
        f3() # calling f3
    except ZeroDivisionError as z:
        print(f"Error:{z} catched in f2")
        raise

def f3():
    raise ZeroDivisionError('Division Failed')

try:
    f1() # calling f1
except:
    print("Catching re-raised error in main")
