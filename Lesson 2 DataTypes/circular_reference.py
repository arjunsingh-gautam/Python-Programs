import sys

a = [1, 2]
b = [3, 4]

print(sys.getrefcount(a))  # Output: 2 (One from 'a', one from function argument)
print(sys.getrefcount(b))  # Output: 2

# Creating circular reference
a.append(b)
b.append(a)

print(sys.getrefcount(a))  # Output: 3 (Increased because 'b' now refers to 'a')
print(sys.getrefcount(b))  # Output: 3 (Increased because 'a' now refers to 'b')

# Deleting variables
del a
del b  # Still not freed due to circular reference
print(sys.getrefcount([1, 2]))  
print(sys.getrefcount([3,4]))
import gc

""" gc.collect()  # Force garbage collection and remove circular reference and free memory """

# Manually break the circular reference and then delete references
""" a[-1] = None  # Remove reference to b
b[-1] = None  # Remove reference to a

del a
del b  # Now reference count drops to zero, and memory is freed """




# Here is the **memory table representation** for your **circular reference example**:



# Explanation of Circular Reference:



"""

## **🔹 Memory Table Before Circular Reference**
| Variable | Object (Value) | Memory Address | Reference Count |
|----------|---------------|---------------|----------------|
| `a`      | `[1, 2]`      | `0xAAA`       | **1** |
| `b`      | `[3, 4]`      | `0xBBB`       | **1** |

- `a` points to `[1, 2]` with **1 reference**.
- `b` points to `[3, 4]` with **1 reference**.

---

## **🔹 Memory Table After Circular Reference**
| Variable | Object (Value) | Memory Address | Reference Count |
|----------|---------------|---------------|----------------|
| `a`      | `[1, 2, →0xBBB]`  | `0xAAA`  | **2** (One from `a`, one from `b`) |
| `b`      | `[3, 4, →0xAAA]`  | `0xBBB`  | **2** (One from `b`, one from `a`) |

- `a` now contains **a reference to `b`** (`→0xBBB`).
- `b` now contains **b reference to `a`** (`→0xAAA`).
- **Both objects now have 2 references!** (One from their variable, one from each other)

---

## **🔹 Memory Table After `del a` and `del b`**
| Variable | Object (Value) | Memory Address | Reference Count |
|----------|---------------|---------------|----------------|
| `[1, 2, →0xBBB]`  | `[1, 2, →0xBBB]` | `0xAAA` | **1** (Only from `b`) |
| `[3, 4, →0xAAA]`  | `[3, 4, →0xAAA]` | `0xBBB` | **1** (Only from `a`) |

- Even though `a` and `b` are deleted, their **objects still exist** in memory because they **point to each other**.
- **Their reference counts never reach 0**, so they are **not freed immediately**.

---

## **🔹 How Does Garbage Collector Handle This?**
1. **Python detects the circular reference** (objects refer to each other).
2. **If there are no outside references**, the garbage collector **removes both**.
3. **If `gc.collect()` is called manually**, Python **forcibly clears the cycle**.

---

### **🔹 Solution: Breaking Circular Reference**
```python
a[-1] = None  # Break reference inside list
b[-1] = None  # Break reference inside list

import gc
gc.collect()  # Now memory is freed
```

🚀 **Now, `gc.collect()` successfully removes the circular reference!**

"""