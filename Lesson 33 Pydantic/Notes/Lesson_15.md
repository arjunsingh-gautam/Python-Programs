# **<span style="color:#ff1744">Why `Employee` Causes `NameError` Inside the Class Body</span>**

---

# **<span style="color:#ff6f00">1. The Problem</span>**

You wrote:

```python
def fullname(self: Employee) -> str:
```

inside:

```python
class Employee(BaseModel):
```

---

## **Why Error Happens?</span>**

```text id="fa1"
At the moment class body is executing,
Employee class does NOT fully exist yet
```

---

# **<span style="color:#ff1744">2. First-Principles Understanding</span>**

---

# **<span style="color:#8338ec">How Python Creates a Class</span>**

When Python sees:

```python
class Employee(BaseModel):
```

---

## **Execution Flow</span>**

```text id="fa2"
1. Create temporary class namespace (dictionary)

2. Execute EVERYTHING inside class body

3. Build class object from collected attributes/methods

4. Assign final class object to name "Employee"
```

---

# **<span style="color:#8338ec">Critical Insight</span>**

During step 2:

```text id="fa3"
Employee name is NOT bound yet
```

So this fails:

```python
self: Employee
```

because:

```text id="fa4"
Python tries to evaluate Employee immediately
but Employee does not exist yet
```

---

# **<span style="color:#ff1744">3. Solution 1 — Forward Reference Using String</span>**

---

# **<span style="color:#3a86ff">Correct Code</span>**

```python
class Employee(BaseModel):

    @computed_field
    @property
    def fullname(self: "Employee") -> str:
        return f"{self.firstname} {self.lastname}"
```

---

# **<span style="color:#ff1744">4. Mechanics of String Forward Reference</span>**

---

## **What Happens Internally?</span>**

Instead of:

```python
Employee
```

Python sees:

```python
"Employee"
```

which is just:

```text id="fa5"
A plain string literal
```

---

## **So During Class Creation</span>**

```text id="fa6"
Python does NOT evaluate it immediately
```

---

## **Later</span>**

Type checkers / libraries resolve it:

```text id="fa7"
"Employee" → actual Employee class
```

---

# **<span style="color:#8338ec">Internal Flow</span>**

```text id="fa8"
Class body execution
    ↓
Annotation stored as string
    ↓
Class fully created
    ↓
Later resolved to actual type
```

---

# **<span style="color:#ff1744">5. Solution 2 — Future Annotations (Modern Best Way)</span>**

---

# **<span style="color:#3a86ff">Code</span>**

```python
from __future__ import annotations
```

Then:

```python
class Employee(BaseModel):

    @computed_field
    @property
    def fullname(self: Employee) -> str:
        return f"{self.firstname} {self.lastname}"
```

---

# **<span style="color:#ff1744">6. Mechanics of `from __future__ import annotations`</span>**

---

## **What It Changes</span>**

Normally:

```python
self: Employee
```

means:

```text id="fa9"
Evaluate Employee immediately
```

---

## **With Future Import</span>**

Python automatically converts ALL annotations into strings internally.

So:

```python
self: Employee
```

becomes internally:

```python
self: "Employee"
```

---

# **<span style="color:#8338ec">Internal Transformation</span>**

```text id="fa10"
Before:
__annotations__ = {'self': Employee}

After future import:
__annotations__ = {'self': 'Employee'}
```

---

# **<span style="color:#ff1744">7. Why This Solves the Problem</span>**

---

Because:

```text id="fa11"
Strings can exist before actual class exists
```

Later:

```text id="fa12"
Type checker / Pydantic resolves them
```

---

# **<span style="color:#ff1744">8. Comparing Both Solutions</span>**

---

| Method                               | How it Works                              | Best Use                    |
| ------------------------------------ | ----------------------------------------- | --------------------------- |
| `"Employee"`                         | Manual string forward reference           | Small/simple cases          |
| `from __future__ import annotations` | Automatically stringifies all annotations | Modern recommended approach |

---

# **<span style="color:#ff1744">9. Internal Mechanics of Resolution</span>**

---

## **Later During Type Inspection</span>**

Libraries like:

- Pydantic
- mypy

call:

```python
typing.get_type_hints()
```

---

## **What Happens?</span>**

```text id="fa13"
1. Read string annotations
2. Look up actual class names in namespace
3. Replace strings with real types
```

---

# **<span style="color:#ff1744">10. Your Correct Code (Modern Best Practice)</span>**

```python
from __future__ import annotations

from pydantic import (
    BaseModel,
    computed_field
)

class Employee(BaseModel):
    firstname: str
    lastname: str
    monthly_salary: float = 0.0

    @computed_field
    @property
    def fullname(self: Employee) -> str:
        return f"{self.firstname} {self.lastname}"

    @computed_field
    @property
    def annual_salary(self: Employee) -> float:
        return self.monthly_salary * 12


e1 = Employee(
    firstname="John",
    lastname="Doe",
    monthly_salary=10000
)

print(e1.model_dump())
```

---

# **<span style="color:#ff1744">11. Important Insight About `self: Employee`</span>**

---

## **Technically Optional</span>**

You usually do NOT need:

```python
self: Employee
```

because Python already knows:

```text id="fa14"
self refers to instance of current class
```

---

## **Why Add It?</span>**

```text id="fa15"
- Better IDE support
- Better static analysis
- Documentation clarity
```

---

# **<span style="color:#ff1744">12. Mental Model</span>**

---

```text id="fa16"
During class creation:
Class name not ready yet

Forward reference delays resolution
until class fully exists
```

---

# **<span style="color:#ff1744">Ultimate Insight</span>**

---

```text id="fa17"
Forward references solve a timing problem:

Type annotation wants the class
before Python has finished creating the class
```
