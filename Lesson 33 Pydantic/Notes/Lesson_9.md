# **<span style="color:#ff1744">The Core Problem — Why `datetime.now()` Fails in Pydantic Fields</span>**

---

## **<span style="color:#ff6f00">What You Expect</span>**

```python
created_at = datetime.now(tz=UTC)
```

You expect:

```text
Each new BlogPost → new timestamp
```

---

## **<span style="color:#ff1744">What Actually Happens</span>**

```text
datetime.now() is executed ONLY ONCE
→ at class definition time
```

So:

```text
All instances get SAME timestamp
```

---

# **<span style="color:#ff1744">Why This Happens (First Principles)</span>**

---

## **Python Class Creation Phase**

When Python sees:

```python
class BlogPost(BaseModel):
    created_at: datetime = datetime.now(tz=UTC)
```

---

## **Execution Flow**

```text
1. Class body executes immediately
2. datetime.now() runs ONCE
3. Result stored as default value
4. That same value reused for all instances
```

---

## **Key Insight**

```text
Default values are evaluated at definition time, not instantiation time
```

---

# **<span style="color:#ff1744">Correct Solution — Delayed Execution</span>**

We need:

```text
Call function at object creation time
NOT at class definition time
```

---

# **<span style="color:#ff6f00">Using `default_factory` (Pydantic Way)</span>**

```python
from datetime import datetime, UTC
from pydantic import BaseModel, Field

class BlogPost(BaseModel):
    created_at: datetime = Field(default_factory=lambda: datetime.now(tz=UTC))
```

---

# **<span style="color:#ff1744">How `lambda` Solves the Problem</span>**

---

## **Instead of Value**

```python
created_at = datetime.now()
```

---

## **We Provide Function**

```python
default_factory = lambda: datetime.now()
```

---

## **Key Difference**

```text
Value → executed immediately
Function → executed later (on demand)
```

---

# **<span style="color:#ff1744">Internal Mechanics of `default_factory`</span>**

---

## **Step-by-Step Execution</span>**

---

## **Step 1 — Class Definition**

```text
Store lambda function reference (NOT executed)
```

---

## **Step 2 — Object Creation**

```python
post = BlogPost()
```

---

## **Step 3 — Pydantic Initialization</span>**

```text
1. Detect missing field (created_at)
2. Check for default_factory
3. Call the function
4. Assign result to field
```

---

## **Step 4 — Result**

```text
Each instance gets fresh datetime
```

---

# **<span style="color:#ff1744">Dry Run Example</span>**

---

```python
post1 = BlogPost()
sleep(2)
post2 = BlogPost()
```

---

## **Execution**

```text
post1 → lambda() → datetime.now() → T1
post2 → lambda() → datetime.now() → T2
```

---

## **Result**

```text
T1 ≠ T2 (correct behavior)
```

---

# **<span style="color:#ff1744">Where `functools.partial` Fits</span>**

---

## **Same Idea — Deferred Execution**

```python
from functools import partial

created_at = Field(default_factory=partial(datetime.now, tz=UTC))
```

---

## **What `partial` Does**

```text
Creates a new function with preset arguments
```

---

## **Equivalent to**

```python
lambda: datetime.now(tz=UTC)
```

---

## **Mechanics**

```text
partial(datetime.now, tz=UTC)
→ returns callable
→ called later by Pydantic
```

---

# **<span style="color:#ff1744">Why This Pattern Works (Core Principle)</span>**

---

## **Immediate Execution vs Deferred Execution**

---

### ❌ Immediate

```python
value = datetime.now()
```

```text
Executed NOW
```

---

### ✅ Deferred

```python
value = lambda: datetime.now()
```

```text
Executed LATER
```

---

# **<span style="color:#ff1744">Mental Model</span>**

---

## **Think of it like this**

```text
Without lambda:
→ "Give me the time NOW"

With lambda:
→ "Give me a machine that tells time when I ask"
```

---

# **<span style="color:#ff1744">Common Mistake</span>**

---

```python
created_at = Field(default=datetime.now())
```

---

## **Problem**

```text
Still evaluated immediately
```

---

## **Correct**

```python
created_at = Field(default_factory=datetime.now)
```

OR

```python
created_at = Field(default_factory=lambda: datetime.now(tz=UTC))
```

---

# **<span style="color:#ff1744">Why Pydantic Uses `default_factory`</span>**

---

## **Design Principle**

```text
Separate:
- static defaults (values)
- dynamic defaults (functions)
```

---

## **So**

```text
default → static value
default_factory → dynamic value
```

---

# **<span style="color:#ff1744">Final Mental Model</span>**

---

```text
Class definition time:
    store function

Instance creation time:
    execute function
    assign result
```

---

# **<span style="color:#ff1744">Ultimate Insight</span>**

---

```text
Whenever default depends on "current state" (time, random, UUID):

NEVER store value
ALWAYS store a function
```

---

If you want deeper clarity, I can show:

**How this same concept applies to dataclasses (`default_factory`) and why mutable defaults break in Python (very important concept).**
