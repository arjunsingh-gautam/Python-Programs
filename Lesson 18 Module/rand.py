# Here we learning about random module and it's functions
from random import *
#1. random() --> generate random float value in between 0 to 1 {not inclusive}
print(random())

#2. uniform() --> generate random float value in between two given numbers (not inclusive)
print(uniform(1,100))

# randint() --> generare a random int value between two given numbers {exclusive}
print(randint(1,1000))

# randrange(beg,end{not inclusive},step) --> genrate a random int no. in the given range 
print(randrange(1,11,2)) # --> random in range ==> [1,3,5,7,9]

# choice --> return a random element from a tuple or list passed as argument
l=['a',True,3+4j,'Bunny','Sunny',5.34]
print(choice(l))

