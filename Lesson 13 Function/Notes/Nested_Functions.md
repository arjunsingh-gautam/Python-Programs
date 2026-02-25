# <span style="color:#2E86C1"><b>Nested Functions — Scope, Lifetime & Binding Explained</b></span>

---

## <span style="color:#AF7AC5"><b>Short Answer</b></span>

When you define a function inside another function:

> It is created in the **local scope of the outer function**, not the global scope.

But its **lifetime depends on references**, not just scope.

Let’s go step by step.

---

## <span style="color:#48C9B0"><b>1️⃣ Where Is It Defined? (Scope)</b></span>

Example:

```python
def outer():
    def inner():
        return "Hello"
    print(inner)
```

Here:

- `inner` exists only inside the local scope of `outer`
- It is a **local variable of outer**
- It is NOT placed in the global namespace

If you try:

```python
outer()
print(inner)
```

You get:

```text
NameError
```

Because `inner` was never defined globally.

So:

> Nested function name lives in the local namespace of the outer function.

---

## <span style="color:#F5B041"><b>2️⃣ When Is It Created?</b></span>

Very important:

The inner function object is created **each time the outer function runs**.

Example:

```python
def outer():
    def inner():
        return 10
    return inner

f1 = outer()
f2 = outer()

print(f1 is f2)
```

Output:

```text
False
```

Each call creates a new function object.

So nested functions are:

- Not created at definition time of outer
- Created at execution time of outer

---

## <span style="color:#E74C3C"><b>3️⃣ Memory Architecture During Execution</b></span>

When `outer()` is called:

1. A stack frame is created
2. `inner` function object is created
3. `inner` is assigned to local variable name inside outer’s frame

Visual:

```
Call Stack Frame (outer)
   inner  ─────────► Function Object (inner)
```

When outer returns:

- Frame is destroyed
- But if `inner` is returned or referenced,
  it survives

---

## <span style="color:#5DADE2"><b>4️⃣ What If Outer Returns Inner?</b></span>

```python
def outer():
    x = 10
    def inner():
        return x
    return inner

f = outer()
print(f())
```

Here:

- `inner` escapes outer
- `x` survives via closure
- `inner` persists because `f` references it

Important:

The name `inner` inside outer is local.
But the function object can live beyond the scope.

Scope ≠ Lifetime.

---

## <span style="color:#BB8FCE"><b>5️⃣ Difference Between Scope and Lifetime</b></span>

| Concept  | Meaning                    |
| -------- | -------------------------- |
| Scope    | Where a name is accessible |
| Lifetime | How long an object exists  |

Inner function:

- Scope → local to outer
- Lifetime → depends on references

---

## <span style="color:#58D68D"><b>6️⃣ Why It Is Not Global</b></span>

Because Python uses lexical scoping.

When compiling:

```python
def outer():
    def inner():
        pass
```

The compiler treats `inner` as:

- A local variable name
- Bound during execution of outer

It is not inserted into:

```python
globals()
```

Check:

```python
print("inner" in globals())
```

Returns:

```text
False
```

---

## <span style="color:#F39C12"><b>7️⃣ Interaction With LEGB Rule</b></span>

Python name resolution follows:

LEGB:

- Local
- Enclosing
- Global
- Built-in

For inner function:

- Its own locals
- Enclosing (outer)
- Global
- Built-in

So inner sees outer’s variables.

But outer cannot see inner unless it is referenced.

---

## <span style="color:#EC7063"><b>8️⃣ Subtle Important Point</b></span>

The function definition inside outer is executed like any other statement.

So:

```python
def outer():
    print("Running outer")
    def inner():
        print("Inner created")
```

Inner is created only when outer runs.

Not at module import time.

---

## <span style="color:#3498DB"><b>9️⃣ Analogy</b></span>

Think of outer as a factory.

Every time you call it:

- It manufactures a new inner function.
- That inner function may carry some captured state.

If you don’t take the inner function outside,
it gets destroyed with the factory shutdown.

If you return it,
it continues to exist independently.

---

## <span style="color:#8E44AD"><b>🔟 Edge Case — Nested but Not Returned</b></span>

```python
def outer():
    def inner():
        return 10
    inner()
```

Here:

- inner exists only during execution
- After outer returns,
  inner is destroyed
- No reference remains

So it is garbage collected.

---

## <span style="color:#1ABC9C"><b>1️⃣1️⃣ Final Precise Answer</b></span>

When we define a function inside another:

- The inner function name is part of the **local scope of the outer function**.
- It is NOT global.
- It is created each time outer runs.
- It survives only if referenced outside.
- If it captures variables, those variables persist via closure.

---

# <span style="color:#2E4053"><b>Final One-Line Summary</b></span>

A nested function is locally scoped to the outer function at definition time, but its lifetime depends entirely on whether references to it escape the outer function.

---

# <span style="color:#2E86C1"><b>How a Returned Inner Function Still Works After Outer Frame Is Destroyed</b></span>

This is a very important conceptual milestone.

Your confusion is correct and healthy:

> If the outer function frame is destroyed,
> how can the inner function still execute and access its variables?

Let’s break this precisely.

---

## <span style="color:#AF7AC5"><b>1️⃣ The Core Example</b></span>

```python
def outer():
    x = 10
    def inner():
        return x
    return inner

f = outer()
print(f())   # 10
```

Question:

- Outer frame is destroyed.
- `x` lived in that frame.
- So how does `inner()` still know `x`?

---

## <span style="color:#48C9B0"><b>2️⃣ Critical Distinction: Frame vs Closure Storage</b></span>

When Python compiles `inner`, it sees:

> `x` is used but not defined locally.

So Python marks `x` as a **free variable**.

Instead of storing `x` as a normal local variable in the frame,
Python moves it into a **cell object**.

---

## <span style="color:#E74C3C"><b>3️⃣ What Is a Cell Object?</b></span>

A cell object is a small container that holds a reference to a variable.

Think of it like:

```text
Cell Object
   └── reference to x = 10
```

When `outer()` runs:

1. `x` is placed in a cell object.
2. `inner` stores a reference to that cell in `inner.__closure__`.

Check:

```python
f = outer()
print(f.__closure__)
```

You’ll see a tuple of cell objects.

So the value of `x` is no longer tied to the outer frame.

It lives inside the cell object.

---

## <span style="color:#5DADE2"><b>4️⃣ What Actually Gets Destroyed?</b></span>

After `outer()` returns:

- The outer **frame** is destroyed.
- But the **cell object is NOT destroyed**.
- Because `inner` still references it.

Objects are destroyed only when reference count becomes zero.

So:

Frame dies.
Cell survives.
Inner function survives.

---

## <span style="color:#BB8FCE"><b>5️⃣ Memory Diagram</b></span>

### During outer() execution:

```text
Call Stack Frame (outer)
    x = 10  → stored in cell
    inner  ─────────────► Function Object (inner)
                              └── __closure__ → (cell_x)
```

### After outer() returns:

```text
Frame destroyed

Global:
    f ─────────────► Function Object (inner)
                         └── __closure__ → (cell_x)
```

The cell remains alive because `inner` holds it.

---

## <span style="color:#F5B041"><b>6️⃣ How Name Resolution Works When f() Is Called</b></span>

When you call:

```python
f()
```

Python follows LEGB rule:

- Local
- Enclosing
- Global
- Built-in

Inside `inner()`:

`x` is not local.

Python checks:

Does this function have a closure?

Yes.

So it looks inside:

```python
f.__closure__
```

and retrieves `x` from cell.

So resolution is:

Local → Closure → Global → Built-in

Closure sits between local and global.

---

## <span style="color:#58D68D"><b>7️⃣ Important: Closure Is Part of Function Object</b></span>

When `inner` is returned:

It carries:

- `__code__`
- `__globals__`
- `__closure__`

Everything needed to execute independently.

So the inner function becomes self-contained.

It does not depend on outer frame anymore.

---

## <span style="color:#F39C12"><b>8️⃣ Why This Design Exists</b></span>

Because Python supports:

- First-class functions
- Higher-order functions
- Decorators
- Functional patterns

Without closures, returning inner functions would be impossible.

Closures extend variable lifetime beyond frame lifetime.

---

## <span style="color:#EC7063"><b>9️⃣ What If No Variable Is Captured?</b></span>

```python
def outer():
    def inner():
        return 10
    return inner
```

Now:

```python
f = outer()
print(f.__closure__)
```

Output:

```text
None
```

Because no free variables were captured.

In this case, inner does not need cell objects.

---

## <span style="color:#3498DB"><b>🔟 Analogy</b></span>

Imagine outer function creates a box.

Inside the box is a note: `x = 10`.

Before outer disappears, it hands the note to inner.

Now inner carries the note in its pocket.

Outer room is demolished.

Inner still has the note.

The pocket is the closure.

---

## <span style="color:#8E44AD"><b>1️⃣1️⃣ Key Insight</b></span>

The outer frame is destroyed.

But:

Captured variables are moved from frame storage into heap-allocated cell objects.

Those cell objects persist.

So inner remains executable.

---

# <span style="color:#2E4053"><b>Final Ultra-Precise Summary</b></span>

When an inner function is returned:

- Outer frame is destroyed.
- Captured variables are stored in cell objects.
- Inner function holds references to those cells via `__closure__`.
- On execution, name resolution checks closure after locals.
- As long as inner function exists, closure variables exist.

Closure extends variable lifetime beyond frame lifetime.

---

# <span style="color:#2E86C1"><b>Why an Inner Function Remains Executable After Being Returned</b></span>

This is the exact conceptual jump from “syntax understanding” to “runtime understanding.”

Your confusion is natural:

> If the inner function is defined inside the outer function,
> and the outer scope disappears,
> how can the inner function still execute?

Let’s break this with precision.

---

## <span style="color:#AF7AC5"><b>1️⃣ Definition Scope ≠ Execution Dependency</b></span>

When you define:

```python
def outer():
    def inner():
        return 10
    return inner
```

Two things happen:

1. `outer` is created at module load time.
2. `inner` is NOT created yet.

Important:

> The body of `outer` runs only when `outer()` is called.

So `inner` is created dynamically at runtime.

---

## <span style="color:#48C9B0"><b>2️⃣ What Happens When outer() Runs?</b></span>

When you call:

```python
f = outer()
```

Python:

1. Creates a new stack frame for `outer`
2. Executes its body
3. Executes the `def inner` statement

That `def inner` statement:

- Creates a new function object
- Assigns it to the local name `inner`

So now:

```text
outer frame
    inner → FunctionObject
```

Then:

```python
return inner
```

This returns the function object.

---

## <span style="color:#E74C3C"><b>3️⃣ The Crucial Point</b></span>

The function object for `inner`:

- Is a standalone object
- Contains:
  - `__code__`
  - `__globals__`
  - `__closure__` (if needed)

It does NOT depend on the outer frame anymore.

The outer frame is just where it was created.

Creation location ≠ execution requirement.

---

## <span style="color:#5DADE2"><b>4️⃣ Think of It Like Object Construction</b></span>

Example:

```python
def factory():
    return [1, 2, 3]
```

The list is created inside factory.

After factory returns:

The list still exists.

Why?

Because it was returned and stored in a variable.

Same logic:

The inner function object is created inside outer,
but once returned, it lives independently.

---

## <span style="color:#BB8FCE"><b>5️⃣ Why It Still Has Access to Outer Variables</b></span>

If inner uses outer variables:

```python
def outer():
    x = 10
    def inner():
        return x
    return inner
```

Then Python:

- Detects `x` is used by inner
- Creates a cell object
- Stores `x` inside that cell
- Attaches the cell to `inner.__closure__`

So inner carries everything needed.

Outer frame is no longer required.

---

## <span style="color:#58D68D"><b>6️⃣ Name Resolution After Return</b></span>

When you call:

```python
f = outer()
f()
```

Inside `inner`:

Python resolves names in this order:

1. Local
2. Closure (captured variables)
3. Global
4. Built-in

So `x` is resolved via the closure cell.

It does NOT search outer frame (which is gone).

---

## <span style="color:#F39C12"><b>7️⃣ Key Insight</b></span>

The outer frame is only needed to:

- Create the inner function object
- Prepare closure cells

After that, the inner function is self-contained.

It has:

- Executable bytecode
- References to globals
- References to captured variables

That’s sufficient to execute.

---

## <span style="color:#EC7063"><b>8️⃣ Deep Runtime View</b></span>

Function object structure contains:

- Pointer to code object
- Pointer to global namespace
- Tuple of closure cells

When you call `f()`:

1. Python creates new frame for `inner`
2. Loads its code
3. Loads closure references
4. Executes

No dependency on outer frame exists anymore.

---

## <span style="color:#3498DB"><b>9️⃣ Analogy</b></span>

Imagine:

Outer function is a workshop.

Inner function is a machine built inside it.

When outer returns:

The workshop closes.

But the machine is moved outside.

The machine carries:

- Its blueprint (code)
- Required parts (closure variables)

So it can still operate.

---

## <span style="color:#8E44AD"><b>🔟 Final Precise Explanation</b></span>

Inner remains executable because:

- It is compiled into a standalone function object.
- It contains its own code object.
- It carries references to globals.
- If needed, it carries closure cell references.
- Execution does not depend on the defining frame.

The defining scope matters only at creation time.

Not at execution time.

---

# <span style="color:#2E4053"><b>Ultra Clean Summary</b></span>

An inner function remains executable after being returned because it becomes an independent function object carrying all necessary execution context (code, globals, and closure references). The outer frame is only required for creation, not for execution.

---
