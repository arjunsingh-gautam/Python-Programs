# **<span style="color:#c1121f">zip() and enumerate() in Python</span>**

# 🔹 `zip()` in Python

## What is `zip()`?

`zip()` **combines multiple iterables element-by-element** into tuples.

Think of it as **horizontal pairing**.

---

## Syntax

```python
zip(iterable1, iterable2, ..., iterableN)
```

Returns:
➡️ a **zip object (iterator)** in Python 3

---

## Basic Example

```python
names = ["Alice", "Bob", "Charlie"]
scores = [85, 90, 95]

z = zip(names, scores)
print(list(z))
```

### Output

```python
[('Alice', 85), ('Bob', 90), ('Charlie', 95)]
```

---

## 🧠 How `zip()` works internally (dry run)

Input:

```python
A = [a1, a2, a3]
B = [b1, b2, b3]
```

Step-by-step:

```
Iteration 1 → (a1, b1)
Iteration 2 → (a2, b2)
Iteration 3 → (a3, b3)
Stop when shortest iterable ends
```

---

## ⚠️ Important Rule: Stops at shortest iterable

```python
a = [1, 2, 3]
b = ['x', 'y']

print(list(zip(a, b)))
```

Output:

```python
[(1, 'x'), (2, 'y')]
```

---

## Common Use Cases of `zip()`

### 1️⃣ Looping over multiple lists

```python
for name, score in zip(names, scores):
    print(name, score)
```

✔️ Cleaner than indexing

---

### 2️⃣ Creating dictionaries

```python
keys = ["id", "name", "age"]
values = [101, "Arj", 21]

d = dict(zip(keys, values))
```

Output:

```python
{'id': 101, 'name': 'Arj', 'age': 21}
```

---

### 3️⃣ Unzipping (transpose)

```python
pairs = [(1, 'a'), (2, 'b'), (3, 'c')]
nums, chars = zip(*pairs)

print(nums)
print(chars)
```

Output:

```python
(1, 2, 3)
('a', 'b', 'c')
```

---

### 4️⃣ Matrix transpose

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

transpose = list(zip(*matrix))
```

Output:

```python
[(1, 4), (2, 5), (3, 6)]
```

---

### 5️⃣ Comparing two sequences

```python
for a, b in zip(old_data, new_data):
    if a != b:
        print("Changed")
```

---

### 6️⃣ Parallel sorting

```python
names = ["A", "B", "C"]
scores = [90, 70, 80]

sorted_pairs = sorted(zip(scores, names))
```

Output:

```python
[(70, 'B'), (80, 'C'), (90, 'A')]
```

---

---

# 🔹 `enumerate()` in Python

## What is `enumerate()`?

`enumerate()` **adds an index to elements while iterating**.

Think of it as:

```
(index, value)
```

---

## Syntax

```python
enumerate(iterable, start=0)
```

Returns:
➡️ an **enumerate object (iterator)**

---

## Basic Example

```python
fruits = ["apple", "banana", "mango"]

for index, fruit in enumerate(fruits):
    print(index, fruit)
```

Output:

```
0 apple
1 banana
2 mango
```

---

## 🧠 How `enumerate()` works internally (dry run)

Input:

```python
fruits = ["apple", "banana"]
```

Execution:

```
Iteration 1 → (0, "apple")
Iteration 2 → (1, "banana")
```

---

## Custom Start Index

```python
for i, fruit in enumerate(fruits, start=1):
    print(i, fruit)
```

Output:

```
1 apple
2 banana
```

---

## Common Use Cases of `enumerate()`

### 1️⃣ Replace `range(len())` (best practice)

❌ Bad:

```python
for i in range(len(fruits)):
    print(i, fruits[i])
```

✅ Good:

```python
for i, fruit in enumerate(fruits):
    print(i, fruit)
```

---

### 2️⃣ Index-based updates

```python
nums = [10, 20, 30]

for i, val in enumerate(nums):
    nums[i] = val * 2
```

Result:

```python
[20, 40, 60]
```

---

### 3️⃣ Find index of element (with condition)

```python
for i, val in enumerate(nums):
    if val == 30:
        print(i)
```

---

### 4️⃣ Debugging loops

```python
for i, item in enumerate(data):
    print(f"Step {i}: {item}")
```

---

### 5️⃣ Tracking positions in algorithms

```python
max_val = float('-inf')
max_idx = -1

for i, val in enumerate(arr):
    if val > max_val:
        max_val = val
        max_idx = i
```

---

---

# 🔹 Using `zip()` + `enumerate()` together

```python
names = ["A", "B", "C"]
scores = [90, 80, 85]

for i, (name, score) in enumerate(zip(names, scores), start=1):
    print(i, name, score)
```

Output:

```
1 A 90
2 B 80
3 C 85
```

---

# ⚠️ Important Pitfalls

### `zip()` is single-use

```python
z = zip(a, b)
list(z)
list(z)  # empty
```

---

### Both are lazy iterators

- Memory efficient
- Not materialized until consumed

---

# 🧠 Mental Models

| Function      | Think of it as       |
| ------------- | -------------------- |
| `zip()`       | Horizontal pairing   |
| `enumerate()` | Auto index generator |

---

# Interview One-Liners

### zip

> `zip()` combines multiple iterables element-wise into tuples and stops at the shortest iterable.

### enumerate

> `enumerate()` adds an index to each element of an iterable, avoiding manual index tracking.

---
