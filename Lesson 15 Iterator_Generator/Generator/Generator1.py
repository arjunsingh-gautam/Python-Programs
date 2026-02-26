# In this module we will implement Generator in Python

# Generator: Is a special function ie contains yield keyword instead of return
# In generator the computation is suspended until resume by next() or send()    

def square_numbers(n):
    for i in range(1,n+1):
        yield i**2
gen=square_numbers(5) # Return Generator object ready to be used
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

# Generator using Comprehension

cube_gen=(x**3 for x in range(4))
print(next(cube_gen)) 
print(next(cube_gen)) 
print(next(cube_gen)) 
print(next(cube_gen)) 
print(next(cube_gen)) 



