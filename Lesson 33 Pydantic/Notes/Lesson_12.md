# **<span style="color:#ff1744">Field Validators in Pydantic — Deep Dive (Mechanics + Patterns)</span>**

---

# **<span style="color:#ff6f00">1. What is a Field Validator?</span>**

A **field validator** is a function that:

```text id="fv1"
Intercepts a field’s value during model creation
→ validates / transforms it
→ returns a clean value (or raises an error)
```

---

## **<span style="color:#3a86ff">Basic Example</span>**

```python
from pydantic import BaseModel, field_validator

class User(BaseModel):
    age: int

    @field_validator("age")
    def validate_age(cls, v):
        if v < 0:
            raise ValueError("Age must be positive")
        return v
```

---

# **<span style="color:#ff1744">2. Where Validators Sit in the Pipeline</span>**

---

## **Full Validation Flow**

```text id="fv2"
Raw input
   ↓
Type parsing / coercion
   ↓
Field validators
   ↓
Model creation
```

---

## **Key Insight**

```text id="fv3"
Validators are hooks inside Pydantic’s validation pipeline
```

---

# **<span style="color:#ff1744">3. Internal Mechanics (Step-by-Step)</span>**

---

## **Input**

```python
User(age="25")
```

---

## **Execution Flow**

```text id="fv4"
1. Read schema (age: int)
2. Parse input → "25" → 25
3. Call validator(validate_age)
4. Check condition (25 >= 0)
5. Return value
6. Store in model
```

---

## **If Invalid**

```python
User(age=-5)
```

```text id="fv5"
Validator raises ValueError
→ Pydantic wraps into ValidationError
```

---

# **<span style="color:#ff1744">4. Syntax of Field Validators</span>**

---

## **Basic Syntax**

```python
@field_validator("field_name")
def validator_name(cls, value):
    ...
    return value
```

---

## **Multiple Fields**

```python
@field_validator("age", "salary")
def validate_positive(cls, v):
    if v < 0:
        raise ValueError("Must be positive")
    return v
```

---

## **Accessing Other Fields**

```python
from pydantic import BaseModel, field_validator

class User(BaseModel):
    password: str
    confirm_password: str

    @field_validator("confirm_password")
    def check_match(cls, v, info):
        if v != info.data["password"]:
            raise ValueError("Passwords do not match")
        return v
```

---

# **<span style="color:#ff1744">5. Validator Modes (Very Important)</span>**

Pydantic v2 introduces **modes**:

---

# **<span style="color:#8338ec">A. `mode="before"`</span>**

---

## **Meaning**

```text id="fv6"
Runs BEFORE type conversion
```

---

## **Example**

```python
@field_validator("age", mode="before")
def convert_str(cls, v):
    if isinstance(v, str):
        return int(v)
    return v
```

---

## **Use Case**

```text id="fv7"
Preprocessing raw input
```

---

# **<span style="color:#8338ec">B. `mode="after"` (default)</span>**

---

## **Meaning**

```text id="fv8"
Runs AFTER type parsing
```

---

## **Example**

```python
@field_validator("age")
def validate_age(cls, v):
    if v < 0:
        raise ValueError("Invalid age")
    return v
```

---

## **Use Case**

```text id="fv9"
Validation on clean typed data
```

---

# **<span style="color:#8338ec">C. `mode="wrap"`</span>**

---

## **Meaning**

```text id="fv10"
Wraps entire validation process
```

---

## **Example**

```python
@field_validator("age", mode="wrap")
def wrap_validator(cls, v, handler):
    print("Before validation")
    result = handler(v)
    print("After validation")
    return result
```

---

## **Use Case**

```text id="fv11"
Logging, instrumentation, advanced control
```

---

# **<span style="color:#ff1744">6. Example Combining Modes</span>**

```python
from pydantic import BaseModel, field_validator

class User(BaseModel):
    age: int

    @field_validator("age", mode="before")
    def preprocess(cls, v):
        return int(v)

    @field_validator("age")
    def validate(cls, v):
        if v < 0:
            raise ValueError("Invalid age")
        return v
```

---

## **Execution**

```text id="fv12"
"25" → preprocess → 25 → validate → OK
```

---

# **<span style="color:#ff1744">7. Common Use Cases</span>**

---

## **<span style="color:#3a86ff">1. Data Cleaning</span>**

```python
strip whitespace, normalize strings
```

---

## **<span style="color:#3a86ff">2. Range Checks</span>**

---

## **<span style="color:#3a86ff">3. Cross-field Validation</span>**

---

## **<span style="color:#3a86ff">4. Type Normalization</span>**

---

# **<span style="color:#ff1744">8. Best Practices</span>**

---

## **<span style="color:#3a86ff">1. Use `Annotated` for Simple Constraints</span>**

```text id="fv13"
Avoid validator if Field(...) is enough
```

---

## **<span style="color:#3a86ff">2. Keep Validators Pure</span>**

```text id="fv14"
No side effects
```

---

## **<span style="color:#3a86ff">3. Always Return Value</span>**

```text id="fv15"
Missing return breaks validation
```

---

## **<span style="color:#3a86ff">4. Use `before` for Parsing, `after` for Validation</span>**

---

## **<span style="color:#3a86ff">5. Keep Logic Small & Focused</span>**

---

## **<span style="color:#3a86ff">6. Avoid Heavy Computation</span>**

```text id="fv16"
Validation should be fast
```

---

# **<span style="color:#ff1744">9. Common Mistakes</span>**

---

## **Mistake 1 — Not returning value**

```python
def validate(cls, v):
    if v < 0:
        raise ValueError()
```

---

## **Mistake 2 — Using validator instead of Field**

```text id="fv17"
Overengineering simple checks
```

---

## **Mistake 3 — Wrong mode usage**

```text id="fv18"
Using after when raw input handling needed
```

---

# **<span style="color:#ff1744">10. Mental Model</span>**

---

```text id="fv19"
Field Validator = checkpoint in data pipeline
```

---

```text id="fv20"
before → clean input
after → validate data
wrap → control entire process
```

---

# **<span style="color:#ff1744">Ultimate Insight</span>**

---

```text id="fv21"
Field validators are NOT the first tool —
they are the precise tool when constraints are not enough
```

---

If you want next-level depth, I can explain:

**model validators vs field validators and how validation order works internally across entire model (very important for complex systems).**
