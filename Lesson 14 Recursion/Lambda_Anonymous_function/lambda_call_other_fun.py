# In this example we will se how we call user defined function inside lambda expressions
def add(t):
    return sum(t)

print((lambda*x:add(x))(1,2,4,5,6,7,9)) # The passed function alwas of type Return TSRS

def maxnum(t):
    return max(t)

print((lambda *x:maxnum(x))(1,4,332,2452,42))
