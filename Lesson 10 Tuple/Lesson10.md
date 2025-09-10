# <span style="color:orange">**Tuple Class in Python**</span>

Tuples in Python are immutable sequences used to store collections of items. Unlike lists, once a tuple is created, its elements cannot be modified. Tuples are often used when the data should remain constant and not change throughout the program.

---

## <span style="color:pink">**How to Declare Tuples**</span>

Tuples can be declared in various ways:

1. **Using Parentheses `()`**:

   ```python
   t = (1, 2, 3)
   print(t)  # Output: (1, 2, 3)
   ```

2. **Without Parentheses (Comma-Separated Values)**:

   ```python
   t = 1, 2, 3
   print(t)  # Output: (1, 2, 3)
   ```

3. **Using the `tuple()` Constructor**:

   ```python
   t = tuple([1, 2, 3])
   print(t)  # Output: (1, 2, 3)
   ```

4. **Creating a Single-Element Tuple**:

   - You must include a trailing comma.

   ```python
   t = (1,)
   print(t)  # Output: (1,)
   ```

5. **Empty Tuple**:
   ```python
   t = ()
   print(t)  # Output: ()
   ```

---

## <span style="color:pink">**Properties of Tuples**</span>

1. **Ordered**: The elements have a defined order.
2. **Immutable**: Once defined, the elements cannot be changed.
3. **Allow Duplicates**: Tuples can contain duplicate values.
4. **Heterogeneous**: Tuples can store items of different data types.

---

## <span style="color:pink">**Concatenation of Tuples**</span>

Tuples can be concatenated using the `+` operator.

```python
t1 = (1, 2, 3)
t2 = (4, 5)
result = t1 + t2
print(result)  # Output: (1, 2, 3, 4, 5)
```

---

## <span style="color:pink">**Repetition of Tuples**</span>

Tuples can be repeated using the `*` operator.

```python
t = (1, 2)
result = t * 3
print(result)  # Output: (1, 2, 1, 2, 1, 2)
```

---

## <span style="color:pink">**Comparison of Tuples**</span>

Tuples are compared element-wise, and the comparison stops at the first unequal pair of elements.

```python
t1 = (1, 2, 3)
t2 = (1, 2, 4)

print(t1 < t2)  # Output: True (compares 3 with 4)
print(t1 == t2)  # Output: False
```

---

## <span style="color:pink">**Tuple Methods**</span>

Tuples have a limited number of methods since they are immutable.

1. **`tuple.count(x)`**:
   Returns the number of times `x` appears in the tuple.

   ```python
   t = (1, 2, 2, 3)
   print(t.count(2))  # Output: 2
   ```

2. **`tuple.index(x, start, end)`**:
   Returns the first index of `x` in the tuple. Raises `ValueError` if `x` is not found.

   ```python
   t = (1, 2, 3, 2)
   print(t.index(2))  # Output: 1
   ```

---

## <span style="color:pink">**Immutability and Workaround**</span>

Tuples are immutable, but they can store mutable objects like lists. This allows indirect modification.

```python
t = ([1, 2], [3, 4])
t[0][0] = 99
print(t)  # Output: ([99, 2], [3, 4])
```

---

## <span style="color:pink">**Use Cases of Tuples**</span>

1. **Returning Multiple Values from a Function**:

   ```python
   def divide(a, b):
       return a // b, a % b

   result = divide(10, 3)
   print(result)  # Output: (3, 1)
   ```

2. **Using as Keys in Dictionaries**:
   Tuples can be used as dictionary keys since they are hashable.

   ```python
   points = {(1, 2): "A", (3, 4): "B"}
   print(points[(1, 2)])  # Output: "A"
   ```

---

## <span style="color:pink">**Tuple Packing and Unpacking**</span>

1. **Packing**:
   Grouping multiple values into a tuple.

   ```python
   t = 1, 2, 3
   print(t)  # Output: (1, 2, 3)
   ```

2. **Unpacking**:
   Assigning tuple values to variables.

   ```python
   t = (1, 2, 3)
   a, b, c = t
   print(a, b, c)  # Output: 1 2 3
   ```

3. **Using `*` for Arbitrary Elements**:
   ```python
   t = (1, 2, 3, 4)
   a, *b, c = t
   print(a, b, c)  # Output: 1 [2, 3] 4
   ```

---

## <span style="color:pink">**Error Conditions**</span>

1. **Modifying a Tuple**:

   ```python
   t = (1, 2, 3)
   # t[0] = 10  # Raises TypeError
   ```

2. **Accessing Invalid Index**:

   ```python
   t = (1, 2, 3)
   # print(t[5])  # Raises IndexError
   ```

3. **Using Unhashable Elements**:
   ```python
   # t = ([1, 2], 3)  # List inside a tuple is unhashable
   ```

This detailed overview of tuples covers their properties, operations, methods, and practical examples. Let me know if you need clarification on any part!
