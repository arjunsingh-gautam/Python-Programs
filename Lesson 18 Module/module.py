# To check use of __name__:
# __name__ help us to check whether module is directly executed or indirectly by importing
if __name__=='__main__':
    print("module executed directly just like main program") # in direct execution __name__=__main__
else:
    print("module executed indirectly because of import statement") # indirect executiong by import __name__='__modulename__'