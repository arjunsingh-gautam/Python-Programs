# <span style="color:orange">**Set Class in Python**</span>

The `set` class in Python represents an unordered collection of unique and immutable elements. Sets are highly optimized for membership testing and eliminate duplicate entries automatically.

---

### <span style="color:pink">**Properties of Sets**</span>

1. **Unordered**:
   Sets do not maintain any order of elements.

   ```python
   s = {1, 2, 3}
   print(s)  # Output: {1, 2, 3} (order may vary)
   ```

2. **Unique Elements**:
   Sets automatically remove duplicate values.

   ```python
   s = {1, 2, 2, 3}
   print(s)  # Output: {1, 2, 3}
   ```

3. **Mutable**:
   The set itself is mutable (elements can be added or removed), but its elements must be immutable.

4. **Unindexed**:
   Sets do not support indexing or slicing.

   ```python
   s = {1, 2, 3}
   # print(s[0])  # Raises TypeError
   ```

5. **Dynamic**:
   Sets grow or shrink as elements are added or removed.

---

### <span style="color:pink">**Precautions with Sets**</span>

1. Elements must be immutable:

   - Lists or other sets cannot be elements of a set.
   - Tuples are allowed because they are immutable.

   ```python
   s = {1, (2, 3), "Python"}  # Valid
   # s = {1, [2, 3]}  # Raises TypeError
   ```

2. Sets are unordered:

   - Operations that depend on order (e.g., indexing) are not allowed.

3. Cannot create an empty set using `{}`:
   - `{}` creates an empty dictionary, not a set. Use `set()` instead.

---

### <span style="color:pink">**How to Declare Sets**</span>

1. **Using Curly Braces `{}`**:

   ```python
   s = {1, 2, 3}
   print(s)  # Output: {1, 2, 3}
   ```

2. **Using `set()` Constructor**:

   ```python
   s = set([1, 2, 3])
   print(s)  # Output: {1, 2, 3}
   ```

3. **Empty Set**:
   ```python
   s = set()
   print(s)  # Output: set()
   ```

---

### <span style="color:pink">**Comparison Operators on Sets**</span>

1. **Equality (`==`)**:

   - Returns `True` if two sets have the same elements.

   ```python
   print({1, 2, 3} == {3, 2, 1})  # Output: True
   ```

2. **Subset (`<=`)**:

   - Returns `True` if all elements of one set are in another.

   ```python
   print({1, 2} <= {1, 2, 3})  # Output: True
   ```

3. **Proper Subset (`<`)**:

   - Returns `True` if the first set is a subset of the second but not equal.

   ```python
   print({1, 2} < {1, 2, 3})  # Output: True
   ```

4. **Superset (`>=`)**:

   - Returns `True` if all elements of the second set are in the first.

   ```python
   print({1, 2, 3} >= {2, 3})  # Output: True
   ```

5. **Proper Superset (`>`)**:

   - Returns `True` if the first set is a superset of the second but not equal.

   ```python
   print({1, 2, 3} > {1, 2})  # Output: True
   ```

6. **Inequality (`!=`)**:
   - Returns `True` if two sets have different elements.
   ```python
   print({1, 2, 3} != {1, 2})  # Output: True
   ```

---

### <span style="color:pink">**Set Methods**</span>

#### **Adding and Removing Elements**

1. **`add(x)`**:
   Adds `x` to the set. No effect if `x` is already present.

   ```python
   s = {1, 2}
   s.add(3)
   print(s)  # Output: {1, 2, 3}
   ```

2. **`remove(x)`**:
   Removes `x` from the set. Raises `KeyError` if `x` is not found.

   ```python
   s = {1, 2, 3}
   s.remove(2)
   print(s)  # Output: {1, 3}
   ```

3. **`discard(x)`**:
   Removes `x` if present; does nothing if `x` is absent.

   ```python
   s = {1, 2, 3}
   s.discard(4)  # No error
   print(s)  # Output: {1, 2, 3}
   ```

4. **`pop()`**:
   Removes and returns an arbitrary element. Raises `KeyError` if the set is empty.

   ```python
   s = {1, 2, 3}
   element = s.pop()
   print(element)  # Output: 1 (or any other element)
   print(s)  # Output: Remaining elements
   ```

5. **`clear()`**:
   Removes all elements from the set.
   ```python
   s = {1, 2, 3}
   s.clear()
   print(s)  # Output: set()
   ```

---

#### **Set Operations**

1. **Union (`|` or `union()`):**
   Combines elements from both sets.

   ```python
   s1 = {1, 2}
   s2 = {2, 3}
   print(s1 | s2)  # Output: {1, 2, 3}
   ```

2. **Intersection (`&` or `intersection()`):**
   Common elements between sets.

   ```python
   s1 = {1, 2}
   s2 = {2, 3}
   print(s1 & s2)  # Output: {2}
   ```

3. **Difference (`-` or `difference()`):**
   Elements in the first set but not in the second.

   ```python
   s1 = {1, 2, 3}
   s2 = {2, 3}
   print(s1 - s2)  # Output: {1}
   ```

4. **Symmetric Difference (`^` or `symmetric_difference()`):**
   Elements in either set but not in both.
   ```python
   s1 = {1, 2}
   s2 = {2, 3}
   print(s1 ^ s2)  # Output: {1, 3}
   ```

---

#### **Membership Testing**

- Use the `in` and `not in` operators.
  ```python
  s = {1, 2, 3}
  print(2 in s)  # Output: True
  print(4 not in s)  # Output: True
  ```

---

#### **Iterating Over a Set**

```python
s = {1, 2, 3}
for element in s:
    print(element)
```

---

#### **Built-in Functions**

1. **`len()`**: Returns the number of elements.
2. **`min()` and `max()`**: Returns the smallest/largest element.
3. **`sum()`**: Returns the sum of elements (only for numeric sets).
4. **`sorted()`**: Returns a sorted list from the set.

---

## <span style="color:yellow">**Set Comprehension in Python**</span>

Set comprehension is a concise way to create sets in Python by specifying a condition or an operation within curly braces `{}`. It allows you to generate sets dynamically while filtering or transforming elements in a single line of code.

---

### **Syntax of Set Comprehension**

```python
{expression for item in iterable if condition}
```

- **`expression`**: The value to include in the set.
- **`item`**: The current element in the iteration.
- **`iterable`**: Any iterable object like a list, tuple, range, etc.
- **`if condition`**: (Optional) A condition to filter elements.

---

### **Examples of Set Comprehension**

#### 1. **Basic Example**

Create a set of squares from 1 to 5:

```python
squares = {x**2 for x in range(1, 6)}
print(squares)  # Output: {1, 4, 9, 16, 25}
```

---

#### 2. **Set Comprehension with Conditions**

Create a set of even numbers from 1 to 10:

```python
even_numbers = {x for x in range(1, 11) if x % 2 == 0}
print(even_numbers)  # Output: {2, 4, 6, 8, 10}
```

---

#### 3. **Set Comprehension with Strings**

Extract unique vowels from a string:

```python
vowels = {char for char in "hello world" if char in "aeiou"}
print(vowels)  # Output: {'o', 'e'}
```

---

#### 4. **Set Comprehension with Nested Loops**

Generate a Cartesian product of two sets:

```python
cartesian_product = {(x, y) for x in {1, 2} for y in {3, 4}}
print(cartesian_product)  # Output: {(1, 3), (1, 4), (2, 3), (2, 4)}
```

---

#### 5. **Remove Duplicates from a List**

Convert a list with duplicates into a unique set of elements:

```python
numbers = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = {x for x in numbers}
print(unique_numbers)  # Output: {1, 2, 3, 4, 5}
```

---

### **Key Points about Set Comprehension**

1. **Order**:
   Sets are unordered collections, so the order of elements in the result may differ.

2. **Uniqueness**:
   Duplicate results are automatically removed.

   ```python
   result = {x % 3 for x in range(10)}
   print(result)  # Output: {0, 1, 2}
   ```

3. **Immutability of Elements**:
   The elements in the resulting set must be immutable (e.g., integers, strings, tuples).

4. **Efficiency**:
   Set comprehension is faster and more readable than using a traditional loop with `add()`.

---

### **Practical Use Cases of Set Comprehension**

1. **Filter Unique Words**:

   ```python
   sentence = "Python is great and Python is easy"
   unique_words = {word.lower() for word in sentence.split()}
   print(unique_words)  # Output: {'python', 'is', 'great', 'and', 'easy'}
   ```

2. **Generate Unique Random Numbers**:

   ```python
   import random
   random_set = {random.randint(1, 20) for _ in range(10)}
   print(random_set)
   ```

3. **Remove Special Characters**:

   ```python
   text = "Hello! How are you?"
   clean_characters = {char for char in text if char.isalnum()}
   print(clean_characters)  # Output: {'H', 'o', 'l', 'e', 'w', 'r', 'y', 'u'}
   ```

4. **Mathematical Operations**:
   ```python
   multiples_of_3 = {x for x in range(1, 20) if x % 3 == 0}
   print(multiples_of_3)  # Output: {3, 6, 9, 12, 15, 18}
   ```

---

### **Benefits of Set Comprehension**

1. **Concise and Readable**: Simplifies the creation of sets compared to using loops.
2. **Efficient**: Combines iteration, condition-checking, and set-building in one step.
3. **Unique Results**: Automatically removes duplicates.

---

Let me know if you need further assistance or additional examples!
