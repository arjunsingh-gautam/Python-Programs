def f1(): # generator function
    yield 10
    yield 30
    yield 40
    yield 98
it=f1() # generator object
print(next(it)) # runs the function f1() but first pauses after first yield 10 is executed
print(next(it)) # resumes and execute 2nd yield call of yield 20
print(next(it))
print(next(it))

for e in f1(): 
    print(e,end=' ')