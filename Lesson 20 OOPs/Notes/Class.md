# <span style="color:#003566">**Class**</span>

## <span style="color:#ffc300">**Class Basics**</span>

### <span style="color:#ef233c"> **1) A class is a _blueprint_**</span>

- **Definition:** a class declares what data (attributes) and behavior (methods) objects of that type will have.
- **Important:** declaring a class **does not** create any instance storage. It only creates a _class object_ that holds the definitions.

```python
class Dog:
    species = "Canis"          # class attribute (shared)
    def __init__(self, name):  # initializer (constructor)
        self.name = name       # instance attribute (per-object)
    def bark(self):            # method (a function defined on the class)
        return f"{self.name} says woof"
```

- After the `class` statement runs, `Dog` (the class object) exists with its attributes (`species`, `__init__`, `bark`) stored on the class.

---

### <span style="color:#ef233c"> **2) Memory: when space is allocated?**</span>

- **Class definition time:** Python creates the class object. The _function objects_ for methods live on the class (in `Dog.__dict__`). No per-instance storage yet.
- **Object creation time (`Dog("Fido")`)**: Python allocates an _instance object_, normally with an `__dict__`, and fills instance attributes (like `name`). That's where per-object data is stored.
- So: _class = shared blueprint + shared methods; instance = per-object data storage_.

```python
print("class attrs:", Dog.__dict__.keys())  # contains 'species', '__init__', 'bark'
d = Dog("Fido")
print("instance dict:", d.__dict__)         # {'name': 'Fido'}
```

---

### <span style="color:#ef233c"> **3) Methods vs data — who owns what?**</span>

- **Methods** are defined once on the class. They are _not copied_ into each instance. When you access `d.bark`, Python returns a _bound method_ which wraps the function and the instance.
- **Instance attributes** (like `name`) live in `d.__dict__` (unless you use `__slots__`).
- **Class attributes** (like `species`) live in `Dog.__dict__` and are shared by all instances unless an instance overrides them.

Example showing sharing vs per-instance:

```python
a = Dog("Fido")
b = Dog("Rex")

print(a.species, b.species)  # both "Canis"
a.species = "Wolf"          # shadows class attribute on instance a
print(a.species, b.species)  # "Wolf", "Canis"
```

---

### <span style="color:#ef233c"> **4) Attribute lookup order (how Python finds `x` when you do `obj.x`)**</span>

1. Look in `obj.__dict__` (instance attributes)
2. Look in the class (`obj.__class__.__dict__`)
3. Look up the inheritance chain (base classes)
4. If nothing, `AttributeError`

This is why instance attributes can _override_ class attributes.

---

### <span style="color:#ef233c"> **5) `self` and how methods work**</span>

- A method is just a function whose first parameter conventionally named `self`.
- When you call `d.bark()`, Python implicitly does `Dog.bark(d)`. The instance is passed in as the first argument.
- That’s how methods get access to instance data.

```python
# inside class
def set_name(self, new_name):
    self.name = new_name    # modifies instance state via self
```

---

### <span style="color:#ef233c"> **6) Class variables vs instance variables**</span>

- **Class variables** (defined directly in class body) are shared across instances.
- **Instance variables** (created in `__init__` or elsewhere on `self`) are unique to each object.
- **Pitfall:** mutable class variables (lists/dicts) are shared — often a source of bugs.

```python
class C:
    shared = []          # one list shared by all instances

a = C(); b = C()
a.shared.append(1)
print(b.shared)  # [1]  ← surprise if you expected separate lists
```

If you want separate lists, initialize them in `__init__` as `self.data = []`.

---

### <span style="color:#ef233c"> **7) Memory optimization: `__slots__`**</span>

- By default, instances have a `__dict__` and can have arbitrary attributes (flexible but more memory per instance).
- `__slots__` lets you declare a fixed set of attributes and prevent `__dict__` creation, saving memory for many instances:

```python
class Lite:
    __slots__ = ("x", "y")
    def __init__(self, x, y):
        self.x = x; self.y = y
```

---

### <span style="color:#ef233c"> **8) Method types: instance, class, static**</span>

- `def f(self, ...)` → **instance method** (receives instance)
- `@classmethod def f(cls, ...)` → **class method** (receives class)
- `@staticmethod def f(...)` → **static method** (no implicit first arg)

Use classmethods for alternative constructors or behavior that operates on the class, staticmethods for utility functions tied to class namespace.

---

### <span style="color:#ef233c"> **9) Why this design matters (practical benefits)**</span>

- **Encapsulation:** data + functions close together → easier reasoning.
- **Reusability:** classes can be extended via inheritance.
- **Memory efficiency for methods:** methods are stored once, not per-instance.
- **Clear structure:** objects model real-world entities; attribute lookup is predictable.

---

### <span style="color:#ef233c"> **10) Short example that ties it all** </span>

```python
class Student:
    school = "Central High"         # class attribute (shared)

    def __init__(self, name, grades):
        self.name = name            # instance attribute (per student)
        self.grades = grades

    def avg(self):
        return sum(self.grades) / len(self.grades)

s1 = Student("Alice", [90, 95])
s2 = Student("Bob",   [80, 85])
print(s1.avg(), s2.avg())         # per-instance behaviour
print(s1.school, s2.school)       # same shared class attribute
```

---

### <span style="color:#ef233c"> **Precautions / common gotchas**

- Don’t store mutable per-instance data as class attributes (shared mutation).
- Remember methods are functions — you can inspect `Student.avg` (function) vs `s1.avg` (bound method).
- Overusing class attributes for per-instance state will cause bugs.
- `__slots__` saves memory but removes flexibility (no dynamic attributes, less introspection).

---

### Quick summary

- **Class** = blueprint (data + behavior definitions).
- **Instance** = allocated memory that holds per-object data (created when you call the class).
- **Methods** live on the class and are shared; **instance attributes** live in each object.
- Attribute lookup: instance → class → base classes.
- Use `__init__` to initialize per-instance data; use `__slots__` to save memory when you have many objects.

---

## <span style="color:#ffc300"> **Complete Syntax of a Class (Boilerplate)**</span>

```python
class ClassName:
    # -------------------------
    # 1. Class Data Members
    # -------------------------
    class_variable = "shared by all objects"

    # -------------------------
    # 2. Constructor
    # -------------------------
    def __init__(self, value1, value2):
        # Instance Data Members (unique for each object)
        self.value1 = value1
        self.value2 = value2

    # -------------------------
    # 3. Instance Method
    # -------------------------
    def instance_method(self):
        # Works on object’s data (uses self)
        return f"value1 = {self.value1}, value2 = {self.value2}"

    # -------------------------
    # 4. Class Method
    # -------------------------
    @classmethod
    def class_method(cls):
        # Works on the class itself (uses cls)
        return f"class_variable = {cls.class_variable}"

    # -------------------------
    # 5. Static Method
    # -------------------------
    @staticmethod
    def static_method(info):
        # Utility function, no access to class or instance
        return f"Info: {info}"

    # -------------------------
    # 6. Destructor
    # -------------------------
    def __del__(self):
        print(f"Object with value1={self.value1} destroyed")
```

---

### **Breaking It Down**

### <span style="color:#ef233c"> 1) **Class Data Members**</span>

- Defined directly inside the class body.
- Shared across all instances unless shadowed by an instance.

```python
class_variable = "shared"
```

### <span style="color:#ef233c"> 2) **Constructor (`__init__`)**</span>

- Special method that initializes instance variables when an object is created.
- Runs automatically when you do `obj = ClassName(...)`.

```python
def __init__(self, value1, value2):
    self.value1 = value1
    self.value2 = value2
```

### <span style="color:#ef233c"> 3) **Instance Methods**</span>

- Most common methods.
- Always take `self` as the first parameter.
- Used to read/update **instance data members**.

```python
def instance_method(self):
    return self.value1
```

### <span style="color:#ef233c"> 4) **Class Methods**</span>

- Defined with `@classmethod`.
- First parameter is `cls` (class itself).
- Used to access/modify **class data members**.

```python
@classmethod
def class_method(cls):
    return cls.class_variable
```

### <span style="color:#ef233c"> 5) **Static Methods**</span>

- Defined with `@staticmethod`.
- No `self` or `cls`.
- Behaves like a normal function but logically belongs to the class.

```python
@staticmethod
def static_method(info):
    return f"Info: {info}"
```

### <span style="color:#ef233c"> 6) **Destructor (`__del__`)**</span>

- Special method called when an object is destroyed (garbage collected).
- In practice, rarely used in Python (since garbage collection is automatic).

```python
def __del__(self):
    print("Object destroyed")
```

---

### **🎯 Example in Action**

```python
class Student:
    # Class Data Member
    school_name = "Central High"

    def __init__(self, name, grade):
        # Instance Data Members
        self.name = name
        self.grade = grade

    # Instance Method
    def show(self):
        return f"{self.name} is in grade {self.grade}"

    # Class Method
    @classmethod
    def get_school(cls):
        return cls.school_name

    # Static Method
    @staticmethod
    def greet():
        return "Welcome to the school system!"

    # Destructor
    def __del__(self):
        print(f"Student {self.name} is being removed")
```

Usage:

```python
s1 = Student("Alice", 10)
print(s1.show())            # instance method
print(Student.get_school()) # class method
print(Student.greet())      # static method
del s1                      # destructor runs
```

---

👉 So the **boilerplate** for any OOP class in Python is:

- **Class variables** (shared data)
- **Constructor** (`__init__`)
- **Instance methods** (operate on objects)
- **Class methods** (operate on the class)
- **Static methods** (utility functions)
- **Destructor** (`__del__`, optional)

---
