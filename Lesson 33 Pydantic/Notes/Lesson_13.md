# **<span style="color:#ff1744">`model_validator` in Pydantic — Full Deep Dive</span>**

---

# **<span style="color:#ff6f00">1. What is a `model_validator`?</span>**

A `model_validator` is a function that:

```text
Validates the ENTIRE model (all fields together)
```

---

## **<span style="color:#3a86ff">Key Idea</span>**

```text
field_validator → works on ONE field
model_validator → works on WHOLE object
```

---

## **<span style="color:#3a86ff">Example</span>**

```python
from pydantic import BaseModel, model_validator

class User(BaseModel):
    password: str
    confirm_password: str

    @model_validator(mode="after")
    def check_passwords(self):
        if self.password != self.confirm_password:
            raise ValueError("Passwords do not match")
        return self
```

---

# **<span style="color:#ff1744">2. Why `model_validator` Exists (Causality)</span>**

---

## **Problem with Field Validators**

```text
Field validators only see ONE field at a time
```

---

## **Example Problem**

```text
password and confirm_password must match
```

---

## **Why field_validator fails**

```text
It cannot reliably access other fields (order issues)
```

---

## **Solution**

```text
Validate after full model is constructed
```

---

# **<span style="color:#ff1744">3. Difference: Field vs Model Validator</span>**

---

| Feature  | field_validator   | model_validator   |
| -------- | ----------------- | ----------------- |
| Scope    | Single field      | Entire model      |
| Input    | Value             | Model / dict      |
| Use case | Simple validation | Cross-field logic |
| Timing   | Per field         | Whole model stage |

---

# **<span style="color:#ff1744">4. Mechanics of `model_validator`</span>**

---

# **<span style="color:#8338ec">Validation Pipeline</span>**

```text
Raw input
   ↓
Field parsing
   ↓
Field validators
   ↓
Model construction
   ↓
model_validator
```

---

# **<span style="color:#8338ec">Step-by-Step Execution</span>**

---

## **Input**

```python
User(password="abc", confirm_password="abc")
```

---

## **Flow**

```text
1. Parse fields → password, confirm_password
2. Apply field validators (if any)
3. Create model instance
4. Call model_validator
5. Validate cross-field logic
6. Return model
```

---

# **<span style="color:#ff1744">5. Modes of `model_validator`</span>**

---

# **<span style="color:#8338ec">A. mode="before"</span>**

---

## **Meaning**

```text
Runs BEFORE model creation
Works on raw input dict
```

---

## **Example**

```python
@model_validator(mode="before")
def preprocess(cls, data):
    data["name"] = data["name"].strip()
    return data
```

---

## **Use Case**

```text
Input cleaning / transformation
```

---

# **<span style="color:#8338ec">B. mode="after"</span>**

---

## **Meaning**

```text
Runs AFTER model creation
Works on full model instance
```

---

## **Example**

```python
@model_validator(mode="after")
def validate(self):
    if self.a > self.b:
        raise ValueError("Invalid relation")
    return self
```

---

## **Use Case**

```text
Cross-field validation
```

---

# **<span style="color:#8338ec">C. mode="wrap"</span>**

---

## **Meaning**

```text
Wraps entire validation process
```

---

## **Example**

```python
@model_validator(mode="wrap")
def wrapper(cls, data, handler):
    print("Before validation")
    model = handler(data)
    print("After validation")
    return model
```

---

## **Use Case**

```text
Logging, debugging, advanced control
```

---

# **<span style="color:#ff1744">6. Example with Full Flow</span>**

```python
from pydantic import BaseModel, model_validator

class Order(BaseModel):
    price: float
    discount: float

    @model_validator(mode="after")
    def check_discount(self):
        if self.discount > self.price:
            raise ValueError("Discount cannot exceed price")
        return self
```

---

## **Execution**

```text
Input → parse fields → create model → run validator → return model
```

---

# **<span style="color:#ff1744">7. Syntax Summary</span>**

---

## **Before Mode**

```python
@model_validator(mode="before")
def func(cls, data: dict):
    return data
```

---

## **After Mode**

```python
@model_validator(mode="after")
def func(self):
    return self
```

---

## **Wrap Mode**

```python
@model_validator(mode="wrap")
def func(cls, data, handler):
    return handler(data)
```

---

# **<span style="color:#ff1744">8. Best Practices</span>**

---

## **<span style="color:#3a86ff">1. Use Field Validators First</span>**

```text
Use model_validator ONLY when necessary
```

---

## **<span style="color:#3a86ff">2. Keep Logic Focused</span>**

```text
One responsibility per validator
```

---

## **<span style="color:#3a86ff">3. Prefer mode="after" for Validation</span>**

---

## **<span style="color:#3a86ff">4. Always Return Data</span>**

```text
Return self or data
```

---

## **<span style="color:#3a86ff">5. Avoid Heavy Computation</span>**

---

## **<span style="color:#3a86ff">6. Use Clear Error Messages</span>**

---

# **<span style="color:#ff1744">9. Common Mistakes</span>**

---

## **Mistake 1 — Forgetting return**

---

## **Mistake 2 — Using field_validator for cross-field logic**

---

## **Mistake 3 — Wrong mode usage**

---

## **Mistake 4 — Mutating data incorrectly in before mode**

---

# **<span style="color:#ff1744">10. Use Cases</span>**

---

## **<span style="color:#3a86ff">1. Cross-field Validation</span>**

```text
password confirmation
date ranges
```

---

## **<span style="color:#3a86ff">2. Business Rules</span>**

```text
price vs discount
start_date < end_date
```

---

## **<span style="color:#3a86ff">3. Data Normalization</span>**

---

## **<span style="color:#3a86ff">4. Derived Fields</span>**

---

# **<span style="color:#ff1744">11. Mental Model</span>**

---

```text
field_validator → validate parts
model_validator → validate whole
```

---

```text
before → clean input
after → enforce rules
wrap → control pipeline
```

---

# **<span style="color:#ff1744">Ultimate Insight</span>**

---

```text
model_validator is where business logic lives
field_validator is where data correctness lives
```

---

If you want next-level mastery, I can explain:

**Execution order of multiple validators and how Pydantic builds full validation graph internally (very important for debugging complex models).**
