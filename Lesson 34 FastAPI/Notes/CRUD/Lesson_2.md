# <span style="color:#2563eb">**What is the Difference Between PUT and PATCH?**</span>

Both:

```http id="m1x7"
PUT
PATCH
```

are HTTP methods used for:

# <span style="color:#dc2626">**Updating existing resources**

But they differ fundamentally in:

- semantics
- intent
- update strategy
- API design philosophy

This distinction is extremely important in proper REST API design.

---

# <span style="color:#2563eb">**Core Difference**</span>

| Method | Meaning                   |
| ------ | ------------------------- |
| PUT    | Replace entire resource   |
| PATCH  | Partially modify resource |

---

# <span style="color:#2563eb">**Most Important Mental Model**</span>

# <span style="color:#dc2626">**PUT = Replace**

# <span style="color:#dc2626">**PATCH = Modify**

---

# <span style="color:#2563eb">**Feynman Analogy**</span>

Imagine updating a student form.

Current student:

```json id="q4v2"
{
  "name": "Arjun",
  "age": 22,
  "city": "Mumbai"
}
```

---

# <span style="color:#dc2626">**PUT Analogy**</span>

PUT means:

```text id="p8m5"
Submit entirely new student form
replacing old one completely
```

If field missing:

it may be removed/reset.

---

# <span style="color:#dc2626">**PATCH Analogy**</span>

PATCH means:

```text id="t7x1"
Only change specific fields
without touching others
```

Example:

```json id="x2m8"
{
  "city": "Pune"
}
```

Only city changes.

---

# <span style="color:#2563eb">**Understanding PUT in Detail**</span>

# <span style="color:#dc2626">**PUT Semantics**</span>

PUT represents:

> Full replacement of resource state.

---

# <span style="color:#2563eb">**PUT Example**</span>

Suppose existing user:

```json id="n9v3"
{
  "name": "Arjun",
  "age": 22,
  "city": "Mumbai"
}
```

---

# <span style="color:#dc2626">**PUT Request**</span>

```http id="a5m2"
PUT /users/1
```

Body:

```json id="r8x4"
{
  "name": "Rahul",
  "age": 25,
  "city": "Pune"
}
```

---

# <span style="color:#2563eb">**Meaning**</span>

```text id="k3v7"
Replace old resource entirely
with this new version
```

---

# <span style="color:#2563eb">**Important PUT Property**</span>

PUT expects:

# <span style="color:#dc2626">**Complete representation of resource**

---

# <span style="color:#2563eb">**Potential Danger**</span>

Suppose request body:

```json id="p6m1"
{
  "name": "Rahul"
}
```

If implemented strictly:

old fields may disappear:

```json id="u4x9"
{
  "name": "Rahul"
}
```

Age/city lost.

Because PUT means replacement.

---

# <span style="color:#2563eb">**Understanding PATCH in Detail**</span>

# <span style="color:#dc2626">**PATCH Semantics**</span>

PATCH represents:

> Partial modification of resource.

---

# <span style="color:#2563eb">**PATCH Example**</span>

Current user:

```json id="f1m8"
{
  "name": "Arjun",
  "age": 22,
  "city": "Mumbai"
}
```

---

# <span style="color:#dc2626">**PATCH Request**</span>

```http id="w2m5"
PATCH /users/1
```

Body:

```json id="z8x1"
{
  "city": "Pune"
}
```

---

# <span style="color:#2563eb">**Result**</span>

```json id="n4v7"
{
  "name": "Arjun",
  "age": 22,
  "city": "Pune"
}
```

Only specified fields change.

---

# <span style="color:#2563eb">**Key Concept**</span>

PATCH modifies:

# <span style="color:#dc2626">**Subset of resource state**

---

# <span style="color:#2563eb">**Deep REST Design Semantics**</span>

This difference exists because HTTP methods encode:

# <span style="color:#dc2626">**Intent**

not just mechanics.

---

# <span style="color:#2563eb">**PUT Intent**</span>

```text id="t1m9"
Here is the new complete state
of resource
```

---

# <span style="color:#2563eb">**PATCH Intent**</span>

```text id="q5x7"
Apply these specific modifications
to existing resource
```

---

# <span style="color:#2563eb">**Another Important Difference — Idempotency**</span>

# <span style="color:#dc2626">**What is Idempotency?**</span>

An operation is idempotent if:

```text id="m8v4"
Repeating it multiple times
produces same result
```

---

# <span style="color:#2563eb">**PUT is Idempotent**</span>

Example:

```http id="c7m1"
PUT /users/1
```

with:

```json id="j2v9"
{
  "name": "Rahul"
}
```

Repeated 100 times:

same final state.

---

# <span style="color:#2563eb">**PATCH May or May Not Be Idempotent**</span>

Depends on implementation.

Example:

```json id="v3m8"
{
  "increment_views": 1
}
```

Repeated calls change state repeatedly.

Not idempotent.

---

# <span style="color:#2563eb">**PUT vs PATCH According to REST Principles**</span>

| Principle            | PUT           | PATCH        |
| -------------------- | ------------- | ------------ |
| Resource replacement | Yes           | No           |
| Partial updates      | No            | Yes          |
| Requires full object | Usually yes   | No           |
| Idempotent           | Yes           | Usually      |
| Semantics            | Replace state | Modify state |

---

# <span style="color:#2563eb">**When to Use PUT**</span>

Use PUT when:

---

# <span style="color:#dc2626">**1. Replacing Entire Resource**</span>

Example:

```text id="b8x2"
Full profile update
```

---

# <span style="color:#dc2626">**2. Client Knows Full Resource State**</span>

Client sends entire object confidently.

---

# <span style="color:#dc2626">**3. Strict REST Semantics Important**</span>

---

# <span style="color:#dc2626">**4. Resource Synchronization Systems**</span>

Example:

```text id="r4m7"
Sync local state with server
```

---

# <span style="color:#2563eb">**When to Use PATCH**</span>

Use PATCH when:

---

# <span style="color:#dc2626">**1. Partial Updates Needed**</span>

Most common real-world case.

---

# <span style="color:#dc2626">**2. Large Resources Exist**</span>

Avoid resending entire object.

---

# <span style="color:#dc2626">**3. UI Updates Small Fields Frequently**</span>

Example:

```text id="d7x1"
Change profile picture only
```

---

# <span style="color:#dc2626">**4. Sparse Modifications**</span>

Only few fields change.

---

# <span style="color:#2563eb">**Why PATCH Became Important**</span>

Without PATCH:

clients had to:

```text id="x9m3"
Fetch full resource
      ↓
Modify locally
      ↓
PUT full object back
```

Inefficient and risky.

PATCH solves this elegantly.

---

# <span style="color:#2563eb">**How This Affects Pydantic Schema Design**</span>

Very important.

---

# <span style="color:#dc2626">**PUT Schema Design**</span>

Usually:

# <span style="color:#dc2626">**All fields required**

Example:

```python id="u3v8"
class UserUpdate(BaseModel):

    name: str
    age: int
    city: str
```

---

# <span style="color:#2563eb">**Why?**</span>

PUT expects full replacement.

---

# <span style="color:#dc2626">**PATCH Schema Design**</span>

Usually:

# <span style="color:#dc2626">**All fields optional**

Example:

```python id="m9x4"
from typing import Optional

class UserPatch(BaseModel):

    name: Optional[str] = None
    age: Optional[int] = None
    city: Optional[str] = None
```

---

# <span style="color:#2563eb">**Why?**</span>

PATCH updates only provided fields.

---

# <span style="color:#2563eb">**FastAPI PUT Example**</span>

```python id="a2v7"
@app.put("/users/{id}")
def replace_user(
    id: int,
    data: UserUpdate,
    db: Session = Depends(get_db)
):

    user = db.get(User, id)

    user.name = data.name
    user.age = data.age
    user.city = data.city

    db.commit()

    return user
```

---

# <span style="color:#2563eb">**FastAPI PATCH Example**</span>

```python id="f5x1"
@app.patch("/users/{id}")
def patch_user(
    id: int,
    data: UserPatch,
    db: Session = Depends(get_db)
):

    user = db.get(User, id)

    if data.name is not None:
        user.name = data.name

    if data.age is not None:
        user.age = data.age

    if data.city is not None:
        user.city = data.city

    db.commit()

    return user
```

---

# <span style="color:#2563eb">**Mental Model for API Design**</span>

---

# <span style="color:#dc2626">**PUT Mental Model**</span>

```text id="m1k8"
"Here is the entire new version
of resource"
```

---

# <span style="color:#dc2626">**PATCH Mental Model**</span>

```text id="q4v6"
"Apply these modifications
to existing resource"
```

---

# <span style="color:#2563eb">**Real-World Industry Practice**</span>

In practice:

- many APIs misuse PUT for partial updates
- PATCH semantics sometimes ignored

But good API design should preserve proper intent.

Modern systems increasingly prefer:

# <span style="color:#dc2626">**PATCH for partial updates**

because most UI interactions modify only few fields.

---

# <span style="color:#2563eb">**Important Engineering Insight**</span>

HTTP methods are not merely syntax.

They encode:

# <span style="color:#dc2626">**Behavioral semantics and system intent**

Good API design communicates meaning clearly through method choice.

---

# <span style="color:#2563eb">**Final Summary Table**</span>

| Aspect         | PUT              | PATCH               |
| -------------- | ---------------- | ------------------- |
| Purpose        | Replace resource | Partial modify      |
| Data Sent      | Full object      | Changed fields only |
| Missing Fields | May reset/remove | Preserved           |
| Idempotent     | Yes              | Usually             |
| Schema Style   | Required fields  | Optional fields     |
| Best For       | Full replacement | Partial updates     |

---

# <span style="color:#2563eb">**Final Master Mental Model**</span>

```text id="t7x2"
PUT
   =
Resource replacement semantics

PATCH
   =
Resource modification semantics
```

The difference is fundamentally about:

# <span style="color:#dc2626">**intent of state transition**
