import sys
import mypkg
print("mypkg" in sys.modules)
print(type(mypkg),id(mypkg))
import mypkg
print(type(mypkg),id(mypkg))
