# <span style="color:#2E86C1"><b>Understanding `__get__` and `__set__` — Descriptor Mechanics in Depth</b></span>

We’ll explain:

1. Exact syntax of `__get__` and `__set__`
2. What arguments they receive
3. When Python calls each
4. Data vs Non-data descriptor difference
5. Complete attribute resolution rules
6. Step-by-step dry run examples

---

# <span style="color:#AF7AC5"><b>1️⃣ Syntax of `__get__` and `__set__`</b></span>

A descriptor is any object that defines one or more of:

```python
def __get__(self, instance, owner):
    ...

def __set__(self, instance, value):
    ...

def __delete__(self, instance):
    ...
```

Where:

- `self` → descriptor instance
- `instance` → object being accessed (or None if accessed via class)
- `owner` → class of the instance

---

# <span style="color:#48C9B0"><b>2️⃣ What Happens During Attribute Access?</b></span>

When you write:

```python
obj.attr
```

Python internally performs:

```text
type(obj).__dict__['attr'].__get__(obj, type(obj))
```

If the attribute in class is a descriptor.

---

When you write:

```python
obj.attr = value
```

Python internally performs:

```text
type(obj).__dict__['attr'].__set__(obj, value)
```

If it is a **data descriptor**.

---

# <span style="color:#E74C3C"><b>3️⃣ Example of Descriptor with **get** and **set**</b></span>

```python
class Positive:
    def __get__(self, instance, owner):
        print("Getter called")
        return instance._value

    def __set__(self, instance, value):
        print("Setter called")
        if value < 0:
            raise ValueError("Must be positive")
        instance._value = value
```

Using it:

```python
class Product:
    price = Positive()

    def __init__(self, price):
        self.price = price
```

---

# <span style="color:#5DADE2"><b>4️⃣ Dry Run — Assignment</b></span>

```python
p = Product(100)
```

Inside `__init__`:

```python
self.price = 100
```

Python checks:

1. Does class have attribute `price`?
   ✔ Yes.
2. Is it a descriptor?
   ✔ Yes.
3. Does it have `__set__`?
   ✔ Yes → DATA descriptor.

So instead of writing to instance dictionary:

Python calls:

```python
Positive.__set__(descriptor_instance, p, 100)
```

---

# <span style="color:#BB8FCE"><b>5️⃣ Dry Run — Access</b></span>

```python
print(p.price)
```

Python checks:

1. Does class have descriptor named `price`?
   ✔ Yes.
2. Does it have `__get__`?
   ✔ Yes.

So calls:

```python
Positive.__get__(descriptor_instance, p, Product)
```

---

# <span style="color:#F5B041"><b>6️⃣ Data Descriptor vs Non-Data Descriptor</b></span>

### ✔ Data Descriptor

Has:

```python
__get__ and __set__
```

OR

```python
__get__ and __delete__
```

### ✔ Non-Data Descriptor

Has:

```python
__get__ only
```

---

# <span style="color:#58D68D"><b>7️⃣ Why Does This Matter?</b></span>

Because Python lookup order depends on this.

---

# <span style="color:#AF7AC5"><b>8️⃣ Attribute Lookup Rules (Important)</b></span>

When reading:

```python
obj.attr
```

Python follows this order:

### 1️⃣ Data Descriptor

If class attribute is data descriptor → call `__get__`

### 2️⃣ Instance Dictionary

If exists in `obj.__dict__`, return it

### 3️⃣ Non-Data Descriptor

If class attribute is non-data descriptor → call `__get__`

### 4️⃣ Class Attribute

Return raw value

---

When writing:

```python
obj.attr = value
```

Python follows:

### 1️⃣ If class attribute is data descriptor

Call `__set__`

### 2️⃣ Otherwise

Write to `obj.__dict__`

---

# <span style="color:#E74C3C"><b>9️⃣ Example Showing Difference</b></span>

## Non-Data Descriptor Example

```python
class NonData:
    def __get__(self, instance, owner):
        return 10

class A:
    x = NonData()

a = A()
print(a.x)   # 10
a.x = 50
print(a.x)   # 50
```

Why?

Because non-data descriptor does NOT intercept writes.

Instance dictionary overrides it.

---

## Data Descriptor Example

```python
class Data:
    def __get__(self, instance, owner):
        return 10

    def __set__(self, instance, value):
        print("Intercepted")

class A:
    x = Data()

a = A()
a.x = 50   # Calls __set__
print(a.x) # Still 10
```

Here instance dictionary cannot override descriptor.

---

# <span style="color:#5DADE2"><b>🔟 How Python Knows When To Call Setter vs Getter?</b></span>

It depends on operation type:

### Reading:

```python
obj.attr
```

→ Python checks for `__get__`.

### Writing:

```python
obj.attr = value
```

→ Python checks for `__set__`.

### Deleting:

```python
del obj.attr
```

→ Python checks for `__delete__`.

So the action determines which method is triggered.

---

# <span style="color:#BB8FCE"><b>1️⃣1️⃣ Why Data Descriptor Has Priority?</b></span>

Because:

If instance dictionary was checked first:

- Descriptor validation could be bypassed.
- Encapsulation broken.

So Python enforces:

```text
Data Descriptor > Instance Dict > Non-Data Descriptor
```

---

# <span style="color:#F5B041"><b>1️⃣2️⃣ Real-World Descriptor Examples</b></span>

| Feature      | Descriptor Type     |
| ------------ | ------------------- |
| property     | Data descriptor     |
| classmethod  | Non-data descriptor |
| staticmethod | Non-data descriptor |
| Methods      | Non-data descriptor |

Function objects implement `__get__` only.

That’s why methods auto-bind.

---

# <span style="color:#2E4053"><b>Final Conceptual Summary</b></span>

- `__get__` handles attribute access.
- `__set__` handles assignment.
- Data descriptor has `__set__` → intercepts writes.
- Non-data descriptor has only `__get__`.
- Python attribute lookup prioritizes data descriptors.
- This system enables properties, method binding, validation, ORMs, and advanced frameworks.

Descriptors are the foundation of Python’s attribute control system.

---

If you want next, we can:

- Visualize full attribute resolution algorithm
- Explore interaction with `__getattribute__`
- Implement advanced ORM-style descriptor
- Dive into CPython C-level lookup logic

You are now understanding Python at object model core level.
