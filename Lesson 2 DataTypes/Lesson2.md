# <span style="color:orange">Variable & Data-Types </span>

## <span style="color:pink">Comments </span>

- Used to make code more understandable
- This statements are ignored by compiler while compiling

1. **Single Line Comment**

```python
# single line comment
```

2. **Multi-Line Comment**

```python
"""statement-1
   statement -2"""

```

## <span style="color:pink">Tokens in Python </span>

- In Python, **tokens** are the smallest elements of a program that are meaningful to the compiler or interpreter. They represent the building blocks of the code. Python tokens can be broadly categorized into the following types:

---

## **1. Keywords**

- Reserved words that have a special meaning in Python and cannot be used as variable names.
- Examples: `if`, `else`, `while`, `for`, `def`, `class`, `return`, `break`.

### Example:

```python
if True:
    print("This is a keyword example.")
```

---

## **2. Identifiers**

- Names used to identify variables, functions, classes, or objects.
- Rules for identifiers:
  - Must start with a letter (A-Z, a-z) or an underscore (`_`).
  - Followed by letters, digits (0-9), or underscores.
  - Cannot use Python keywords.
  - Case-sensitive (`name` and `Name` are different).

### Example:

```python
variable_name = 10  # Valid identifier
_name = "Python"    # Valid identifier
# 123var = 5        # Invalid identifier (cannot start with a digit)
```

---

## **3. Literals**

- Represent fixed values in Python. These are classified into:
  1. **String Literals**: `'hello'`, `"world"`, `'''multiline'''`.
  2. **Numeric Literals**: Integers, floating-point numbers, complex numbers (`10`, `3.14`, `2+3j`).
  3. **Boolean Literals**: `True`, `False`.
  4. **Special Literal**: `None`.

### Example:

```python
name = "Alice"  # String literal
age = 25        # Integer literal
pi = 3.14       # Floating-point literal
is_valid = True # Boolean literal
nothing = None  # Special literal
```

---

## **4. Operators**

- Symbols that perform operations on variables and values.
- Types:
  - **Arithmetic**: `+`, `-`, `*`, `/`, `//`, `%`, `**`.
  - **Relational**: `==`, `!=`, `<`, `>`, `<=`, `>=`.
  - **Logical**: `and`, `or`, `not`.
  - **Assignment**: `=`, `+=`, `-=`, etc.
  - **Bitwise**: `&`, `|`, `^`, `~`, `<<`, `>>`.

### Example:

```python
a = 10 + 20  # Arithmetic
b = (a > 15) and (a < 50)  # Logical and relational
```

---

## **5. Delimiters**

- Special symbols that serve as separators in the code.
- Examples: `()`, `{}`, `[]`, `:`, `,`, `.`, `;`, `@`, `=`, `->`.

### Example:

```python
def func(a, b):  # Delimiters: (), :
    return a + b
```

---

## **6. Comments**

- Statements that are ignored by the Python interpreter.
- Single-line comments: Start with `#`.
- Multi-line comments: Enclosed in `'''` or `"""`.

### Example:

```python
# This is a single-line comment
"""
This is a
multi-line comment
"""
```

---

## **7. Punctuators**

- Used to define the structure of a program.
- Includes `:`, `,`, `;`, `@`, etc.

### Example:

```python
class MyClass:
    pass
```

---

## **8. Indentation**

- Not a traditional token but essential for Python syntax.
- Python uses indentation to define code blocks.

### Example:

```python
if True:
    print("Indented code block")
```

---

### **Full Example:**

Here’s how different tokens work together in a program:

```python
# Keyword, Identifier, Literal, Operator, Delimiter
def add_numbers(a, b):  # Keywords: def; Identifiers: add_numbers, a, b; Delimiter: (, ):
    return a + b        # Keyword: return; Operator: +; Delimiter: :

result = add_numbers(5, 10)  # Identifier: result; Delimiter: (, )
print("Sum is:", result)     # Keyword: print; Delimiter: (, )
```

---

### **Summary**

| **Token Type** | **Example**           |
| -------------- | --------------------- |
| Keywords       | `if`, `else`, `def`   |
| Identifiers    | `x`, `add_numbers`    |
| Literals       | `42`, `3.14`, `"Hi"`  |
| Operators      | `+`, `-`, `and`       |
| Delimiters     | `()`, `{}`, `:`       |
| Comments       | `# This is a comment` |

Let me know if you'd like more details on any specific token type!

## <span style="color: pink;">Identifiers in Python</span>

### Definition

Identifiers are names given to entities in Python such as variables, functions, classes, modules, etc. They help in uniquely identifying these entities during program execution.

### Rules for Writing Identifiers

1. **Character Set**:

   - Can include letters (both uppercase and lowercase), digits, and underscores (`_`).
   - Cannot start with a digit. For example, `var_1` is valid, but `1_var` is not.

2. **Case Sensitivity**:

   - Python identifiers are case-sensitive. For example, `myVar`, `myvar`, and `MYVAR` are considered different.

3. **Reserved Words**:

   - Python keywords like `if`, `else`, `while`, `for`, etc., cannot be used as identifiers.

4. **Length**:

   - No limit on identifier length, but it's recommended to keep them reasonably short for readability.

5. **Best Practices**:
   - Use descriptive names that convey the purpose of the entity.
   - Avoid using special characters other than underscores (`_`) unless necessary.

### Examples

- Valid Identifiers:
  - `var_name`
  - `_my_var`
  - `myVar`
  - `PI`
- Invalid Identifiers:
  - `1var` (starts with a digit)
  - `my-var` (contains a hyphen)
  - `for` (reserved keyword)

### Use Cases

- **Variables**: `count`, `total_amount`
- **Functions**: `calculate_area()`, `print_details()`
- **Classes**: `Car`, `Student`
- **Modules**: `math`, `random`

### Importance

- **Readability**: Clear and meaningful identifiers enhance code readability.
- **Clarity**: Helps in understanding the purpose of variables, functions, etc., at a glance.
- **Debugging**: Well-chosen identifiers make debugging easier by indicating where issues might arise.

### Conclusion

Identifiers in Python are essential for naming various programming elements and play a crucial role in making code understandable and maintainable.

## <span style="color:pink">Data </span>

Data is any piece of information which is used by the program to accomplish a task

## <span style="color:pink">Variables </span>

- Variables are <u>**used to hold data**</u> during execution of the program
- Variables are **containers** that store data
- In Pyton we declare variables **dynamically**
  - automatic declaration
  - memory allocation
  - data type of varible are dynamically alloted according to the data store

### <span style="color:yellow">Variable Naming Rules: </span>

1. Valid Characters:

- Variable names can consist of letters (a-z, A-Z), numbers (0-9), and underscores (\_).
- The first character of a variable name cannot be a number.

2. Case Sensitivity:

- Python is _case-sensitive_. This means that **my_variable** and **My_Variable** are considered different variables.

3. Reserved Words:

- Avoid using Python keywords and reserved words as variable names. For example, you cannot use words like if, else, for, etc., as variable names.

4. Conventions:

- Follow the Python naming conventions to write clean and readable code.
- Use descriptive names that convey the purpose of the variable.
- Use lowercase letters for variable names, separated by underscores for readability (snake_case).

5. Length:

- Keep variable names reasonably short while maintaining clarity. Long and descriptive names are encouraged, but excessively long names can make the code less readable.

Examples of valid variable names:

```python

my_variable = 42
user_name = "JohnDoe"
total_amount = 100.5
```

Examples of invalid variable names:

```python

2nd_variable = 42  # Variable name cannot start with a number
total-amount = 100  # Hyphens are not allowed in variable names
if = 5  # 'if' is a reserved keyword
```

### <span style="color:yellow">type() function: </span>

- predefined function to check data type of a variable
  > Basically tells the data type of object jiske address ko varibale refer kar raha hai

### <span style="color:yellow">id() function: </span>

- predefined to check id(address) of object of a variable
  ✅ **In CPython, `id()` returns the virtual memory address where the object is stored.**  
  ❌ **It is not always the actual physical memory address (depends on Python implementation).**

## <span style="color:pink">Data Types (class in Python) </span>

- **Numbers**
  - int ---> 5
  - float ---> 3.73
  - complex ----> 3 + 4j
- **Boolean**
  - bool ---> True, False
- **String** - str ---> "MySirG" > use double qoutes " " for string
  > double and char are not there in python

### <span style="color:yellow">print() function: </span>

- print defined function used for printing

# <span style="color:orange">Python Data Types</span>

## 1. Numeric Types

### Integer (`int`)

- **Description:** Whole numbers, positive or negative, without decimals.
- **Example:**
  ```python
  x = 10
  y = -5
  ```

### Float (`float`)

- **Description:** Numbers, positive or negative, containing one or more decimals.
- **Example:**
  ```python
  a = 10.5
  b = -3.14
  ```

### Complex (`complex`)

- **Description:** Numbers expressed in the form of `a + bj`, where `a` and `b` are floats and `j` represents the imaginary unit.
- **Example:**
  ```python
  z = 3 + 4j
  ```

## **How Python Interpreter Stores `int`, `float`, and `complex` Numbers?**

Python dynamically manages memory for numeric data types using **heap memory** and **reference counting**. Let’s break it down:

---

## **1️⃣ Integer (`int`) Storage**

📌 **Python uses a variable-length representation for integers (`PyLongObject`).**

### 🔹 **Key Features of `int` Storage**

✅ Small integers (`-5 to 256`) are **interned (cached)** for efficiency.  
✅ Large integers are stored as **arrays of digits (base-230 representation)** for arbitrary precision.  
✅ Python does **not** have fixed-size integers (unlike C’s `int`, `long`).

### 🛠 **Example of `int` Interning**

```python
a = 256
b = 256
print(id(a) == id(b))  # True (Same object due to interning)

x = 257
y = 257
print(id(x) == id(y))  # May be False (Separate objects)
```

### 🔹 **Memory Layout (`PyLongObject` in CPython)**

- Python stores integers as an array of "digits" in **base 2³⁰ (or 2³¹ in 64-bit systems)**.
- The structure in **C (CPython)**:
  ```c
  struct _longobject {
      PyObject_VAR_HEAD
      digit ob_digit[1];  // Array of digits (variable length)
  };
  ```
- **Small integers (-5 to 256) are preallocated** and stored in a global array for reuse.

---

## **2️⃣ Float (`float`) Storage**

📌 **Python stores floats as 64-bit IEEE-754 double-precision numbers.**

### 🔹 **Key Features of `float` Storage**

✅ Always **occupies 8 bytes (64-bit)** in memory.  
✅ Supports a **sign bit, exponent, and fraction (mantissa)** representation.  
✅ **Not arbitrary precision** like `int`, meaning some precision loss may occur.

### 🛠 **Example of Float Precision Issue**

```python
print(0.1 + 0.2)  # Output: 0.30000000000000004 (Floating-point error)
```

### 🔹 **Memory Layout (`PyFloatObject` in CPython)**

- Python internally uses a simple **C struct (`PyFloatObject`)**:
  ```c
  struct _floatobject {
      PyObject_HEAD
      double ob_fval;  // IEEE 754 64-bit float
  };
  ```
- **All floats occupy 8 bytes in memory, regardless of the number's magnitude.**

---

## **3️⃣ Complex (`complex`) Storage**

📌 **Python stores complex numbers as two `float` values (real & imaginary parts).**

### 🔹 **Key Features of `complex` Storage**

✅ Uses two **64-bit `float` numbers** internally.  
✅ Supports complex arithmetic directly.  
✅ Not interned like `int`, meaning each complex number is a new object.

### 🛠 **Example of Complex Number Storage**

```python
z = 3 + 4j
print(z.real, z.imag)  # Output: 3.0 4.0
```

### 🔹 **Memory Layout (`PyComplexObject` in CPython)**

- Python stores complex numbers using a struct with two `double` values:
  ```c
  struct _complexobject {
      PyObject_HEAD
      double cval_real;  // Real part (64-bit float)
      double cval_imag;  // Imaginary part (64-bit float)
  };
  ```
- Each complex number requires **16 bytes** (8 bytes for real + 8 bytes for imaginary).

---

## **🔄 Memory Management for Numbers**

### 🔹 **Reference Counting (Garbage Collection)**

- Python **stores numbers on the heap**, and memory is managed using **reference counting**.
- When a variable is **no longer referenced**, Python frees its memory.

### 🛠 **Example of Reference Counting**

```python
import sys

x = 1000
print(sys.getrefcount(x))  # Number of references to x
```

---

## **🚀 Summary Table**

| Type      | Representation                   | Memory (CPython)                 | Precision                        |
| --------- | -------------------------------- | -------------------------------- | -------------------------------- |
| `int`     | Arbitrary precision (Base-230)   | Varies (Small `int`s are cached) | Infinite (until memory runs out) |
| `float`   | IEEE 754 (64-bit `double`)       | 8 bytes                          | Fixed (15-17 decimal places)     |
| `complex` | Two `float` values (real + imag) | 16 bytes                         | Same as `float`                  |

### **📝 Key Takeaways**

✅ **Integers (`int`) are stored dynamically using arbitrary precision** but small ones are **cached**.  
✅ **Floats (`float`) are stored as 64-bit IEEE-754 doubles**, leading to precision errors.  
✅ **Complex numbers (`complex`) use two 64-bit `float` values** internally.  
✅ Python **automatically manages memory** using reference counting and garbage collection.

---

---

## 2. Sequence Types

### String (`str`)

- **Description:** Ordered sequences of characters enclosed in single, double, or triple quotes.
- **Example:**
  ```python
  text = "Hello, World!"
  ```

### List (`list`)

- **Description:** Ordered, mutable collections of items, enclosed in square brackets.
- **Example:**
  ```python
  fruits = ["apple", "banana", "cherry"]
  ```

### Tuple (`tuple`)

- **Description:** Ordered, immutable collections of items, enclosed in parentheses.
- **Example:**
  ```python
  dimensions = (1920, 1080)
  ```

## 3. Mapping Type

### Dictionary (`dict`)

- **Description:** Unordered collections of key-value pairs, enclosed in curly braces.
- **Example:**
  ```python
  person = {"name": "John", "age": 30, "city": "New York"}
  ```

## 4. Set Types

### Set (`set`)

- **Description:** Unordered collections of unique items, enclosed in curly braces.
- **Example:**
  ```python
  unique_numbers = {1, 2, 3, 4, 5}
  ```

### Frozenset (`frozenset`)

- **Description:** Immutable version of a set.
- **Example:**
  ```python
  frozen_numbers = frozenset([1, 2, 3, 4, 5])
  ```

## 5. Boolean Type

### Boolean (`bool`)

- **Description:** Represents `True` or `False`.
- **Example:**
  ```python
  is_active = True
  is_deleted = False
  ```

## 6. None Type

### NoneType (`None`)

- **Description:** Represents the absence of a value.
- **Example:**
  ```python
  result = None
  ```

## 7. Binary Types

### Bytes (`bytes`)

- **Description:** Immutable sequences of bytes.
- **Example:**
  ```python
  byte_data = b'hello'
  ```

#### **🔹 Correct Ways to Create Different `bytes` Values**

| Code                  | Output                    | Explanation                  |
| --------------------- | ------------------------- | ---------------------------- |
| `bytes(5)`            | `b'\x00\x00\x00\x00\x00'` | 5 zero bytes                 |
| `bytes([100])`        | `b'd'`                    | Byte value 100 (ASCII `'d'`) |
| `bytes([65, 66, 67])` | `b'ABC'`                  | ASCII for 'A', 'B', 'C'      |
| `b'd'`                | `b'd'`                    | Directly writing bytes       |
| `b'd'*5`              | `b'ddddd'`                | Repeats `'d'` 5 times        |

### Bytearray (`bytearray`)

- **Description:** Mutable sequences of bytes.
- **Example:**
  ```python
  mutable_byte_data = bytearray(b'hello')
  ```

### Memoryview (`memoryview`)

- **Description:** Allows for a view on a byte array.
- **Example:**

  ```python
  byte_view = memoryview(b'hello')
  ```

  ## **🔹 What is `memoryview` in Python?**

  The `memoryview` object in Python provides a **memory-efficient way to manipulate large binary data** without making copies.

✔ **It allows direct access to the memory of objects like `bytes`, `bytearray`, or `array.array`**  
✔ **It avoids unnecessary memory allocation**, making it efficient for handling large datasets.

---

## **🔹 How `memoryview` Works**

A `memoryview` does **not** create a new copy of the data. Instead, it provides a **view** (reference) to the memory buffer of an object, allowing you to manipulate the underlying data directly.

🔹 **Key Benefits of `memoryview`:**  
✅ **Avoids copying data → More efficient**  
✅ **Allows slicing and modifying `bytearray` efficiently**  
✅ **Useful for working with large binary data (files, network packets, images, etc.)**

---

## **🛠 Example 1: Creating a `memoryview`**

```python
data = bytearray([65, 66, 67, 68, 69])  # bytearray of ASCII (A, B, C, D, E)
mv = memoryview(data)

print(mv[0])  # Output: 65 (ASCII of 'A')
print(bytes(mv[:3]))  # Output: b'ABC' (First 3 bytes)
```

- `memoryview(data)` creates a **view** of `data` instead of making a copy.
- `mv[0]` accesses the first byte (65, which is `'A'` in ASCII).
- `bytes(mv[:3])` converts the first 3 bytes back into a `bytes` object.

---

## **🛠 Example 2: Modifying a `bytearray` Using `memoryview`**

```python
data = bytearray(b'ABCDE')  # Mutable bytearray
mv = memoryview(data)

mv[0] = 97  # Changing 'A' (65) to 'a' (97)
print(data)  # Output: bytearray(b'aBCDE')
```

- Since `bytearray` is mutable, `memoryview` allows direct modification.

---

## **🛠 Example 3: Using `memoryview` for Slicing**

```python
data = bytearray(range(10))  # bytearray from 0 to 9
mv = memoryview(data)

slice_mv = mv[3:7]  # View of elements 3 to 6
print(list(slice_mv))  # Output: [3, 4, 5, 6]
```

- `mv[3:7]` creates a **view** of a portion of the data without copying.

---

## **🚀 When to Use `memoryview`?**

✅ **Efficiently process large binary files (images, audio, video, network packets, etc.)**  
✅ **Modify data in-place (without extra copies)**  
✅ **Optimize memory usage for large datasets**

---

## **📌 Summary**

| Feature               | `memoryview`                                   |
| --------------------- | ---------------------------------------------- |
| **Copies data?**      | ❌ No (just a reference)                       |
| **Saves memory?**     | ✅ Yes                                         |
| **Supports slicing?** | ✅ Yes                                         |
| **Modifiable?**       | ✅ If source is mutable (e.g., `bytearray`)    |
| **Use case**          | Large binary data, memory-efficient operations |

---

---

## Summary

Python provides various data types to handle different kinds of data. Understanding these data types and their properties is crucial for efficient programming.

In Python, variables and memory management revolve around dynamic typing, reference counting, and the use of namespaces and private heap space. Let’s break this down step-by-step.

---

## **1. Variables and Memory Management in Python**

![Dynamic Typing](img/DT.png)

### **Dynamic Typing**

- In Python, variables do not have a fixed type. Instead, they are references (or labels) to objects in memory.
  - Example:
    ```python
    x = 42       # x points to an integer object 42
    x = "hello"  # x now points to a string object "hello"
    ```

### **Object Model**

- Every value in Python is an **object**. Each object has:
  - **Type**: Defines what kind of data it holds (e.g., `int`, `str`, `list`).
  - **Value**: The actual data stored.
  - **Reference Count**: Tracks how many variables are pointing to this object.
  - **Memory Address**: The location in memory where the object is stored.

### **Reference Counting**

- Python uses reference counting to manage memory:
  - Each object keeps track of how many references point to it.
  - When the reference count drops to 0, the object is deallocated.
  - Example:
    ```python
    a = [1, 2, 3]  # List object created, reference count = 1
    b = a          # Reference count = 2
    del a          # Reference count = 1
    del b          # Reference count = 0 (object is garbage collected)
    ```

### **Garbage Collection**

- Python has an automatic garbage collector that handles objects with circular references.
  - Example of circular reference:
    ```python
    a = []
    b = [a]
    a.append(b)
    del a, b  # Circular reference, resolved by garbage collector
    ```

---

## **2. Namespace and Private Heap Space**

### **Namespace**

- A **namespace** is a container that maps variable names to objects.

  - **Types of Namespaces**:

    1. **Local Namespace**: Created inside a function or method, holds local variables.
    2. **Global Namespace**: At the module level, contains global variables.
    3. **Built-in Namespace**: Includes Python's built-in functions and exceptions (e.g., `len`, `print`).

  - Example:

    ```python
    x = 10  # Global namespace

    def foo():
        y = 20  # Local namespace
        print(x, y)

    foo()
    print(x)  # Accessible
    # print(y)  # Error: y is not defined
    ```

- Namespaces are implemented as dictionaries.

---

### **Functions Used to Check Namespace in Python** 🚀

In the provided code, we used multiple functions to inspect the **global, local, and built-in namespaces**. Let's break them down one by one:

---

## **1️⃣ `dir()` - List All Names in a Namespace**

- **Purpose:** Lists all the names (variables, functions, modules, etc.) in the current namespace.
- **Usage in Code:**
  ```python
  print("All Names in Global Namespace:", dir())
  ```
- **Example Output:**
  ```
  ['__annotations__', '__builtins__', '__doc__', ..., 'my_function', 'x', 'y']
  ```
- **Explanation:**
  - It includes **both built-in and user-defined names**.
  - Special names starting with `__` (like `__doc__`, `__name__`) are part of Python's internal system.

---

## **2️⃣ `dir(__builtins__)` - List All Built-in Functions & Variables**

- **Purpose:** Lists all built-in functions, classes, and exceptions in Python.
- **Usage in Code:**
  ```python
  print("Built-in Functions and Variables:", dir(__builtins__))
  ```
- **Example Output:**
  ```
  ['ArithmeticError', 'AssertionError', ..., 'print', 'range', 'zip']
  ```
- **Explanation:**
  - This shows all **default functions and exceptions** provided by Python.
  - Example functions: `print()`, `len()`, `range()`, `zip()`
  - Example exceptions: `ValueError`, `TypeError`, `IndexError`

---

## **3️⃣ `globals()` - Get All Global Variables and Their Values**

- **Purpose:** Returns a **dictionary** of all global variables and their values.
- **Usage in Code:**
  ```python
  print("Global Namespace Variables:", globals())
  ```
- **Example Output:**
  ```python
  {'__name__': '__main__', 'x': 42, 'y': 'hello', 'my_function': <function my_function at 0x...>}
  ```
- **Explanation:**
  - Keys are **variable names**, values are **their current values**.
  - It includes:
    - `x: 42` (user-defined variable)
    - `y: 'hello'` (user-defined variable)
    - `my_function`: function reference
    - Python internal variables like `__name__`

---

## **4️⃣ `locals()` - Get All Local Variables in a Function**

- **Purpose:** Returns a **dictionary** of all local variables inside a function.
- **Usage in Code:**
  ```python
  def my_function():
      a = 10
      b = 20
      print("Local Namespace inside function:", locals())
  ```
- **Example Output (when function is called):**
  ```
  Local Namespace inside function: {'a': 10, 'b': 20}
  ```
- **Explanation:**
  - Lists **only** the variables defined inside the function.
  - Here, it returns `{ 'a': 10, 'b': 20 }`.

---

## **5️⃣ Filtering User-Defined Names (Excluding Built-ins)**

- **Purpose:** Get only **user-defined** variables and functions.
- **Usage in Code:**
  ```python
  user_defined = [name for name in dir() if not name.startswith("__")]
  print("User-Defined Names:", user_defined)
  ```
- **Example Output:**
  ```
  User-Defined Names: ['my_function', 'x', 'y']
  ```
- **Explanation:**
  - `dir()` returns all names (built-in and user-defined).
  - We filter out names that start with `"__"` (Python’s internal names).
  - This leaves **only the variables and functions defined by the user**.

---

### **Final Thoughts 💡**

| **Function**        | **Purpose**                                                   | **Returns**                                    |
| ------------------- | ------------------------------------------------------------- | ---------------------------------------------- |
| `dir()`             | Lists all names in the namespace                              | `['x', 'y', 'my_function', '__name__', ...]`   |
| `dir(__builtins__)` | Lists all built-in functions & exceptions                     | `['print', 'int', 'range', 'ValueError', ...]` |
| `globals()`         | Returns a dictionary of all global variables                  | `{ 'x': 42, 'y': 'hello', ...}`                |
| `locals()`          | Returns a dictionary of all local variables inside a function | `{ 'a': 10, 'b': 20 }`                         |

---

### **🚀 Summary**

- `dir()` → Lists all names in the current scope.
- `dir(__builtins__)` → Lists all built-in Python functions.
- `globals()` → Shows all global variables and their values.
- `locals()` → Shows local variables inside a function.
- Filtering with `[name for name in dir() if not name.startswith("__")]` helps remove built-ins.

---

---

### **Private Heap Space**

- Python objects and data structures are stored in a **private heap space**:
  - Managed by Python's memory manager.
  - Developers cannot access it directly.
  - All objects (variables, functions, classes) are stored in this space.
  - Python provides access to this memory through variables and references.

---

## **3. Working Mechanics with Example**

### **Step-by-Step Example**

```python
x = 42           # Step 1: Create an integer object and store in memory
y = x            # Step 2: `y` references the same object as `x`
z = [1, 2, 3]    # Step 3: Create a list object and store in memory
z.append(4)      # Step 4: Modify the list in-place (mutable object)
```

- **Step 1: Integer Object**:

  - Python creates an integer object `42` in memory.
  - `x` is a reference to this object.

- **Step 2: Shared Reference**:

  - `y = x` makes `y` point to the same object as `x`.
  - Reference count of the integer object increases to 2.

- **Step 3: List Object**:

  - A new list `[1, 2, 3]` is created in the heap.
  - `z` references this list.

- **Step 4: Modification**:
  - Lists are mutable, so `z.append(4)` modifies the same list object.

---

## **4. Scoping Rules**

- Python determines where a variable is accessible using **LEGB rule**:
  - **L**ocal: Defined inside a function.
  - **E**nclosing: Defined in the enclosing function for nested functions.
  - **G**lobal: Defined at the module level.
  - **B**uilt-in: Predefined in Python.

### **Example**

```python
x = "global"

def outer():
    x = "enclosing"

    def inner():
        x = "local"
        print(x)  # local

    inner()
    print(x)  # enclosing

outer()
print(x)  # global
```

---

## **5. Private Variables**

- Python does not have "true" private variables but uses name mangling:

  - Variables prefixed with `__` are considered private.
  - Example:

    ```python
    class MyClass:
        def __init__(self):
            self.__private = "hidden"

        def reveal(self):
            return self.__private

    obj = MyClass()
    print(obj.reveal())  # Accesses private variable
    # print(obj.__private)  # Error: AttributeError
    ```

---

## **Summary of Key Concepts**

| **Feature**            | **Description**                                                       |
| ---------------------- | --------------------------------------------------------------------- |
| **Dynamic Typing**     | Variables are references to objects; types are checked at runtime.    |
| **Namespaces**         | Containers for variables; implemented as dictionaries.                |
| **Private Heap Space** | Stores all objects and is managed internally by Python.               |
| **Reference Counting** | Tracks how many references point to an object.                        |
| **Garbage Collection** | Cleans up objects with 0 references and resolves circular references. |
| **LEGB Rule**          | Determines the scope of variables.                                    |

Would you like further details on any specific aspect?

---

# <span style="color:yellow"> LEGB Rule</span>

The **LEGB rule** in Python determines the order in which the interpreter searches for a variable's value. It stands for:

1. **Local**: The innermost scope, inside the current function or method.
2. **Enclosing**: The scope of any enclosing functions (in case of nested functions).
3. **Global**: The module-level scope, for variables defined at the top of the script or file.
4. **Built-in**: The outermost scope, containing Python’s built-in functions and constants (e.g., `len`, `print`).

The search follows this order, and the interpreter stops as soon as it finds the variable.

---

## **Detailed Explanation with Simple Examples**

### **1. Local Scope**

- Variables defined inside a function belong to the local scope.
- They are not accessible outside the function.

```python
def my_function():
    x = 10  # Local variable
    print(x)

my_function()  # Output: 10
# print(x)  # Error: x is not defined outside the function
```

---

### **2. Enclosing Scope**

- Variables defined in enclosing functions (for nested functions) belong to the enclosing scope.
- These are accessible within the nested function but not at the global level.

```python
def outer_function():
    y = "enclosing"  # Enclosing scope variable

    def inner_function():
        print(y)  # Accesses enclosing scope variable

    inner_function()

outer_function()  # Output: enclosing
```

---

### **3. Global Scope**

- Variables defined at the top level of a module or script belong to the global scope.
- These can be accessed from any function, provided they are not shadowed by local variables.

```python
z = "global"  # Global variable

def display():
    print(z)  # Accesses global variable

display()  # Output: global
```

---

### **4. Built-in Scope**

- The outermost scope contains Python’s built-in functions, constants, and exceptions (e.g., `len`, `print`).
- These are available everywhere unless overridden by variables in inner scopes.

```python
# Using a built-in function
print(len([1, 2, 3]))  # Output: 3
```

If you override a built-in name:

```python
def len(x):  # Overriding the built-in len function
    return "Overridden!"

print(len([1, 2, 3]))  # Output: Overridden!
```

---

### **Combined Example**

Let’s see how the LEGB rule works with overlapping variable names.

```python
x = "global"  # Global scope

def outer():
    x = "enclosing"  # Enclosing scope

    def inner():
        x = "local"  # Local scope
        print(x)  # Searches local first

    inner()
    print(x)  # Searches enclosing after local

outer()
print(x)  # Searches global after local and enclosing
```

**Output**:

```
local
enclosing
global
```

---

### **Key Points**

1. **Local scope takes precedence**: The interpreter first looks inside the function for a variable.
2. **Global is accessed only if local and enclosing do not define the variable**.
3. **Built-in scope is the last resort**: Used if no other scopes define the variable.

---

### **Example with an Undefined Variable**

If the variable is not found in any scope, Python raises a `NameError`.

```python
def foo():
    print(a)  # 'a' is not defined in any scope

foo()  # Error: NameError: name 'a' is not defined
```

---

# <span style="color:orange">Everything is an Object</span>

- In Python, **everything is an object** means that every entity, whether it's a variable, function, class, or even data types like integers, strings, lists, etc., is represented as an instance of some class and has associated methods and attributes.

- Python follows the **object-oriented programming** paradigm, and all entities in Python inherit from the base `object` class, either directly or indirectly.

---

## **Key Concept: Everything is an Object**

- Every value in Python is an object.
- Objects have attributes (data) and methods (functions that operate on the data).
- Types like integers (`int`), strings (`str`), functions (`function`), classes (`type`), and even modules are objects.

---

## **Examples of Objects**

### **1. Data Types as Objects**

All data types like `int`, `float`, `str`, `list`, etc., are instances of built-in classes.

```python
# Integer is an object
a = 10
print(type(a))  # Output: <class 'int'>

# String is an object
s = "Hello"
print(type(s))  # Output: <class 'str'>
```

Each object has methods and attributes:

```python
# Using a method of the string object
print(s.upper())  # Output: HELLO
```

---

### **2. Functions as Objects**

Functions are first-class objects in Python, meaning:

- They can be assigned to variables.
- They can be passed as arguments.
- They can be returned from other functions.

```python
# Defining a function
def greet(name):
    return f"Hello, {name}!"

# Function as an object
print(type(greet))  # Output: <class 'function'>

# Assigning function to a variable
say_hello = greet
print(say_hello("Alice"))  # Output: Hello, Alice!
```

---

### **3. Classes and Instances as Objects**

- A **class** is an object of the `type` class.
- An **instance** is an object created from a class.

```python
# Defining a class
class Person:
    def __init__(self, name):
        self.name = name

# Class is an object
print(type(Person))  # Output: <class 'type'>

# Creating an instance of the class
p = Person("John")
print(type(p))  # Output: <class '__main__.Person'>
```

---

### **4. Modules as Objects**

Modules are also objects in Python. You can import a module and use its attributes.

```python
import math

# Module is an object
print(type(math))  # Output: <class 'module'>

# Accessing module attributes
print(math.sqrt(16))  # Output: 4.0
```

---

### **5. Built-in Objects**

Even Python's built-in functions and exceptions are objects.

```python
# Built-in function
print(type(len))  # Output: <class 'builtin_function_or_method'>

# Exception as an object
print(type(ValueError))  # Output: <class 'type'>
```

---

## **Common Object Types**

| **Object Type**      | **Description**                                   | **Example**                   |
| -------------------- | ------------------------------------------------- | ----------------------------- |
| **Instance**         | An object created from a class                    | `p = Person("John")`          |
| **Function**         | A callable object created using `def` or `lambda` | `def greet(): pass`           |
| **Class**            | A blueprint for creating objects                  | `class Person: pass`          |
| **Module**           | A file containing Python code                     | `import math`                 |
| **Type**             | The class of an object                            | `type(10)` -> `<class 'int'>` |
| **Iterator**         | An object with `__iter__` and `__next__` methods  | `iter([1, 2, 3])`             |
| **Generator**        | An object returned by a generator function        | `yield x`                     |
| **Built-in objects** | Python’s predefined objects                       | `len`, `print`, `ValueError`  |

---

## **Deep Dive: Objects in Memory**

1. **Object Identity**: Each object has a unique identity in memory, which can be checked using `id()`.

   ```python
   x = 42
   y = 42
   print(id(x) == id(y))  # Output: True (same memory location for small integers)
   ```

2. **Object Type**: The type of an object determines the operations it supports.

   ```python
   print(type([1, 2, 3]))  # Output: <class 'list'>
   ```

3. **Object Attributes and Methods**: Use `dir()` to view an object’s attributes and methods.
   ```python
   print(dir(str))  # Output: List of methods for string objects
   ```

---

## **Summary**

- Everything in Python (variables, data types, functions, classes, modules) is an object.
- Objects have types, methods, and attributes.
- Python’s object model allows for flexibility, making the language highly object-oriented.

Would you like an advanced example or further clarification on a specific object type?
