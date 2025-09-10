# <span style="color:#003566"> **Objects in Python**</span>

### <span style="color:#ef233c"> 1. Introduction</span>

- In **Object-Oriented Programming (OOP)**, a class provides the **blueprint** (model/specification), while an **object** represents the **real entity** created from that class.
- Defining a class **does not create memory space** for its data members and methods.
- Memory is allocated only when we **create an object** of the class.

---

### <span style="color:#ef233c"> 2. Definition of Object</span>

- **An object is an instance of a class.**
- **Instance** means allocation of sufficient memory space for the class’s **data members (variables)** and **methods (functions)**.
- Objects allow us to store and manipulate data in real-time applications.

---

### <span style="color:#ef233c"> 3. Purpose of Object</span>

1. To **store data** inside memory.
2. To **perform operations** or data processing using the class methods.
3. To **represent real-world entities** such as `Student`, `Employee`, `BankAccount`, etc.
4. Without objects, class definitions are useless (just specifications).

---

### <span style="color:#ef233c"> 4. Syntax for Creating Objects</span>

```python
# Syntax
variable_name = ClassName()          # Default constructor call
variable_name = ClassName(arg1, arg2, ...)  # Parameterized constructor call
```

### Examples

```python
# Creating an object of Student
s1 = Student()

# Creating an object of Employee
e1 = Employee(10, "Rossum")
```

---

### <span style="color:#ef233c"> 5. Internal Working of Object Creation</span>

1. When `obj = ClassName()` is executed:

   - Python allocates **memory** for the object.
   - `__init__()` constructor is **automatically called** to initialize the object.
   - The reference (address) of the memory location is stored in `obj`.

2. If the class definition is not loaded before object creation, Python raises a **NameError**.

---

### <span style="color:#ef233c"> 6. Differences Between Class and Object</span>

| **Aspect** | **Class**                                                       | **Object**                                                   |
| ---------- | --------------------------------------------------------------- | ------------------------------------------------------------ |
| Definition | Collection of data members (variables) and methods (functions). | Instance of a class (real entity created from class).        |
| Memory     | No memory allocated when a class is defined.                    | Memory allocated when an object is created.                  |
| Existence  | Exists only once in a program (single definition).              | Multiple objects can be created from one class.              |
| Purpose    | Acts as **specification / blueprint** for real-world entities.  | Used to **store data and perform operations**.               |
| Loading    | Loaded into main memory **once** when the program starts.       | Created after class definition is loaded.                    |
| Error      | No error defining a class.                                      | Creating an object without class definition → **NameError**. |

---

### <span style="color:#ef233c"> 7. Example Program</span>

```python
class Student:
    def __init__(self, sid, name):
        self.sid = sid
        self.name = name

    def display(self):
        print(f"Student ID: {self.sid}, Name: {self.name}")


# Creating multiple objects
s1 = Student(101, "Alice")
s2 = Student(102, "Bob")

s1.display()   # Student ID: 101, Name: Alice
s2.display()   # Student ID: 102, Name: Bob
```

### Explanation:

- `Student` is the **class** (blueprint).
- `s1` and `s2` are **objects** (instances with different data).
- Both share the same class definition but have their own **separate memory spaces** for data.

---

### <span style="color:#ef233c"> 8. Key Points to Remember about Objects</span>

1. An object is created only **after class definition is available**.
2. Each object has **its own copy of instance variables**, but methods are shared.
3. Objects allow **real-world modeling** in programs.
4. Objects serve as the **bridge between data and behavior** of a class.
5. Using multiple objects, we can represent multiple entities from the same class.

---

Excellent question — this is **one of the most important topics** to truly understand Python OOP.
Let’s go step by step into the **memory architecture of Classes and Objects in Python**.

---

## <span style="color:#ffc300"> **Memory Architecture of Classes and Objects in Python**</span>

---

### 1. Where Are Things Stored in Python?

- Python stores everything as **objects** in memory.
- Each **class definition** and **object (instance)** lives in **heap memory**.
- **Variables (names)** act as **references** to these objects, and they live in **stack memory** (namespace dictionary).

---

### 2. Memory Layout of a Class

When a class is defined:

```python
class Test:
    class_var = 100  # class attribute

    def __init__(self, x):
        self.x = x   # instance attribute
```

#### What happens internally:

1. Python creates a **class object** (`Test`) and stores it in memory.
2. A **namespace dictionary** is created for the class.

   - It contains entries for:

     - Class attributes (`class_var`)
     - Methods (`__init__`, etc.)

3. Each method is stored as a **function object** in the class dictionary.
4. Memory is **not allocated for instance attributes yet** (they belong to objects).

---

#### Class Memory Representation (Dictionary)

```python
Test.__dict__
```

Output (approx):

```python
{
  '__module__': '__main__',
  'class_var': 100,
  '__init__': <function Test.__init__ at 0x7f9...>,
  '__dict__': <attribute '__dict__' of 'Test' objects>,
  '__weakref__': <attribute '__weakref__' of 'Test' objects>,
  '__doc__': None
}
```

---

### 3. Memory Layout of an Object

When an object is created:

```python
t1 = Test(10)
```

#### What happens internally:

1. Python allocates **heap memory** for the new object `t1`.
2. A **separate instance dictionary** is created for storing instance-specific attributes (`self.x`).
3. The **class reference** (`__class__`) is stored in the object to access class-level members.
4. If we access an attribute, Python looks in:

   - Object’s namespace dictionary (instance attributes).
   - Then in the Class namespace dictionary (class attributes, methods).
   - Then in Parent classes (MRO → Method Resolution Order).

---

#### Object Memory Representation (Dictionary)

```python
t1.__dict__
```

Output:

```python
{'x': 10}
```

Notice that `class_var` is not inside the object — it stays in the class dictionary.

---

### 4. Combined Example

```python
class Demo:
    class_attr = "I am Class Attribute"

    def __init__(self, val):
        self.instance_attr = val

    def show(self):
        print(f"Instance Attribute: {self.instance_attr}, Class Attribute: {Demo.class_attr}")


# Create objects
d1 = Demo(100)
d2 = Demo(200)

# Inspect memory
print(Demo.__dict__)   # Class dictionary
print(d1.__dict__)     # Instance dictionary of d1
print(d2.__dict__)     # Instance dictionary of d2
```

#### Output:

```python
# Class Dictionary
{
  '__module__': '__main__',
  'class_attr': 'I am Class Attribute',
  '__init__': <function Demo.__init__ at 0x...>,
  'show': <function Demo.show at 0x...>,
  '__dict__': <attribute '__dict__' of 'Demo' objects>,
  '__weakref__': <attribute '__weakref__' of 'Demo' objects>,
  '__doc__': None
}

# Object d1 dictionary
{'instance_attr': 100}

# Object d2 dictionary
{'instance_attr': 200}
```

---

### 5. Attribute Resolution Order

When you access an attribute like `d1.class_attr`, Python follows this order (MRO):

1. Search in `d1.__dict__` (instance attributes).
2. If not found, search in `Demo.__dict__` (class attributes).
3. If not found, search in parent classes (`object`, etc.).
4. If still not found → `AttributeError`.

---

### 6. Special Members in Memory

Every object automatically has:

- `__dict__` → Holds instance attributes.
- `__class__` → Points to its class.
- `__weakref__` → Used internally for weak references.

Every class automatically has:

- `__dict__` → Holds class attributes and methods.
- `__bases__` → Tuple of base classes.
- `__name__` → Class name as a string.
- `__module__` → Module name where class is defined.

---

### 7. Visual Representation

```
Class: Demo
-------------------------
class_attr → "I am Class Attribute"
__init__ → <function>
show → <function>

Objects:
-------------------------
d1: {'instance_attr': 100}
d2: {'instance_attr': 200}
```

👉 Both `d1` and `d2` share `class_attr` from the class but have their own `instance_attr`.

---

### 8. Key Takeaways

1. **Class attributes** live in the **class dictionary**, shared across all objects.
2. **Instance attributes** live in the **object’s dictionary**, unique for each object.
3. Methods are stored in the **class dictionary** as function objects, and bound to objects when called.
4. Attribute resolution follows **object → class → parent classes (MRO)**.
5. Objects don’t store methods themselves; they store only **data**, and borrow methods from their class.

---

Excellent point — this is where many learners get confused.
Let’s carefully unpack it:

---

## <span style="color:#ffc300"> **Why Instance Methods Are in the Class Dict, but Still Access Instance Attributes**</span>

---

### 1. Methods in Python are Just Functions

When you define:

```python
class Demo:
    def __init__(self, val):
        self.val = val   # instance attribute

    def show(self):
        print(self.val)
```

#### Internally:

- `__init__` and `show` are **function objects** stored in the **class dictionary**:

```python
print(Demo.__dict__)
```

Output (approx):

```python
{
  '__module__': '__main__',
  '__init__': <function Demo.__init__ at 0x...>,
  'show': <function Demo.show at 0x...>,
  '__dict__': <attribute '__dict__' of 'Demo' objects>,
  '__weakref__': <attribute '__weakref__' of 'Demo' objects>,
  '__doc__': None
}
```

Notice: **methods are not in the object dict**, they are in the class dict.

---

### 2. What Happens When You Call an Instance Method

```python
d1 = Demo(10)
d1.show()
```

- Step 1: Python looks for `show` in `d1.__dict__` → not found.
- Step 2: Looks in `Demo.__dict__` → finds `<function Demo.show at ...>`.
- Step 3: Python automatically converts that **function** into a **bound method**, binding it with the object `d1`.

Effectively, Python does this behind the scenes:

```python
Demo.show(d1)
```

So the first argument (`self`) is filled with the object reference (`d1`).

---

### 3. How Instance Methods Access Instance Attributes

- Inside `show`, we wrote `print(self.val)`.
- Since `self` points to the object (`d1`), Python looks into `d1.__dict__`:

```python
print(d1.__dict__)   # {'val': 10}
```

Thus, `self.val` → looks inside the instance dictionary, not the class dictionary.

---

### 4. Key Idea

- **Methods live in the class dictionary.**
- **Attributes live in the object dictionary.**
- Binding (`self`) is the bridge:

```
Object ----> (self) ----> Method (from class dict)
```

That’s why instance methods can freely access instance attributes.

---

### 5. Demonstration

```python
class Student:
    def __init__(self, name):
        self.name = name   # instance attribute

    def greet(self):
        print(f"Hello, my name is {self.name}")

s1 = Student("Alice")
s2 = Student("Bob")

print(Student.__dict__)   # method stored in class dict
print(s1.__dict__)        # instance attributes of s1
print(s2.__dict__)        # instance attributes of s2

# Calls
s1.greet()   # internally Student.greet(s1)
s2.greet()   # internally Student.greet(s2)
```

Output:

```
Hello, my name is Alice
Hello, my name is Bob
```

---

✅ So:

- **Instance methods are stored once (in class dict).**
- **They get bound to different objects automatically.**
- **`self` is just a reference to the object, giving access to its instance attributes.**

---
