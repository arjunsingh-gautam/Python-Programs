# **<span style="color:#c1121f">Higher Order Functions in Python</span>**

`map`, `filter`, and `reduce` are called **higher-order functions** because they **operate on other functions**.

### Formal definition

A **higher-order function** is a function that does **at least one** of the following:

1. **Takes another function as an argument**
2. **Returns a function as its result**

`map`, `filter`, and `reduce` satisfy **condition #1**.

---

## 1️⃣ `map` — function as input

```python
map(func, iterable)
```

- `func` is a **function**
- `map` applies `func` to every element

```python
nums = [1, 2, 3]
result = list(map(lambda x: x * 2, nums))
```

Here:

- `lambda x: x * 2` is passed **as data**
- `map` **controls how and when** that function runs

➡️ **Function passed to another function → higher-order**

---

## 2️⃣ `filter` — function decides truth

```python
filter(predicate, iterable)
```

- `predicate` is a function returning `True/False`

```python
nums = [1, 2, 3, 4]
result = list(filter(lambda x: x % 2 == 0, nums))
```

`filter`:

- Calls your function
- Uses its result to decide inclusion

➡️ Again, **function passed as argument**

---

## 3️⃣ `reduce` — function defines accumulation logic

```python
reduce(func, iterable)
```

```python
from functools import reduce
nums = [1, 2, 3, 4]
result = reduce(lambda a, b: a + b, nums)
```

Here:

- `reduce` doesn’t know **how** to combine elements
- You **inject behavior** via a function

➡️ Behavior abstraction → higher-order

---

## Why this matters (conceptually)

Higher-order functions allow:

- **Abstraction of control flow**
- **Separation of “what” from “how”**
- **Reusable logic**

Example:

```python
# loop logic is abstracted
map(f, data)
filter(f, data)
reduce(f, data)
```

Instead of rewriting loops every time.

---

## Key intuition (important)

> **Functions are treated like values**
> They can be passed around just like:
>
> - integers
> - strings
> - objects

This is called **first-class functions**, and higher-order functions are built on top of that idea.

---

## One-line answer (interview-ready)

> `map`, `filter`, and `reduce` are called higher-order functions because they **take other functions as arguments and apply them to data**, abstracting the control flow.

---

# **<span style="#c1121f">User Defined Higher Order Function</span>**

A **user-defined Higher-Order Function (HOF)** is simply a function **you write yourself** that
✔️ **accepts another function as an argument** and/or
✔️ **returns a function**

---

## 1️⃣ HOF that **takes a function as argument**

### Example 1: Custom `apply`

```python
def apply(func, value):
    return func(value)

def square(x):
    return x * x

print(apply(square, 5))   # 25
```

✔️ `apply` is a **HOF** because it **receives a function** (`square`).

---

### Example 2: Custom `map`

```python
def my_map(func, iterable):
    result = []
    for item in iterable:
        result.append(func(item))
    return result

print(my_map(lambda x: x + 1, [1, 2, 3]))
# [2, 3, 4]
```

➡️ This is literally how `map` works internally.

---

## 2️⃣ HOF that **returns a function**

### Example 3: Function factory

```python
def power(n):
    def inner(x):
        return x ** n
    return inner

square = power(2)
cube = power(3)

print(square(4))  # 16
print(cube(4))    # 64
```

✔️ `power` is a **HOF** because it **returns another function**.

---

## 3️⃣ HOF that does **both**

### Example 4: Logger wrapper

```python
def logger(func):
    def wrapper(x):
        print("Calling function with:", x)
        return func(x)
    return wrapper

@logger
def double(x):
    return x * 2

print(double(5))
```

Output:

```
Calling function with: 5
10
```

➡️ This is the **foundation of decorators**.

---

## 4️⃣ Real-world useful HOF

### Example 5: Retry mechanism (very practical)

```python
def retry(func, times):
    def wrapper():
        for _ in range(times):
            try:
                return func()
            except Exception:
                pass
        raise Exception("Failed after retries")
    return wrapper
```

Usage:

```python
@retry(times=3)
def risky_operation():
    ...
```

✔️ Production-grade HOF usage.

---

## 5️⃣ Custom `filter` (interview-friendly)

```python
def my_filter(predicate, data):
    result = []
    for item in data:
        if predicate(item):
            result.append(item)
    return result

print(my_filter(lambda x: x % 2 == 0, [1, 2, 3, 4]))
# [2, 4]
```

---

## Mental model (important)

Think of HOFs as **behavior injectors**:

```text
Data  +  Behavior  →  Result
```

You pass:

- **data** (list, values)
- **behavior** (function)

---

## Interview one-liner

> A user-defined higher-order function is a function written by the programmer that **accepts functions as parameters or returns functions**, enabling abstraction and reusable control flow.

---

# **<span style="color:#c1121f">Why use in-built HOFs like `map,reduce,filter`?</span>**

> Built-in higher-order functions like `map`, `filter`, and `reduce` are used **instead of explicit loops** because they make code **more expressive, safer, more optimizable, and easier for both humans and the interpreter to reason about**.

Now let’s break this down **properly**, not just “clean code” talk.

---

## 1️⃣ Express _intent_, not _mechanism_

### Loop (mechanism-focused)

```python
result = []
for x in nums:
    if x % 2 == 0:
        result.append(x * 2)
```

You are telling Python **HOW** to do it:

- iterate
- check condition
- append

### HOF (intent-focused)

```python
result = list(map(lambda x: x * 2, filter(lambda x: x % 2 == 0, nums)))
```

You are telling Python **WHAT** you want:

- filter even numbers
- transform them

🔑 **Higher-level abstraction = clearer intent**

This matters in:

- large codebases
- fast-moving startups
- code reviews

---

## 2️⃣ Reduced surface area for bugs

### Loops are mutable and error-prone

Common loop bugs:

- forgetting to initialize list
- wrong append
- off-by-one errors
- modifying list while iterating

```python
for i in range(len(nums)):
    nums.append(nums[i] * 2)   # 💥 infinite loop bug
```

### HOFs are _controlled execution_

- No index handling
- No mutation during iteration
- No loop state exposure

```python
map(func, iterable)  # execution model is sealed
```

🔒 **Less control → fewer bugs**

---

## 3️⃣ Optimizable by the interpreter

This is important and often missed.

### Built-in HOFs are:

- Written in **C (CPython)**
- Highly optimized
- Use tight internal loops

Example:

```python
map(f, data)
```

Internally:

```c
while (iterator_has_next) {
    call_function_pointer();
}
```

Your Python loop:

```python
for x in data:
    f(x)
```

Has:

- Python bytecode per iteration
- Python-level variable lookup
- Python-level append

➡️ **HOFs reduce Python-level overhead**

⚠️ Note:

- `map/filter` are **not always faster**
- But they _allow_ optimizations

---

## 4️⃣ Lazy evaluation = memory efficiency

### Loops often materialize data

```python
result = []
for x in nums:
    result.append(f(x))
```

### HOFs are lazy (in Python 3)

```python
mapped = map(f, nums)   # no computation yet
```

Only computed when consumed:

```python
next(mapped)
```

Benefits:

- Lower memory usage
- Better for large data streams
- Works well with generators

---

## 5️⃣ Composability (pipeline style)

HOFs compose **naturally**:

```python
pipeline = map(
    normalize,
    filter(is_valid,
        map(parse, raw_data)
    )
)
```

This mirrors:

- functional pipelines
- dataflow graphs
- ML preprocessing steps

Loops don’t compose well without nesting or flags.

---

## 6️⃣ Separation of concerns (critical for scaling)

```python
map(func, data)
```

- `func` → business logic
- `map` → iteration strategy

Change business logic → loop untouched
Change iteration → logic untouched

This separation:

- simplifies testing
- improves refactoring
- enables reuse

---

## 7️⃣ Parallelization & vectorization potential

This is **future-proofing**.

Conceptually:

```python
map(f, data)
```

Can become:

- parallel map
- distributed map
- GPU map

Loops **hard-code sequential execution**.

This is why:

- Spark
- Ray
- Dask
- NumPy

all use map-like abstractions.

---

## 8️⃣ When loops are actually better (important!)

Be honest — interviews like this.

Use **loops** when:

- logic is complex with early exits
- multiple dependent conditions
- need fine-grained control
- performance profiling proves loop is faster

Example:

```python
for x in data:
    if x < 0:
        break
    if expensive_check(x):
        do_something()
```

This is NOT map/filter territory.

---

## Final mental model

| Loop             | HOF            |
| ---------------- | -------------- |
| HOW              | WHAT           |
| Mutable state    | Stateless      |
| Error-prone      | Safer          |
| Hard to optimize | Optimizable    |
| Sequential       | Parallelizable |

---

## Interview-ready answer (concise)

> Built-in higher-order functions like `map`, `filter`, and `reduce` are preferred over loops because they express intent clearly, reduce bugs, enable interpreter-level optimizations, support lazy evaluation, and compose well into data pipelines. Loops are still useful when control flow is complex or performance-critical.

---
