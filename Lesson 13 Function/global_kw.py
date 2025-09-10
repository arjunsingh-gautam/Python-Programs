# In this program how we can use global keyword to modify global variable inside function scope
var1=0
var2=0
def modify():
    global var1 # Now any change to var1 in function scope is change to its global definition
    var1+=1 # Here 
    var2=0 ## This local variable in scope of function
    var2+=1
modify()
print(f"Value of var1={var1}\nValue of var2={var2}")