# This program check whether id() return memory address in cpython
import ctypes

x = 42
print(id(x))  # Python's unique identifier
address_x=id(x)
print(ctypes.cast(address_x, ctypes.py_object).value)  # Access object using memory address
