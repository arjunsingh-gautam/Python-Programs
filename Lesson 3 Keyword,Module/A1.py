# We want to print x instance object from A2.py in A1.py
# We use 'import' Keyword
#Method 1
"""import A2
print(A2.x)"""


#Method 2
"""from A2 import x
print(x)"""
##################################################################################################################
#If A1.py already has 'x=10' and we want to print 'x=5' of A2.py in it
#Method1
"""x=10
import A2
print(x)
print(A2.x)"""

#Method-2
"""x=10
from A2 import x as X
print(x)
print(X)"""
#################################################################################################################
"""from A2 import z
z=17
print(z) """
# Output: 17

"""z=17
from A2 import z
print(z)"""
#Output:34
