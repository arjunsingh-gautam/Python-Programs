# <span style="color:#003566">**OOPs Basics**</span>

## <span style="color:#ffc300">**Object Oriented Programming**</span>

### <span style="color:#ef233c"> 1. **What is OOP?**

- A **programming paradigm** (</span>style/approach of writing programs).
- In OOP, we structure code around **objects**: entities that combine **data** (attributes) and **behavior** (methods).
- Example in real life:

  - **Car** = object
  - Data: `color`, `speed`, `fuel`
  - Behavior: `drive()`, `brake()`, `refuel()`

Instead of just writing functions and variables everywhere, we model things as objects that **know stuff** and **can do stuff**.

---

### <span style="color:#ef233c"> 2. **Why is it popular?**</span>

OOP became popular becau</span>se it matches **how humans think about the world**:

- We see things as **entities with properties and actions**.
- It makes big systems easier to design in terms of smaller, understandable pieces (objects).

Also:

- It was heavily adopted in big languages (C++, Java, Python, etc.) — so it spread widely.
- Encourages **reuse** and **organization** of code.

---

### <span style="color:#ef233c"> 3. **Why is it important in software development?**</span>

Here’s what OOP gives us:

### 🔑 Benefits:

1. **Encapsulation** → keep data + behavior together.
   (A `BankAccount` object manages its own balance, instead of letting anyone mess with raw variables.)

2. **Abstraction** → hide complexity behind a simple interface.
   (You just call `car.drive()` — you don’t care about the physics inside.)

3. **Inheritance** → create new classes by reusing old ones.
   (`ElectricCar` can inherit from `Car` and just add battery-related stuff.)

4. **Polymorphism** → same interface, different behavior.
   (`animal.speak()` → Dog says _Woof_, Cat says _Meow_.)

### 🚀 Why it matters:

- Makes **large projects manageable** (teams can work on separate objects).
- Promotes **code reuse** (don’t reinvent the wheel).
- Improves **maintainability** (easier to update/extend).
- Fits well with **real-world modeling** (games, apps, simulations, GUIs).

---

✅ **Summary:**
OOP = programming with objects that bundle **data** + **behavior**.
It’s popular because it’s natural, reusable, and maintainable.
It’s important because modern software is too complex to manage with just raw functions and variables.

---

## <span style="color:#ffc300">**What makes a Language Object Oriented**</span>

### <span style="color:#ef233c"> 🔑 1. **Classes and Objects**</span>

- A **class** defines a blueprint (like a template).
- An **object** is an actual instance of that class.

👉 If a language supports creating and using classes/objects, that’s the foundation of OOP.

Example in Python:

```python
class Dog:
    def __init__(self, name):
        self.name = name

dog1 = Dog("Buddy")  # object
```

---

### <span style="color:#ef233c"> 🔑 2. **Encapsulation</span>**

- Ability to **bundle data and methods** inside a class.
- Often includes hiding details (using `private`/`protected` attributes).

Example:

```python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance   # private

    def deposit(self, amount):
        self.__balance += amount
```

---

### <span style="color:#ef233c"> 🔑 3. **Inheritance**</span>

- One class can **reuse/extend** another class.
- Encourages reusability and hierarchy.

Example:

```python
class Vehicle:
    def move(self):
        print("Moving")

class Car(Vehicle):   # inherits Vehicle
    pass
```

---

### <span style="color:#ef233c"> 🔑 4. \*_Polymorphism_</span>\*

- The same method name can work differently depending on the object.

Example:

```python
class Dog:
    def speak(self):
        return "Woof"

class Cat:
    def speak(self):
        return "Meow"

for animal in [Dog(), Cat()]:
    print(animal.speak())  # same method name, different behavior
```

---

### <span style="color:#ef233c"> 🔑 5. **Abstraction**</span>

- Ability to define **general concepts** and hide complex details.
- In Python, this can be done with **abstract base classes**.

Example:

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
```

---

### ✅ So, a language is _object-oriented_ if it supports:

1. Classes & Objects
2. Encapsulation
3. Inheritance
4. Polymorphism
5. (Optionally) Abstraction

---
