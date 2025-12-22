# dir()--> List out all the members of a module, return a  `list`

import sys
print(sys.modules.keys()) # Does not contain calci as key since not imported  # Return: False
import calci
print(sys.modules.keys()) # Contains calci as key since now cacli module object is loaded in memory # Return True
print()
l=dir(calci)
print(l)

#help()--> Provide complete documentation about members of a module
help(calci)