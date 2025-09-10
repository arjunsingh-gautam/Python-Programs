# The predefined variable like __doc__,__name__,__annotations__,__cached__,__loader__ are used by PVM or programmer if required

''' This program is about predefine variable return by dir()''' # documentation string
#__doc__ --> The variable hold documentation string
print(__doc__)

#__file__ --> Provide the name of current file
import os
print(f"File Name: {__file__}")
print(f"Absolut Path:{os.path.abspath(__file__)}")
print(f"Directory Name: {os.path.dirname(os.path.abspath(__file__))}")

#__name__: We can determine wheter a module is executed directly or indirectly 
import module
