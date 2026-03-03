# <span style="color:#1d3557">**Inheritance in OOP – First Principle Understanding**</span>

---

## <span style="color:#457b9d">**1. What is Inheritance? (Causality and Effect)**</span>

### <span style="color:#2a9d8f">**Core Idea**</span>

Inheritance is a mechanism where one class (child) acquires the properties and behavior of another class (parent).

If:

- Class A defines structure + behavior
- Class B wants to reuse that structure + behavior

Then instead of rewriting code, B inherits from A.

---

### <span style="color:#2a9d8f">**Why It Is Important (Causality → Effect)**</span>

Let’s break it from cause-effect perspective.

#### 1️⃣ Code Duplication Problem

Without inheritance:

```python
class Dog:
    def eat(self):
        pass
    def breathe(self):
        pass

class Cat:
    def eat(self):
        pass
    def breathe(self):
        pass
```

Cause: Repeated logic
Effect: Hard to maintain, error-prone, violates DRY principle.

---

#### 2️⃣ Abstraction of Common Behavior

We observe:

- Dog eats
- Cat eats
- Cow eats

Common abstraction → Animal

So:

```python
class Animal:
    def eat(self):
        pass
    def breathe(self):
        pass
```

Then:

```python
class Dog(Animal):
    pass
```

Cause: Identify shared abstraction
Effect: Cleaner hierarchy, easier extension.

---

#### 3️⃣ Extensibility

Inheritance allows:

- Extend behavior
- Override behavior
- Specialize behavior

This enables polymorphism.

---

### <span style="color:#2a9d8f">**Conceptual View**</span>

Inheritance represents:

- “is-a” relationship
  Dog is-a Animal
  Student is-a Person

If it’s not "is-a", inheritance is probably wrong.

---

# <span style="color:#1d3557">**Inheritance in Python – Syntax and Internal Working**</span>

---

## <span style="color:#457b9d">**Basic Syntax**</span>

```python
class Parent:
    pass

class Child(Parent):
    pass
```

General form:

```python
class ChildClass(ParentClass):
    # body
```

Multiple inheritance:

```python
class C(A, B):
    pass
```

---

## <span style="color:#457b9d">**Example with Dry Run**</span>

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("Animal sound")

class Dog(Animal):
    def speak(self):
        print("Woof")
```

### Dry Run

```python
d = Dog("Tommy")
d.speak()
```

### Step-by-step execution

1. Python reads class Animal
2. Python creates class object Animal
3. Python reads class Dog(Animal)
4. Python creates class object Dog
   - Dog.**bases** = (Animal,)
   - Dog.**mro** computed

5. `d = Dog("Tommy")`
   - Python calls Dog.**init**
   - Dog doesn’t define **init**
   - Python searches in MRO
   - Finds Animal.**init**
   - Executes it
   - self.name = "Tommy"

6. `d.speak()`
   - Python looks in Dog
   - Finds speak in Dog
   - Executes Dog.speak()

Output:

```
Woof
```

---

## <span style="color:#457b9d">**Internal Working – What Python Actually Does**</span>

Every class in Python is an object.

Check:

```python
print(Dog.__bases__)
print(Dog.__mro__)
```

Output:

```
(<class '__main__.Animal'>,)
(<class '__main__.Dog'>, <class '__main__.Animal'>, <class 'object'>)
```

### Important Metadata:

- `__bases__` → tuple of parent classes
- `__mro__` → Method Resolution Order
- `__dict__` → namespace of class

---

# <span style="color:#1d3557">**How Attribute & Method Lookup Works (Interpreter Algorithm)**</span>

---

## <span style="color:#457b9d">**The Exact Lookup Algorithm (Simplified)**</span>

When you do:

```python
obj.attribute
```

Python follows this order:

1. Check instance namespace → `obj.__dict__`
2. Check class namespace → `obj.__class__.__dict__`
3. Follow MRO chain
4. Stop at object
5. If not found → AttributeError

---

## <span style="color:#457b9d">**Example: Naming Conflict**</span>

```python
class Parent:
    x = 10

class Child(Parent):
    x = 20

c = Child()
print(c.x)
```

### Resolution:

1. c.**dict** → not found
2. Child.**dict** → x = 20 → returned

Output:

```
20
```

Child overrides parent.

---

## <span style="color:#457b9d">**Method Conflict Example**</span>

```python
class Parent:
    def show(self):
        print("Parent")

class Child(Parent):
    def show(self):
        print("Child")

c = Child()
c.show()
```

Resolution:

- Look in Child → found → stop
- Parent ignored

Output:

```
Child
```

---

## <span style="color:#457b9d">**Multiple Inheritance and MRO (C3 Linearization)**</span>

```python
class A:
    pass

class B(A):
    pass

class C(A):
    pass

class D(B, C):
    pass
```

Check:

```python
print(D.__mro__)
```

Python uses C3 Linearization:

Rules:

1. Child before parent
2. Left-to-right priority
3. Preserve monotonicity

MRO:

```
D → B → C → A → object
```

---

# <span style="color:#1d3557">**Sub-class and Super-class Explained**</span>

---

## <span style="color:#457b9d">**Super-class (Parent Class)**</span>

A class that provides:

- Common behavior
- Shared logic
- General abstraction

Example:

```python
class Animal:
    pass
```

Animal is superclass.

---

## <span style="color:#457b9d">**Sub-class (Child Class)**</span>

A class that:

- Inherits from superclass
- Extends or modifies behavior

```python
class Dog(Animal):
    pass
```

Dog is subclass.

---

# <span style="color:#1d3557">**Metadata Information in Inheritance**</span>

---

## <span style="color:#457b9d">**Useful Class Metadata**</span>

| Attribute    | Meaning              |
| ------------ | -------------------- |
| `__bases__`  | Direct parents       |
| `__mro__`    | Resolution order     |
| `__dict__`   | Namespace            |
| `__name__`   | Class name           |
| `__module__` | Module where defined |

Example:

```python
print(Dog.__bases__)
print(Dog.__mro__)
print(Dog.__dict__)
```

---

# <span style="color:#1d3557">**Best Practices While Designing Superclass & Subclass**</span>

---

## <span style="color:#457b9d">**When Designing Superclass**</span>

### 1. Keep It General

Superclass should represent abstraction.

Bad:

```python
class Dog:
```

Good:

```python
class Animal:
```

---

### 2. Avoid Over-Specification

Do not put behavior that applies only to one subclass.

---

### 3. Use Protected Conventions

Use `_internal_var` for subclass-accessible variables.

---

### 4. Design for Extension

Use template method pattern:

```python
class Animal:
    def speak(self):
        raise NotImplementedError
```

Forces subclasses to implement.

---

## <span style="color:#457b9d">**When Designing Subclass**</span>

### 1. Respect Liskov Substitution Principle

If B inherits from A:

Anywhere A is expected, B should work.

---

### 2. Call super() Properly

```python
class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)
```

Internally:

`super()` uses MRO to find next class.

---

### 3. Do Not Break Parent Contracts

If parent method returns int, subclass should not suddenly return list.

---

# <span style="color:#1d3557">**Mental Model Summary**</span>

Inheritance in Python is:

- A relationship between class objects
- Stored in `__bases__`
- Resolved using MRO
- Lookup done via instance → class → MRO chain
- Based on C3 linearization

---

> Further scope:

- How `super()` internally works
- How descriptor protocol interacts with inheritance
- How method binding happens
- How metaclasses influence inheritance
- How memory layout is managed in CPython
