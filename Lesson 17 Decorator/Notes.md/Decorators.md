# <span style="color:#2E86C1"><b>Decorators in Python — Complete Deep Dive</b></span>

This will be a **system-level explanation** covering:

- What decorators really are
- Required boilerplate structure
- How they work internally
- Complete dry run
- Best practices
- When to use / avoid them

We go from syntax → runtime → design philosophy.

---

# <span style="color:#AF7AC5"><b>1️⃣ What Is a Decorator?</b></span>

A decorator is:

> A callable that takes a function and returns a new callable, usually modifying or extending the original function’s behavior.

At core:

```python
def decorator(func):
    def wrapper(*args, **kwargs):
        # extra behavior
        return func(*args, **kwargs)
    return wrapper
```

Decorator syntax:

```python
@decorator
def f():
    pass
```

Is equivalent to:

```python
f = decorator(f)
```

That’s it.

Everything else is design pattern.

---

# <span style="color:#48C9B0"><b>2️⃣ Why Decorators Exist</b></span>

Decorators solve:

- Cross-cutting concerns
- Logging
- Authentication
- Timing
- Validation
- Caching
- Access control

Without modifying original function logic.

They promote:

✔ Separation of concerns
✔ Reusability
✔ Clean architecture

---

# <span style="color:#E74C3C"><b>3️⃣ Essential Boilerplate Elements</b></span>

### 🔹 1. Outer Function (Decorator Function)

```python
def decorator(func):
```

- Receives the original function
- Should return a callable
- Often captures func in closure

Best practice:

- Use meaningful name (e.g., `log_calls`)
- Keep logic minimal here

---

### 🔹 2. Wrapper Function

```python
def wrapper(*args, **kwargs):
```

This is CRITICAL.

Why use `*args, **kwargs`?

Because:

- You don’t know original function signature
- Ensures compatibility
- Makes decorator reusable

Best practice:
✔ Always use `*args, **kwargs` unless specific signature needed

---

### 🔹 3. Calling Original Function

```python
result = func(*args, **kwargs)
```

Must forward arguments correctly.

Best practice:
✔ Return original result
✔ Don’t swallow return unless intentional

---

### 🔹 4. Return Wrapper

```python
return wrapper
```

Without returning wrapper, decorator fails.

---

### 🔹 5. Use functools.wraps (VERY IMPORTANT)

```python
from functools import wraps

def decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper
```

Why?

Without `wraps`:

- `__name__` becomes "wrapper"
- `__doc__` lost
- Debugging harder

Best practice:
✔ Always use `@wraps(func)`

---

# <span style="color:#5DADE2"><b>4️⃣ How Decoration Happens (Complete Mechanism)</b></span>

Example:

```python
from functools import wraps

def log_calls(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Calling function")
        result = func(*args, **kwargs)
        print("Function finished")
        return result
    return wrapper

@log_calls
def add(a, b):
    return a + b
```

---

## 🔹 Step-by-Step Execution at Definition Time

When Python reads:

```python
@log_calls
def add(a, b):
```

It performs:

### Step 1

Create function object for `add`.

### Step 2

Call decorator:

```python
add = log_calls(add)
```

Now:

- `add` refers to wrapper
- Original function is stored inside wrapper closure

---

## 🔹 Memory Diagram

```text
add ─────► wrapper function
              └── closure → original add
```

---

# <span style="color:#BB8FCE"><b>5️⃣ Execution Dry Run</b></span>

Now:

```python
add(3, 4)
```

Actually means:

```python
wrapper(3, 4)
```

Inside wrapper:

1. Print "Calling function"
2. Call original `func(3,4)`
3. Print "Function finished"
4. Return result

Final output:

```
Calling function
Function finished
7
```

---

# <span style="color:#F5B041"><b>6️⃣ Decorator With Arguments (Advanced)</b></span>

When decorator needs parameters:

```python
def repeat(times):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(times):
                func(*args, **kwargs)
        return wrapper
    return decorator
```

Usage:

```python
@repeat(3)
def greet():
    print("Hello")
```

Execution flow:

1. `repeat(3)` → returns decorator
2. decorator receives greet
3. returns wrapper
4. greet replaced by wrapper

So:

```python
greet = repeat(3)(greet)
```

Two layers involved.

---

# <span style="color:#58D68D"><b>7️⃣ When To Use Decorators</b></span>

✔ Logging
✔ Timing functions
✔ Authentication
✔ Input validation
✔ Caching
✔ Access control
✔ Retry logic
✔ Transaction management
✔ Rate limiting

Use when:

- You want to modify behavior consistently
- Without touching original function logic
- Across multiple functions

---

# <span style="color:#F39C12"><b>8️⃣ Best Practices</b></span>

### ✔ Always use functools.wraps

### ✔ Keep wrapper minimal

### ✔ Don’t hide errors unintentionally

### ✔ Preserve return values

### ✔ Use clear naming

### ✔ Avoid deep decorator stacking without documentation

### ✔ Consider function signature preservation (inspect.signature if needed)

---

# <span style="color:#EC7063"><b>9️⃣ When To Avoid Decorators</b></span>

❌ When logic becomes too complex
❌ When debugging becomes difficult
❌ When behavior becomes hidden and surprising
❌ When simple helper function is clearer
❌ When state management becomes messy

If decorator:

- Modifies too much logic
- Makes flow non-obvious
- Breaks readability

Avoid.

---

# <span style="color:#3498DB"><b>🔟 Common Mistakes</b></span>

### ❌ Forgetting return in wrapper

### ❌ Not forwarding arguments

### ❌ Not returning wrapper

### ❌ Not using wraps

### ❌ Modifying global state accidentally

---

# <span style="color:#8E44AD"><b>1️⃣1️⃣ Conceptual Model</b></span>

Decorator is:

> Higher-order function that transforms another function.

Equivalent to:

```python
f = decorator(f)
```

So decorator does not change original function.
It replaces the reference.

---

# <span style="color:#1ABC9C"><b>1️⃣2️⃣ Full Mechanism Summary</b></span>

1. Function object created.
2. Decorator called with that function.
3. Decorator returns wrapper.
4. Original name reassigned to wrapper.
5. Wrapper executes extra behavior.
6. Wrapper calls original via closure.
7. Wrapper returns result.

---

# <span style="color:#2E4053"><b>Ultra Clean Summary</b></span>

Decorators:

- Are syntactic sugar for function reassignment
- Use closures to remember original function
- Replace function reference with wrapper
- Modify behavior transparently
- Enable powerful abstraction
- Should be used carefully and cleanly

---

If you want next, we can explore:

- How multiple decorators stack internally
- Class-based decorators
- Descriptor interaction with decorators
- Async decorators
- Performance impact of decorators

You're now thinking at framework-design level.
