# In this code we will see how list store reference to it's element in a contiguous block of memory and act as array of pointers:

# Code-1: Segmentation fault due to pointer arithmatic on reference address which is not allowed

""" import ctypes

lst = [10, 20, 30]

print(f"Memory address of the list object itself: {id(lst)}\n")

for i in range(len(lst)):
    # Get the address where the reference (pointer) is stored
    ref_address = id(lst) + ctypes.sizeof(ctypes.py_object) * (i + 1)
    
    # Get the actual stored address from the reference
    stored_address = ctypes.cast(ref_address, ctypes.POINTER(ctypes.py_object)).contents.value

    print(f"Index {i}: Reference Address = {ref_address}, Stored Object Address = {id(lst[i])}")


 """

""" The error **-1073741819** (or **0xC0000005**) is a **segmentation fault (access violation)**. It occurs because Python **does not allow direct pointer arithmetic on `id()` values** as I attempted in the previous approach. """


""" ### **Correct Approach to Print Reference Addresses & Stored Object Addresses**
Instead of computing pointer addresses manually, we should **use the `ctypes` module to directly access the memory locations stored in the list**. """

#### **Fixed Code:**

import ctypes

lst = [10, 20, 30]

print(f"Memory address of the list object itself: {id(lst)}\n")

for i in range(len(lst)):
    # Get address of the reference stored at list[i]
    ref_address = ctypes.addressof(ctypes.py_object(lst[i]))

    # Get the actual address of the object
    obj_address = id(lst[i])

    print(f"Index {i}: Reference Address = {ref_address}, Stored Object Address = {obj_address}")



"""
### **Explanation:**
1. **`id(lst)`** → Gives the memory address of the list itself.
2. **`ctypes.addressof(ctypes.py_object(lst[i]))`** → Gets the **memory address of the reference stored in the list**.
3. **`id(lst[i])`** → Gets the **actual memory address of the object** the reference is pointing to.

---

### **Example Output (May Vary)**
```shell
Memory address of the list object itself: 140719846211136

Index 0: Reference Address = 140719846217312, Stored Object Address = 9789504
Index 1: Reference Address = 140719846217320, Stored Object Address = 9789824
Index 2: Reference Address = 140719846217328, Stored Object Address = 9790144
```

Now, you can see:
- The **Reference Address** (Pointer in List) is different from the **Stored Object Address** (Actual Object).
- This proves that Python lists hold **references (pointers)** to objects, not the objects themselves.

"""