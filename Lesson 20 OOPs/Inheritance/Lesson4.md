# <span style="color:#ff0033">**How Inheritance Affects Dunder Methods and Descriptors in Python**</span>

Inheritance in Python is not just about normal methods.
It deeply affects:

- Special (dunder) methods
- Descriptor behavior
- Operator overloading
- Attribute access mechanics
- Object creation lifecycle

We will go layer by layer.

---

# <span style="color:#ff6f00">**Part 1 — How Inheritance Affects Dunder (Special) Methods**</span>

---

## <span style="color:#2962ff">**1. Dunder Methods Follow MRO — But With a Twist**</span>

Normal method lookup:

```python
obj.method()
```

Search order:

```
instance → class → MRO chain
```

But for many dunder methods (like `__add__`, `__len__`, `__iter__`), Python **does not** search on the instance.

Instead, it looks directly on the **type(obj)**.

---

## <span style="color:#2962ff">**Example: **add** and Inheritance**</span>

```python
class A:
    def __add__(self, other):
        print("A add")
        return 10

class B(A):
    pass
```

```python
b = B()
b + 5
```

### What happens internally?

Python does:

```
type(b).__add__(b, 5)
```

Which means:

1. Check B.**add**
2. Not found
3. Check A.**add**
4. Found → execute

Inheritance applies fully via MRO.

---

## <span style="color:#2962ff">**Example: Overriding Dunder in Child**</span>

```python
class B(A):
    def __add__(self, other):
        print("B add")
        return 20
```

Now:

```python
b = B()
b + 5
```

Resolution:

```
type(b).__mro__ = (B, A, object)
```

Finds B.**add** first.

Output:

```
B add
```

---

## <span style="color:#2962ff">**Important Twist — Some Dunder Methods Are Looked Up on Class Only**</span>

For performance reasons, CPython bypasses instance dictionary for special methods.

Example:

```python
class A:
    def __len__(self):
        return 5

a = A()
a.__len__ = lambda: 100
```

Now:

```python
len(a)
```

Result is still:

```
5
```

Why?

Because Python does:

```
type(a).__len__(a)
```

NOT:

```
a.__len__()
```

Inheritance affects this because:

- Only class-level dunder methods matter
- Child overrides parent cleanly via MRO

---

# <span style="color:#ff6f00">**Part 2 — How Inheritance Affects Descriptors**</span>

Descriptors are objects that define:

- `__get__`
- `__set__`
- `__delete__`

Examples:

- methods
- property
- classmethod
- staticmethod

---

## <span style="color:#2962ff">**Descriptor Lookup Algorithm with Inheritance**</span>

When you do:

```python
obj.attr
```

Python performs:

1. Look in class MRO for descriptor
2. If data descriptor (has **set**), it overrides instance attribute
3. Else check instance dictionary
4. Else non-data descriptor
5. Else normal attribute

Inheritance directly affects step 1 — class MRO traversal.

---

## <span style="color:#2962ff">**Example: Descriptor in Parent Class**</span>

```python
class Descriptor:
    def __get__(self, instance, owner):
        print("Descriptor get")
        return 42

class A:
    x = Descriptor()

class B(A):
    pass
```

```python
b = B()
print(b.x)
```

Resolution:

1. Search B → not found
2. Search A → finds x
3. x is descriptor → call **get**

Output:

```
Descriptor get
42
```

Inheritance makes descriptor fully reusable.

---

## <span style="color:#2962ff">**Overriding Descriptor in Child**</span>

```python
class B(A):
    x = 100
```

Now:

```python
b = B()
print(b.x)
```

Resolution:

1. B.x found
2. It is not descriptor
3. Return 100

Child overrides descriptor completely.

---

# <span style="color:#ff6f00">**Part 3 — Interaction of Inheritance with Properties**</span>

Property is a descriptor.

```python
class A:
    @property
    def value(self):
        return 10
```

```python
class B(A):
    pass
```

`B().value` works because property descriptor is inherited.

---

## <span style="color:#2962ff">**Overriding Only Getter in Child**</span>

```python
class B(A):
    @property
    def value(self):
        return 20
```

MRO ensures B's property shadows A's property.

---

# <span style="color:#ff6f00">**Part 4 — Side Effects of Inheritance**</span>

Now we go into deeper system-level effects.

---

## <span style="color:#d500f9">**1. Diamond Re-execution Problem (Without super)**</span>

If you directly call parent methods:

```python
class B(A):
    def __init__(self):
        A.__init__(self)
```

In diamond:

```
D → B → C → A
```

A may execute twice.

Solution:

Always use super() cooperatively.

---

## <span style="color:#d500f9">**2. Signature Mismatch in Overridden Methods**</span>

Bad:

```python
class A:
    def process(self, x):
        pass

class B(A):
    def process(self):
        pass
```

Now polymorphism breaks.

Solution:

Maintain consistent method signatures.

---

## <span style="color:#d500f9">**3. Fragile Base Class Problem**</span>

If parent changes internal logic:

All subclasses may break unexpectedly.

Example:

Parent adds new required method call.

Solution:

- Keep superclass stable
- Follow Open/Closed principle
- Document extension points

---

## <span style="color:#d500f9">**4. Descriptor Shadowing by Instance Attributes**</span>

If descriptor is non-data descriptor:

Instance attribute may override it.

```python
class A:
    def show(self):
        print("method")
```

Methods are non-data descriptors.

```python
a = A()
a.show = 100
print(a.show)
```

Output:

```
100
```

Inheritance allows this shadowing.

To prevent it:

Use data descriptor (define **set**).

---

## <span style="color:#d500f9">**5. Unexpected Dunder Behavior in Multiple Inheritance**</span>

If two parents define:

```python
__str__
```

Resolution depends on MRO order.

Example:

```python
class A:
    def __str__(self):
        return "A"

class B:
    def __str__(self):
        return "B"

class C(A, B):
    pass
```

C().**str** → A wins.

Order matters.

---

## <span style="color:#d500f9">**6. super() Chain Breakage**</span>

If one class in chain does not call super():

Chain stops.

In cooperative multiple inheritance, every class must call super().

---

# <span style="color:#ff0033">**Deep Internal Insight — Why All This Happens**</span>

Inheritance impacts:

- `__mro__`
- Attribute resolution algorithm
- Descriptor invocation order
- Dunder dispatch mechanics

Core algorithm for attribute access:

```
1. Check for data descriptor in class MRO
2. Check instance dictionary
3. Check non-data descriptor in class MRO
4. Check class attribute
5. Move through MRO
```

For operators:

```
Call type(obj).__dunder__()
```

For super():

```
Find next class in __mro__
Return bound proxy
```

Everything depends on MRO.

---

# <span style="color:#ff0033">**How to Deal with Side Effects Professionally**</span>

1. Keep inheritance shallow
2. Always use cooperative super()
3. Maintain consistent method signatures
4. Avoid overriding dunder unless necessary
5. Understand descriptor priority
6. Test multiple inheritance hierarchies carefully
7. Prefer composition for dynamic behavior

---

# <span style="color:#ff0033">**Mental Model Summary**</span>

Inheritance affects:

- Operator overloading
- Magic methods
- Descriptor resolution
- Attribute shadowing
- Method binding
- Initialization order

All controlled by:

```
__mro__ + descriptor protocol + type-based dispatch
```

---

If you want next level depth, we can explore:

- How function objects become bound methods via descriptor protocol
- How **getattribute** interacts with inheritance
- How metaclasses influence descriptor resolution
- CPython slot lookup optimization for dunder methods

Tell me which direction you want to go deeper into.
