# <span style="color:#2E86C1"><b>Iterators in Python — Complete Deep Explanation</b></span>

We’ll go from **concept → protocol → internals → implementation → comparison → performance → constraints**.

This is foundational to understanding generators, comprehensions, and Python loops.

---

# <span style="color:#AF7AC5"><b>1️⃣ What Is an Iterator?</b></span>

An **iterator** is:

> An object that produces a sequence of values one at a time and remembers its position between calls.

It implements the **Iterator Protocol**.

Instead of storing all values at once, it provides them lazily.

Example:

```python
nums = [1, 2, 3]
it = iter(nums)

print(next(it))  # 1
print(next(it))  # 2
print(next(it))  # 3
```

Here:

- `it` is an iterator.
- `nums` is an iterable (not necessarily an iterator).

---

# <span style="color:#48C9B0"><b>2️⃣ Necessary and Sufficient Conditions</b></span>

For an object to be an **iterator**, it must:

### ✔ 1. Implement `__iter__()`

### ✔ 2. Implement `__next__()`

And satisfy:

```python
iter(obj) is obj
```

Meaning:

- `__iter__()` must return self.

If `__next__()`:

- Returns next value
- Raises `StopIteration` when done

Then the object is a valid iterator.

---

# <span style="color:#E74C3C"><b>3️⃣ Internal Working Mechanism</b></span>

When you write:

```python
for x in iterable:
    print(x)
```

Python internally does:

```python
it = iter(iterable)
while True:
    try:
        value = next(it)
    except StopIteration:
        break
    print(value)
```

So:

- `iter()` gets iterator object.
- `next()` pulls values.
- `StopIteration` signals completion.

---

# <span style="color:#5DADE2"><b>4️⃣ How Iterator Object Works Internally</b></span>

An iterator object typically stores:

- Reference to underlying data
- Current position
- Any state required

Example (simplified list iterator concept):

```text
ListIterator
 ├── reference to list
 ├── current index
```

Each call to `__next__()`:

1. Check index
2. Return element
3. Increment index
4. Raise StopIteration if done

---

# <span style="color:#BB8FCE"><b>5️⃣ Create Iterator — All Possible Ways</b></span>

## 🔹 Method 1 — Using Built-in Iterables

```python
nums = [1, 2, 3]
it = iter(nums)
```

Lists are iterable.
Their iterators are separate objects.

---

## 🔹 Method 2 — Custom Iterator Class

Boilerplate:

```python
class Counter:
    def __init__(self, limit):
        self.limit = limit
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.limit:
            self.current += 1
            return self.current
        else:
            raise StopIteration
```

Usage:

```python
c = Counter(3)
for num in c:
    print(num)
```

Explanation:

- `__iter__()` returns self → object is iterator.
- `__next__()` defines iteration logic.

---

## 🔹 Method 3 — Iterable That Returns Separate Iterator

Better design pattern:

```python
class MyRange:
    def __init__(self, n):
        self.n = n

    def __iter__(self):
        return MyRangeIterator(self.n)


class MyRangeIterator:
    def __init__(self, n):
        self.current = 0
        self.n = n

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.n:
            val = self.current
            self.current += 1
            return val
        else:
            raise StopIteration
```

Why better?

Because:

- Multiple independent iterations possible.
- Clean separation of iterable and iterator.

---

## 🔹 Method 4 — Generators (Shortcut)

Generator automatically implements iterator protocol:

```python
def gen(n):
    for i in range(n):
        yield i
```

Calling:

```python
g = gen(3)
```

`g` is an iterator.

Generators are syntactic sugar for iterator class.

---

# <span style="color:#F5B041"><b>6️⃣ Iterable vs Iterator — Fundamental Difference</b></span>

| Feature                 | Iterable     | Iterator   |
| ----------------------- | ------------ | ---------- |
| Has `__iter__()`        | Yes          | Yes        |
| Has `__next__()`        | No (usually) | Yes        |
| Maintains state         | No           | Yes        |
| Multiple loops possible | Yes          | Usually no |

Example:

```python
nums = [1, 2, 3]
```

`nums` is iterable.

```python
it = iter(nums)
```

`it` is iterator.

Iterating twice:

```python
for x in nums:  # Works again
```

But:

```python
for x in it:  # After exhaustion, empty
```

Because iterator maintains state.

---

## 🔹 Internal Mechanism Difference

Iterable:

```text
Iterable
   └── __iter__() → returns new iterator
```

Iterator:

```text
Iterator
   ├── __iter__() → returns self
   └── __next__()
```

---

# <span style="color:#58D68D"><b>7️⃣ Example Showing Difference</b></span>

```python
nums = [1,2,3]

it1 = iter(nums)
it2 = iter(nums)

print(next(it1))  # 1
print(next(it2))  # 1
```

Two separate iterators.

But:

```python
print(next(it1))  # 2
print(next(it1))  # 3
print(next(it1))  # StopIteration
```

State stored inside iterator.

---

# <span style="color:#F39C12"><b>8️⃣ How Python Determines Iterable</b></span>

When calling `iter(obj)`:

Python checks:

1. If object has `__iter__`
2. Else if has `__getitem__` (sequence protocol fallback)
3. Otherwise TypeError

So old-style iteration works via `__getitem__`.

---

# <span style="color:#EC7063"><b>9️⃣ Advantages of Iterators</b></span>

✔ Memory efficient
✔ Lazy evaluation
✔ Work with infinite sequences
✔ Composable
✔ Streaming data processing
✔ No need to pre-store values

---

# <span style="color:#3498DB"><b>🔟 Constraints</b></span>

❌ One-time traversal (usually)
❌ No random access
❌ Cannot rewind
❌ Harder debugging
❌ Slight per-step overhead

---

# <span style="color:#8E44AD"><b>1️⃣1️⃣ Internal CPython View</b></span>

At C level:

Iterator objects implement:

```
tp_iter
tp_iternext
```

`next()` calls `tp_iternext`.

If NULL returned → StopIteration.

This makes iteration extremely efficient.

---

# <span style="color:#1ABC9C"><b>1️⃣2️⃣ Conceptual Model</b></span>

Iterable = Container
Iterator = Cursor

Think:

- Iterable → bookshelf
- Iterator → bookmark

Bookmark remembers position.

---

# <span style="color:#2E4053"><b>Final Ultra-Clean Summary</b></span>

- Iterator = object implementing `__iter__` and `__next__`.
- `__iter__()` returns self.
- `__next__()` returns next value or raises StopIteration.
- Iterable produces iterator.
- Generators are automatically iterators.
- Iterators enable lazy, memory-efficient computation.

---
