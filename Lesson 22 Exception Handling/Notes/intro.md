# **<span style="color:#84a98c">Exception Handling in Python</span>**

## What is meant by Exception Handling?

**Exception handling** is the mechanism used in Python to **detect, manage, and respond to runtime errors** (exceptions) so that the program does not terminate abruptly.

It allows a program to:

- Handle unexpected situations gracefully
- Continue execution or exit cleanly
- Provide meaningful error messages instead of crashing

---

## What are Exceptions?

### Definition

An **exception** is an **abnormal event** that occurs **during program execution** and **disrupts the normal flow of instructions**.

Exceptions are **runtime errors** that Python **detects and raises automatically** when something goes wrong.

---

### Example

```python
x = 10
y = 0
print(x / y)
```

Python raises:

```
ZeroDivisionError: division by zero
```

Here:

- The program syntax is correct
- The error happens during execution
- Python raises an exception object

---

## Difference Between Error and Exception

| Aspect       | Error                            | Exception                       |
| ------------ | -------------------------------- | ------------------------------- |
| Meaning      | A serious problem in the program | A runtime abnormal condition    |
| Recoverable? | Usually not                      | Yes, can be handled             |
| Example      | SyntaxError, IndentationError    | ZeroDivisionError, ValueError   |
| Handling     | Program stops immediately        | Can be handled using try-except |
| Occurs       | Before or during execution       | Only during execution           |

### Key Idea

- **Errors** indicate bugs that must be fixed.
- **Exceptions** indicate situations that may occur during normal execution and should be handled.

---

## Types of Exceptions in Python (with examples)

### 1. Built-in Exceptions

Python provides many built-in exception classes.

---

### a) ZeroDivisionError

```python
print(10 / 0)
```

---

### b) TypeError

```python
print("10" + 5)
```

---

### c) ValueError

```python
int("abc")
```

---

### d) IndexError

```python
lst = [1, 2, 3]
print(lst[5])
```

---

### e) KeyError

```python
d = {"a": 1}
print(d["b"])
```

---

### f) FileNotFoundError

```python
open("data.txt")
```

---

### g) NameError

```python
print(x)
```

---

### 2. User-Defined Exceptions

Programmers can define their own exceptions.

```python
class AgeError(Exception):
    pass

age = -5
if age < 0:
    raise AgeError("Age cannot be negative")
```

---

## Why Handling Exceptions is Important

1. **Prevents program crash**

   - Program continues instead of stopping abruptly

2. **Improves user experience**

   - Users see meaningful messages

3. **Maintains program flow**

   - Allows alternate logic when errors occur

4. **Improves reliability**

   - Handles unpredictable input and conditions

5. **Essential for real-world applications**

   - Network failures, file access, invalid user input are common

---

## How Exceptions Are Handled in Python

Python uses the **try-except-else-finally** construct.

---

### Basic Syntax

```python
try:
    # risky code
except ExceptionType:
    # handling code
```

---

### Example

```python
try:
    x = int(input("Enter a number: "))
    print(10 / x)
except ZeroDivisionError:
    print("Cannot divide by zero")
except ValueError:
    print("Invalid input")
```

---

### try-except-else

- `else` runs only if no exception occurs

```python
try:
    print(10 / 2)
except ZeroDivisionError:
    print("Error")
else:
    print("Execution successful")
```

---

### finally Block

- Always executes, whether exception occurs or not
- Used for cleanup operations

```python
try:
    file = open("data.txt")
except FileNotFoundError:
    print("File not found")
finally:
    print("Closing resources")
```

---

## How Python Handles Exceptions Internally (Simplified)

1. Python executes code line by line
2. If an error occurs:

   - Python creates an exception object

3. Python searches for a matching `except` block
4. If found:

   - That block executes

5. If not found:

   - Program terminates with traceback

---

## Key Takeaways

- Exceptions are runtime abnormal events
- Errors usually indicate bugs; exceptions are expected runtime problems
- Python provides many built-in exceptions
- try-except prevents program crashes
- Exception handling is critical for robust software

---

# **<span style="color:#84a98c"> Types of Errors in Python</span>**

In Python, errors are broadly classified into **three categories** based on **when they occur** and **how they affect program execution**:

1. Compile-time errors
2. Run-time errors
3. Logical errors

---

## 1. Compile-Time Errors (Syntax Errors)

### Definition

A **compile-time error** is an error that occurs **before the program starts executing**, when Python is **parsing (reading and converting)** the source code into bytecode.

Python cannot proceed to execution if a compile-time error exists.

In Python, compile-time errors are primarily **syntax errors**.

---

### Cause

Compile-time errors occur due to **violations of Python’s grammar rules**.

Common causes include:

- Missing colon `:` after `if`, `for`, `while`, `def`, `class`
- Incorrect indentation
- Missing or extra parentheses `()`, brackets `[]`, braces `{}`
- Misspelled keywords
- Unterminated strings
- Invalid variable or function definitions

---

### Example

```python
if x > 10
    print("Greater")
```

Error:

```
SyntaxError: expected ':'
```

The program never runs because Python cannot compile the code.

---

### Methods to Fix Compile-Time Errors

1. **Read the error message carefully**

   - Python usually points to the exact line and position.

2. **Check syntax rules**

   - Colons, indentation, brackets, keywords.

3. **Use a code editor or IDE**

   - Syntax highlighting and linting catch errors early.

4. **Run code frequently**

   - Small changes help isolate syntax mistakes quickly.

5. **Follow PEP-8 formatting**

   - Reduces structural errors.

---

## 2. Run-Time Errors (Exceptions)

### Definition

A **run-time error** occurs **while the program is executing**, after the code has been successfully compiled.

These errors are also called **exceptions** in Python.

---

### Cause

Run-time errors occur due to **invalid operations during execution**, such as:

- Division by zero
- Accessing an index that does not exist
- Using a variable before assignment
- Opening a file that does not exist
- Invalid type operations

---

### Example

```python
x = 10
y = 0
print(x / y)
```

Error:

```
ZeroDivisionError: division by zero
```

The program starts running, then crashes at the error point.

---

### Methods to Fix Run-Time Errors

1. **Understand the exception type**

   - Python clearly names the error (e.g., `IndexError`, `TypeError`).

2. **Validate inputs**

   - Check values before performing operations.

3. **Use try-except blocks**

```python
try:
    print(x / y)
except ZeroDivisionError:
    print("Cannot divide by zero")
```

4. **Use defensive programming**

   - Assume inputs may be incorrect.

5. **Add logging and print statements**

   - Helps identify execution flow and state.

---

## 3. Logical Errors

### Definition

A **logical error** occurs when a program **runs without crashing**, but produces **incorrect output** due to flawed logic.

Python does not raise any error for logical mistakes.

---

### Cause

Logical errors are caused by **incorrect reasoning or algorithm design**, such as:

- Wrong formula
- Incorrect condition
- Using wrong operator
- Incorrect loop boundaries
- Misunderstanding problem requirements

---

### Example

```python
# Intended: check if number is even
x = 7
if x % 2 == 1:
    print("Even")
```

Output:

```
Even
```

The program runs successfully, but the result is wrong.

---

### Methods to Fix Logical Errors

1. **Manually trace the program**

   - Step through each line using sample values.

2. **Use print statements**

```python
print("x =", x)
print("x % 2 =", x % 2)
```

3. **Use a debugger**

   - Step execution line by line.

4. **Write test cases**

   - Compare expected vs actual output.

5. **Break problem into smaller parts**

   - Validate each step independently.

6. **Review algorithm and assumptions**

   - Re-check problem understanding.

---

## Comparison Summary

| Error Type   | When It Occurs   | Program Runs? | Detected By Python |
| ------------ | ---------------- | ------------- | ------------------ |
| Compile-time | Before execution | No            | Yes                |
| Run-time     | During execution | Stops midway  | Yes                |
| Logical      | After execution  | Yes           | No                 |

---

## Key Takeaway

- Compile-time errors prevent execution.
- Run-time errors crash the program during execution.
- Logical errors silently produce wrong results and are the hardest to detect.

Mastering error types is essential for **debugging, writing robust code, and interviews**.

---
