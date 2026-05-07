# **<span style="color:#ff1744">What is `ValidationInfo` in Pydantic?</span>**

---

## **<span style="color:#ff6f00">Definition</span>**

`ValidationInfo` is a special object passed to validators that provides:

```text id="vi1"
Context about the validation process
```

---

## **<span style="color:#3a86ff">What It Contains</span>**

```text id="vi2"
- data → already validated fields
- context → external data passed to validation
- field_name → current field
- config → model configuration
```

---

## **<span style="color:#8338ec">Key Idea</span>**

```text id="vi3"
Validators normally see only value
ValidationInfo gives "full awareness"
```

---

# **<span style="color:#ff1744">1. Why `ValidationInfo` Exists (Causality)</span>**

---

## **Problem Without It**

```text id="vi4"
Validator only knows:
- current field value

But sometimes we need:
- other fields
- external context
```

---

## **Example Problem**

```text id="vi5"
confirm_password must match password
```

---

## **Solution**

```text id="vi6"
Provide access to validation context via ValidationInfo
```

---

# **<span style="color:#ff1744">2. How to Use `ValidationInfo`</span>**

---

## **Basic Syntax**

```python
from pydantic import BaseModel, field_validator, ValidationInfo

class User(BaseModel):
    password: str
    confirm_password: str

    @field_validator("confirm_password")
    def check_password(cls, v, info: ValidationInfo):
        if v != info.data.get("password"):
            raise ValueError("Passwords do not match")
        return v
```

---

# **<span style="color:#ff1744">3. Internal Mechanics</span>**

---

# **<span style="color:#8338ec">Execution Flow</span>**

---

## **Step 1 — Input**

```python
User(password="abc", confirm_password="abc")
```

---

## **Step 2 — Field Parsing**

```text id="vi7"
password parsed first
```

---

## **Step 3 — Validator Called**

```text id="vi8"
confirm_password validator runs
```

---

## **Step 4 — `ValidationInfo` Passed**

```text id="vi9"
info.data = {"password": "abc"}
```

---

## **Step 5 — Comparison**

```text id="vi10"
confirm_password == password → OK
```

---

# **<span style="color:#ff1744">4. Key Attributes of `ValidationInfo`</span>**

---

## **<span style="color:#3a86ff">1. `info.data`</span>**

```text id="vi11"
Already validated fields
```

---

## **Example**

```python
info.data["password"]
```

---

## **<span style="color:#3a86ff">2. `info.context`</span>**

```text id="vi12"
External context passed during validation
```

---

## **Example**

```python
User.model_validate(data, context={"role": "admin"})
```

---

## **Usage**

```python
if info.context.get("role") == "admin":
    ...
```

---

## **<span style="color:#3a86ff">3. `info.field_name`</span>**

```text id="vi13"
Current field being validated
```

---

## **<span style="color:#3a86ff">4. `info.config`</span>**

```text id="vi14"
Model configuration
```

---

# **<span style="color:#ff1744">5. Important Behavior (Very Critical)</span>**

---

## **Order Matters**

```text id="vi15"
info.data only contains fields validated BEFORE current field
```

---

## **Example Problem**

```python
class User(BaseModel):
    confirm_password: str
    password: str
```

```text id="vi16"
password not available yet → validation fails
```

---

## **Solution**

```text id="vi17"
Ensure correct field order
OR use model_validator
```

---

# **<span style="color:#ff1744">6. Example with Context</span>**

---

```python
from pydantic import BaseModel, field_validator, ValidationInfo

class User(BaseModel):
    age: int

    @field_validator("age")
    def check_age(cls, v, info: ValidationInfo):
        if info.context and info.context.get("is_admin"):
            return v
        if v < 18:
            raise ValueError("Must be adult")
        return v
```

---

## **Usage**

```python
User.model_validate({"age": 16}, context={"is_admin": True})
```

---

## **Result**

```text id="vi18"
Validation passes because of context
```

---

# **<span style="color:#ff1744">7. When to Use `ValidationInfo`</span>**

---

## **<span style="color:#3a86ff">1. Cross-field validation (lightweight)</span>**

---

## **<span style="color:#3a86ff">2. Context-aware validation</span>**

---

## **<span style="color:#3a86ff">3. Conditional rules</span>**

---

## **<span style="color:#3a86ff">4. Dynamic validation behavior</span>**

---

# **<span style="color:#ff1744">8. When NOT to Use It</span>**

---

## **<span style="color:#3a86ff">1. Complex cross-field logic</span>**

```text id="vi19"
Use model_validator instead
```

---

## **<span style="color:#3a86ff">2. Simple constraints</span>**

```text id="vi20"
Use Field / Annotated
```

---

# **<span style="color:#ff1744">9. Best Practices</span>**

---

## **<span style="color:#3a86ff">1. Use only when needed</span>**

---

## **<span style="color:#3a86ff">2. Be aware of field order</span>**

---

## **<span style="color:#3a86ff">3. Prefer model_validator for complex logic</span>**

---

## **<span style="color:#3a86ff">4. Keep validators simple</span>**

---

# **<span style="color:#ff1744">10. Mental Model</span>**

---

```text id="vi21"
ValidationInfo = "context object for validation"
```

---

```text id="vi22"
value → current field
info → surrounding world
```

---

# **<span style="color:#ff1744">Ultimate Insight</span>**

---

```text id="vi23"
ValidationInfo bridges the gap between
isolated field validation and full model awareness
```

---

If you want deeper understanding, I can explain:

**exact execution order of fields + validators + model validators and how ValidationInfo evolves step by step (very useful for debugging complex validation flows).**
