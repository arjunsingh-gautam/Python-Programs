- Function object
- Execution frame
- Memory lifetime
- Why functions are callable
- How they differ from normal objects

This is Python runtime model level understanding.

---

# 1️⃣ Function Object — What It Actually Is

When you write:

```python
def f(x, y=10):
    return x + y
```

Python creates a **function object**.

It is:

```python
type(f)  →  <class 'function'>
```

So:

> A function is an instance of the built-in `function` class.

It is not syntax after definition — it is a full object in memory.

---

# 2️⃣ Internal Structure of a Function Object

Conceptually:

```
Function Object
 ├── __code__        (compiled bytecode object)
 ├── __globals__     (reference to global namespace dict)
 ├── __defaults__    (tuple of default argument values)
 ├── __kwdefaults__  (default keyword-only arguments)
 ├── __closure__     (captured free variables)
 ├── __annotations__ (type hints)
 ├── __dict__        (user-defined attributes)
 ├── __name__
 ├── __qualname__
 └── __doc__
```

Important distinction:

### 🔹 C-level stored attributes

These are stored in fixed slots of the function object (not inside `__dict__`):

- `__code__`
- `__globals__`
- `__defaults__`
- `__closure__`

### 🔹 Dynamic attributes

Stored inside:

```python
f.__dict__
```

Example:

```python
f.version = "1.0"
```

Now:

```python
f.__dict__ → {'version': '1.0'}
```

---

# 3️⃣ Memory Architecture Overview

There are 3 main layers involved when calling a function:

---

## 🔵 Layer 1 — Code Object (Persistent)

`f.__code__`

This contains:

- Bytecode instructions
- Variable names
- Constants
- Metadata

It is immutable and shared.

---

## 🔵 Layer 2 — Function Object (Persistent)

Stores:

- Reference to code object
- Default values
- Globals
- Closure
- Custom attributes

Lives as long as references exist.

Destroyed only when reference count becomes zero.

---

## 🔴 Layer 3 — Execution Frame (Temporary)

Created every time you call:

```python
f(5)
```

Frame contains:

- Local variables
- Parameters
- Stack for computation
- Instruction pointer
- Reference to globals
- Reference to code object

Destroyed after function returns.

---

# 4️⃣ Lifetime & Persistency

## What persists?

✔ Function object
✔ Code object
✔ Defaults
✔ Closure variables
✔ Function `__dict__`

## What does NOT persist?

❌ Local variables
❌ Parameters
❌ Temporary computation state

Those live inside the frame.

---

# 5️⃣ Visual Memory Flow

Before call:

```
Global Namespace
    f ─────────────► Function Object
                        ├── __code__
                        ├── __dict__
                        ├── __defaults__
```

During call:

```
Call Stack
   Frame
     x = 5
     y = 10
```

After return:

```
Frame destroyed
Function object unchanged
```

---

# 6️⃣ Why Default Arguments Persist

Example:

```python
def f(x, cache=[]):
    cache.append(x)
    return cache
```

`cache` is stored in:

```python
f.__defaults__
```

Which belongs to the function object.

So it persists across calls.

That’s why mutable default arguments behave unexpectedly.

---

# 7️⃣ What Makes Function Objects Special?

Functions differ from normal objects because:

### 🔹 They are CALLABLE

Normal object:

```python
class A:
    pass

a = A()
```

Calling:

```python
a()
```

Raises:

```
TypeError
```

Because `A` instances do not implement `__call__`.

---

# 8️⃣ Callable Nature of Function Objects

Every function object implements:

```python
f.__call__()
```

When you do:

```python
f(10)
```

Python internally does:

```python
f.__call__(10)
```

Under the hood:

1. `__call__` creates frame
2. Binds arguments
3. Executes bytecode
4. Returns result

---

# 9️⃣ Why Functions Are Callable (Internal Reason)

In CPython C structure:

Function type defines:

```
tp_call slot
```

The type object for functions has a `tp_call` pointer.

When Python sees:

```python
CALL_FUNCTION
```

It checks:

- Does object have callable slot?
- If yes → invoke it.

So callable behavior is defined at the **type level**, not instance level.

---

# 🔟 Making Any Object Callable

You can replicate function-like behavior:

```python
class A:
    def __call__(self, x):
        return x + 1

a = A()
a(5)   # works
```

Why?

Because class A defines `__call__`.

So:

> Callable = object with **call** method.

Functions just come with it built-in.

---

# 1️⃣1️⃣ How Functions Become Methods

When a function is defined inside a class:

```python
class A:
    def greet(self):
        pass
```

That function is stored in class dictionary.

When accessed via instance:

```python
a = A()
a.greet
```

Python triggers descriptor protocol:

- Function's `__get__`
- Creates a bound method object
- Attaches instance as first argument

So:

Function object → descriptor → method object

That is special behavior unique to function type.

---

# 1️⃣2️⃣ Difference from Simple Object

| Feature              | Function Object | Simple Object                |
| -------------------- | --------------- | ---------------------------- |
| Callable             | Yes (built-in)  | No (unless defines **call**) |
| Has code             | Yes             | No                           |
| Has execution frame  | Yes             | No                           |
| Has defaults storage | Yes             | No                           |
| Descriptor behavior  | Yes             | No                           |

Functions are specialized objects designed to represent executable code.

---

# 1️⃣3️⃣ Recursion & Frames

Each recursive call creates new frame.

Example:

```python
def f(n):
    if n == 0:
        return
    f(n-1)
```

Each call has separate frame.

But all calls use the same function object.

---

# 1️⃣4️⃣ Final Mental Model

A function consists of:

```
Function Object
    + Code Object
    + Metadata
    + Default values
    + Closure references
    + Custom attributes

Each call:
    → creates new execution frame
    → frame destroyed after return
```

Function object persists.
Frame does not.

---

# 1️⃣5️⃣ Ultra-Clean Summary

- Function is a first-class object.
- Callable behavior comes from type-level `__call__`.
- Execution creates temporary frame.
- Persistent data stored in function object.
- Frames are isolated per call.
- Descriptor protocol makes functions behave specially in classes.

---
