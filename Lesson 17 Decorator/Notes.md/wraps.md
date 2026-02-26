# <span style="color:#2E86C1"><b>`functools.wraps` — Deep Explanation & Mechanism</b></span>

We will cover:

1. What problem `wraps` solves
2. Internal mechanism
3. How it works under the hood
4. How it helps with multiple decorators
5. Why using it is best practice
6. Full dry run example

---

# <span style="color:#AF7AC5"><b>1️⃣ The Core Problem Without `wraps`</b></span>

Consider this decorator:

```python
def log(func):
    def wrapper(*args, **kwargs):
        print("Calling function")
        return func(*args, **kwargs)
    return wrapper
```

Use it:

```python
@log
def add(a, b):
    """Add two numbers"""
    return a + b
```

Now check:

```python
print(add.__name__)
print(add.__doc__)
```

Output:

```
wrapper
None
```

Problem:

- Original metadata is lost
- Debugging harder
- Documentation broken
- Introspection tools fail
- Stacked decorators become confusing

---

# <span style="color:#48C9B0"><b>2️⃣ What `wraps` Does</b></span>

Correct version:

```python
from functools import wraps

def log(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Calling function")
        return func(*args, **kwargs)
    return wrapper
```

Now:

```python
print(add.__name__)
print(add.__doc__)
```

Output:

```
add
Add two numbers
```

So `wraps` copies metadata from original function to wrapper.

---

# <span style="color:#E74C3C"><b>3️⃣ How `wraps` Works Internally</b></span>

`wraps` is just a decorator factory.

Simplified source idea:

```python
def wraps(wrapped):
    def decorator(wrapper):
        update_wrapper(wrapper, wrapped)
        return wrapper
    return decorator
```

So:

```python
@wraps(func)
def wrapper(...):
```

Is equivalent to:

```python
wrapper = wraps(func)(wrapper)
```

And inside that:

```python
update_wrapper(wrapper, func)
```

---

# <span style="color:#5DADE2"><b>4️⃣ What `update_wrapper` Copies</b></span>

By default, it copies:

- `__name__`
- `__module__`
- `__doc__`
- `__annotations__`
- `__qualname__`

And most importantly:

```python
wrapper.__wrapped__ = original_function
```

That `__wrapped__` attribute is CRUCIAL.

It allows introspection tools to trace back original function.

---

# <span style="color:#BB8FCE"><b>5️⃣ Why `__wrapped__` Is Important</b></span>

When multiple decorators are stacked:

```python
@decorator1
@decorator2
def f():
    pass
```

This becomes:

```python
f = decorator1(decorator2(f))
```

So actual structure:

```
f → wrapper1
       └── wrapper2
             └── original f
```

Without `wraps`, there is no reliable way to access original function.

With `wraps`:

Each wrapper stores:

```python
__wrapped__
```

So Python can unwrap step by step.

This is used by:

- inspect module
- help()
- debugging tools
- type checkers
- testing frameworks

---

# <span style="color:#F5B041"><b>6️⃣ Dry Run of Multiple Decorators</b></span>

Example:

```python
from functools import wraps

def deco1(func):
    @wraps(func)
    def wrapper1(*args, **kwargs):
        print("Deco1 Before")
        result = func(*args, **kwargs)
        print("Deco1 After")
        return result
    return wrapper1

def deco2(func):
    @wraps(func)
    def wrapper2(*args, **kwargs):
        print("Deco2 Before")
        result = func(*args, **kwargs)
        print("Deco2 After")
        return result
    return wrapper2

@deco1
@deco2
def greet():
    print("Hello")
```

Decoration time:

1. greet created.
2. greet = deco2(greet)
3. greet = deco1(greet)

So call stack becomes:

```
wrapper1
   calls wrapper2
        calls original greet
```

Call:

```python
greet()
```

Execution order:

```
Deco1 Before
Deco2 Before
Hello
Deco2 After
Deco1 After
```

Because wrappers chain.

---

# <span style="color:#58D68D"><b>7️⃣ How `wraps` Helps in This Chain</b></span>

Each wrapper contains:

```python
wrapper.__wrapped__ = original_func
```

So structure is:

```
wrapper1.__wrapped__ → wrapper2
wrapper2.__wrapped__ → original greet
```

So tools can unwrap:

```python
inspect.unwrap(greet)
```

Returns original function.

Without `wraps`, this breaks.

---

# <span style="color:#F39C12"><b>8️⃣ Why Using `wraps` Is Best Practice</b></span>

### ✔ Preserves Metadata

Documentation remains intact.

### ✔ Enables Introspection

Frameworks like Flask, FastAPI depend on metadata.

### ✔ Maintains Debugging Clarity

Stack traces are meaningful.

### ✔ Allows Unwrapping

Testing frameworks rely on `__wrapped__`.

### ✔ Maintains Signature (with inspect tools)

---

# <span style="color:#EC7063"><b>9️⃣ What Happens If You Don’t Use `wraps`?</b></span>

Problems:

- `__name__` becomes "wrapper"
- Multiple decorators create confusing metadata
- Tools break
- IDE autocomplete misbehaves
- Documentation incorrect

Especially dangerous in:

- Web frameworks
- CLI frameworks
- Testing libraries

---

# <span style="color:#3498DB"><b>🔟 Conceptual Mental Model</b></span>

Decorators replace function references.

`wraps` makes wrapper _impersonate_ original function.

It copies identity metadata and links original via `__wrapped__`.

Think of it as:

> Wrapper wearing the identity card of original function.

---

# <span style="color:#8E44AD"><b>1️⃣1️⃣ When Might You Avoid wraps?</b></span>

Almost never.

Only if:

- You intentionally want wrapper identity.
- You’re doing very low-level manipulation.

Otherwise:

✔ Always use wraps.

---

# <span style="color:#2E4053"><b>Final Ultra-Clean Summary</b></span>

- `wraps` is a decorator factory.
- It calls `update_wrapper`.
- Copies metadata from original to wrapper.
- Sets `__wrapped__` for unwrapping.
- Essential for stacked decorators.
- Required for clean, maintainable code.

---

# <span style="color:#2E86C1"><b>Yes — But Let’s State It Precisely</b></span>

Your statement:

> “wraps basically wraps original function metadata with wrapper function instead of its own”

You are **very close**, but let’s refine it into an exact technical statement.

---

## <span style="color:#AF7AC5"><b>What `wraps` Actually Does</b></span>

`functools.wraps`:

> Copies selected metadata from the original function onto the wrapper function
> and attaches a reference to the original via `__wrapped__`.

It does **not** replace the wrapper.
It modifies the wrapper.

---

## <span style="color:#48C9B0"><b>Without wraps</b></span>

```python
def deco(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper
```

After decoration:

```python
@deco
def greet():
    pass
```

Now:

```python
print(greet.__name__)
```

Output:

```
wrapper
```

Because `greet` now refers to the wrapper function object.

The original function object is hidden in closure.

---

## <span style="color:#E74C3C"><b>With wraps</b></span>

```python
from functools import wraps

def deco(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper
```

Now:

```python
print(greet.__name__)
```

Output:

```
greet
```

So what happened?

`wraps` copied:

- `__name__`
- `__doc__`
- `__module__`
- `__annotations__`
- `__qualname__`

From original → into wrapper.

And also set:

```python
wrapper.__wrapped__ = original_function
```

---

## <span style="color:#5DADE2"><b>Important Clarification</b></span>

It does **not**:

- Merge both identities
- Keep both metadata sets
- Replace wrapper’s code

It simply:

> Makes the wrapper look like the original function.

The wrapper still executes its own logic.

---

## <span style="color:#BB8FCE"><b>Precise Technical Description</b></span>

Instead of saying:

> wraps wraps original function metadata with wrapper

Better phrasing:

> wraps copies original function’s metadata onto the wrapper function and links the original function via the `__wrapped__` attribute.

---

## <span style="color:#F5B041"><b>Think of It Like This</b></span>

Without wraps:

```
Original Function → hidden
Wrapper → visible identity
```

With wraps:

```
Wrapper → visible identity
   but wearing original’s name badge
   and carrying a link to original
```

---

## <span style="color:#58D68D"><b>Why This Matters</b></span>

Tools like:

- inspect
- help()
- type checkers
- testing frameworks
- web frameworks

Rely on:

```python
__name__
__doc__
__annotations__
__wrapped__
```

Without wraps, these tools break or misbehave.

---

# <span style="color:#2E4053"><b>Final Correct Statement</b></span>

Yes — `wraps` makes the wrapper function inherit the original function’s metadata and attaches the original function reference to `__wrapped__`, so the wrapper behaves like the original in identity and introspection.

---
