# <span style="color:#003566">**Types of Methods in a Class**</span>

## <span style="color:#ffc300">**Instance Mehtod**</span>

✅ **Definition**:

- Instance methods are functions **inside a class** that operate on **individual objects (instances)**.
- They always take **`self`** as the first parameter → which represents the **current object**.

---

### <span style="color:#ef233c"> **1. Can we use different name instead of `self`?**</span>

- **Yes**. Python does not force the keyword `self`.
- You can use any valid variable name (e.g., `obj`, `this`, `me`).
- BUT ⚠️ — **best practice is to always use `self`** for readability & consistency.

```python
class Demo:
    def show(this, value):   # using 'this' instead of self
        print("Value is:", value)

d = Demo()
d.show(10)   # ✅ Works fine
```

👉 Though this works, **avoid doing it**. Other Python programmers will expect `self`.

---

### <span style="color:#ef233c"> **2. Precautions while writing Instance Methods**</span>

- Always put `self` as the **first parameter**.
- Access instance variables as `self.varname` (not just `varname`).
- Ensure instance variables exist before using them (usually initialize them in `__init__`).
- Don’t misuse instance methods for class-level logic (use `@classmethod` or `@staticmethod` for that).

---

### <span style="color:#ef233c"> **3. Best Practices**</span>

- ✅ Use `self` for clarity.
- ✅ Initialize **all instance variables** in `__init__` so they are guaranteed to exist.
- ✅ Use meaningful method names (e.g., `deposit_money()`, not `do_stuff()`).
- ❌ Avoid modifying class-level data from instance methods unless necessary.
- ❌ Avoid creating instance variables dynamically inside random methods (creates confusion).

---

### <span style="color:#ef233c"> **4. Accessing Instance Methods**</span>

### a) Via **Object Name**

```python
class Student:
    def __init__(self, name):
        self.name = name

    def display(self):   # Instance Method
        print("Student Name:", self.name)

s = Student("Alice")
s.display()   # ✅ Accessed via object name
```

---

### b) Via **self (inside another instance method)**

```python
class Student:
    def __init__(self, name):
        self.name = name

    def greet(self):
        self.display()   # ✅ Accessed using self

    def display(self):
        print("Hello,", self.name)

s = Student("Bob")
s.greet()   # Calls display() internally
```

---

### <span style="color:#ef233c">**5. Example: Good Programming with Instance Methods**</span>

Let’s model a **Bank Account** 👇

```python
class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder   # Instance Variable
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"{amount} deposited. New Balance = {self.balance}")
        else:
            print("❌ Invalid deposit amount")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"{amount} withdrawn. New Balance = {self.balance}")
        else:
            print("❌ Insufficient balance")

    def show_balance(self):
        print(f"Account Holder: {self.account_holder}, Balance: {self.balance}")


# ✅ Using instance methods
account1 = BankAccount("Alice", 1000)
account1.deposit(500)      # Alice deposits 500
account1.withdraw(300)     # Alice withdraws 300
account1.show_balance()    # Check balance
```

### Output

```
500 deposited. New Balance = 1500
300 withdrawn. New Balance = 1200
Account Holder: Alice, Balance: 1200
```

---

# 🎯 Summary

- **Instance methods** → Object-level methods, always take `self`.
- `self` can be renamed, but **don’t** — always use `self`.
- Initialize attributes in constructor (`__init__`).
- Access methods:

  - `object.method()`
  - `self.method()` (inside class).

- Great for modeling **real-world entities** (students, accounts, employees).

---

## <span style="color:#ffc300"> **Class Methods in Python**</span>

### <span style="color:#ef233c"> 1. What is `cls`?</span>

- `cls` is an **implicit object** passed automatically to a class method (just like `self` in instance methods).
- It refers to the **current class** — not an object.
- With `cls`, we can:

  - Access/modify **class variables**.
  - Call **other class methods**.
  - Create **alternative constructors**.

---

### <span style="color:#ef233c"> 2. Can we use something other than `cls`?</span>

✅ Yes, you can technically use any name (e.g., `klass`, `c`, `thisclass`), but:

- 🚫 Not recommended → It breaks Python conventions.
- ✅ Best practice → Always use `cls` (just like `self` for instance methods).

```python
class Demo:
    @classmethod
    def method(klass):   # works, but unusual
        print("Class is:", klass.__name__)

Demo.method()   # Class is: Demo
```

---

### <span style="color:#ef233c"> 3. Precautions while writing Class Methods</span>

1. Always use the `@classmethod` decorator.
2. Always use `cls` as the first parameter.
3. Don’t confuse **instance variables** (`self.name`) with **class variables** (`cls.school`).
4. Keep instance-specific logic inside **instance methods**.
5. Use class methods when the behavior is **common for all objects**.

---

### <span style="color:#ef233c"> 4. Best Practices</span>

- Use class methods for:

  - **Class-wide operations** (like updating a shared value).
  - **Alternative constructors** (to create objects in special ways).

- Don’t modify instance variables (`self.x`) in class methods.
- Follow naming conventions (`cls` always).

---

### <span style="color:#ef233c"> 5. Ways to Access Class Methods</span>

```python
class Student:
    school = "ABC School"   # class data member

    def __init__(self, name):
        self.name = name    # instance data member

    @classmethod
    def get_school(cls):
        return f"School is: {cls.school}"
```

### ✅ Access via **class name**

```python
print(Student.get_school())   # School is: ABC School
```

### ✅ Access via **cls** (inside another class method)

```python
class Student:
    school = "ABC School"

    @classmethod
    def method1(cls):
        return cls.method2()

    @classmethod
    def method2(cls):
        return f"Accessed via cls: {cls.school}"

print(Student.method1())   # Accessed via cls: ABC School
```

### ✅ Access via **object**

```python
s = Student("Alice")
print(s.get_school())   # School is: ABC School
```

### ✅ Access via **self** (inside an instance method)

```python
class Student:
    school = "ABC School"
    def __init__(self, name):
        self.name = name
    @classmethod
    def get_school(cls):
        return cls.school
    def show(self):
        print(self.get_school())   # accessing class method with self

s = Student("Alice")
s.show()   # ABC School
```

---

### <span style="color:#ef233c"> 6. Good Programming Example: All Use Cases of Class Methods</span>

```python
class BankAccount:
    bank_name = "ABC Bank"   # Class data member (shared)
    interest_rate = 0.05     # Class data member (shared)

    def __init__(self, owner, balance=0):
        self.owner = owner         # Instance data member
        self.balance = balance

    # Instance method → object-specific logic
    def deposit(self, amount):
        self.balance += amount
        print(f"{self.owner} deposited {amount}. Balance = {self.balance}")

    # Class method → shared logic
    @classmethod
    def change_interest_rate(cls, new_rate):
        cls.interest_rate = new_rate
        print(f"Interest rate updated to {cls.interest_rate}")

    # Class method → alternative constructor
    @classmethod
    def from_string(cls, account_str):
        owner, balance = account_str.split("-")
        return cls(owner, float(balance))

    # Instance method accessing class method through self
    def show_interest(self):
        print(f"{self.owner}'s account will earn {self.balance * self.interest_rate} interest.")

# ✅ Access via class name
BankAccount.change_interest_rate(0.07)

# ✅ Access via object
a1 = BankAccount("Alice", 1000)
a1.deposit(500)
a1.show_interest()

a2 = BankAccount("Bob", 2000)
a2.show_interest()

# ✅ Alternative constructor using class method
a3 = BankAccount.from_string("Charlie-1500")
a3.show_interest()
```

### 📝 Output:

```
Interest rate updated to 0.07
Alice deposited 500. Balance = 1500
Alice's account will earn 105.0 interest.
Bob's account will earn 140.0 interest.
Charlie's account will earn 105.0 interest.
```

---

✅ **Summary**

- `cls` = reference to class (convention, like `self`).
- Class methods are used for **class-level operations** and **alternative constructors**.
- Access them via **class name, object, cls, or self**.
- Best practice → Always use `cls`, use class methods only for shared/common behavior.

---

Alright, let’s build complete notes on **Static Methods in Python** in a structured way.

---

## <span style="color:#ffc300"> **Static Methods in Python**</span>

### <spans style="color:#ef233c"> 1. What is a Static Method?</span>

- A **static method** belongs to a class but does **not** take `self` (object) or `cls` (class) as its first parameter.
- It behaves like a **normal function**, but it is placed inside a class because it is logically related to that class.
- Typically used for **utility** or **helper functions**.

---

### <spans style="color:#ef233c"> 2. Syntax of Static Method</span>

```python
class ClassName:
    @staticmethod
    def static_method_name(param1, param2, ...):
        # perform universal/utility operation
```

---

### <spans style="color:#ef233c"> 3. Precautions while Writing Static Methods</span>

1. Do not use `self` or `cls` as parameters (they are not tied to objects or class).
2. They should not modify instance variables or class variables directly.
3. Keep them for **independent, reusable logic** (utility tasks).
4. If a method frequently accesses or modifies class data, it should be a **class method** instead.

---

### <spans style="color:#ef233c"> 4. Uses of Static Methods</span>

- **Utility functions**: operations that don’t depend on object state (e.g., math calculations, string formatting).
- **Data validation**: checking input formats, constraints.
- **Helper functions**: supporting class functionality without touching object/class data.

---

### <spans style="color:#ef233c"> 5. Best Practices</span>

- Use static methods only if the method does not need to know about the class (`cls`) or the object (`self`).
- Group utility functions inside classes for **better organization**, instead of keeping them outside as plain functions.
- If the method interacts with **class variables** → make it a class method.
- If the method interacts with **instance variables** → make it an instance method.

---

### <spans style="color:#ef233c"> 6. Accessing Static Methods</span>

Static methods can be called in different ways:

#### (a) Using Class Name

```python
class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

print(MathUtils.add(5, 10))   # 15
```

#### (b) Using Object Name

```python
obj = MathUtils()
print(obj.add(3, 7))   # 10
```

#### (c) Using `cls` (from inside a class method)

```python
class MathUtils:
    @staticmethod
    def multiply(a, b):
        return a * b

    @classmethod
    def call_static(cls):
        return cls.multiply(4, 5)

print(MathUtils.call_static())   # 20
```

#### (d) Using `self` (from inside an instance method)

```python
class MathUtils:
    @staticmethod
    def square(x):
        return x * x

    def show_square(self, value):
        return self.square(value)

obj = MathUtils()
print(obj.show_square(6))   # 36
```

---

### <spans style="color:#ef233c">7. Good Programming Example of Static Methods</span>

```python
class Validator:
    @staticmethod
    def is_positive_number(value):
        """Check if the given value is a positive number"""
        return isinstance(value, (int, float)) and value > 0

    @staticmethod
    def is_valid_email(email):
        """Simple email validation"""
        return "@" in email and "." in email

class BankAccount:
    interest_rate = 0.05

    def __init__(self, owner, balance):
        if not Validator.is_positive_number(balance):
            raise ValueError("Balance must be a positive number")
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if not Validator.is_positive_number(amount):
            raise ValueError("Deposit must be a positive number")
        self.balance += amount
        print(f"{amount} deposited. New balance: {self.balance}")

    def withdraw(self, amount):
        if not Validator.is_positive_number(amount):
            raise ValueError("Withdrawal must be a positive number")
        if self.balance >= amount:
            self.balance -= amount
            print(f"{amount} withdrawn. New balance: {self.balance}")
        else:
            print("Insufficient funds!")

# Usage
acc1 = BankAccount("Alice", 1000)
acc1.deposit(200)
acc1.withdraw(150)

# Static methods accessed directly using class
print(Validator.is_valid_email("test@example.com"))   # True
print(Validator.is_valid_email("wrong-email"))       # False
```

---

### 8. Summary

- **Static Method**: Function inside a class with no `self` or `cls`.
- **Access**: via class name, object name, cls (inside classmethod), self (inside instancemethod).
- **Use cases**: Utility functions, validation, independent operations.
- **Best practice**: Use static methods when no class-level or object-level data is required.

---
