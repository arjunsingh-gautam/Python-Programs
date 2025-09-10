# <span style="color:#003566">**Constructors in Python**</span>

---

### <span style="color:#ef233c"> 1. Introduction</span>

- The main purpose of a **constructor** in Python is **to initialize an object at the time of creation**.
- Initializing means **placing user-defined or default values** inside the object so that the object does not remain empty.
- Python provides a special method `__init__()` for constructors.

---

### <span style="color:#ef233c"> 2. Definition of Constructor</span>

A **constructor** is a special method in Python:

- That is **automatically and implicitly invoked** by the Python Virtual Machine (PVM) when an object is created.
- Its role is to initialize the object by defining its **instance variables**.

---

### <span style="color:#ef233c"> 3. Syntax of Constructor</span>

```python
class ClassName:
    def __init__(self, list_of_formal_parameters_if_any):
        # Initialization block
        # Assign values to instance variables
```

---

### <span style="color:#ef233c"> 4. Properties / Rules of Constructors</span>

1. Constructor name is always `__init__`.
2. Called **automatically** at the time of object creation.
3. Cannot return values except `None`.
4. Can **participate in inheritance** (child classes can call parent constructors).
5. Can be **overridden** (child class can define its own constructor, replacing the parent’s).
6. Each object creation executes the constructor **once**.

---

### <span style="color:#ef233c"> 5. Internal Working of Constructor</span>

1. When `obj = ClassName()` is executed:

   - Memory is allocated for the object.
   - PVM **implicitly calls the `__init__` method** with `self` pointing to the newly created object.

2. Instance variables assigned inside `__init__` become unique to each object.
3. If no constructor is defined, Python provides a **default empty constructor** automatically.

---

### <span style="color:#ef233c"> 6. Types of Constructors</span>

### (a) Default / Parameter-less Constructor

- Takes no formal arguments other than `self`.
- Initializes all objects with the **same values**.

```python
class Test:
    def __init__(self):
        print("Default constructor called")
        self.a = 10
        self.b = 20

# Every object gets same values
t1 = Test()
t2 = Test()
print(t1.a, t1.b)   # 10 20
print(t2.a, t2.b)   # 10 20
```

---

### (b) Parameterized Constructor

- Takes additional parameters apart from `self`.
- Initializes objects with **different values**.

```python
class Test:
    def __init__(self, x, y):
        print("Parameterized constructor called")
        self.a = x
        self.b = y

t1 = Test(1, 2)
t2 = Test(10, 20)
print(t1.a, t1.b)   # 1 2
print(t2.a, t2.b)   # 10 20
```

---

### (c) Unified Constructor (Default + Parameterized)

- Python **does not support constructor overloading** (latest definition overrides previous).
- To support both default and parameterized usage, we use **default arguments**.

```python
class Test:
    def __init__(self, x=0, y=0):
        print("Default/Parameterized constructor called")
        self.a = x
        self.b = y

t1 = Test()        # Acts as default constructor
t2 = Test(5, 15)   # Acts as parameterized constructor
```

---

## <span style="color:#ef233c"> 7. Use Cases of Constructors</span>

1. **Initialization of object data** (assigning values at object creation).
2. **Ensuring no object is left empty**.
3. **Input validation** at the time of object creation.
4. **Inheritance handling** – calling parent constructors from child constructors.
5. **Encapsulation** – hiding internal implementation details by setting private variables in constructors.

---

## <span style="color:#ef233c"> 8. Precautions with Constructors</span>

1. Always use `self` as the first parameter (mandatory).
2. Avoid returning values (returning anything other than `None` will cause errors).
3. If using default parameters, ensure order is correct (non-default args should not follow default args).
4. If constructor is overridden in a child class, explicitly call the parent constructor with `super().__init__()` if needed.
5. Do not overload multiple constructors with the same name (`__init__`), as Python keeps only the **latest one**.

---

## <span style="color:#ef233c"> 9. Best Practices for Constructors</span>

1. Keep constructors **simple and lightweight** (only initialization, not heavy logic).
2. Use **default parameters** instead of multiple constructors.
3. Use **meaningful names** for constructor parameters.
4. For complex initialization, delegate work to **helper methods** instead of making constructors large.
5. Always call `super().__init__()` in child classes if parent initialization is necessary.

---

## <span style="color:#ef233c"> 10. Example: Demonstrating All Concepts</span>

```python
class Person:
    def __init__(self, name="Unknown", age=0):
        """Unified constructor with default arguments"""
        if age < 0:
            raise ValueError("Age cannot be negative")
        self.name = name
        self.age = age
        print(f"Object initialized: {self.name}, {self.age}")

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")


# Case 1: Default Constructor
p1 = Person()
p1.display()

# Case 2: Parameterized Constructor
p2 = Person("Alice", 25)
p2.display()

# Case 3: Invalid input handled inside constructor
try:
    p3 = Person("Bob", -5)
except ValueError as e:
    print("Error:", e)
```

**Output:**

```
Object initialized: Unknown, 0
Name: Unknown, Age: 0
Object initialized: Alice, 25
Name: Alice, Age: 25
Error: Age cannot be negative
```

---

## <span style="color:#ef233c"> 11. Summary</span>

- **Constructor** (`__init__`) initializes objects.
- Types: **Default** (same values), **Parameterized** (different values), **Unified** (default args).
- **Called automatically** by PVM during object creation.
- Best used for **initializing, validating, and securing object data**.
- Cannot overload multiple constructors; use default parameters.

---
