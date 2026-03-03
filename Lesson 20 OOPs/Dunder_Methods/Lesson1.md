# <span style="color:#2E86C1"><b>Dunder Methods in Python — Complete Deep Dive</b></span>

We’ll cover:

1. What dunder (magic) methods are
2. Why they exist (causality)
3. How they work internally (execution flow)
4. Categories every Python programmer must know
5. Dry-run examples with mechanics
6. How Python dispatches them internally
7. Best practices

---

# <span style="color:#AF7AC5"><b>1️⃣ What Are Dunder Methods?</b></span>

“Dunder” = **Double UNDERscore**

They are special methods like:

```python
__init__
__str__
__add__
__len__
__getitem__
```

They are not meant to be called directly.

Instead:

> Python calls them automatically when certain operations happen.

Example:

```python
len(obj)
```

Actually calls:

```python
obj.__len__()
```

---

# <span style="color:#48C9B0"><b>2️⃣ Why Do Dunder Methods Exist?</b></span>

They allow:

✔ Operator overloading
✔ Custom object behavior
✔ Integration with Python built-ins
✔ Protocol implementation
✔ Making objects act like built-ins

Without dunder methods:

- Objects would be plain data holders.
- No polymorphism with built-in syntax.
- `+`, `len`, `print`, iteration would not work on custom classes.

---

# <span style="color:#E74C3C"><b>3️⃣ How They Work Internally</b></span>

When Python sees an operation:

```python
a + b
```

It does NOT directly evaluate it.

Internally, Python does roughly:

```python
type(a).__add__(a, b)
```

If not implemented, it tries reverse method:

```python
type(b).__radd__(b, a)
```

So operators map to dunder methods.

This is called **operator dispatch**.

---

# <span style="color:#5DADE2"><b>4️⃣ Categories of Important Dunder Methods</b></span>

---

## 🔹 A. Object Creation & Lifecycle

| Method     | Purpose             |
| ---------- | ------------------- |
| `__new__`  | Create instance     |
| `__init__` | Initialize instance |
| `__del__`  | Destructor          |

---

## 🔹 B. String Representation

| Method       | Purpose                  |
| ------------ | ------------------------ |
| `__str__`    | User-friendly print      |
| `__repr__`   | Developer representation |
| `__format__` | Custom formatting        |

---

## 🔹 C. Arithmetic Operators

| Operator | Method         |
| -------- | -------------- |
| `+`      | `__add__`      |
| `-`      | `__sub__`      |
| `*`      | `__mul__`      |
| `/`      | `__truediv__`  |
| `//`     | `__floordiv__` |
| `%`      | `__mod__`      |
| `**`     | `__pow__`      |

Reverse versions:

```python
__radd__, __rmul__, etc.
```

---

## 🔹 D. Comparison Operators

| Operator | Method   |
| -------- | -------- |
| `==`     | `__eq__` |
| `!=`     | `__ne__` |
| `<`      | `__lt__` |
| `<=`     | `__le__` |
| `>`      | `__gt__` |
| `>=`     | `__ge__` |

---

## 🔹 E. Container Protocol

| Operation    | Method         |
| ------------ | -------------- |
| `len(obj)`   | `__len__`      |
| `obj[i]`     | `__getitem__`  |
| `obj[i] = x` | `__setitem__`  |
| `del obj[i]` | `__delitem__`  |
| `x in obj`   | `__contains__` |

---

## 🔹 F. Iteration Protocol

| Operation   | Method     |
| ----------- | ---------- |
| `iter(obj)` | `__iter__` |
| `next(obj)` | `__next__` |

---

## 🔹 G. Callable Objects

| Operation | Method     |
| --------- | ---------- |
| `obj()`   | `__call__` |

---

## 🔹 H. Context Managers

| Operation | Method                  |
| --------- | ----------------------- |
| `with`    | `__enter__`, `__exit__` |

---

## 🔹 I. Attribute Access Control

| Operation | Method             |
| --------- | ------------------ |
| Access    | `__getattribute__` |
| Fallback  | `__getattr__`      |
| Set       | `__setattr__`      |
| Delete    | `__delattr__`      |

---

# <span style="color:#BB8FCE"><b>5️⃣ Dry Run Examples with Execution Flow</b></span>

---

## Example 1 — `__add__`

```python
class Vector:
    def __init__(self, x):
        self.x = x

    def __add__(self, other):
        return Vector(self.x + other.x)
```

Execution:

```python
v1 = Vector(5)
v2 = Vector(3)
v3 = v1 + v2
```

Flow:

1. Python sees `v1 + v2`
2. Calls:

```python
Vector.__add__(v1, v2)
```

3. Returns new object.

---

## Example 2 — `__len__`

```python
class MyList:
    def __init__(self, items):
        self.items = items

    def __len__(self):
        return len(self.items)
```

Execution:

```python
len(obj)
```

Internally:

```python
obj.__len__()
```

---

## Example 3 — `__getitem__`

```python
class MyContainer:
    def __getitem__(self, index):
        return index * 2
```

Execution:

```python
obj[5]
```

Internally:

```python
obj.__getitem__(5)
```

---

## Example 4 — `__call__`

```python
class Multiplier:
    def __init__(self, n):
        self.n = n

    def __call__(self, value):
        return self.n * value
```

Execution:

```python
m = Multiplier(3)
m(10)
```

Internally:

```python
m.__call__(10)
```

---

## Example 5 — Iteration

```python
class Counter:
    def __init__(self, n):
        self.n = n
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.n:
            self.current += 1
            return self.current
        raise StopIteration
```

Execution:

```python
for x in Counter(3):
```

Internally:

1. `iter(obj)` → calls `__iter__`
2. Loop calls `__next__` repeatedly
3. Stops at `StopIteration`

---

# <span style="color:#F5B041"><b>6️⃣ Internal Dispatch Mechanism</b></span>

Important detail:

Python does NOT always call:

```python
obj.__add__()
```

It often calls:

```python
type(obj).__add__(obj, other)
```

This avoids instance dictionary override issues.

So operator dispatch is based on class type.

---

# <span style="color:#58D68D"><b>7️⃣ Why Direct Call to obj.**add**() Is Not Recommended</b></span>

Because:

- Special methods are looked up on type, not instance.
- Calling directly may bypass Python’s dispatch logic.

Example:

```python
a + b
```

Is not same as:

```python
a.__add__(b)
```

Python uses internal slot mechanism.

---

# <span style="color:#EC7063"><b>8️⃣ Important Internal Concept: Slots</b></span>

At CPython level:

Each special method maps to a C-level slot like:

```
tp_add
tp_iter
tp_call
```

These slots are used for speed.

So dunder methods integrate into interpreter execution engine.

---

# <span style="color:#3498DB"><b>9️⃣ Why Dunder Methods Are Powerful</b></span>

They allow custom objects to:

✔ Behave like numbers
✔ Behave like containers
✔ Behave like functions
✔ Behave like context managers
✔ Behave like iterators

They enable polymorphism with built-in syntax.

---

# <span style="color:#8E44AD"><b>🔟 Best Practices</b></span>

✔ Implement `__repr__` for debugging
✔ Keep `__str__` user-friendly
✔ Keep arithmetic operations pure
✔ Maintain consistency between comparison methods
✔ Raise appropriate exceptions
✔ Do not overuse magic

---

# <span style="color:#2E4053"><b>Final Summary</b></span>

Dunder methods:

- Are special hooks used by Python’s interpreter.
- Map language operations to method calls.
- Enable operator overloading.
- Implement protocols (iteration, context, container, callable).
- Are dispatched through class-level lookup and C-level slots.

They are how Python makes objects behave like built-in types.

---
