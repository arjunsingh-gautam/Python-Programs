# Module Reloading
import importlib # imp is deprecated in version 3.4 use importlib
import time 
import module3
module3.add(10,20)
print("Program entering into sleeping state")
time.sleep(45) # I will update module3 with product() function this program execution has been stopped
print("Just wake up and calling updated function")

# import module3 # Error: Since here no reloading of update version will take place since module is load only once by PVM

# To solve the reload issue we can import reload() function from imp module
importlib.reload(module3)
module3.product(10,20)