# <span style="color:orange"> **Iterative Statements in Python**</span>

## <span style="color:pink"> **1. While Loop**</span>

The `while` loop repeats a block of code as long as its condition evaluates to `True`.

**Syntax:**

```python
while condition:
    # Code block
    # termination condition(usually to update the conditional checking variable to avoid infinite looping)
```

**Working:**

1. The condition is evaluated.
2. If `True`, the code block executes.
3. After execution, the condition is rechecked.
4. The loop stops when the condition evaluates to `False`.

**Example:**

```python
count = 0
while count < 5:
    print(count)
    count += 1
```

**Special Points:**

- Ideal for scenarios where the number of iterations is not predetermined.
- Ensure the loop has a mechanism to break or change the condition; otherwise, it may lead to an infinite loop.

**Precautions:**

- Always modify the variables involved in the condition within the loop to prevent infinite loops.

---

## <span style="color:pink"> **2. For Loop** </span>

The `for` loop iterates over a sequence (e.g., list, string, range) or an iterator.

**Syntax:**

```python
for variable in sequence:
    # Code block
```

**Working:**

1. The loop picks an element from the sequence one at a time.
2. Assigns it to the loop variable.
3. Executes the code block for each element.
4. Stops when all elements are exhausted.

**Example:**

```python
for num in range(5):
    print(num)
```

**Special Points:**

- Best for iterating over collections or sequences with a known size.
- Can iterate over custom iterators.

**Precautions:**

- Avoid modifying the sequence being iterated directly during the loop.

---

### <span style="color:yellow"> **Differences Between `while` and `for` Loops**</span>

| Feature            | `while` Loop                            | `for` Loop                                                   |
| ------------------ | --------------------------------------- | ------------------------------------------------------------ |
| Condition          | Runs until a condition is `False`.      | Iterates over elements in a sequence.                        |
| Use Case           | When iterations depend on a condition.  | When the number of iterations is known or over a collection. |
| Infinite Loop Risk | Higher if the condition is not updated. | Lower unless explicitly coded.                               |
| Syntax Complexity  | Simpler but requires careful condition. | Easier for sequences or ranges.                              |

---

## <span style="color:pink"> **Soft Keywords: `break`, `continue`, `pass`**</span>

### <span style="color:yellow">**1. `break`**</span>

Stops the loop immediately, skipping the remaining iterations.

**Syntax:**

```python
for i in range(5):
    if i == 3:
        break
    print(i)
```

**Working:**

- When encountered, control exits the loop block entirely.

**Precautions:**

- Avoid excessive use as it can make logic harder to follow.

---

### <span style="color:yellow"> **2. `continue`**</span>

Skips the current iteration and moves to the next.

**Syntax:**

```python
for i in range(5):
    if i == 2:
        continue
    print(i)
```

**Working:**

- When encountered, the loop jumps to the next iteration without completing the rest of the current iteration.

**Precautions:**

- Ensure conditions triggering `continue` are intentional to avoid skipping critical logic.

---

### <span style="color:yellow"> **3. `pass`**</span>

A placeholder that does nothing.

**Syntax:**

```python
if True:
    pass
```

**Working:**

- Used as a placeholder for future code, maintaining syntactic correctness.

**Precautions:**

- Use only when code is incomplete or deliberately left empty.

---

## <span style="color:pink"> **`while-else` and `for-else` Loops**</span>

### <span style="color:yellow"> **`while-else`**</span>

Executes the `else` block when the `while` loop condition becomes `False`.

**Syntax:**

```python
count = 0
while count < 3:
    print(count)
    count += 1
else:
    print("Loop ended naturally")
```

**Special Points:**

- The `else` block is skipped if the loop is terminated with a `break`.

---

### <span style="color:yellow"> **`for-else`**</span>

Executes the `else` block if the loop completes all iterations without encountering a `break`.

**Syntax:**

```python
for i in range(3):
    print(i)
else:
    print("Loop ended without break")
```

**Special Points:**

- Useful for checking if a loop terminated normally (e.g., searching a collection).

---

### **Key Takeaways**

1. Use `while` for condition-based loops and `for` for sequence-based loops.
2. Soft keywords (`break`, `continue`, `pass`) control loop behavior but should be used judiciously.
3. `else` clauses in loops provide additional functionality when loops terminate naturally.

## <span style="color:pink">`do-while` in Python</span>

- Python does not have a built-in `do-while` loop like some other languages (e.g., C++ or Java). However, we can mimic a `do-while` loop using a `while` loop or other Python constructs. A `do-while` loop guarantees that the code block runs **at least once**, regardless of the condition.

### **1. Mimicking a `do-while` Loop with a `while` Loop**

You can structure a `while` loop to run the body first and then check the condition.

**Example:**

```python
# Example: Guess the number game
number = 5
guess = None

while True:
    guess = int(input("Guess the number: "))
    if guess == number:
        print("Correct!")
        break
    print("Try again.")
```

**Explanation:**

- The code block executes at least once.
- The `break` statement exits the loop if the condition is met.

---

### **2. Using a `while True` Loop with a Condition Inside**

Instead of checking the condition in the `while`, you check it explicitly after executing the code block.

**Example:**

```python
# Example: Summing numbers until a negative number is entered
sum = 0

while True:
    num = int(input("Enter a number (negative to stop): "))
    sum += num
    if num < 0:
        break

print(f"Total sum is: {sum}")
```

**Explanation:**

- The loop runs indefinitely (`while True`) until a `break` statement is encountered.
- The condition is checked after the block of code executes.

---

### **3. Using a `while` Loop with a Flag**

You can use a flag variable to control when to exit the loop.

**Example:**

```python
# Example: Read and process input
keep_running = True

while keep_running:
    command = input("Enter a command (type 'exit' to quit): ")
    print(f"Processing command: {command}")
    if command == "exit":
        keep_running = False
```

**Explanation:**

- The flag (`keep_running`) ensures the block runs at least once.
- The condition to exit is set within the loop.

---

### **4. Using a `while` Loop with `break` for Structured Execution**

This approach uses `break` to exit the loop after the condition check.

**Example:**

```python
# Example: Login system
correct_password = "python123"

while True:
    password = input("Enter password: ")
    if password == correct_password:
        print("Access granted!")
        break
    print("Incorrect password, try again.")
```

---

### **5. Using a Function and Recursion**

You can mimic a `do-while` loop using recursion, though it's not the most Pythonic way.

**Example:**

```python
# Example: Recursive do-while mimic
def do_while_example():
    num = int(input("Enter a number (negative to stop): "))
    if num >= 0:
        do_while_example()

do_while_example()
```

**Explanation:**

- The function calls itself after processing the input.
- It stops when the condition is met.

---

### **6. Using `try` and `except` for Safe Input**

In some cases, you may use a `try-except` block to mimic `do-while` for input validation.

**Example:**

```python
# Example: Get valid integer input
while True:
    try:
        num = int(input("Enter a valid integer: "))
        print(f"You entered: {num}")
        break
    except ValueError:
        print("Invalid input. Try again.")
```

**Explanation:**

- The code block executes at least once and retries until valid input is provided.

---

### **Key Points**

- Python's flexibility allows you to mimic `do-while` behavior in several ways.
- The most common approach is to use `while True` with a condition inside.
- Avoid excessive recursion in Python to prevent hitting the recursion limit.
- Always ensure the loop has a way to terminate to avoid infinite loops.

## <span style="color:pink">For loop for infinite iteration</span>

- Yes, a `for` loop in Python can run infinitely under certain conditions. While a `while True` loop is more common for infinite iterations, a `for` loop can also achieve this by iterating over an infinite sequence. Here's how:

### **Using an Infinite Sequence**

You can use Python's `itertools` module to create an infinite iterator, such as `itertools.count`, which generates an endless sequence of numbers.

#### **Example 1: Using `itertools.count`**

```python
import itertools

for i in itertools.count():
    print(i)  # This will print numbers starting from 0 indefinitely
```

#### **Example 2: Custom Infinite Iterator**

You can define your own generator to produce values indefinitely.

```python
def infinite_generator():
    while True:
        yield "Infinite"

for value in infinite_generator():
    print(value)  # This will print "Infinite" indefinitely
```

### **When to Use?**

Infinite loops are useful in scenarios such as:

- Continuously monitoring a condition or input.
- Implementing server processes.
- Creating streams of data.

**Caution:** Always ensure you have a condition or mechanism to break out of an infinite loop to avoid consuming resources indefinitely. For example, use `break` or an external signal.

## <span style="color:pink">How `break` and `continue` work internally</span>

- Do They Call a Method?
  - No, break and continue do not invoke methods or functions. They are translated into low-level opcodes (BREAK_LOOP and JUMP_ABSOLUTE) by the Python compiler.
  - These opcodes directly adjust the flow of control in the interpreter.

## <span style="color:pink">`range()` in Python</span>

### **`range()` in Python**

The `range()` function is a built-in function in Python used to generate a sequence of numbers. It is primarily used in loops to iterate over a sequence of numbers.

---

### **Use of `range()`**

- **Generate sequences of numbers**: Commonly used in loops to iterate over a defined range of numbers.
- **Memory-efficient iteration**: It generates values on demand, making it more memory-efficient than a list of numbers.

---

### **Syntax**

```python
range([start], stop[, step])
```

- `start`: The starting number of the sequence (inclusive). Default is `0`.
- `stop`: The end number of the sequence (exclusive).
- `step`: The increment or decrement value. Default is `1`.

---

### **Examples**

1. **Basic usage:**

   ```python
   for i in range(5):
       print(i)
   ```

   **Output:**

   ```
   0
   1
   2
   3
   4
   ```

2. **With `start` and `stop`:**

   ```python
   for i in range(2, 6):
       print(i)
   ```

   **Output:**

   ```
   2
   3
   4
   5
   ```

3. **With `step`:**

   ```python
   for i in range(0, 10, 2):
       print(i)
   ```

   **Output:**

   ```
   0
   2
   4
   6
   8
   ```

4. **Reverse sequence:**
   ```python
   for i in range(10, 0, -2):
       print(i)
   ```
   **Output:**
   ```
   10
   8
   6
   4
   2
   ```

---

### **Class**

`range` is a class in Python. It represents an immutable sequence of numbers and is a part of the `builtins` module.

**Type:**

```python
print(type(range(5)))
# Output: <class 'range'>
```

---

### **Properties of `range`**

1. **Immutable:** The sequence generated by `range()` cannot be modified.
2. **Lazy Evaluation:** It generates numbers on demand, making it memory-efficient.
3. **Iterable:** It can be converted to a list or used directly in a loop.

**Example:**

```python
r = range(5)
print(list(r))  # [0, 1, 2, 3, 4]
```

---

### **Methods**

`range` objects do not have their own methods, but they support certain operations:

1. **`in` operator:**
   Check if a value is in the range.

   ```python
   print(3 in range(5))  # True
   print(6 in range(5))  # False
   ```

2. **Indexing:**
   Retrieve elements by index.

   ```python
   r = range(2, 10, 2)
   print(r[2])  # 6
   ```

3. **Slicing:**
   Get a subsequence.

   ```python
   r = range(10)
   print(list(r[2:8:2]))  # [2, 4, 6]
   ```

4. **Length:**
   Get the total number of elements.
   ```python
   r = range(2, 10, 2)
   print(len(r))  # 4
   ```

---

### **Precautions**

1. **Avoid large ranges directly as lists:**

   - `range` is memory-efficient, but converting it to a list for a very large range can cause memory issues.

   ```python
   r = range(10**9)  # Efficient
   large_list = list(r)  # MemoryError for large ranges
   ```

2. **Ensure `step` is not `0`:**

   - A `step` value of `0` will raise a `ValueError`.

   ```python
   range(1, 10, 0)  # ValueError: range() arg 3 must not be zero
   ```

3. **Exclusive `stop`:**
   - The `stop` value is excluded, which might lead to off-by-one errors if not handled correctly.

---

### **Special Points**

- **Efficient in Loops:** Unlike lists, `range` does not store all the numbers in memory. It generates them one at a time during iteration.
- **Works with large ranges:** You can safely create large ranges without worrying about memory usage.
- **Supports slicing and indexing:** You can extract subsequences without converting to a list.
- **Immutable nature:** `range` objects cannot be modified once created.

---

### **Difference Between `range()` and `list`**

| Feature          | `range()`                          | `list`                                    |
| ---------------- | ---------------------------------- | ----------------------------------------- |
| **Memory Usage** | Memory-efficient (lazy evaluation) | Stores all elements in memory             |
| **Mutability**   | Immutable                          | Mutable                                   |
| **Performance**  | Faster for iteration               | Slower for iteration (more memory access) |

---

### **Conclusion**

`range()` is a versatile and memory-efficient way to generate sequences of numbers in Python. It is widely used in loops, supports slicing, indexing, and is immutable, making it a robust tool for iteration tasks.

## <span style="color:pink"> **Lazy Evaluation**</span>

**Lazy evaluation** is a programming concept where the evaluation of an expression is delayed until its value is actually required. Instead of computing all values upfront, computations are deferred, and values are generated on demand. This helps in optimizing memory usage and computation time.

---

### **Key Features of Lazy Evaluation**

1. **On-demand computation**:

   - Values are calculated only when needed.
   - If a value is never accessed, it is never computed.

2. **Memory efficiency**:

   - Large data structures or sequences are not stored in memory. Instead, values are generated one at a time when iterated over.

3. **Performance optimization**:

   - Avoids unnecessary calculations and improves program efficiency, especially for large datasets.

4. **Use of Iterators**:
   - Iterators and generators are common tools for implementing lazy evaluation in Python.

---

### **Lazy Evaluation in Python**

In Python, **lazy evaluation** is commonly seen with:

1. **`range()`**:

   - Does not generate the entire sequence upfront. Instead, it generates each number one at a time during iteration.

   ```python
   r = range(1, 1000000)  # No memory issue
   print(r)  # range(1, 1000000)
   for i in r:  # Generates values on demand
       print(i)
       break
   ```

2. **Generators**:

   - A generator function produces values lazily using the `yield` keyword.

   ```python
   def lazy_generator():
       for i in range(5):
           yield i

   gen = lazy_generator()
   print(next(gen))  # 0 (value generated when requested)
   print(next(gen))  # 1
   ```

3. **Iterators**:

   - Many built-in functions in Python, like `map()`, `filter()`, and `zip()`, return iterators that operate lazily.

   **Example with `map()`:**

   ```python
   result = map(lambda x: x * 2, range(5))  # Lazy operation
   print(next(result))  # 0 (computed on demand)
   print(next(result))  # 2
   ```

4. **`itertools` module**:

   - Functions like `itertools.count()` and `itertools.islice()` generate values lazily.

   ```python
   import itertools
   counter = itertools.count(start=1)
   print(next(counter))  # 1
   print(next(counter))  # 2
   ```

---

### **Advantages of Lazy Evaluation**

1. **Efficient use of memory**:

   - Suitable for large datasets or infinite sequences.

   ```python
   large_range = range(1, 10**9)  # Memory-efficient
   print(large_range[100])  # Access specific value without computing all
   ```

2. **Faster performance**:

   - Skips unnecessary calculations.

   ```python
   result = (x for x in range(10) if x % 2 == 0)  # Generator expression
   print(next(result))  # 0 (no need to compute all values)
   ```

3. **Infinite sequences**:

   - Enables working with infinite streams of data.

   ```python
   def infinite_numbers():
       i = 0
       while True:
           yield i
           i += 1

   gen = infinite_numbers()
   print(next(gen))  # 0
   print(next(gen))  # 1
   ```

---

### **Disadvantages of Lazy Evaluation**

1. **Delayed Errors**:

   - Errors in a lazy expression are only triggered when the value is accessed.

   ```python
   result = (1 / x for x in [1, 0, 2])
   print(next(result))  # 1.0
   print(next(result))  # ZeroDivisionError occurs here
   ```

2. **Debugging Complexity**:

   - Since values are computed on demand, debugging lazy evaluations can be harder.

3. **Reusability Issues**:
   - Generators and iterators are exhausted once iterated; they cannot be reused.
   ```python
   gen = (x for x in range(5))
   list(gen)  # [0, 1, 2, 3, 4]
   list(gen)  # [] (already exhausted)
   ```

---

### **Eager Evaluation vs. Lazy Evaluation**

| **Aspect**             | **Lazy Evaluation**               | **Eager Evaluation**                  |
| ---------------------- | --------------------------------- | ------------------------------------- |
| **Computation**        | On-demand                         | Immediate                             |
| **Memory Usage**       | Efficient                         | May use more memory                   |
| **Performance**        | Faster for unused or partial data | May be slower due to unnecessary work |
| **Examples in Python** | `range()`, generators, `map()`    | Lists, tuples, direct function calls  |

---

### **Conclusion**

Lazy evaluation is a powerful concept that optimizes memory usage and improves performance by computing values only when required. It is particularly beneficial for handling large datasets, infinite sequences, or cases where not all values need to be computed. Understanding lazy evaluation can help you write more efficient Python code, especially when working with iterators, generators, and similar constructs.

---

### **How `for` Statements Work in Python – Mechanics & Execution Flow**

The `for` loop in Python is used for iterating over sequences such as lists, tuples, strings, dictionaries, sets, and even generators or custom iterable objects. It abstracts away the need for manually managing loop indices, making iteration clean and readable.

---

## **1. Mechanics of `for` Loop Execution**

Python’s `for` loop works differently from traditional C-style loops (`for (i=0; i<n; i++)`). Instead of using an index-based loop, Python follows an **iterator-based approach**.

### **Execution Steps:**

1. The `for` loop takes an **iterable** (e.g., list, tuple, string, range, dictionary, etc.).
2. The loop gets an **iterator** from the iterable using the built-in `iter()` function.
3. The loop repeatedly calls `next()` on the iterator to fetch the next element.
4. If there are no more elements (`StopIteration` is raised), the loop exits.

---

## **2. Example & Internal Working**

### **Example Code:**

```python
numbers = [10, 20, 30]
for num in numbers:
    print(num)
```

### **How It Works Internally:**

1. The iterable `numbers = [10, 20, 30]` is passed to `iter()`, which creates an iterator.
2. `next()` is called on the iterator to get each value.
3. When all elements are exhausted, `StopIteration` is raised, and the loop exits.

#### **Equivalent Code Using `iter()` and `next()`:**

```python
numbers = [10, 20, 30]
iterator = iter(numbers)  # Create an iterator

while True:
    try:
        num = next(iterator)  # Get next item
        print(num)
    except StopIteration:  # Exit when no more items
        break
```

---

## **3. Variations of `for` Loop**

### **(a) Iterating Over a `range()`**

Python’s `range()` is commonly used for indexed loops:

```python
for i in range(5):  # i goes from 0 to 4
    print(i)
```

**How it works:**

- `range(5)` generates an iterable sequence `[0, 1, 2, 3, 4]`.
- The loop fetches each number one by one.

### **(b) Looping Over Strings**

```python
for char in "Python":
    print(char)
```

Each character is fetched one by one from the string.

### **(c) Iterating Over Dictionaries**

```python
data = {"a": 1, "b": 2, "c": 3}
for key, value in data.items():
    print(key, value)
```

- `.items()` returns key-value pairs.

---

## **4. Breaking or Skipping Iterations**

### **Using `break`**

Stops the loop prematurely:

```python
for num in range(10):
    if num == 5:
        break  # Loop stops when num is 5
    print(num)
```

### **Using `continue`**

Skips current iteration and moves to the next:

```python
for num in range(5):
    if num == 2:
        continue  # Skips when num is 2
    print(num)
```

---

## **5. `else` Clause in `for` Loops**

Python supports `else` in `for` loops:

```python
for num in range(3):
    print(num)
else:
    print("Loop completed successfully")
```

- The `else` block **executes only if the loop runs completely without a `break`**.

---

## **6. Using `for` With `enumerate()`**

`enumerate()` provides an index while iterating:

```python
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(index, fruit)
```

**Output:**

```
0 apple
1 banana
2 cherry
```

---

## **7. Summary**

| Feature                | Explanation                                                                   |
| ---------------------- | ----------------------------------------------------------------------------- |
| **Iterates over**      | Any iterable (list, tuple, string, dictionary, generator, etc.)               |
| **Mechanism**          | Uses `iter()` and `next()` internally                                         |
| **Exit Condition**     | Stops when `StopIteration` is raised                                          |
| **Control Statements** | `break` (stop loop), `continue` (skip iteration), `else` (runs if no `break`) |

---
