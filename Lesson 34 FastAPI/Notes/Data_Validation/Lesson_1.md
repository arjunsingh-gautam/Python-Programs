# <span style="color:#2563eb">**Why Pydantic Schemas are Important in FastAPI**</span>

Pydantic schemas are one of the most important concepts in FastAPI.

They solve a massive engineering problem:

# <span style="color:#dc2626">**How do we trust and structure incoming/outgoing API data?**</span>

APIs constantly exchange data:

- request bodies
- query parameters
- database objects
- response payloads
- nested JSON structures

Without schemas:

- data becomes inconsistent
- validation becomes manual
- APIs become fragile
- security issues appear
- code becomes messy

Pydantic provides:

```text id="m1x7"
Structured,
validated,
typed,
predictable data models
```

---

# <span style="color:#2563eb">**What is a Pydantic Schema?**</span>

A schema is:

> A structured definition of data shape and validation rules.

Example:

```python id="q4v2"
from pydantic import BaseModel

class User(BaseModel):

    name: str
    age: int
```

This schema defines:

```text id="p8m5"
A valid User object must contain:
- name as string
- age as integer
```

---

# <span style="color:#2563eb">**Mental Model of Pydantic Schemas**</span>

Think of schemas as:

# <span style="color:#dc2626">**Data Contracts**</span>

They define:

```text id="t7x1"
What data is allowed
What data is forbidden
What format is expected
```

---

# <span style="color:#2563eb">**Why FastAPI Depends Heavily on Pydantic**</span>

FastAPI philosophy:

```text id="x2m8"
Type-driven API development
```

FastAPI uses schemas for:

| Purpose                  | Usage                  |
| ------------------------ | ---------------------- |
| Request validation       | Input checking         |
| Response serialization   | Output formatting      |
| Documentation generation | OpenAPI                |
| Type safety              | IDE support            |
| Security                 | Prevent malformed data |

---

# <span style="color:#2563eb">**Problem Without Pydantic**</span>

Without schemas:

```python id="n9v3"
@app.post("/users")
def create_user(data: dict):

    if "name" not in data:
        ...
```

Problems:

- manual validation
- repetitive code
- weak typing
- inconsistent API behavior
- hidden bugs

---

# <span style="color:#2563eb">**How Pydantic Solves This**</span>

```python id="a5m2"
class User(BaseModel):

    name: str
    age: int
```

FastAPI automatically:

- validates
- converts types
- rejects invalid data
- generates docs

---

# <span style="color:#2563eb">**Example Request Validation**</span>

## <span style="color:#16a34a">**Schema**</span>

```python id="r8x4"
class User(BaseModel):

    name: str
    age: int
```

---

## <span style="color:#16a34a">**Route**</span>

```python id="k3v7"
@app.post("/users")
def create_user(user: User):

    return user
```

---

## <span style="color:#16a34a">**Valid Request**</span>

```json id="p6m1"
{
  "name": "Arjun",
  "age": 22
}
```

Accepted.

---

## <span style="color:#16a34a">**Invalid Request**</span>

```json id="u4x9"
{
  "name": "Arjun",
  "age": "hello"
}
```

Automatically rejected.

---

# <span style="color:#2563eb">**Internal Mechanics of Pydantic in FastAPI**</span>

# <span style="color:#dc2626">**Request Lifecycle**</span>

```text id="f1m8"
HTTP Request
      ↓
JSON Parsing
      ↓
Pydantic Schema Validation
      ↓
Type Conversion
      ↓
Python Object Creation
      ↓
Route Function Execution
```

---

# <span style="color:#2563eb">**What Happens Internally**</span>

Request:

```json id="w2m5"
{
  "name": "Arjun",
  "age": 22
}
```

---

## <span style="color:#16a34a">**Step 1 — FastAPI Reads JSON**</span>

Converts request body into Python dictionary.

---

## <span style="color:#16a34a">**Step 2 — Pydantic Validates Fields**</span>

Checks:

```text id="z8x1"
name → string?
age → integer?
```

---

## <span style="color:#16a34a">**Step 3 — Pydantic Creates Model Object**</span>

```python id="n4v7"
User(
   name="Arjun",
   age=22
)
```

---

## <span style="color:#16a34a">**Step 4 — Route Receives Structured Object**</span>

```python id="t1m9"
user: User
```

instead of raw dictionary.

---

# <span style="color:#2563eb">**How to Design Pydantic Schemas for Different HTTP Requests**</span>

Different HTTP methods require different schema design strategies.

---

# <span style="color:#dc2626">**1. POST Request Schemas**</span>

POST usually creates new resource.

---

## <span style="color:#16a34a">**Design Principle**</span>

Include:

- required fields
- creation constraints

---

## <span style="color:#16a34a">**Example**</span>

```python id="q5x7"
class UserCreate(BaseModel):

    name: str
    email: str
    password: str
```

---

# <span style="color:#2563eb">**Why Separate Create Schema?**</span>

Creation needs:

- password
- required input fields

but response may not expose password.

---

# <span style="color:#dc2626">**2. Response Schemas**</span>

Never expose internal data directly.

---

## <span style="color:#16a34a">**Example**</span>

```python id="m8v4"
class UserResponse(BaseModel):

    id: int
    name: str
    email: str
```

---

## <span style="color:#16a34a">**Why Important?**</span>

Avoid leaking:

- passwords
- tokens
- internal metadata

---

# <span style="color:#dc2626">**3. PUT Request Schemas**</span>

PUT replaces entire resource.

---

## <span style="color:#16a34a">**Design Principle**</span>

Usually all fields required.

```python id="c7m1"
class UserUpdate(BaseModel):

    name: str
    email: str
```

---

# <span style="color:#dc2626">**4. PATCH Request Schemas**</span>

PATCH partially updates resource.

---

## <span style="color:#16a34a">**Design Principle**</span>

Fields optional.

```python id="j2v9"
from typing import Optional

class UserPatch(BaseModel):

    name: Optional[str] = None
    email: Optional[str] = None
```

---

# <span style="color:#2563eb">**Why Optional Fields?**</span>

PATCH may send only:

```json id="v3m8"
{
  "email": "new@mail.com"
}
```

Not entire object.

---

# <span style="color:#dc2626">**5. Query Parameter Schemas**</span>

Useful for filtering/pagination.

---

## <span style="color:#16a34a">**Example**</span>

```python id="b8x2"
class UserFilter(BaseModel):

    page: int = 1
    limit: int = 10
    active: bool = True
```

---

# <span style="color:#2563eb">**Design Principles of Pydantic Schemas**</span>

# <span style="color:#dc2626">**Most Important Engineering Principles**</span>

---

# <span style="color:#dc2626">**1. Separate Input and Output Schemas**</span>

Bad:

```python id="r4m7"
class User(BaseModel):
```

used everywhere.

Good:

```python id="d7x1"
UserCreate
UserUpdate
UserResponse
```

---

# <span style="color:#2563eb">**Why?**</span>

Different operations require different data shapes.

---

# <span style="color:#dc2626">**2. Never Expose Internal Fields**</span>

Bad:

```python id="x9m3"
password_hash
internal_notes
secret_key
```

in response schema.

---

# <span style="color:#dc2626">**3. Validate at Boundary Layer**</span>

Validation should happen:

```text id="u3v8"
Immediately when request enters system
```

Pydantic handles this perfectly.

---

# <span style="color:#dc2626">**4. Keep Schemas Focused**</span>

Bad:

```python id="m9x4"
Huge mega-schema with 50 fields
```

Better:

```python id="a2v7"
Small focused schemas
```

---

# <span style="color:#dc2626">**5. Use Nested Schemas**</span>

Good architecture.

---

# <span style="color:#2563eb">**Elaborate Example of Good Schema Design**</span>

# <span style="color:#dc2626">**Scenario: E-Commerce API**</span>

---

# <span style="color:#2563eb">**Folder Structure**</span>

```text id="f5x1"
project/
│
├── schemas/
│   ├── user.py
│   ├── product.py
│   └── order.py
│
├── routes/
├── services/
├── database/
└── main.py
```

---

# <span style="color:#2563eb">**user.py**</span>

```python id="m1k8"
from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):

    name: str
    email: EmailStr
    password: str

class UserResponse(BaseModel):

    id: int
    name: str
    email: EmailStr
```

---

# <span style="color:#2563eb">**product.py**</span>

```python id="q4v6"
class ProductResponse(BaseModel):

    id: int
    name: str
    price: float
```

---

# <span style="color:#2563eb">**order.py**</span>

```python id="t7x2"
from typing import List

class OrderItem(BaseModel):

    product_id: int
    quantity: int

class OrderCreate(BaseModel):

    user_id: int
    items: List[OrderItem]
```

---

# <span style="color:#2563eb">**Why This Design is Good**</span>

| Principle               | Benefit               |
| ----------------------- | --------------------- |
| Separated schemas       | Clean architecture    |
| Nested schemas          | Structured validation |
| Focused models          | Maintainability       |
| Input/output separation | Security              |
| Reusable components     | Scalability           |

---

# <span style="color:#2563eb">**How to Structure Project with Pydantic Schemas**</span>

Recommended architecture:

```text id="z7m3"
project/
│
├── routes/
├── schemas/
├── services/
├── repositories/
├── models/
├── database/
└── main.py
```

---

# <span style="color:#2563eb">**Role of Each Layer**</span>

| Layer        | Responsibility            |
| ------------ | ------------------------- |
| routes       | HTTP endpoints            |
| schemas      | Validation/data contracts |
| services     | Business logic            |
| repositories | DB access                 |
| models       | ORM/database models       |

---

# <span style="color:#2563eb">**Important Distinction: Schema vs Database Model**</span>

Very important.

---

## <span style="color:#16a34a">**Pydantic Schema**</span>

Used for:

- validation
- serialization
- API contracts

---

## <span style="color:#16a34a">**Database Model**</span>

Used for:

- database tables
- ORM mapping

They are NOT the same thing.

---

# <span style="color:#2563eb">**Best Practices**</span>

---

# <span style="color:#dc2626">**1. Use Strong Types**</span>

Good:

```python id="p8x4"
EmailStr
UUID
datetime
HttpUrl
```

instead of generic strings.

---

# <span style="color:#dc2626">**2. Add Validation Constraints**</span>

Example:

```python id="k3m7"
from pydantic import Field

age: int = Field(gt=0)
```

---

# <span style="color:#dc2626">**3. Avoid Using dict Everywhere**</span>

Bad:

```python id="v6t2"
data: dict
```

Schemas provide structure.

---

# <span style="color:#dc2626">**4. Use response_model in Routes**</span>

Example:

```python id="w1x5"
@app.get(
    "/users/{id}",
    response_model=UserResponse
)
```

Very important for output validation.

---

# <span style="color:#dc2626">**5. Reuse Nested Schemas**</span>

Avoid duplication.

---

# <span style="color:#2563eb">**Common Mistakes Beginners Make**</span>

---

# <span style="color:#dc2626">**1. One Schema for Everything**</span>

Bad design.

---

# <span style="color:#dc2626">**2. Returning ORM Objects Directly**</span>

Can expose hidden fields.

---

# <span style="color:#dc2626">**3. Using Optional Everywhere**</span>

Weakens validation.

---

# <span style="color:#dc2626">**4. Mixing DB Models and API Schemas**</span>

Creates tight coupling.

---

# <span style="color:#dc2626">**5. Putting Business Logic in Schemas**</span>

Schemas should validate structure, not execute workflows.

---

# <span style="color:#2563eb">**Coding Exercise to Strengthen Learning**</span>

# <span style="color:#dc2626">**Mini Student Management API**</span>

---

# <span style="color:#2563eb">**Requirements**</span>

---

## <span style="color:#16a34a">**1. Create Separate Schemas**</span>

Create:

```text id="x5m1"
StudentCreate
StudentResponse
StudentUpdate
```

---

## <span style="color:#16a34a">**2. Add Validation**</span>

Rules:

- age > 0
- email valid
- CGPA between 0 and 10

---

## <span style="color:#16a34a">**3. Create Nested Schema**</span>

Add:

```text id="n8v3"
Address schema
```

inside student.

---

## <span style="color:#16a34a">**4. Create Routes**</span>

Implement:

```text id="r2x7"
POST /students
GET /students/{id}
PATCH /students/{id}
```

---

## <span style="color:#16a34a">**5. Use response_model**</span>

Ensure password never returned.

---

# <span style="color:#2563eb">**Advanced Challenge**</span>

Implement:

- pagination schema
- authentication schemas
- generic API response wrapper
- nested order system
- schema inheritance
- custom validators

This exercise will deeply strengthen understanding of:

- API contract design
- validation architecture
- request/response separation
- scalable FastAPI structure
- professional backend engineering
