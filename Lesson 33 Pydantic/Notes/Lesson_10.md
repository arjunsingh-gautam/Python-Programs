# **<span style="color:#ff1744">What is `default_factory`?</span>**

---

## **<span style="color:#ff6f00">Definition</span>**

`default_factory` is a mechanism used in:

- `dataclasses`
- Pydantic

to define:

```text
A function that is called to generate a default value at object creation time
```

---

## **<span style="color:#3a86ff">Key Idea</span>**

```text
default → value
default_factory → function that produces value
```

---

# **<span style="color:#ff1744">1. Why `default_factory` Exists (Causality)</span>**

---

## **Problem 1 — Dynamic Values**

```python
created_at = datetime.now()
```

```text
Evaluated once → same value reused
```

---

## **Problem 2 — Mutable Defaults**

```python
items = []
```

```text
Shared across all instances → bugs
```

---

## **Solution**

```text
Delay value creation until object instantiation
```

---

# **<span style="color:#ff1744">2. Difference: `default` vs `default_factory`</span>**

---

| Feature       | `default`           | `default_factory`  |
| ------------- | ------------------- | ------------------ |
| Type          | Value               | Function           |
| Execution     | At class definition | At object creation |
| Dynamic?      | ❌ No               | ✅ Yes             |
| Mutable safe? | ❌ No               | ✅ Yes             |

---

# **<span style="color:#ff1744">3. Example — The Problem with `default`</span>**

---

## **Wrong Code**

```python
from datetime import datetime
from pydantic import BaseModel

class Blog(BaseModel):
    created_at: datetime = datetime.now()
```

---

## **What Happens**

```text
datetime.now() runs once
All objects get same timestamp
```

---

# **<span style="color:#ff1744">4. Correct Code Using `default_factory`</span>**

```python
from datetime import datetime, UTC
from pydantic import BaseModel, Field

class Blog(BaseModel):
    created_at: datetime = Field(default_factory=lambda: datetime.now(tz=UTC))
```

---

## **Behavior**

```text
Each instance gets fresh timestamp
```

---

# **<span style="color:#ff1744">5. Internal Mechanics of `default_factory`</span>**

---

# **<span style="color:#8338ec">Step-by-Step Execution</span>**

---

## **Step 1 — Class Definition**

```text
Store function reference (lambda)
DO NOT execute it
```

---

## **Step 2 — Object Creation**

```python
blog = Blog()
```

---

## **Step 3 — Field Resolution**

```text
1. Check if value provided → No
2. Check default_factory → Yes
3. Call function
4. Assign returned value
```

---

## **Step 4 — Result**

```text
created_at gets new value each time
```

---

# **<span style="color:#ff1744">6. Dry Run Example</span>**

---

```python
b1 = Blog()
sleep(2)
b2 = Blog()
```

---

## **Execution Flow**

```text
b1 → lambda() → datetime.now() → T1
b2 → lambda() → datetime.now() → T2
```

---

## **Result**

```text
T1 ≠ T2
```

---

# **<span style="color:#ff1744">7. Example with Mutable Default (Critical)</span>**

---

## **Wrong**

```python
from dataclasses import dataclass

@dataclass
class Cart:
    items: list = []
```

---

## **Problem**

```text
All instances share SAME list
```

---

## **Correct**

```python
from dataclasses import dataclass, field

@dataclass
class Cart:
    items: list = field(default_factory=list)
```

---

## **Now**

```text
Each instance gets new list
```

---

# **<span style="color:#ff1744">8. How `default_factory` Works Internally</span>**

---

## **Conceptual Model**

```text
default → stored value
default_factory → stored callable
```

---

## **Execution Model**

```text
on object creation:
    if value missing:
        call default_factory()
        assign result
```

---

## **Pseudo Code**

```text
if field_value not provided:
    if default_factory exists:
        value = default_factory()
```

---

# **<span style="color:#ff1744">9. Use Cases of `default_factory`</span>**

---

## **<span style="color:#3a86ff">1. Timestamps</span>**

```python
default_factory=datetime.now
```

---

## **<span style="color:#3a86ff">2. Unique IDs</span>**

```python
import uuid
default_factory=uuid.uuid4
```

---

## **<span style="color:#3a86ff">3. Mutable Objects</span>**

```python
default_factory=list
default_factory=dict
```

---

## **<span style="color:#3a86ff">4. Random Values</span>**

```python
default_factory=random.random
```

---

## **<span style="color:#3a86ff">5. Derived Defaults</span>**

```python
default_factory=lambda: compute_value()
```

---

# **<span style="color:#ff1744">10. `lambda` vs Direct Function</span>**

---

## **Simple Case**

```python
default_factory=list
```

---

## **With Arguments**

```python
default_factory=lambda: datetime.now(tz=UTC)
```

---

# **<span style="color:#ff1744">11. Common Mistakes</span>**

---

## **Mistake 1 — Calling function immediately**

```python
default_factory=datetime.now()  # ❌ wrong
```

---

## **Correct**

```python
default_factory=datetime.now
```

---

## **Mistake 2 — Using mutable default**

```python
items = []  # ❌
```

---

## **Mistake 3 — Confusing default with factory**

```text
default → static
default_factory → dynamic
```

---

# **<span style="color:#ff1744">12. Analogy</span>**

---

## **default**

```text
Prepared food stored once
Everyone gets same portion
```

---

## **default_factory**

```text
Chef cooks fresh food for each order
```

---

# **<span style="color:#ff1744">13. Final Mental Model</span>**

---

```text
default → "use this value"
default_factory → "call this function to get value"
```

---

# **<span style="color:#ff1744">Ultimate Insight</span>**

---

```text
If default depends on time, randomness, or mutation:
→ NEVER use default
→ ALWAYS use default_factory
```

---

If you want next level clarity, I can explain:

**Why mutable defaults break Python functions and how this connects deeply with memory model and object references (very important concept).**
