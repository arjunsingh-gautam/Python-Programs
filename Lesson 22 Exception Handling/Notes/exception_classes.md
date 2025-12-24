# 1. What are Exception Classes in Python?

### Definition

An **exception class** is a **blueprint** that defines:

- The _type_ of runtime error
- The _category_ of abnormal behavior
- The _name_ and _structure_ of the error

All exception classes in Python:

- Are **classes**
- Inherit from the base class `BaseException`

---

### Exception Hierarchy (Core Idea)

```
BaseException
 ├── Exception
 │    ├── ArithmeticError
 │    ├── LookupError
 │    ├── TypeError
 │    ├── ValueError
 │    └── ...
 ├── SystemExit
 ├── KeyboardInterrupt
 └── GeneratorExit
```

Important:

- You normally catch exceptions derived from `Exception`
- You usually do NOT catch `SystemExit` or `KeyboardInterrupt`

---

# 2. What are Exception Objects?

### Definition

An **exception object** is an **instance of an exception class** that is created **at runtime** when an error occurs.

---

### Example

```python
try:
    x = 10 / 0
except ZeroDivisionError as e:
    print(e)
```

Here:

- `ZeroDivisionError` → exception class
- `e` → exception object created at runtime

---

### What an Exception Object Contains

- Error message
- Stack trace information
- Context about where and why the error occurred

---

# 3. Built-in Exception Classes and Their Runtime Errors

Below are the **most important built-in exception classes**, grouped by category.
(These are what Python developers are expected to know.)

---

## A. Arithmetic Exceptions

### ArithmeticError (Base class)

| Exception         | Raised When                   |
| ----------------- | ----------------------------- |
| ZeroDivisionError | Division or modulo by zero    |
| OverflowError     | Result too large to represent |

```python
10 / 0
```

---

## B. Type and Value Exceptions

| Exception  | Raised When                     |
| ---------- | ------------------------------- |
| TypeError  | Operation on incompatible types |
| ValueError | Correct type but invalid value  |

```python
"10" + 5      # TypeError
int("abc")   # ValueError
```

---

## C. Lookup Exceptions

### LookupError (Base class)

| Exception  | Raised When              |
| ---------- | ------------------------ |
| IndexError | Invalid list/tuple index |
| KeyError   | Missing dictionary key   |

```python
lst[10]
d["missing"]
```

---

## D. Name and Attribute Exceptions

| Exception      | Raised When          |
| -------------- | -------------------- |
| NameError      | Variable not defined |
| AttributeError | Attribute not found  |

```python
print(x)
obj.non_existing_attr
```

---

## E. Import Exceptions

| Exception           | Raised When           |
| ------------------- | --------------------- |
| ImportError         | Import fails          |
| ModuleNotFoundError | Module does not exist |

```python
import fake_module
```

---

## F. File and IO Exceptions

| Exception         | Raised When                  |
| ----------------- | ---------------------------- |
| FileNotFoundError | File does not exist          |
| PermissionError   | No permission to access file |
| IOError / OSError | OS-level IO failures         |

```python
open("missing.txt")
```

---

## G. Assertion Exception

| Exception      | Raised When            |
| -------------- | ---------------------- |
| AssertionError | assert condition fails |

```python
assert 2 + 2 == 5
```

---

## H. Runtime Control Exceptions

| Exception      | Raised When                      |
| -------------- | -------------------------------- |
| RuntimeError   | Generic runtime failure          |
| RecursionError | Maximum recursion depth exceeded |

```python
def f():
    f()
```

---

## I. System-Level Exceptions (Usually Not Caught)

| Exception         | Raised When       |
| ----------------- | ----------------- |
| KeyboardInterrupt | Ctrl+C pressed    |
| SystemExit        | sys.exit() called |

---

# 4. How Python Reacts to Runtime Errors

Internally:

1. Python executes code line by line
2. When an error occurs:

   - Python **creates an exception object**

3. It **matches the object’s class** with `except` blocks
4. If matched:

   - Handler executes

5. If not:

   - Program crashes with traceback

---

# 5. Creating Your Own Exception Classes

## Why Create Custom Exceptions?

- To represent **domain-specific errors**
- To make error handling **clear and meaningful**
- To avoid using generic exceptions everywhere

---

## Basic Rule

Your exception class **must inherit from `Exception`**

---

## Simple Custom Exception

```python
class AgeError(Exception):
    pass
```

Usage:

```python
age = -5
if age < 0:
    raise AgeError("Age cannot be negative")
```

---

## Custom Exception with Logic

```python
class InsufficientBalanceError(Exception):
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        super().__init__(
            f"Balance {balance} is insufficient for withdrawal {amount}"
        )
```

Usage:

```python
balance = 100
withdraw = 200

if withdraw > balance:
    raise InsufficientBalanceError(balance, withdraw)
```

---

## Catching Custom Exceptions

```python
try:
    raise AgeError("Invalid age")
except AgeError as e:
    print(e)
```

---

# 6. Exception Classes vs Exception Objects (Summary)

| Aspect  | Exception Class    | Exception Object                     |
| ------- | ------------------ | ------------------------------------ |
| Nature  | Blueprint          | Instance                             |
| Created | At definition time | At runtime                           |
| Purpose | Defines error type | Carries error details                |
| Example | ZeroDivisionError  | e in `except ZeroDivisionError as e` |

---

# 7. Key Takeaways

- Exception classes define **types of runtime errors**
- Exception objects are **created at runtime**
- Python has a rich built-in exception hierarchy
- Custom exceptions improve clarity and control
- Always inherit from `Exception`, not `BaseException`

---
