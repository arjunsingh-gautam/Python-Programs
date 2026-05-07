# **<span style="color:#ff1744">Adding Constraints in Pydantic — The Pythonic Way</span>**

---

# **<span style="color:#ff6f00">1. Why Constraints Matter (Quick Context)</span>**

```text id="c0"
Validation is not just "type correctness"
It is also "value correctness"
```

Example:

```text id="c1"
age: int  → type is correct
age = -5 → logically invalid
```

---

# **<span style="color:#ff1744">2. The Most Pythonic Way — `Annotated` (Modern Best Practice)</span>**

---

## **<span style="color:#3a86ff">What is `Annotated`?</span>**

`Annotated` lets you attach **validation metadata** to a type:

```text id="c2"
Type + Constraints = Annotated
```

---

## **<span style="color:#3a86ff">Example</span>**

```python id="c3"
from typing import Annotated
from pydantic import BaseModel, Field

class User(BaseModel):
    age: Annotated[int, Field(gt=0, lt=120)]
```

---

## **<span style="color:#8338ec">Meaning</span>**

```text id="c4"
age must be:
> 0 and < 120
```

---

# **<span style="color:#ff1744">3. How `Annotated` Works (Mechanics)</span>**

---

## **Step-by-Step**

```text id="c5"
1. Python sees Annotated[int, Field(...)]
2. Extract base type → int
3. Extract metadata → Field constraints
4. Pydantic builds validation schema
5. During runtime:
    - Check type
    - Apply constraints
```

---

## **Internal View**

```text id="c6"
Annotated[T, metadata] → (T + validation rules)
```

---

## **Execution Flow**

```text id="c7"
Input → type check → constraint check → accept/reject
```

---

# **<span style="color:#ff1744">4. Why `Annotated` is Preferred</span>**

---

## **<span style="color:#3a86ff">Benefits</span>**

```text id="c8"
- Clean separation of type and validation
- Reusable constraints
- Better readability
- Compatible with typing ecosystem
```

---

## **Example Reusability**

```python id="c9"
Age = Annotated[int, Field(gt=0, lt=120)]

class User(BaseModel):
    age: Age
```

---

# **<span style="color:#ff1744">5. Other Ways to Add Constraints</span>**

---

# **<span style="color:#8338ec">A. Using `Field` (Classic Way)</span>**

```python id="c10"
class User(BaseModel):
    age: int = Field(gt=0, lt=120)
```

---

## **Mechanics**

```text id="c11"
Type → int
Constraints → stored in Field
```

---

## **Limitation**

```text id="c12"
Mixes type + validation → less clean than Annotated
```

---

# **<span style="color:#8338ec">B. Using Constrained Types (Old Style)</span>**

---

## **Example**

```python id="c13"
from pydantic import conint

class User(BaseModel):
    age: conint(gt=0, lt=120)
```

---

## **Mechanics**

```text id="c14"
conint creates a custom type with constraints
```

---

## **Problem**

```text id="c15"
Less readable, less flexible
Deprecated-style approach in modern usage
```

---

# **<span style="color:#8338ec">C. Using Validators (Custom Logic)</span>**

---

## **Example**

```python id="c16"
from pydantic import field_validator

class User(BaseModel):
    age: int

    @field_validator("age")
    def validate_age(cls, v):
        if v < 0:
            raise ValueError("Invalid age")
        return v
```

---

## **Use When**

```text id="c17"
Complex validation logic required
```

---

# **<span style="color:#ff1744">6. Types of Constraints You Can Add</span>**

---

## **<span style="color:#3a86ff">Numeric</span>**

```python id="c18"
Field(gt=0, ge=1, lt=100, le=99)
```

---

## **<span style="color:#3a86ff">String</span>**

```python id="c19"
Field(min_length=3, max_length=50, pattern="^[a-z]+$")
```

---

## **<span style="color:#3a86ff">List</span>**

```python id="c20"
Field(min_length=1, max_length=10)
```

---

## **<span style="color:#3a86ff">Decimal / Float</span>**

```python id="c21"
Field(gt=0, multiple_of=0.5)
```

---

# **<span style="color:#ff1744">7. Combining Constraints with `Annotated`</span>**

---

```python id="c22"
from typing import Annotated
from pydantic import BaseModel, Field

Price = Annotated[float, Field(gt=0)]

class Product(BaseModel):
    price: Price
```

---

# **<span style="color:#ff1744">8. Real Example (Complete)</span>**

```python id="c23"
from typing import Annotated
from pydantic import BaseModel, Field

class User(BaseModel):
    name: Annotated[str, Field(min_length=3, max_length=50)]
    age: Annotated[int, Field(gt=0, lt=120)]
```

---

## **Validation Flow**

```text id="c24"
1. Check name type → str
2. Check length
3. Check age type → int
4. Check range
5. Accept or raise error
```

---

# **<span style="color:#ff1744">9. When to Use Which Method</span>**

---

| Method            | Use Case                            |
| ----------------- | ----------------------------------- |
| Annotated         | Modern, clean, reusable constraints |
| Field             | Simple constraints                  |
| Validators        | Complex/custom logic                |
| Constrained types | Legacy / avoid                      |

---

# **<span style="color:#ff1744">10. Best Practices</span>**

---

## **<span style="color:#3a86ff">1. Prefer `Annotated`</span>**

```text id="c25"
Modern + clean + reusable
```

---

## **<span style="color:#3a86ff">2. Use Validators for Complex Rules</span>**

---

## **<span style="color:#3a86ff">3. Avoid Overcomplicating Types</span>**

---

## **<span style="color:#3a86ff">4. Reuse Constraint Types</span>**

---

# **<span style="color:#ff1744">11. Mental Model</span>**

---

```text id="c26"
Type hint → defines structure
Annotated → attaches rules
Pydantic → enforces rules
```

---

# **<span style="color:#ff1744">Ultimate Insight</span>**

---

```text id="c27"
Annotated turns type hints into powerful validation schemas
without breaking Python’s typing philosophy
```

---

If you want next level depth, I can explain:

**How Pydantic compiles these constraints into fast validation pipelines (very important for performance understanding).**
