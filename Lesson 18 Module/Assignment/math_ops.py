print("math_ops module loaded")
PI=3.14
def add(a,b):
    return a+b

def test():
    print("Testing add:",add(2,3))

if __name__=='__main__':
    test()
else:
    print("Can't execute test since script is run by external script using import")