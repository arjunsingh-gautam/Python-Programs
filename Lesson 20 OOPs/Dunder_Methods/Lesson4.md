# <span style="color:#2E86C1"><b>`__repr__` and `__str__` in Python — Internal Working & Deep Understanding</b></span>

We will cover:

1. What `__repr__` and `__str__` are
2. How Python decides which one to call
3. Internal execution flow (step-by-step dry run)
4. When to use each
5. Difference with clear examples
6. Best practices

---

# <span style="color:#AF7AC5"><b>1️⃣ What Is `__repr__`?</b></span>

`__repr__` is the **official string representation** of an object.

Goal:

> Represent object in an unambiguous way for developers.

It is mainly used for:

- Debugging
- Logging
- Interpreter display
- Recreating object (if possible)

---

# <span style="color:#48C9B0"><b>2️⃣ What Is `__str__`?</b></span>

`__str__` is the **informal / user-friendly representation**.

Goal:

> Produce readable output for end users.

Used when:

- Printing to console
- Displaying messages

---

# <span style="color:#E74C3C"><b>3️⃣ How Python Chooses Between Them</b></span>

When you do:

```python
print(obj)
```

Python does:

1️⃣ Try calling:

```python
obj.__str__()
```

2️⃣ If not defined, fallback to:

```python
obj.__repr__()
```

---

When you do:

```python
obj
```

in interactive shell:

Python calls:

```python
obj.__repr__()
```

NOT `__str__`.

---

When you do:

```python
repr(obj)
```

Python calls:

```python
obj.__repr__()
```

---

When you do:

```python
str(obj)
```

Python calls:

```python
obj.__str__()
```

If missing → fallback to `__repr__`.

---

# <span style="color:#5DADE2"><b>4️⃣ Internal Execution Flow (Dry Run)</b></span>

Example:

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        print("Calling __repr__")
        return f"Person('{self.name}', {self.age})"

    def __str__(self):
        print("Calling __str__")
        return f"{self.name}, {self.age} years old"
```

---

## Case 1 — Interactive Mode

```python
p = Person("Alice", 25)
p
```

Execution:

1. Interpreter wants object representation.
2. Calls:

```python
Person.__repr__(p)
```

Output:

```
Calling __repr__
Person('Alice', 25)
```

---

## Case 2 — print()

```python
print(p)
```

Execution:

1. `print()` internally calls `str(p)`
2. `str()` calls:

```python
Person.__str__(p)
```

Output:

```
Calling __str__
Alice, 25 years old
```

---

## Case 3 — str() explicitly

```python
str(p)
```

Calls `__str__`.

---

## Case 4 — repr() explicitly

```python
repr(p)
```

Calls `__repr__`.

---

# <span style="color:#BB8FCE"><b>5️⃣ What If Only `__repr__` Is Defined?</b></span>

```python
class A:
    def __repr__(self):
        return "Developer View"
```

Now:

```python
print(A())
```

Since `__str__` is missing, Python falls back to `__repr__`.

So:

✔ `__repr__` is fallback
❌ `__str__` is not fallback for `__repr__`

---

# <span style="color:#F5B041"><b>6️⃣ Why Two Separate Methods?</b></span>

Because two different audiences exist:

| Method     | Audience   |
| ---------- | ---------- |
| `__repr__` | Developers |
| `__str__`  | End Users  |

Example:

```python
datetime.datetime(2025, 1, 1)
```

repr:

```
datetime.datetime(2025, 1, 1, 0, 0)
```

str:

```
2025-01-01 00:00:00
```

Different purposes.

---

# <span style="color:#58D68D"><b>7️⃣ When To Use `__repr__`</b></span>

Use when:

✔ You want debug-friendly representation
✔ Object needs to be reconstructable
✔ Writing libraries
✔ Logging
✔ Debugging

Best example:

```python
class Vector:
    def __repr__(self):
        return f"Vector({self.x}, {self.y})"
```

So in console:

```python
Vector(3,4)
```

---

# <span style="color:#AF7AC5"><b>8️⃣ When To Use `__str__`</b></span>

Use when:

✔ Displaying readable info
✔ UI output
✔ User messages
✔ Clean formatting

Example:

```python
def __str__(self):
    return f"Vector with coordinates ({self.x}, {self.y})"
```

---

# <span style="color:#E74C3C"><b>9️⃣ Difference Between `__repr__` and `__str__`</b></span>

| Feature                        | `__repr__`                | `__str__`              |
| ------------------------------ | ------------------------- | ---------------------- |
| Purpose                        | Developer view            | User-friendly          |
| Called by                      | repr(), interactive shell | print(), str()         |
| Fallback                       | Used if **str** missing   | No fallback to **str** |
| Should be unambiguous          | Yes                       | Not required           |
| Should recreate object ideally | Yes                       | No                     |

---

# <span style="color:#5DADE2"><b>🔟 Important Internal Detail</b></span>

When printing a container:

```python
lst = [Person("Alice", 25)]
print(lst)
```

Python calls:

```python
Person.__repr__()
```

NOT `__str__`.

Because containers use `repr()` on elements.

So always define good `__repr__`.

---

# <span style="color:#BB8FCE"><b>1️⃣1️⃣ Best Practices</b></span>

✔ Always implement `__repr__`
✔ Make `__repr__` unambiguous
✔ Make `__repr__` reconstructable if possible
✔ Use f-strings
✔ Avoid heavy computation
✔ Keep `__str__` simple and readable
✔ If only one needed → implement `__repr__` only

Common pattern:

```python
def __repr__(self):
    return f"{self.__class__.__name__}({self.attr})"
```

---

# <span style="color:#F5B041"><b>1️⃣2️⃣ Minimal Good Template</b></span>

```python
class Example:
    def __init__(self, x):
        self.x = x

    def __repr__(self):
        return f"Example({self.x})"

    def __str__(self):
        return f"Value is {self.x}"
```

---

# <span style="color:#2E4053"><b>Final Summary</b></span>

- `__repr__` → developer representation.
- `__str__` → user-friendly display.
- print() → calls `__str__`
- interactive shell → calls `__repr__`
- If `__str__` missing → fallback to `__repr__`
- Containers use `__repr__` of elements.
- Always define `__repr__` in professional code.

---
