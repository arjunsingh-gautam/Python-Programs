x=[1,2]
print(x)
print(id(x))
del x # delete the reference variable x but int object is not deleted from private heap space
import gc
gc.collect()  # WHen garbage collector runs id of [1,2] changes since a new object is created as previous one forcefully get released by garbage collector but this behavior is only witness with list for other there is no change in id after garbage collection also
# Different id for list object is because they are not cached by the Interpreter therefore after garbage collection they are created once again
y=[1,2]
print(id(y)) # here y is pointing to same object which is previously pointed by x

# object have only id

# Now run it for another sequen type tuple:(1,2): id remains same after garbage collection
# Reason: CPython caches mutable object like tuple,string therefore still referenced by cache even after garbage collection
