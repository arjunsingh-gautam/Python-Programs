# In this program we will se eg. of user defined higher order function in Python
def apply(func, value):
    return func(value)

def square(x):
    return x * x

print(apply(square, 5))   # 25
