# **<span style="color:#ff1744">What is Serialization in Pydantic?</span>**

---

# **<span style="color:#ff6f00">1. Definition</span>**

Serialization means:

```text id="sr1"
Converting Python objects/models into transferable formats
```

Usually:

```text id="sr2"
Python object
    ↓
dict / JSON
```

---

# **<span style="color:#ff1744">2. Why Serialization Exists (Causality)</span>**

---

## **Problem</span>**

Python objects cannot directly:

```text id="sr3"
- travel over network
- be stored in databases/files
- be sent as API responses
```

---

## **Solution</span>**

Convert them into:

```text id="sr4"
JSON-compatible structures
```

---

# **<span style="color:#ff1744">3. Serialization in Pydantic</span>**

---

## **Main Methods</span>**

| Method              | Output      |
| ------------------- | ----------- |
| `model_dump()`      | Python dict |
| `model_dump_json()` | JSON string |

---

# **<span style="color:#ff1744">4. Basic Example</span>**

```python id="sr5"
from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int

u = User(name="Arj", age=25)

print(u.model_dump())
```

---

## **Output</span>**

```python id="sr6"
{
    "name": "Arj",
    "age": 25
}
```

---

# **<span style="color:#ff1744">5. Internal Mechanics of Serialization</span>**

---

# **<span style="color:#8338ec">Step-by-Step Flow</span>**

---

## **Step 1 — Read Model Fields</span>**

Pydantic inspects:

```text id="sr7"
name
age
```

---

## **Step 2 — Extract Values</span>**

```text id="sr8"
u.name
u.age
```

---

## **Step 3 — Convert Complex Types</span>**

Examples:

```text id="sr9"
datetime → ISO string
Enum → value
nested model → dict
```

---

## **Step 4 — Produce Serializable Structure</span>**

---

# **<span style="color:#ff1744">6. Important Serialization Rules</span>**

---

# **<span style="color:#8338ec">A. Nested Models Serialize Recursively</span>**

---

## **Example</span>**

```python id="sr10"
class Address(BaseModel):
    city: str

class User(BaseModel):
    name: str
    address: Address
```

---

## **Serialization</span>**

```python id="sr11"
u.model_dump()
```

---

## **Result</span>**

```python id="sr12"
{
    "name": "Arj",
    "address": {
        "city": "Mumbai"
    }
}
```

---

## **Mechanics</span>**

```text id="sr13"
Recursive traversal of nested models
```

---

# **<span style="color:#8338ec">B. Datetime Serialization</span>**

---

## **Example</span>**

```python id="sr14"
from datetime import datetime

created_at: datetime
```

---

## **Serialized As</span>**

```text id="sr15"
ISO formatted string
```

---

# **<span style="color:#8338ec">C. Enum Serialization</span>**

---

## **Configurable</span>**

```python id="sr16"
use_enum_values=True
```

---

# **<span style="color:#8338ec">D. Computed Fields Included</span>**

If marked:

```python id="sr17"
@computed_field
```

they appear in dump.

---

# **<span style="color:#ff1744">7. Important Serialization Options</span>**

---

# **<span style="color:#8338ec">exclude_none=True</span>**

---

## **Example</span>**

```python id="sr18"
u.model_dump(exclude_none=True)
```

---

## **Purpose</span>**

```text id="sr19"
Removes fields with None
```

---

# **<span style="color:#8338ec">exclude_unset=True</span>**

---

## **Purpose</span>**

```text id="sr20"
Only serialize fields explicitly provided
```

---

# **<span style="color:#8338ec">exclude_defaults=True</span>**

---

## **Purpose</span>**

```text id="sr21"
Skip default-valued fields
```

---

# **<span style="color:#8338ec">by_alias=True</span>**

---

## **Purpose</span>**

Serialize using aliases.

---

# **<span style="color:#ff1744">8. Detailed Example — Good Serialization Design</span>**

---

```python id="sr22"
from datetime import datetime
from pydantic import BaseModel, Field, ConfigDict

class Address(BaseModel):
    city: str
    country: str

class User(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True
    )

    full_name: str = Field(alias="fullName")
    age: int
    address: Address
    created_at: datetime | None = None
```

---

# **Object Creation</span>**

```python id="sr23"
u = User(
    fullName="Arj",
    age=25,
    address={
        "city": "Mumbai",
        "country": "India"
    }
)
```

---

# **Serialization</span>**

```python id="sr24"
u.model_dump(
    by_alias=True,
    exclude_none=True
)
```

---

# **Output</span>**

```python id="sr25"
{
    "fullName": "Arj",
    "age": 25,
    "address": {
        "city": "Mumbai",
        "country": "India"
    }
}
```

---

# **<span style="color:#ff1744">9. Internal Execution Mechanics (Detailed Dry Run)</span>**

---

# **<span style="color:#8338ec">Step 1 — Start Serialization</span>**

```text id="sr26"
Call model_dump()
```

---

# **<span style="color:#8338ec">Step 2 — Traverse Fields</span>**

```text id="sr27"
full_name
age
address
created_at
```

---

# **<span style="color:#8338ec">Step 3 — Apply Serialization Rules</span>**

---

## **Alias Rule</span>**

```text id="sr28"
full_name → fullName
```

---

## **Exclude None Rule</span>**

```text id="sr29"
created_at skipped
```

---

## **Nested Model Rule</span>**

```text id="sr30"
address recursively serialized
```

---

# **<span style="color:#8338ec">Step 4 — Final Dict Returned</span>**

---

# **<span style="color:#ff1744">10. Best Serialization Practices</span>**

---

# **<span style="color:#8338ec">1. Serialize API-Friendly Structures</span>**

```text id="sr31"
Prefer JSON-compatible types
```

---

# **<span style="color:#8338ec">2. Use Aliases for External APIs</span>**

```text id="sr32"
Internal names ≠ external names
```

---

# **<span style="color:#8338ec">3. Avoid Exposing Internal Fields</span>**

Use:

```python id="sr33"
exclude=True
```

---

# **<span style="color:#8338ec">4. Use `exclude_none=True`</span>**

```text id="sr34"
Cleaner payloads
```

---

# **<span style="color:#8338ec">5. Keep Serialization Deterministic</span>**

```text id="sr35"
Same model → same output
```

---

# **<span style="color:#8338ec">6. Separate Internal vs External Models</span>**

---

## **Reason</span>**

```text id="sr36"
Internal structures should not leak
```

---

# **<span style="color:#ff1744">11. Different Serialization Design Practices</span>**

---

# **<span style="color:#8338ec">A. Public API Serialization</span>**

```text id="sr37"
Strict
clean
exclude sensitive data
```

---

# **<span style="color:#8338ec">B. Database Serialization</span>**

```text id="sr38"
Preserve all fields
```

---

# **<span style="color:#8338ec">C. Event Serialization</span>**

```text id="sr39"
Stable schema
version-safe
```

---

# **<span style="color:#8338ec">D. Logging Serialization</span>**

```text id="sr40"
Human-readable
```

---

# **<span style="color:#ff1744">12. Common Mistakes</span>**

---

## **Mistake 1 — Exposing secrets</span>**

---

## **Mistake 2 — Serializing huge nested objects blindly</span>**

---

## **Mistake 3 — Mixing internal and external schemas</span>**

---

## **Mistake 4 — Not handling datetime consistently</span>**

---

# **<span style="color:#ff1744">13. Mental Model</span>**

---

```text id="sr41"
Validation:
external → safe internal object

Serialization:
internal object → safe external representation
```

---

# **<span style="color:#ff1744">Ultimate Insight</span>**

---

```text id="sr42"
Serialization is not just conversion —
it is controlled exposure of structured information
```
