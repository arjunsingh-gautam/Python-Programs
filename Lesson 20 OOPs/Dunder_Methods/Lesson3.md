# <span style="color:#2E86C1"><b>Reverse Methods in Python (`__radd__`, `__rsub__`, etc.) — Complete Explanation</b></span>

Reverse methods are part of Python’s **operator overloading resolution mechanism**.

We’ll explain:

1. What reverse methods are
2. Why they exist (fundamental causality)
3. When Python calls them
4. Exact resolution order
5. Step-by-step dry run
6. Special subclass priority rule
7. Practical examples
8. Common mistakes

---

# <span style="color:#AF7AC5"><b>1️⃣ What Is a Reverse Method?</b></span>

A reverse method is the “right-hand version” of an operator method.

For example:

| Operator | Normal        | Reverse        |
| -------- | ------------- | -------------- |
| `+`      | `__add__`     | `__radd__`     |
| `-`      | `__sub__`     | `__rsub__`     |
| `*`      | `__mul__`     | `__rmul__`     |
| `/`      | `__truediv__` | `__rtruediv__` |

If you write:

```python
a + b
```

Python first tries:

```python
a.__add__(b)
```

If that fails, Python tries:

```python
b.__radd__(a)
```

That second attempt is the reverse method.

---

# <span style="color:#48C9B0"><b>2️⃣ Why Reverse Methods Exist (Causality)</b></span>

Problem:

What if left operand doesn’t know how to handle the right operand?

Example:

```python
5 + Vector(3)
```

`int` does not know how to add `Vector`.

If Python stopped there, the operation would fail.

Instead, Python gives the right operand a chance:

```python
Vector.__radd__(vector_instance, 5)
```

Reverse methods allow **cooperative binary operations**.

---

# <span style="color:#E74C3C"><b>3️⃣ Operator Resolution Order (Exact Rules)</b></span>

For:

```python
a + b
```

Python follows this order:

---

### Step 1

Call:

```python
type(a).__add__(a, b)
```

If returns NOT `NotImplemented`, return result.

---

### Step 2

If result was `NotImplemented`:

Call:

```python
type(b).__radd__(b, a)
```

If returns NOT `NotImplemented`, return result.

---

### Step 3

If both return `NotImplemented` → raise:

```python
TypeError
```

---

# <span style="color:#5DADE2"><b>4️⃣ Important: Why Return NotImplemented?</b></span>

Inside `__add__`, you must write:

```python
return NotImplemented
```

Not:

```python
return None
```

Why?

Because only `NotImplemented` tells Python:

> “I cannot handle this — try reverse method.”

If you return `None`, Python thinks operation succeeded.

---

# <span style="color:#BB8FCE"><b>5️⃣ Complete Dry Run Example</b></span>

```python
class Vector:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        print("Calling __add__")
        if isinstance(other, Vector):
            return Vector(self.value + other.value)
        return NotImplemented

    def __radd__(self, other):
        print("Calling __radd__")
        return Vector(self.value + other)
```

---

## Case 1 — Same Types

```python
v1 = Vector(5)
v2 = Vector(3)
v1 + v2
```

Flow:

1. Call `Vector.__add__(v1, v2)`
2. Handles it.
3. Reverse method never called.

---

## Case 2 — Mixed Types

```python
5 + v1
```

Flow:

1. Call `int.__add__(5, v1)`
2. Returns `NotImplemented`
3. Call `Vector.__radd__(v1, 5)`
4. Handles it.

---

# <span style="color:#F5B041"><b>6️⃣ Special Rule: Subclass Priority</b></span>

If:

- `b` is subclass of `a`
- Both implement operator

Then Python prefers subclass method first.

Example:

```python
class A:
    def __add__(self, other):
        print("A add")
        return 1

class B(A):
    def __radd__(self, other):
        print("B radd")
        return 2
```

If:

```python
a = A()
b = B()
a + b
```

Python prefers subclass’s reverse method.

This ensures subclass gets priority in mixed-type operations.

---

# <span style="color:#58D68D"><b>7️⃣ Reverse vs Normal Method Difference</b></span>

Normal method:

```python
a.__add__(b)
```

Reverse method:

```python
b.__radd__(a)
```

Notice:

Operands are swapped.

---

# <span style="color:#AF7AC5"><b>8️⃣ In-Place Operator Interaction</b></span>

For:

```python
a += b
```

Python tries:

1. `a.__iadd__(b)`
2. If not present → fallback to:
   - `a.__add__(b)`
   - then assign result back

Reverse method not directly involved here unless fallback.

---

# <span style="color:#E74C3C"><b>9️⃣ Why This Design Is Powerful</b></span>

Reverse methods enable:

✔ Mixed-type arithmetic
✔ Cooperation between types
✔ Symmetric operations
✔ Extensible numeric systems

Example:

NumPy arrays + integers work because of reverse methods.

---

# <span style="color:#5DADE2"><b>🔟 Practical Real-World Use Case</b></span>

### Example: Money Class

```python
class Money:
    def __init__(self, amount):
        self.amount = amount

    def __add__(self, other):
        if isinstance(other, Money):
            return Money(self.amount + other.amount)
        return NotImplemented

    def __radd__(self, other):
        if isinstance(other, int):
            return Money(self.amount + other)
        return NotImplemented
```

Now:

```python
Money(10) + 5
5 + Money(10)
```

Both work.

---

# <span style="color:#BB8FCE"><b>1️⃣1️⃣ Constraints</b></span>

- Reverse method only called if normal method returns `NotImplemented`.
- Cannot override Python built-in operator precedence.
- Must maintain logical symmetry.
- Should avoid side effects.

---

# <span style="color:#2E4053"><b>Final Summary</b></span>

Reverse method:

- Is right-hand fallback operator method.
- Called when left operand cannot handle operation.
- Uses swapped operands.
- Enables mixed-type arithmetic.
- Works through Python’s operator resolution chain.
- Requires returning `NotImplemented` to activate fallback.

Without reverse methods, mixed-type operations would fail frequently.

---
