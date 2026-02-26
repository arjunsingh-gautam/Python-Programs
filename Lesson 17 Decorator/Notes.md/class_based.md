# <span style="color:#2E86C1"><b>Class-Based Decorators — Complete Deep Explanation</b></span>

We’ll cover:

1. What class-based decorators are
2. Boilerplate structure
3. Each required element and best practices
4. Full dry run mechanism
5. Parameterized class decorators
6. When to use them
7. Constraints & pitfalls

---

# <span style="color:#AF7AC5"><b>1️⃣ What Is a Class-Based Decorator?</b></span>

A class-based decorator is:

> A class whose instances are callable and are used to wrap functions.

Remember:

A decorator must be **callable**.

In function-based decorators:

- The decorator is a function returning a wrapper.

In class-based decorators:

- The decorator is a class.
- The class instance replaces the function.
- The class defines `__call__`.

---

# <span style="color:#48C9B0"><b>2️⃣ Basic Boilerplate Structure</b></span>

Minimal structure:

```python
class Decorator:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        # extra behavior
        return self.func(*args, **kwargs)
```

Usage:

```python
@Decorator
def greet():
    print("Hello")
```

Equivalent to:

```python
greet = Decorator(greet)
```

---

# <span style="color:#E74C3C"><b>3️⃣ Understanding Each Element</b></span>

## 🔹 `__init__(self, func)`

This runs at decoration time.

When Python reads:

```python
@Decorator
def greet():
```

It performs:

```python
greet = Decorator(greet)
```

So:

- `__init__` receives original function
- Stores it inside instance

Best practice:
✔ Always store original function (`self.func = func`)
✔ Avoid heavy logic in `__init__`
✔ Optionally use `functools.update_wrapper`

---

## 🔹 `__call__(self, *args, **kwargs)`

This runs at function call time.

When user calls:

```python
greet()
```

It actually calls:

```python
instance.__call__()
```

Best practice:
✔ Always forward arguments
✔ Always return original result unless intentional
✔ Keep logic minimal and readable

---

# <span style="color:#5DADE2"><b>4️⃣ Full Dry Run — Simple Example</b></span>

Example:

```python
from functools import update_wrapper

class Log:
    def __init__(self, func):
        self.func = func
        update_wrapper(self, func)   # preserve metadata

    def __call__(self, *args, **kwargs):
        print("Before call")
        result = self.func(*args, **kwargs)
        print("After call")
        return result


@Log
def add(a, b):
    return a + b
```

---

## 🔹 Step-by-Step Execution

### Step 1 — Function Definition

Python creates function object `add`.

---

### Step 2 — Decoration Happens

Decorator syntax:

```python
add = Log(add)
```

So:

- `Log.__init__(self, add)` runs
- `self.func = add`
- `add` now refers to instance of Log

Now memory:

```
add → Log instance
         └── func → original add function
```

---

### Step 3 — Call

```python
add(3, 4)
```

Actually calls:

```python
Log_instance.__call__(3,4)
```

Inside `__call__`:

1. Print "Before call"
2. Call original `self.func(3,4)`
3. Print "After call"
4. Return result

Output:

```
Before call
After call
7
```

---

# <span style="color:#BB8FCE"><b>5️⃣ Why Use Class-Based Decorators?</b></span>

They are useful when:

✔ You need persistent state
✔ You need multiple configuration fields
✔ Logic becomes complex
✔ You want cleaner separation

Example with state:

```python
class CountCalls:
    def __init__(self, func):
        self.func = func
        self.count = 0

    def __call__(self, *args, **kwargs):
        self.count += 1
        print(f"Call number {self.count}")
        return self.func(*args, **kwargs)
```

Now function remembers call count.

Harder to manage cleanly in simple function decorator.

---

# <span style="color:#F5B041"><b>6️⃣ Parameterized Class Decorator</b></span>

If decorator itself takes arguments:

```python
class Repeat:
    def __init__(self, times):
        self.times = times

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            for _ in range(self.times):
                func(*args, **kwargs)
        return wrapper
```

Usage:

```python
@Repeat(3)
def greet():
    print("Hello")
```

Flow:

1. Repeat(3) → creates instance
2. That instance receives `greet`
3. Returns wrapper
4. greet replaced by wrapper

So two-stage call:

```
Repeat(3)(greet)
```

---

# <span style="color:#58D68D"><b>7️⃣ Best Practices</b></span>

### ✔ Preserve Metadata

Use:

```python
from functools import update_wrapper
update_wrapper(self, func)
```

or:

```python
functools.wraps(func)
```

### ✔ Keep `__init__` Light

Heavy computation should not happen at decoration time.

### ✔ Always Forward Arguments Properly

Use `*args, **kwargs`

### ✔ Maintain Return Value

Unless intentional transformation.

### ✔ Avoid Hidden Side Effects

Decorators should not silently change core logic.

---

# <span style="color:#F39C12"><b>8️⃣ Constraints & Pitfalls</b></span>

❌ Without `update_wrapper`, metadata lost
❌ Harder to read than function-based decorator
❌ Can complicate debugging
❌ Stateful decorators may cause thread-safety issues
❌ More verbose

---

# <span style="color:#EC7063"><b>9️⃣ Class vs Function Decorator Comparison</b></span>

| Feature                  | Function Decorator | Class Decorator |
| ------------------------ | ------------------ | --------------- |
| Simplicity               | High               | Moderate        |
| Stateful                 | Harder             | Easier          |
| Readability              | Cleaner            | Verbose         |
| Good for simple wrapping | Yes                | Overkill        |
| Good for complex logic   | Limited            | Yes             |

---

# <span style="color:#3498DB"><b>🔟 When To Use Class-Based Decorators</b></span>

✔ You need persistent internal state
✔ Complex configuration
✔ Multiple helper methods
✔ Object-oriented design preference

Avoid when:

❌ Simple logging
❌ Small validation
❌ Quick wrapper logic

Function decorator is cleaner there.

---

# <span style="color:#2E4053"><b>Final Mental Model</b></span>

Function decorator:

```
f = decorator(f)
```

Class decorator:

```
f = Decorator(f)
```

Call time:

```
f(...) → instance.__call__(...)
```

Class-based decorator replaces function with an object that behaves like a function.

---
