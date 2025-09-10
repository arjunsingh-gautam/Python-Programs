# <span style="color:#003566"> **Destructors in Python and Garbage Collector**</span>

---

## 1. Purpose

- **Constructor**: initializes the object when it is created.
- **Destructor**: de-allocates resources when the object is destroyed.
- In Python, object destruction is **handled automatically** by the Garbage Collector (GC), which reclaims memory of unreferenced objects.

---

## 2. Definition of Destructor

A **Destructor** is a special method named `__del__()` in Python.
It is **called automatically by the Garbage Collector** just before the object is destroyed from memory.

### Syntax:

```python
def __del__(self):
    # cleanup code
    print("Destructor called, object deleted")
```

---

## 3. When is the Destructor Called?

The destructor is invoked by the **Garbage Collector** in these cases:

1. **Automatic Garbage Collection** (default):

   - At the end of program execution, all remaining objects are deleted.
   - GC automatically calls destructors of objects.

2. **Forced Garbage Collection by assigning None**:

   ```python
   obj = MyClass()
   obj = None   # Now no references exist, object is destroyed
   ```

3. **Forced Garbage Collection by using `del` keyword**:

   ```python
   obj = MyClass()
   del obj   # Explicitly deletes reference, triggering destructor
   ```

---

## 4. Example: Destructor in Action

```python
class Demo:
    def __init__(self, name):
        self.name = name
        print(f"Object {self.name} created")

    def __del__(self):
        print(f"Destructor called, {self.name} deleted")

# Main Program
d1 = Demo("Obj1")
d2 = Demo("Obj2")

d1 = None      # Force garbage collection
del d2         # Another way to force garbage collection

print("End of Program")
```

### Output:

```
Object Obj1 created
Object Obj2 created
Destructor called, Obj1 deleted
Destructor called, Obj2 deleted
End of Program
```

---

## 5. Garbage Collector in Python

### Internal Working:

- Python maintains **reference counting** for every object.
- Each time a variable references an object, its reference count increases.
- When reference count drops to **0**, the object is considered unreachable and collected by the GC.
- The **GC module** (`import gc`) provides control functions:

  - `gc.isenabled()` → check if GC is enabled.
  - `gc.enable()` → enable GC manually.
  - `gc.disable()` → disable GC manually.

### Example:

```python
import gc

print(gc.isenabled())   # True (by default enabled)
gc.disable()
print(gc.isenabled())   # False
gc.enable()
print(gc.isenabled())   # True
```

---

## 6. Do We Need to Write Destructors in Python?

- **Not mandatory**: Python already has an automatic Garbage Collector that destroys unused objects.
- You **write destructors only** when you need to perform **explicit cleanup** tasks like:

  - Closing database connections
  - Releasing file handles
  - Disconnecting from network sockets

- In most cases, using **context managers (`with` statement)** is preferred over destructors for resource management.

---

## 7. How Destructor Works Internally

1. Object created → Reference count = 1
2. Additional references → count increases.
3. References deleted or reassigned → count decreases.
4. When count = 0 → object becomes unreachable.
5. GC calls `__del__()` before reclaiming memory.

---

## 8. Precautions & Best Practices

### Precautions:

1. Do not **rely on exact timing** of destructor calls:

   - GC may delay collection.
   - In circular references, `__del__` may never be called.

2. Do not perform critical operations inside destructors (e.g., important database commits).
3. Be careful when combining destructors with multithreading — object cleanup may be unpredictable.

### Best Practices:

1. Prefer **context managers (`with` statement)** for resource management over destructors.
   Example:

   ```python
   with open("file.txt") as f:
       data = f.read()
   # File automatically closed, no need for __del__
   ```

2. Use `__del__` only for non-trivial cleanup when context managers or `try/finally` blocks are not feasible.
3. Avoid **circular references** (objects referring to each other), since destructors may not get called.

---

# ✅ Summary

- **Destructor** = `__del__()` method, called by **Garbage Collector** when object is deleted.
- **GC** works via **reference counting** + **cycle detection**.
- Destructor can be triggered:

  - Automatically at program end
  - By setting object to `None`
  - By using `del` keyword

- Writing destructors is **optional** in Python (unlike C++).
- Prefer **context managers** for resource cleanup.

---
