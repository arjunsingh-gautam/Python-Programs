# <span style="color:orange">**List Class in Python**</span>

## <span style="color:pink">**1. What is the `list` Class in Python?**</span>

The `list` class in Python is a built-in, mutable sequence that can hold a collection of items in a specific order.

### **Key Features:**

- **Ordered:** Elements in a list maintain their order.
- **Mutable:** You can modify lists (add, remove, or change elements).
- **Heterogeneous:** A list can store elements of different data types (e.g., integers, strings, other lists).
- **Dynamic Size:** Lists can grow or shrink as elements are added or removed.
- **Supports Iteration:** Lists can be traversed using loops or comprehensions.

---

## <span style="color:pink">**2. How to Declare and Initialize a List**</span>

### **Methods for Declaration and Initialization:**

#### **Empty List**

```python
# Two ways to declare an empty list
empty_list1 = []
empty_list2 = list()
```

#### **With Elements**

```python
# List with elements
list_with_elements = [10, 20, 30]

# Using the list constructor
list_from_iterable = list((1, 2, 3))  # From a tuple
```

#### **Dynamic Initialization Using Loops**

```python
# List comprehension
squared_numbers = [x**2 for x in range(5)]  # [0, 1, 4, 9, 16]
```

---

## <span style="color:pink">**3. Details About the `list` Class**</span>

### **Constructor Syntax:**

```python
list(iterable)
```

- **Parameter:**
  - `iterable`: Any object that can return its elements one at a time, such as strings, tuples, sets, or ranges.
- **Return Value:**
  - A new list object containing the elements of the iterable.

### **Error Handling:**

- A **TypeError** is raised if the argument passed is not iterable.
  ```python
  list(10)  # TypeError: 'int' object is not iterable
  ```

### **Attributes:**

- Lists do not have predefined attributes like size or capacity. The size adjusts dynamically as elements are added or removed.

---

## <span style="color:pink">**4. Accessing List Elements**</span>

### **Indexing**

- Positive indexing starts from `0` (left to right).
- Negative indexing starts from `-1` (right to left).

```python
my_list = [10, 20, 30, 40]
print(my_list[0])   # Output: 10
print(my_list[-1])  # Output: 40
```

### **Slicing**

- Syntax: `list[start:end:step]`
  - `start`: Starting index (inclusive).
  - `end`: Ending index (exclusive).
  - `step`: The interval between indices.

### **Rules and Default Values in Slicing (`list[start:end:step]`)**

The slicing operation in Python follows specific rules when `start`, `end`, and `step` are not provided explicitly. Here’s a breakdown:

#### **1. Default Values:**

- **`start` (beginning index):**
  - Defaults to `0` if not specified.
- **`end` (stopping index, exclusive):**
  - Defaults to `len(list)` (end of the list) if not specified.
- **`step` (increment between elements):**
  - Defaults to `1` if not specified.

#### **2. Behavior Based on `step` Sign:**

- If `step` is **positive** (`+n`):
  - **Traverses from left to right**.
  - Default `start = 0`, `end = len(list)`.
- If `step` is **negative** (`-n`):
  - **Traverses from right to left**.
  - Default `start = -1` (last element), `end = -(len(list)+1)`.

#### **3. Out-of-Bounds Handling:**

- If `start` or `end` exceed valid indices, Python **automatically adjusts within the valid range**.
- If `step == 0`, it raises a **ValueError** (`slice step cannot be zero`).

---

### **Examples:**

#### **1. Default values**

```python
lst = [10, 20, 30, 40, 50]
print(lst[:])       # [10, 20, 30, 40, 50]  (Equivalent to lst[0:len(lst):1])
print(lst[::])      # [10, 20, 30, 40, 50]  (Same as lst[:])
```

#### **2. Specified step value**

```python
print(lst[::2])     # [10, 30, 50] (Every second element)
print(lst[::-1])    # [50, 40, 30, 20, 10] (Reversed list)
```

#### **3. Out-of-bounds handling**

```python
print(lst[:100])    # [10, 20, 30, 40, 50] (Stops at len(lst))
print(lst[-100:])   # [10, 20, 30, 40, 50] (Starts from the beginning)
```

Examples:

```python
my_list = [10, 20, 30, 40, 50]
print(my_list[1:4])   # Output: [20, 30, 40]
print(my_list[::-1])  # Output: [50, 40, 30, 20, 10] (reversed)
```

---

## <span style="color:pink">**5. Memory Allocation of Lists**</span>

### **Dynamic Memory Management:**

- Lists in Python are dynamic arrays. The Python Virtual Machine (PVM) allocates memory for a list dynamically as it grows or shrinks.

### **Identity of Lists:**

- Even if two lists contain identical elements, they are stored at different memory addresses.

```python
a = [1, 2, 3]
b = [1, 2, 3]
print(id(a) == id(b))  # Output: False
```

## <span style="color:yellow">List as an Array of Pointers</span>

Yes, you can think of a **list in Python** as an array of pointers (or references) where each pointer points to a different object in memory. This is because Python lists do not directly store their elements but instead store references (memory addresses) to the actual objects.

### **List as an Array of Pointers**

- A Python list consists of a **contiguous block of memory** that contains references to objects stored elsewhere in memory.
- These references point to the memory locations of the actual elements (which may include integers, strings, lists, or any other objects).

---

### **Example and Memory Representation**

```python
my_list = [42, "hello", [1, 2], 3.14]
```

#### Memory Breakdown:

| **List Index** | **Element** | **Type** | **Memory Address (ID)** | **Stored Object Memory Address** |
| -------------- | ----------- | -------- | ----------------------- | -------------------------------- |
| 0              | `42`        | Integer  | `0x7ffabcd12345`        | `0x7ffabcd54321`                 |
| 1              | `"hello"`   | String   | `0x7ffabcd12346`        | `0x7ffabcd54322`                 |
| 2              | `[1, 2]`    | List     | `0x7ffabcd12347`        | `0x7ffabcd54323`                 |
| 3              | `3.14`      | Float    | `0x7ffabcd12348`        | `0x7ffabcd54324`                 |

- **`my_list`** is stored as an array of pointers. The list object itself has its memory address, which holds references (pointers) to the memory addresses of the individual elements.
- Each element's actual data (e.g., the integer `42` or the string `"hello"`) is stored in separate memory locations.

---

### **Memory Working Table**

Below is a simplified representation of memory for the above example:

| **Memory Address** | **Contents**                       |
| ------------------ | ---------------------------------- |
| `0x7ffabcd11111`   | Pointer to `my_list` (list object) |
| `0x7ffabcd12345`   | Pointer to integer `42`            |
| `0x7ffabcd54321`   | Actual integer value `42`          |
| `0x7ffabcd12346`   | Pointer to string `"hello"`        |
| `0x7ffabcd54322`   | Actual string data `"hello"`       |
| `0x7ffabcd12347`   | Pointer to nested list `[1, 2]`    |
| `0x7ffabcd54323`   | Actual list data `[1, 2]`          |
| `0x7ffabcd12348`   | Pointer to float `3.14`            |
| `0x7ffabcd54324`   | Actual float value `3.14`          |

---

### **How It Works Internally**

1. **The List Object (`my_list`):**

   - Stored at a specific memory location (`0x7ffabcd11111`).
   - Contains pointers (`0x7ffabcd12345`, `0x7ffabcd12346`, etc.) to the actual elements.

2. **Each Element:**
   - Each pointer in the list points to a separate memory location where the actual object is stored.
   - For example:
     - The integer `42` is stored at `0x7ffabcd54321`.
     - The string `"hello"` is stored at `0x7ffabcd54322`.

---

### **Why Lists Can Store Heterogeneous Data**

- Since Python lists store references to objects rather than the objects themselves, they can easily hold data of different types.
- The memory address for each element can point to objects of varying types and sizes, enabling heterogeneity.

#### Example:

```python
heterogeneous_list = [10, "Python", 3.14, True]

# Check IDs of elements
for i, element in enumerate(heterogeneous_list):
    print(f"Index {i}: Element = {element}, ID = {id(element)}")
```

Output:

```
Index 0: Element = 10, ID = 140715094495952
Index 1: Element = Python, ID = 140715094824464
Index 2: Element = 3.14, ID = 140715094495904
Index 3: Element = True, ID = 140715094495888
```

---

### **Why Lists Can Be Efficient**

1. **Contiguous Memory for Pointers:**
   - Python lists allocate contiguous memory for the pointers (references), making them efficient for indexing and iteration.
2. **Dynamic Growth:**
   - When a list grows, Python allocates extra space to reduce the need for frequent reallocations.

---

### **Why Identical Lists Have Different IDs**

Two identical lists (e.g., `[1, 2, 3]` and `[1, 2, 3]`) have different IDs because:

1. Each list object is a separate reference array.
2. Even if the contents are identical, the underlying memory addresses for the list objects differ.

#### Example:

```python
list1 = [1, 2, 3]
list2 = [1, 2, 3]

print(id(list1))  # Example: 140363435014912
print(id(list2))  # Example: 140363435015040
```

- **Why?**
  - Each list is a separate object with its own reference array.
  - Since lists are mutable, Python ensures they are not accidentally modified via shared references.

---

### **Conclusion**

- A Python list behaves like an **array of pointers**, where each pointer refers to the actual object stored in memory.
- This design allows lists to handle heterogeneous data, dynamic resizing, and efficient access while maintaining the integrity of mutable objects.

---

## <span style="color:pink">**6. Inserting into Lists**</span>

### **Using `append()`**

- Adds an element to the end of the list.

```python
my_list = [1, 2]
my_list.append(3)
print(my_list)  # Output: [1, 2, 3]
```

### **Using `insert()`**

- Inserts an element at a specified position.

```python
my_list = [1, 2]
my_list.insert(1, 10)  # Insert 10 at index 1
print(my_list)  # Output: [1, 10, 2]
```

---

## <span style="color:pink">**7. Packing and Unpacking**</span>

### **Packing:**

- Combine multiple variables into a list.

```python
a, b, c = 10, 20, 30
my_list = [a, b, c]  # Packing
```

### **Unpacking:**

- Assign list elements to variables.

```python
my_list = [1, 2, 3]
a, b, c = my_list
print(a, b, c)  # Output: 1 2 3
```

---

## <span style="color:pink">**8. Built-in Functions**</span>

### **Functions and Examples:**

- `min(list)`: Smallest element.
- `max(list)`: Largest element.
- `sum(list)`: Sum of elements.
- `sorted(list)`: Returns a sorted version of the list.
- `len(list)`: Number of elements.

```python
my_list = [3, 1, 4, 1, 5]
print(min(my_list))   # Output: 1
print(max(my_list))   # Output: 5
print(sum(my_list))   # Output: 14
print(sorted(my_list))  # Output: [1, 1, 3, 4, 5]
print(len(my_list))   # Output: 5
```

---

## <span style="color:pink">**9. List Methods**</span>

### **Common Methods:**

- `clear()`: Removes all elements.
- `reverse()`: Reverses the list in place.
- `sort()`: Sorts the list in place.
- `pop(index)`: Removes and returns the element at `index`.
- `index(element)`: Returns the index of the first occurrence of `element`.
- `count(element)`: Counts occurrences of `element`.
- `remove(element)`: Removes the first occurrence of `element`.

Examples:

```python
my_list = [3, 1, 4, 1, 5]
my_list.reverse()  # [5, 1, 4, 1, 3]
my_list.sort()     # [1, 1, 3, 4, 5]
print(my_list.pop(2))  # Removes element at index 2 (value 3)
my_list.remove(1)   # Removes the first 1
```

---

## <span style="color:pink">**10. List Comparisons**</span>

### **Using Relational Operators:**

- Operators like `<`, `>`, `<=`, `>=`, `==`, and `!=` compare lists element by element.

```python
a = [1, 2, 3]
b = [1, 3, 2]
print(a < b)  # True (compares 2 < 3)
print(a == b) # False
```

---

## <span style="color:pink">**11. Concatenation and Repetition**</span>

### **Concatenation:**

- Combines two or more lists.

```python
a = [1, 2]
b = [3, 4]
print(a + b)  # Output: [1, 2, 3, 4]
```

### **Repetition:**

- Repeats a list.

```python
a = [1, 2]
print(a * 3)  # Output: [1, 2, 1, 2, 1, 2]
```

---

## <span style="color:pink">**12. Nested Lists**</span>

- Lists can contain other lists.

```python
nested_list = [[1, 2], [3, 4]]
print(nested_list[1][0])  # Output: 3
```

---

## <span style="color:pink">**13. List Comprehension**</span>

- A concise way to create lists.
- Syntax: `[expression for item in iterable if condition]`

```python
squares = [x**2 for x in range(5)]
print(squares)  # Output: [0, 1, 4, 9, 16]
```

---

## <span style="color:pink">**14. Taking User Input for a List**</span>

There are several ways to take a list as input from a user in Python, depending on the use case. Below are the most common methods:

---

### **1. Input as Space-Separated Values**

- The user provides space-separated values, which are then split into a list.

#### Example:

```python
# Input: 1 2 3 4 5
user_input = input("Enter space-separated values: ")  # Input: "1 2 3 4 5"
my_list = user_input.split()  # Result: ['1', '2', '3', '4', '5']
print(my_list)
```

#### Conversion to Specific Type:

```python
# Convert to integers
my_list = list(map(int, user_input.split()))  # Result: [1, 2, 3, 4, 5]
print(my_list)
```

---

### **2. Input as Comma-Separated Values**

- The user enters values separated by commas.

#### Example:

```python
# Input: 10,20,30,40
user_input = input("Enter comma-separated values: ")  # Input: "10,20,30,40"
my_list = user_input.split(",")  # Result: ['10', '20', '30', '40']
print(my_list)
```

#### Conversion to Specific Type:

```python
# Convert to integers
my_list = list(map(int, user_input.split(",")))  # Result: [10, 20, 30, 40]
print(my_list)
```

---

### **3. Taking Input Using List Comprehension**

- Allows user to provide input for a list, one element at a time.

#### Example:

```python
# Input: 3 elements one by one
n = int(input("Enter the number of elements: "))  # Input: 3
my_list = [input(f"Enter element {i + 1}: ") for i in range(n)]
print(my_list)
```

#### Conversion to Specific Type:

```python
# For integers
my_list = [int(input(f"Enter element {i + 1}: ")) for i in range(n)]
print(my_list)
```

---

### **4. Using `eval` for Direct List Input**

- The user directly enters the list in Python list syntax.

#### Example:

```python
# Input: [1, 2, 3, 4, 5]
user_input = input("Enter a list: ")  # Input: "[1, 2, 3, 4, 5]"
my_list = eval(user_input)  # Result: [1, 2, 3, 4, 5]
print(my_list)
```

#### **Caution:**

- `eval` can execute arbitrary code, so it should only be used in trusted environments.

---

### **5. Input as Nested Lists**

- Users can input nested lists, either as a formatted string or element by element.

#### Example (Comma-Separated):

```python
# Input: 1,2,3;4,5,6;7,8,9
user_input = input("Enter rows of nested lists separated by ';': ")  # Input: "1,2,3;4,5,6;7,8,9"
nested_list = [list(map(int, row.split(","))) for row in user_input.split(";")]
print(nested_list)  # Result: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
```

---

### **6. Input Using `ast.literal_eval`**

- A safer alternative to `eval` for parsing list-like strings.

#### Example:

```python
import ast

# Input: [1, 2, 3, 4, 5]
user_input = input("Enter a list: ")  # Input: "[1, 2, 3, 4, 5]"
my_list = ast.literal_eval(user_input)  # Result: [1, 2, 3, 4, 5]
print(my_list)
```

---

### **7. Input of Mixed Types**

- For lists with elements of mixed types (e.g., integers and strings).

#### Example:

```python
# Input: 10,hello,3.14,True
user_input = input("Enter mixed type elements separated by commas: ")  # Input: "10,hello,3.14,True"
my_list = [eval(elem) for elem in user_input.split(",")]
print(my_list)  # Result: [10, 'hello', 3.14, True]
```

---

### **8. Input Using File Redirection or Reading from a File**

- Read the list from a file or a redirected input.

#### Example:

```python
# File content: 1 2 3 4 5
with open("input.txt", "r") as file:
    my_list = list(map(int, file.read().split()))
print(my_list)  # Result: [1, 2, 3, 4, 5]
```

---

### **9. Taking Multiple Lists as Input**

- Users can input multiple lists in a structured format.

#### Example:

```python
# Input: 1,2,3;4,5,6;7,8,9
user_input = input("Enter multiple lists separated by ';': ")  # Input: "1,2,3;4,5,6;7,8,9"
list_of_lists = [list(map(int, sublist.split(","))) for sublist in user_input.split(";")]
print(list_of_lists)  # Result: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
```

---

### **10. Input Using `numpy` for Arrays (Advanced)**

- Useful for numerical lists or matrix-like input.

#### Example:

```python
import numpy as np

# Input: 1 2 3 4 5
user_input = input("Enter space-separated numbers: ")  # Input: "1 2 3 4 5"
my_array = np.fromstring(user_input, dtype=int, sep=" ")
print(my_array)  # Result: array([1, 2, 3, 4, 5])
```

---

### **Summary**

The method to use depends on the specific scenario:

- **Simple list input:** Use `split()` or `map()`.
- **Structured input:** Use nested loops or `list comprehension`.
- **Mixed types:** Use `eval()` cautiously or `ast.literal_eval`.
- **Advanced needs:** Use libraries like `numpy`.

---

---

## <span style="color:#33ff00">Hash Number</span>

### **What is a Hash Number?**

A **hash number** (or hash value) is an integer value generated by a **hash function**. A hash function takes an input (such as a Python object) and returns a fixed-size numerical value, which is used to uniquely identify that object.

In Python, the built-in `hash()` function is used to compute the hash value of an object.

### **Why is the Hash Number Required?**

Hash numbers are primarily used in data structures such as **hash tables**, which are the underlying mechanism for collections like dictionaries (`dict`) and sets (`set`). Hashing provides:

1. **Efficient Lookups:** Hash numbers allow constant-time (O(1)) average complexity for lookups, insertions, and deletions in hash-based collections.
2. **Uniqueness:** Hashing ensures unique identification for objects, helping to distinguish between different elements even if they seem identical in some contexts.
3. **Organization:** Objects are stored in memory slots determined by their hash values.

---

### **What Happens If Python Does Not Have the Concept of Hash Numbers?**

1. **Inefficient Collections:** Without hashing, collections like dictionaries and sets would need to search through all elements (O(n)) for lookups, insertions, or deletions.
2. **No Quick Membership Checks:** Operations like `if key in dictionary` would require linear time complexity, making these data structures slow for large datasets.
3. **Duplication Issues:** Without unique hash numbers, objects with identical values may incorrectly appear as duplicates.
4. **Inefficient Sorting:** Hashing helps organize objects efficiently in hash tables. Without it, additional mechanisms would be required to store and organize data.

---

### **Hashable Objects vs. Unhashable Objects**

#### **Hashable Objects**

- **Definition:** Objects that have a fixed hash value during their lifetime. They can be used as keys in dictionaries and elements in sets.
- **Requirements for Hashable Objects:**
  1. **Immutable:** The object’s value cannot change after it is created.
  2. **Implements `__hash__`:** The object must have a `__hash__` method that returns a valid hash value.
  3. **Equality Consistency:** If two objects are equal (`__eq__`), they must have the same hash value.

#### **Examples of Hashable Objects:**

1. **Immutable Types:**
   - Integers (`int`): `hash(42)` → `42`
   - Strings (`str`): `hash("hello")` → A fixed integer
   - Tuples (`tuple`) (if all elements are hashable): `hash((1, 2, 3))` → A fixed integer
2. **Custom Classes:**
   - A class can be hashable if it implements `__hash__` and `__eq__`.

#### **Unhashable Objects**

- **Definition:** Objects that do not have a fixed hash value and cannot be used as keys in dictionaries or elements in sets.
- **Reasons for Being Unhashable:**
  1. **Mutability:** The object's value can change after creation, which would break hash-based collections.
  2. **No `__hash__`:** The object does not implement a `__hash__` method.

#### **Examples of Unhashable Objects:**

1. **Mutable Types:**
   - Lists (`list`): `hash([1, 2, 3])` → Raises `TypeError`
   - Dictionaries (`dict`): `hash({"a": 1})` → Raises `TypeError`
   - Sets (`set`): `hash({1, 2, 3})` → Raises `TypeError`

#### **Key Differences:**

| Feature          | Hashable Objects      | Unhashable Objects    |
| ---------------- | --------------------- | --------------------- |
| **Mutability**   | Immutable             | Mutable               |
| **Used as Keys** | Yes                   | No                    |
| **Examples**     | `int`, `str`, `tuple` | `list`, `dict`, `set` |

---

### **Properties of Hashing**

1. **Deterministic:** The hash value of an object is consistent during its lifetime.

   - Example:
     ```python
     x = "hello"
     print(hash(x))  # Same hash every time during the program
     ```

2. **Equality Consistency:** If two objects are equal (`a == b`), their hash values must also be equal (`hash(a) == hash(b)`).

   - Example:
     ```python
     x = (1, 2, 3)
     y = (1, 2, 3)
     print(hash(x) == hash(y))  # True
     ```

3. **Collisions:** Two different objects may have the same hash value, but Python handles this efficiently using hash tables.
   - Example:
     ```python
     print(hash("a"))  # May collide with another object but handled by Python
     ```

---

### **Example Table for Hashable and Unhashable Objects**

| Object Type | Example     | `hash()` Output | Hashable? | Why/Why Not?                              |
| ----------- | ----------- | --------------- | --------- | ----------------------------------------- |
| `int`       | `42`        | `42`            | Yes       | Immutable and has `__hash__`.             |
| `str`       | `"hello"`   | Unique integer  | Yes       | Immutable and has `__hash__`.             |
| `tuple`     | `(1, 2, 3)` | Unique integer  | Yes       | Immutable (if all elements are hashable). |
| `list`      | `[1, 2, 3]` | `TypeError`     | No        | Mutable; does not have `__hash__`.        |
| `dict`      | `{"a": 1}`  | `TypeError`     | No        | Mutable; does not have `__hash__`.        |
| `set`       | `{1, 2, 3}` | `TypeError`     | No        | Mutable; does not have `__hash__`.        |

---

### **Why Two Identical Lists Have Different IDs**

- Lists are **mutable**, and Python ensures that mutable objects have unique memory locations even if they contain identical values.
- Example:
  ```python
  list1 = [1, 2, 3]
  list2 = [1, 2, 3]
  print(list1 == list2)  # True (same values)
  print(id(list1), id(list2))  # Different IDs
  ```
  If `list1` or `list2` were modified, they would diverge in value, so Python assigns them separate memory addresses.

---

### **Conclusion**

Hashing is critical for efficient data storage and retrieval in Python. Hashable objects (immutable and deterministic) can be used as keys or set elements, while unhashable objects cannot due to mutability or the lack of a `__hash__` method. Python's hash-based collections rely heavily on the principles of hashing to achieve high performance.

## <span style="color:#33ff00">**Shallow vs DeepCopy**</span>

## 🔹 Shallow Copy

- **Definition:** Creates a new object, but only copies references to the nested objects inside it (not the actual objects).
- **Effect:** Changes made to **nested (mutable) objects** in the copy will also reflect in the original.
- **Independent?:** Top-level object is independent, but nested objects are **shared**.
- **Example in Python:**

  ```python
  import copy

  original = [[1, 2], [3, 4]]
  shallow = copy.copy(original)

  shallow[0][0] = 99   # change nested element
  print(original)  # [[99, 2], [3, 4]] → original also affected
  ```

---

## 🔹 Deep Copy

- **Definition:** Creates a new object **and recursively copies all nested objects**.
- **Effect:** Changes in the copy do not affect the original (completely independent).
- **Independent?:** Both top-level and nested objects are **independent**.
- **Example in Python:**

  ```python
  import copy

  original = [[1, 2], [3, 4]]
  deep = copy.deepcopy(original)

  deep[0][0] = 99
  print(original)  # [[1, 2], [3, 4]] → original NOT affected
  ```

---

## 🔑 Key Differences

| Aspect         | Shallow Copy       | Deep Copy                         |
| -------------- | ------------------ | --------------------------------- |
| Copies object? | ✅ Top-level only  | ✅ Top-level + all nested objects |
| Nested objects | Shared (reference) | Independent (new copies)          |
| Memory use     | Less               | More                              |
| Performance    | Faster             | Slower                            |
| Independence   | Partial            | Complete                          |

---

👉 Think of it like **photocopy vs redrawing**:

- **Shallow copy** = photocopy → looks the same but still points to the same inner objects.
- **Deep copy** = redraw → a completely new version, independent of the original.

---
