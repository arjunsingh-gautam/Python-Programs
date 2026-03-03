# <span style="color:#ff1744">**Types of Inheritance in Python and Method Resolution Order (MRO)**</span>

---

## <span style="color:#d500f9">**1. Single Inheritance**</span>

### <span style="color:#00e676">Structure</span>

One child inherits from one parent.

```python
class A:
    def show(self):
        print("A")

class B(A):
    pass
```

### <span style="color:#00e676">MRO</span>

```python
print(B.__mro__)
```

Output:

```
(B, A, object)
```

### <span style="color:#00e676">Resolution Order</span>

When calling `b.show()`:

1. Check B
2. Then A
3. Then object

Simple linear chain.

---

## <span style="color:#d500f9">**2. Multilevel Inheritance**</span>

### <span style="color:#00e676">Structure</span>

Grandparent → Parent → Child

```python
class A:
    def show(self):
        print("A")

class B(A):
    pass

class C(B):
    pass
```

### <span style="color:#00e676">MRO</span>

```python
print(C.__mro__)
```

Output:

```
(C, B, A, object)
```

### <span style="color:#00e676">Resolution</span>

Search path:

C → B → A → object

---

## <span style="color:#d500f9">**3. Hierarchical Inheritance**</span>

### <span style="color:#00e676">Structure</span>

One parent → Multiple children

```python
class A:
    def show(self):
        print("A")

class B(A):
    pass

class C(A):
    pass
```

### <span style="color:#00e676">MRO</span>

```
B → A → object
C → A → object
```

Each subclass has independent MRO.

---

## <span style="color:#d500f9">**4. Multiple Inheritance**</span>

### <span style="color:#00e676">Structure</span>

Child inherits from multiple parents.

```python
class A:
    def show(self):
        print("A")

class B:
    def show(self):
        print("B")

class C(A, B):
    pass
```

### <span style="color:#00e676">MRO (C3 Linearization)</span>

```python
print(C.__mro__)
```

Output:

```
(C, A, B, object)
```

### <span style="color:#00e676">Resolution</span>

When calling `c.show()`:

1. C
2. A
3. B
4. object

Left-to-right priority.

---

## <span style="color:#d500f9">**5. Diamond (Hybrid) Inheritance**</span>

### <span style="color:#00e676">Structure</span>

```
      A
     / \
    B   C
     \ /
      D
```

```python
class A:
    def show(self):
        print("A")

class B(A):
    pass

class C(A):
    pass

class D(B, C):
    pass
```

### <span style="color:#00e676">MRO</span>

```python
print(D.__mro__)
```

Output:

```
(D, B, C, A, object)
```

### <span style="color:#00e676">Why Not (D, B, A, C)?</span>

Because Python uses **C3 linearization**, which ensures:

1. Child precedes parents
2. Left-to-right order preserved
3. Monotonicity (consistent hierarchy ordering)

---

# <span style="color:#ff1744">**C3 Linearization – Core Idea**</span>

For class:

```python
class D(B, C)
```

MRO(D) =

```
[D] + merge(
    MRO(B),
    MRO(C),
    [B, C]
)
```

Python merges lists while preserving:

- Local precedence order
- Parent order consistency

This prevents ambiguity and duplication.

---

# <span style="color:#ff1744">**How super() Works Internally**</span>

---

## <span style="color:#d500f9">**What super() Actually Is**</span>

`super()` does NOT mean:

> "Call parent method"

It means:

> "Call next method in MRO after current class"

This is very important.

---

## <span style="color:#d500f9">**Internal Structure of super()**</span>

When you write:

```python
super().method()
```

Python internally creates:

```
super(CurrentClass, instance)
```

It uses:

- instance.**class**.**mro**
- Finds CurrentClass
- Calls next class in MRO

---

# <span style="color:#ff1744">**super() in Single Inheritance**</span>

```python
class A:
    def greet(self):
        print("A")

class B(A):
    def greet(self):
        super().greet()
        print("B")
```

Execution:

```python
b = B()
b.greet()
```

### Dry Run

MRO(B):

```
(B, A, object)
```

1. Call B.greet
2. super() → next after B → A
3. Call A.greet
4. Print "A"
5. Then print "B"

Output:

```
A
B
```

---

# <span style="color:#ff1744">**super() in Hierarchical Inheritance**</span>

```python
class A:
    def greet(self):
        print("A")

class B(A):
    def greet(self):
        super().greet()
        print("B")

class C(A):
    def greet(self):
        super().greet()
        print("C")
```

Each class has independent chain:

For B:

MRO: (B, A, object)

For C:

MRO: (C, A, object)

super() always moves one step forward in that class’s MRO.

---

# <span style="color:#ff1744">**super() in Diamond (Multiple Inheritance)**</span>

This is where real power appears.

```python
class A:
    def greet(self):
        print("A")

class B(A):
    def greet(self):
        super().greet()
        print("B")

class C(A):
    def greet(self):
        super().greet()
        print("C")

class D(B, C):
    def greet(self):
        super().greet()
        print("D")
```

Check MRO:

```python
print(D.__mro__)
```

Output:

```
(D, B, C, A, object)
```

---

### Execution:

```python
d = D()
d.greet()
```

### Step-by-step resolution

1. D.greet()
2. super() → next after D → B
3. B.greet()
4. super() → next after B → C
5. C.greet()
6. super() → next after C → A
7. A.greet()
8. Then prints unwind:

Output:

```
A
C
B
D
```

Notice:

A runs only once.

This solves diamond problem.

---

# <span style="color:#ff1744">**Why Direct Parent Call Is Dangerous**</span>

Wrong:

```python
A.greet(self)
```

This breaks MRO chain.

In multiple inheritance:

- A may execute multiple times
- Order may break
- Bugs appear

Always use super() in cooperative inheritance.

---

# <span style="color:#ff1744">**super() in **init** (Critical Case)**</span>

Example:

```python
class A:
    def __init__(self):
        print("A")

class B(A):
    def __init__(self):
        super().__init__()
        print("B")

class C(A):
    def __init__(self):
        super().__init__()
        print("C")

class D(B, C):
    def __init__(self):
        super().__init__()
        print("D")
```

Execution:

```python
D()
```

MRO:

```
D → B → C → A → object
```

Call chain:

D → B → C → A

Output:

```
A
C
B
D
```

Every class runs once.

---

# <span style="color:#ff1744">**Internal Algorithm of super() (Conceptual)**</span>

Given:

```python
super(CurrentClass, instance)
```

Python:

1. Fetch instance.**class**.**mro**
2. Find CurrentClass index
3. Take next class in list
4. Return proxy object bound to that next class
5. Method lookup continues from there

super() is a descriptor object that:

- Wraps class
- Wraps instance
- Delegates attribute lookup

---

# <span style="color:#ff1744">**Key Rules for Using super() Safely**</span>

1. Always call super() in cooperative multiple inheritance
2. Keep consistent method signatures
3. Every class in hierarchy should use super()
4. Never mix direct parent calls and super()

---

# <span style="color:#ff1744">**Deep Insight for You**</span>

Since you're aiming for deep system-level mastery:

Understand this clearly:

Inheritance is resolved by:

- **mro**
- C3 linearization
- Descriptor protocol
- super() delegation object

This is why Python avoids traditional diamond ambiguity seen in C++.

---

If you want, next I can explain:

- How C3 algorithm merges lists step-by-step mathematically
- How descriptor protocol interacts with super()
- How method binding happens internally
- Memory layout of inherited classes in CPython

Tell me which layer you want to go deeper into.
