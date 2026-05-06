# **<span style="color:#ff1744">`TypedDict` in Python — What It Is, How It Works, and When to Use It</span>**

---

# **<span style="color:#ff6f00">1. What is `TypedDict`?</span>**

`TypedDict` lets you **describe the expected structure of a dictionary**:

```text id="td1"
Fixed keys + expected value types (shape typing for dicts)
```

---

## **<span style="color:#3a86ff">Basic Example</span>**

```python id="td2"
from typing import TypedDict

class User(TypedDict):
    name: str
    age: int

u: User = {"name": "Arj", "age": 25}
```

---

## **<span style="color:#8338ec">Key Idea</span>**

```text id="td3"
"Dict with a schema"
```

---

# **<span style="color:#ff1744">2. Why `TypedDict` Exists (Causality)</span>**

---

## **<span style="color:#3a86ff">Problem</span>**

```text id="td4"
Plain dicts are flexible but unsafe
No structure → easy to misuse keys/values
```

Example bug:

```python id="td5"
user = {"name": "Arj", "age": "25"}  # wrong type, unnoticed
```

---

## **<span style="color:#3a86ff">Solution</span>**

```text id="td6"
Add structure using TypedDict
```

---

# **<span style="color:#ff1744">3. Mechanics — How `TypedDict` Works</span>**

---

## **<span style="color:#8338ec">At Runtime</span>**

```text id="td7"
TypedDict is just a normal dict
No runtime enforcement
```

---

## **<span style="color:#8338ec">At Static Type Checking</span>**

Tools like mypy:

```text id="td8"
1. Read TypedDict definition
2. Check keys exist
3. Check value types
4. Raise errors if mismatch
```

---

## **<span style="color:#3a86ff">Example</span>**

```python id="td9"
user: User = {"name": "Arj", "age": "25"}  # ❌ type error
```

---

# **<span style="color:#ff1744">4. How It Checks Types</span>**

---

## **<span style="color:#8338ec">Static Checking Rules</span>**

```text id="td10"
1. Required keys must exist
2. Value types must match
3. Extra keys → usually error (depends on checker)
```

---

## **<span style="color:#3a86ff">Example</span>**

```python id="td11"
user: User = {"name": "Arj"}  # ❌ missing age
```

---

## **<span style="color:#3a86ff">Extra Key</span>**

```python id="td12"
user: User = {"name": "Arj", "age": 25, "email": "x"}  # ❌
```

---

# **<span style="color:#ff1744">5. Advanced Features</span>**

---

## **<span style="color:#8338ec">Optional Keys</span>**

```python id="td13"
from typing import TypedDict

class User(TypedDict, total=False):
    name: str
    age: int
```

```text id="td14"
Keys become optional
```

---

## **<span style="color:#8338ec">Partial Optional (Recommended)</span>**

```python id="td15"
from typing import TypedDict, NotRequired

class User(TypedDict):
    name: str
    age: NotRequired[int]
```

---

## **<span style="color:#8338ec">Nested TypedDict</span>**

```python id="td16"
class Address(TypedDict):
    city: str

class User(TypedDict):
    name: str
    address: Address
```

---

# **<span style="color:#ff1744">6. When to Use `TypedDict`</span>**

---

## **<span style="color:#3a86ff">1. Structured JSON-like Data</span>**

```text id="td17"
API responses
Config objects
Parsed JSON
```

---

## **<span style="color:#3a86ff">2. Lightweight Data Structures</span>**

```text id="td18"
When class is overkill
```

---

## **<span style="color:#3a86ff">3. Interfacing External Data</span>**

```text id="td19"
Data coming from outside system
```

---

## **<span style="color:#3a86ff">4. Readability for Dict-based APIs</span>**

---

# **<span style="color:#ff1744">7. When NOT to Use `TypedDict`</span>**

---

## **<span style="color:#3a86ff">1. Need Runtime Validation</span>**

```text id="td20"
TypedDict does NOT enforce at runtime
```

Use Pydantic instead.

---

## **<span style="color:#3a86ff">2. Behavior + Methods Required</span>**

```text id="td21"
TypedDict is just data, no methods
```

Use class/dataclass.

---

## **<span style="color:#3a86ff">3. Complex Domain Logic</span>**

```text id="td22"
Business logic belongs in classes
```

---

## **<span style="color:#3a86ff">4. Highly Dynamic Keys</span>**

```text id="td23"
TypedDict requires fixed keys
```

---

# **<span style="color:#ff1744">8. TypedDict vs Alternatives</span>**

---

| Feature            | TypedDict | Dataclass       | Pydantic        |
| ------------------ | --------- | --------------- | --------------- |
| Runtime validation | ❌        | ❌              | ✅              |
| Structure          | Dict-like | Object          | Object          |
| Performance        | Fast      | Fast            | Slightly slower |
| Use case           | JSON-like | Internal models | External data   |

---

# **<span style="color:#ff1744">9. Example — Real Scenario</span>**

---

## **Without TypedDict**

```python id="td24"
def process(data):
    print(data["name"])  # unsafe
```

---

## **With TypedDict**

```python id="td25"
class User(TypedDict):
    name: str
    age: int

def process(data: User):
    print(data["name"])
```

---

## **Benefit**

```text id="td26"
Static checker ensures correctness
```

---

# **<span style="color:#ff1744">10. Limitations</span>**

---

## **<span style="color:#8338ec">1. No Runtime Enforcement</span>**

```text id="td27"
Invalid data still passes at runtime
```

---

## **<span style="color:#8338ec">2. No Methods</span>**

```text id="td28"
Only structure, no behavior
```

---

## **<span style="color:#8338ec">3. Static Only</span>**

```text id="td29"
Depends on type checker
```

---

# **<span style="color:#ff1744">11. Analogy</span>**

---

## **TypedDict**

```text id="td30"
Blueprint for a dictionary
```

---

## **Runtime dict**

```text id="td31"
Actual building (may or may not follow blueprint)
```

---

## **Type checker**

```text id="td32"
Inspector checking blueprint compliance
```

---

# **<span style="color:#ff1744">12. Final Mental Model</span>**

---

```text id="td33"
TypedDict = structured dict definition (static)
```

---

# **<span style="color:#ff1744">Ultimate Insight</span>**

```text id="td34"
TypedDict improves clarity and correctness at development time,
but does NOT guarantee safety at runtime
```

---

If you want next level clarity, I can explain:

**TypedDict vs dataclass vs Pydantic with real backend/API examples (very important for interviews and production systems).**
