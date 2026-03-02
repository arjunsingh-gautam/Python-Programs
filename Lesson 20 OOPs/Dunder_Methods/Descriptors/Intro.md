# <span style="color:#2E86C1"><b>Descriptors in Python — Deep Internal Explanation</b></span>

Descriptors are one of the most powerful — and most misunderstood — parts of Python’s object model.

We’ll cover:

1. What a descriptor is (simple definition)
2. Why descriptors exist (fundamental causality)
3. How attribute lookup works internally
4. Descriptor protocol methods
5. Data vs non-data descriptors
6. Full working example with dry run
7. What would break without descriptors
8. Real-world uses (property, methods, classmethod, staticmethod)

---

# <span style="color:#AF7AC5"><b>1️⃣ What Is a Descriptor?</b></span>

A **descriptor** is:

> Any object that defines at least one of these methods:
>
> - `__get__`
> - `__set__`
> - `__delete__`

If a class attribute is a descriptor, Python gives it special behavior during attribute access.

In simple words:

> Descriptors customize what happens when you access, assign, or delete an attribute.

---

# <span style="color:#48C9B0"><b>2️⃣ Why Do Descriptors Exist? (Fundamental Causality)</b></span>

Without descriptors:

- Attribute access would just return stored value.
- Methods could not bind automatically.
- Properties would not work.
- Classmethod / staticmethod would not work.
- Validation logic on attribute access impossible.

Descriptors allow:

✔ Method binding
✔ Computed attributes
✔ Controlled attribute setting
✔ ORM field mapping
✔ Lazy loading
✔ Type checking

They make attribute access programmable.

---

# <span style="color:#E74C3C"><b>3️⃣ How Attribute Lookup Works Internally</b></span>

When you do:

```python
obj.attr
```

Python roughly does:

1. Check if class attribute `attr` is a descriptor.
2. If yes → call descriptor’s `__get__`.
3. Otherwise check instance dictionary.
4. Otherwise check class dictionary.
5. Otherwise check parent classes.

Descriptors intercept access.

---

# <span style="color:#5DADE2"><b>4️⃣ Descriptor Protocol</b></span>

Descriptor methods:

```python
__get__(self, instance, owner)
__set__(self, instance, value)
__delete__(self, instance)
```

Where:

- `instance` = object being accessed
- `owner` = class of instance

If descriptor defines:

- `__set__` or `__delete__` → it is a **data descriptor**
- Only `__get__` → **non-data descriptor**

Data descriptors take priority over instance dictionary.

---

# <span style="color:#BB8FCE"><b>5️⃣ Simple Descriptor Example</b></span>

Let’s create custom descriptor.

```python
class PositiveNumber:
    def __get__(self, instance, owner):
        print("Getter called")
        return instance._value

    def __set__(self, instance, value):
        print("Setter called")
        if value < 0:
            raise ValueError("Must be positive")
        instance._value = value
```

Use it:

```python
class Product:
    price = PositiveNumber()

    def __init__(self, price):
        self.price = price
```

---

# <span style="color:#F5B041"><b>6️⃣ Dry Run — Setting Value</b></span>

```python
p = Product(100)
```

Inside `__init__`:

```python
self.price = 100
```

Python sees:

- `price` exists in class
- It is descriptor with `__set__`

So instead of:

```python
self.__dict__['price'] = 100
```

Python calls:

```python
PositiveNumber.__set__(descriptor_instance, p, 100)
```

Setter validates and stores:

```python
p._value = 100
```

---

# <span style="color:#58D68D"><b>7️⃣ Dry Run — Getting Value</b></span>

```python
print(p.price)
```

Python:

1. Finds `price` in class.
2. Sees descriptor with `__get__`.
3. Calls:

```python
PositiveNumber.__get__(descriptor_instance, p, Product)
```

Returns `p._value`.

---

# <span style="color:#AF7AC5"><b>8️⃣ Why Not Just Use Property?</b></span>

`property` is actually built on descriptors.

Descriptors are lower-level.

Property is just a convenience wrapper.

Without descriptor mechanism:

- property could not exist.
- method binding impossible.
- classmethod impossible.

---

# <span style="color:#E74C3C"><b>9️⃣ What Would Break Without Descriptors?</b></span>

### 🔹 Method Binding

When you access:

```python
obj.method
```

Python binds `self` automatically.

How?

Functions implement `__get__`.

Without descriptor protocol:

- Methods would not auto-bind.
- You would need to manually pass instance.

---

### 🔹 property

```python
obj.balance
```

Would just return property object, not computed value.

---

### 🔹 classmethod

Would not bind class automatically.

---

### 🔹 ORMs (Django, SQLAlchemy)

Fields rely on descriptors to manage database access.

Without descriptors:

Most of Python’s OOP magic collapses.

---

# <span style="color:#5DADE2"><b>🔟 Data vs Non-Data Descriptor</b></span>

## Data Descriptor (has **set**)

Takes priority over instance dictionary.

## Non-Data Descriptor (only **get**)

Instance dictionary can override it.

Example:

```python
class A:
    def f(self): pass
```

Function objects implement `__get__`.

They are non-data descriptors.

If you do:

```python
obj.f = 10
```

You override method because it is non-data descriptor.

---

# <span style="color:#BB8FCE"><b>1️⃣1️⃣ How Methods Are Descriptors</b></span>

When you define:

```python
class A:
    def f(self): pass
```

`f` is function object.

Function object has:

```python
__get__(self, instance, owner)
```

When accessed via instance:

```python
a.f
```

It returns bound method.

That binding is descriptor magic.

---

# <span style="color:#F5B041"><b>1️⃣2️⃣ classmethod Internally</b></span>

Simplified:

```python
class classmethod:
    def __init__(self, func):
        self.func = func

    def __get__(self, instance, owner):
        return lambda *args: self.func(owner, *args)
```

It binds class instead of instance.

---

# <span style="color:#58D68D"><b>1️⃣3️⃣ staticmethod Internally</b></span>

Simplified:

```python
class staticmethod:
    def __init__(self, func):
        self.func = func

    def __get__(self, instance, owner):
        return self.func
```

No binding.

---

# <span style="color:#AF7AC5"><b>1️⃣4️⃣ Real-World Use Cases</b></span>

✔ Validation
✔ Lazy computation
✔ ORM field mapping
✔ Caching attributes
✔ Logging access
✔ Type enforcement
✔ Access control

Example: Lazy attribute

```python
class LazyValue:
    def __get__(self, instance, owner):
        value = compute()
        instance.__dict__['value'] = value
        return value
```

---

# <span style="color:#E74C3C"><b>1️⃣5️⃣ Why Descriptors Are Powerful</b></span>

They allow:

> Custom behavior during attribute access at the language level.

They make Python’s object model dynamic and programmable.

---

# <span style="color:#2E4053"><b>Final Conceptual Summary</b></span>

Descriptor = object that controls attribute access.

They power:

- property
- method binding
- classmethod
- staticmethod
- ORM fields
- advanced frameworks

Without descriptors:

- Methods would not bind.
- property would not compute.
- classmethod/staticmethod impossible.
- Python OOP behavior breaks.

Descriptors are the foundation of Python’s attribute access model.

---

# <span style="color:#2E86C1"><b>Why `self.price = value` Does NOT Create `price` in Instance Dict?</b></span>

This is one of the most important rules in Python’s object model.

You observed:

> When assigning `self.price = price`, it does NOT create `price` in instance `__dict__`.
> Instead it calls `__set__` of `PositiveNumber`.

Correct.

Let’s explain **why**, step-by-step, based on Python’s attribute assignment rules.

---

# <span style="color:#AF7AC5"><b>1️⃣ First — The Rule That Controls This</b></span>

When you do:

```python
instance.attr = value
```

Python follows this order:

### 🔹 Assignment Algorithm (Simplified)

1. Check if `attr` exists in the class.
2. If it exists AND is a **data descriptor** (has `__set__`),
   → call descriptor’s `__set__`.
3. Otherwise,
   → store value in `instance.__dict__`.

That is the rule.

Your `PositiveNumber` defines:

```python
def __set__(...)
```

So it is a **data descriptor**.

Data descriptors always override instance dictionary writes.

---

# <span style="color:#48C9B0"><b>2️⃣ What Happens When Class Is Defined?</b></span>

When Python executes:

```python
class Product:
    price = PositiveNumber()
```

It does:

1. Create instance of `PositiveNumber`.
2. Store it inside class dictionary:

```python
Product.__dict__['price'] = descriptor_instance
```

So:

```
Product
 └── price → PositiveNumber object
```

Important:

There is NO `price` inside instance yet.

---

# <span style="color:#E74C3C"><b>3️⃣ Now Step-by-Step Execution of `Product(100)`</b></span>

### Step A — Instance Creation

```python
p = Product(100)
```

Python:

1. Creates empty instance.
2. Calls `__init__(p, 100)`.

At this moment:

```python
p.__dict__ == {}
```

---

### Step B — Inside `__init__`

```python
self.price = price
```

Which becomes:

```python
p.price = 100
```

Now the assignment rule triggers.

---

# <span style="color:#5DADE2"><b>4️⃣ Assignment Resolution Step-by-Step</b></span>

Python evaluates:

```
Does class Product have attribute named "price"?
```

Yes.

```
Is it a descriptor?
```

Yes.

```
Is it a DATA descriptor? (Has __set__?)
```

Yes.

Therefore:

Instead of writing:

```python
p.__dict__['price'] = 100
```

Python calls:

```python
PositiveNumber.__set__(descriptor_instance, p, 100)
```

This is mandatory behavior defined by Python’s descriptor protocol.

---

# <span style="color:#BB8FCE"><b>5️⃣ Why Instance Variable Is NOT Created</b></span>

Because:

Data descriptors take priority over instance dictionary.

They intercept writes.

This is deliberate design.

Otherwise:

Descriptors could not enforce validation.

---

# <span style="color:#F5B041"><b>6️⃣ What If There Was No **set**?</b></span>

If your descriptor only had:

```python
def __get__(...)
```

Then it would be a **non-data descriptor**.

Then assignment would behave differently:

```
instance.price = 100
```

Would create:

```python
instance.__dict__['price'] = 100
```

Because non-data descriptors do NOT intercept writes.

---

# <span style="color:#58D68D"><b>7️⃣ Why Python Designed It This Way?</b></span>

Because descriptors exist to control attribute behavior.

If instance dictionary write happened first:

- Validation would be bypassed.
- Encapsulation broken.
- property would not work.

So Python enforces this precedence:

```
DATA DESCRIPTOR > INSTANCE DICTIONARY
```

This is core rule.

---

# <span style="color:#AF7AC5"><b>8️⃣ Complete Attribute Assignment Precedence</b></span>

When assigning:

```
instance.attr = value
```

Order:

1️⃣ Check class for data descriptor → call **set**
2️⃣ Else → write to instance **dict**

---

When reading:

```
instance.attr
```

Order:

1️⃣ Data descriptor
2️⃣ Instance dictionary
3️⃣ Non-data descriptor
4️⃣ Class dictionary
5️⃣ Parent classes

This is official lookup precedence.

---

# <span style="color:#E74C3C"><b>9️⃣ What Is Stored Inside Instance After Assignment?</b></span>

In your code:

```python
instance._value = value
```

So:

```
p.__dict__ = {'_value': 100}
```

There is NO `'price'` key.

Because `price` is managed by descriptor.

---

# <span style="color:#5DADE2"><b>🔟 Mental Model</b></span>

Think of descriptor as a guard at the gate.

When you try:

```
p.price = 100
```

Guard checks:

- “I control this attribute.”
- “I will handle the assignment.”

So instance dictionary never receives direct value.

---

# <span style="color:#BB8FCE"><b>1️⃣1️⃣ Why This Is Powerful</b></span>

Because it allows:

✔ Validation
✔ Lazy loading
✔ Logging
✔ ORM field mapping
✔ Type enforcement
✔ Access control

Without this rule, descriptors would be useless.

---

# <span style="color:#2E4053"><b>Final Clean Explanation</b></span>

Your instance variable `price` is not created in the instance dictionary because:

- The class defines `price` as a data descriptor.
- Data descriptors intercept assignment.
- Python’s assignment algorithm prioritizes descriptor `__set__` over instance dictionary.
- Therefore, the descriptor controls how and where the value is stored.

This behavior is defined by the descriptor protocol and attribute resolution rules in Python.

---
