# <span style="color:orange">**Dictionary Class in Python**</span>

A dictionary in Python is an **unordered, mutable**, and **key-value** pair data structure. It is implemented as a hash table, making lookups and insertions efficient.

---

## <span style="color:pink">**Properties of Dictionaries**</span>

1. **Unordered**: In Python versions < 3.7, dictionaries are unordered. From Python 3.7 onwards, dictionaries maintain the insertion order.
2. **Mutable**: The contents of a dictionary can be changed after it is created (keys and values can be added, removed, or modified).
3. **Unique Keys**: Each key in a dictionary must be unique. <u>_If a key is duplicated, the last value will overwrite the earlier one._</u>
4. **Hashable Keys**: Keys must be immutable types (e.g., strings, numbers, or tuples with immutable elements). Values can be of any data type.

---

## <span style="color:pink">**Special Points**</span>

1. **Performance**: Dictionary operations like retrieval, insertion, and deletion have an average time complexity of \(O(1)\).
2. **Dynamic Size**: Dictionaries automatically resize to handle additional key-value pairs.
3. **Hashing**: The keys in a dictionary are hashed internally for quick lookups.
4. **No Key Ordering (Pre-Python 3.7)**: Iteration over keys or items might not follow the insertion sequence.

---

## <span style="color:pink">**Precautions**</span>

1. **Hashable Keys**: Avoid using mutable types (like lists) as keys.
   ```python
   # Invalid
   d = {[1, 2]: "value"}  # TypeError: unhashable type: 'list'
   ```
2. **Duplicate Keys**: Overwriting occurs when duplicate keys are used.
   ```python
   d = {"a": 1, "a": 2}
   print(d)  # Output: {'a': 2}
   ```
3. **KeyError**: Accessing a non-existent key raises a `KeyError`.
   ```python
   d = {"x": 10}
   print(d["y"])  # KeyError: 'y'
   ```

---

## <span style="color:pink">**Declaring a Dictionary**</span>

#### 1. **Using `{}` (Dictionary Literals)**

```python
d = {"a": 1, "b": 2, "c": 3}
```

#### 2. **Using `dict()` Constructor**

```python
d = dict(a=1, b=2, c=3)  # Equivalent to {'a': 1, 'b': 2, 'c': 3}
```

#### 3. **From a List of Tuples**

```python
d = dict([("a", 1), ("b", 2), ("c", 3)])
```

#### 4. **Using `zip()`**

```python
keys = ["a", "b", "c"]
values = [1, 2, 3]
d = dict(zip(keys, values))
```

#### 5. **From Default Values**

```python
d = dict.fromkeys(["a", "b", "c"], 0)  # {'a': 0, 'b': 0, 'c': 0}
```

---

## <span style="color:pink">**Comparison Operators on Dictionaries**</span>

1. **Equality (`==`)**: Returns `True` if both dictionaries have the same key-value pairs.

   ```python
   d1 = {"a": 1, "b": 2}
   d2 = {"b": 2, "a": 1}
   print(d1 == d2)  # Output: True
   ```

2. **Inequality (`!=`)**: Returns `True` if dictionaries are not identical.

   ```python
   d1 = {"a": 1}
   d2 = {"a": 2}
   print(d1 != d2)  # Output: True
   ```

3. **Other Comparisons (`<`, `>`)**: Not supported directly.

---

## <span style="color:pink">**Accessing and Editing Dictionary Elements**</span>

#### 1. **Accessing Elements**

- **Using Keys**:
  ```python
  d = {"a": 1, "b": 2}
  print(d["a"])  # Output: 1
  ```
- **Using `get()`**:
  ```python
  print(d.get("c", "Default"))  # Output: 'Default'
  ```

#### 2. **Editing Elements**

- Add/Update Key-Value Pair:

  ```python
  d["c"] = 3  # Adds a new key-value pair
  d["a"] = 10  # Updates the value of an existing key
  ```

- Delete Key-Value Pair:
  ```python
  del d["b"]
  print(d)  # Output: {'a': 10, 'c': 3}
  ```

---

## <span style="color:pink">**Dictionary Methods**</span>

#### 1. **Add/Update**

- `update()`:
  ```python
  d = {"a": 1}
  d.update({"b": 2, "c": 3})
  print(d)  # Output: {'a': 1, 'b': 2, 'c': 3}
  ```

#### 2. **Remove**

- `pop()`:

  ```python
  d = {"a": 1, "b": 2}
  d.pop("a")
  print(d)  # Output: {'b': 2}
  ```

- `popitem()`:

  ```python
  d.popitem()  # Removes the last inserted item
  ```

- `clear()`:
  ```python
  d.clear()  # Removes all items
  ```

#### 3. **Access Keys/Values/Items**

- `keys()`, `values()`, `items()`:
  ```python
  d = {"a": 1, "b": 2}
  print(d.keys())   # Output: dict_keys(['a', 'b'])
  print(d.values()) # Output: dict_values([1, 2])
  print(d.items())  # Output: dict_items([('a', 1), ('b', 2)])
  ```

#### 4. **Check Membership**

- `in`:
  ```python
  print("a" in d)  # Output: True
  ```

#### 5. **Default Values**

- `setdefault()`:
  ```python
  d.setdefault("c", 0)  # Adds 'c' with default value 0 if not present
  ```

---

## <span style="color:pink">**Dictionary Comprehension**</span>

#### Syntax:

```python
{key_expression: value_expression for item in iterable if condition}
```

#### Examples:

1. **Basic Dictionary Comprehension**:

   ```python
   d = {x: x**2 for x in range(5)}
   print(d)  # Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
   ```

2. **Filter Keys**:

   ```python
   d = {x: x*2 for x in range(10) if x % 2 == 0}
   print(d)  # Output: {0: 0, 2: 4, 4: 8, 6: 12, 8: 16}
   ```

3. **From Lists**:
   ```python
   keys = ["name", "age", "city"]
   values = ["Alice", 25, "New York"]
   d = {keys[i]: values[i] for i in range(len(keys))}
   print(d)  # Output: {'name': 'Alice', 'age': 25, 'city': 'New York'}
   ```

---

Let me know if you want detailed use cases or further clarifications!
