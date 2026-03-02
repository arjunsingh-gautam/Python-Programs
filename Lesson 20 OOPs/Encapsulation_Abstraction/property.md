# <span style="color:#2E86C1"><b>`@property` in Python — Deep & Simple Explanation</b></span>

We will cover:

1. What `@property` really is
2. How it works internally (simple mental model)
3. Getter, setter, deleter mechanics with dry run
4. How it implements encapsulation
5. When to use it
6. Best practices

---

# <span style="color:#AF7AC5"><b>1️⃣ What Is `@property`?</b></span>

`@property` lets you:

> Access a method like an attribute.

Without property:

```python
obj.get_balance()
```

With property:

```python
obj.balance
```

But internally — it still calls a function.

So:

✔ Looks like attribute
✔ Behaves like method

That’s the core idea.

---

# <span style="color:#48C9B0"><b>2️⃣ Simple Example (Basic Working)</b></span>

```python
class Person:
    def __init__(self, age):
        self._age = age   # internal variable

    @property
    def age(self):
        return self._age
```

Usage:

```python
p = Person(25)
print(p.age)   # no parentheses
```

Output:

```
25
```

Even though `age()` is a function, you use it like attribute.

---

# <span style="color:#E74C3C"><b>3️⃣ What Actually Happens Internally?</b></span>

Important fact:

`property` is a **descriptor object**.

When Python sees:

```python
@property
def age(self):
```

It converts it into:

```python
age = property(age_function)
```

So inside class dictionary:

```python
Person.__dict__['age']
```

Is not a function anymore.

It is a `property` object.

---

## 🔎 What Happens When You Access `p.age`?

Python does:

1. Look for `"age"` in instance dictionary.
2. Not found.
3. Look in class dictionary.
4. Finds property object.
5. Calls:

```python
property.__get__(instance, owner)
```

That internally calls your getter method.

So:

```python
p.age
```

Actually becomes:

```python
Person.age.__get__(p, Person)
```

Which then calls:

```python
age(self=p)
```

That is the dry run.

---

# <span style="color:#BB8FCE"><b>4️⃣ Full Getter / Setter / Deleter Example</b></span>

```python
class BankAccount:
    def __init__(self, balance):
        self._balance = balance

    @property
    def balance(self):
        print("Getter called")
        return self._balance

    @balance.setter
    def balance(self, value):
        print("Setter called")
        if value < 0:
            raise ValueError("Balance cannot be negative")
        self._balance = value

    @balance.deleter
    def balance(self):
        print("Deleter called")
        del self._balance
```

---

# <span style="color:#5DADE2"><b>5️⃣ Dry Run — Getter</b></span>

```python
acc = BankAccount(1000)
print(acc.balance)
```

Step-by-step:

1. Python sees `acc.balance`.
2. Looks in `acc.__dict__` → not found.
3. Looks in `BankAccount.__dict__`.
4. Finds property object.
5. Calls property.**get**().
6. Calls getter function.
7. Prints "Getter called".
8. Returns `_balance`.

Output:

```
Getter called
1000
```

---

# <span style="color:#F5B041"><b>6️⃣ Dry Run — Setter</b></span>

```python
acc.balance = 2000
```

Step-by-step:

1. Python sees assignment to attribute.
2. Finds property object.
3. Calls property.**set**().
4. Calls setter method.
5. Prints "Setter called".
6. Updates `_balance`.

---

If invalid:

```python
acc.balance = -500
```

Raises:

```
ValueError
```

Invariant protected.

---

# <span style="color:#58D68D"><b>7️⃣ Dry Run — Deleter</b></span>

```python
del acc.balance
```

Python:

1. Calls property.**delete**().
2. Calls deleter method.
3. Deletes `_balance`.

---

# <span style="color:#AF7AC5"><b>8️⃣ Why Not Just Use Normal Attribute?</b></span>

Without property:

```python
self.balance = value
```

Anyone can assign negative number.

No control.

With property:

✔ You validate
✔ You log
✔ You compute
✔ You enforce rules

That is encapsulation.

---

# <span style="color:#E74C3C"><b>9️⃣ How Property Implements Encapsulation</b></span>

Encapsulation means:

> Internal state is protected behind controlled interface.

In property:

- `_balance` is internal
- `balance` is controlled interface
- Setter validates
- Getter controls access

So:

```text
External code → balance
Internal storage → _balance
```

Internal representation can change without breaking API.

---

# <span style="color:#5DADE2"><b>🔟 When To Use `@property`</b></span>

Use it when:

✔ You need validation
✔ You want computed attribute
✔ You want read-only attribute
✔ You want logging
✔ You want lazy evaluation

---

## Example — Computed Property

```python
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def area(self):
        return self.width * self.height
```

Usage:

```python
r = Rectangle(4,5)
print(r.area)   # 20
```

No parentheses.

---

# <span style="color:#F39C12"><b>1️⃣1️⃣ Read-Only Property</b></span>

If you define only getter:

```python
@property
def id(self):
    return self._id
```

Then:

```python
obj.id = 10
```

Raises:

```
AttributeError
```

Immutable interface.

---

# <span style="color:#EC7063"><b>1️⃣2️⃣ Lazy Computation Example</b></span>

```python
class Data:
    def __init__(self, value):
        self._value = value
        self._square = None

    @property
    def square(self):
        if self._square is None:
            print("Computing square...")
            self._square = self._value ** 2
        return self._square
```

First access computes.
Later accesses reuse.

---

# <span style="color:#3498DB"><b>1️⃣3️⃣ Best Practices</b></span>

✔ Always use `_name` for internal storage
✔ Keep property logic simple
✔ Avoid heavy computation inside property
✔ Don’t surprise users (avoid hidden side effects)
✔ Use property when interface must look like attribute

Avoid when:

❌ Complex multi-step operations
❌ Heavy computation
❌ Network calls

---

# <span style="color:#8E44AD"><b>1️⃣4️⃣ Internal Structure of Property Object</b></span>

Internally property stores:

- fget
- fset
- fdel

When accessing:

```
obj.attr → property.__get__()
obj.attr = value → property.__set__()
del obj.attr → property.__delete__()
```

It is a descriptor implementing:

```python
__get__()
__set__()
__delete__()
```

---

# <span style="color:#2E4053"><b>Final Summary</b></span>

`@property`:

- Converts method into managed attribute.
- Uses descriptor protocol internally.
- Enables getter/setter/deleter.
- Implements encapsulation.
- Protects invariants.
- Allows computed attributes.
- Keeps interface clean.

It is Python’s elegant way of enforcing controlled access without breaking attribute syntax.

---
