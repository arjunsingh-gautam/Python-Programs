# In this module we will implement namedtuple

from collections import namedtuple

Color=namedtuple('Color',['red','blue','green'])

color=Color(55,123,228)

print(color[0])
print(color.red)

