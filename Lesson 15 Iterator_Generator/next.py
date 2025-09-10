t1=(1,48,83,19,93)
it=iter(t1)

while True:
    try:
        print(next(it),end=' ')
    except StopIteration:
        break

# next()--> returns the element to which iterator is pointing and shift the pointer of iterator to next element
    