# <span style="color:#2563eb">**What are Path Parameters?**</span>

Path parameters are:

> Dynamic values embedded directly inside a URL path.

Example:

```text id="m1x7"
/users/10
```

Here:

```text id="v8r2"
10
```

is a path parameter.

It represents:

```text id="p4k9"
specific resource identifier
```

---

# <span style="color:#2563eb">**Simple Intuition**</span>

Suppose you have:

```text id="j7t3"
/users/1
/users/2
/users/3
```

Instead of writing:

```python id="x2m5"
@app.get("/users/1")
@app.get("/users/2")
@app.get("/users/3")
```

you write:

```python id="a9v1"
@app.get("/users/{id}")
```

Now one route handles all users dynamically.

---

# <span style="color:#2563eb">**Mental Model of Path Parameters**</span>

# <span style="color:#dc2626">**Language-Agnostic Mental Model**</span>

Think of path parameters as:

```text id="q6n8"
URL placeholders
```

or:

```text id="w4p2"
Variables inside URL structure
```

Example mental abstraction:

```text id="b9x4"
/resource/{variable}
```

When request comes:

```text id="r3m7"
/resource/42
```

framework extracts:

```text id="k1v5"
variable = 42
```

and passes it into your program.

---

# <span style="color:#2563eb">**Why We Need Path Parameters**</span>

# <span style="color:#dc2626">**Core Problem They Solve**</span>

Applications deal with:

- users
- products
- orders
- posts
- comments

Each entity has different IDs.

Without path parameters, routes become impossible to scale.

---

# <span style="color:#2563eb">**Real Problem Without Path Parameters**</span>

Imagine building Instagram.

Without path parameters:

```text id="g2t1"
/user1
/user2
/user3
/user1000000
```

You would need millions of routes.

Impossible.

---

# <span style="color:#2563eb">**What Path Parameters Enable**</span>

They allow:

```text id="f7k9"
One route
    ↓
Handles infinite dynamic resources
```

---

# <span style="color:#2563eb">**Core Philosophy**</span>

Path parameters make routes:

# <span style="color:#dc2626">**Generic and Dynamic**</span>

instead of:

# <span style="color:#dc2626">**Hardcoded and Static**</span>

---

# <span style="color:#2563eb">**FastAPI Path Parameter Syntax**</span>

```python id="t5n2"
@app.get("/users/{id}")
def get_user(id: int):
    return {"user_id": id}
```

---

# <span style="color:#2563eb">**Understanding the Syntax**</span>

---

## <span style="color:#16a34a">**1. Route Placeholder**</span>

```python id="m8x6"
"/users/{id}"
```

means:

```text id="q2v7"
Capture dynamic value from URL
and store it as "id"
```

---

## <span style="color:#16a34a">**2. Function Parameter**</span>

```python id="z4k1"
id: int
```

means:

```text id="w9m3"
Inject captured value into function
and validate as integer
```

---

# <span style="color:#2563eb">**Dry Run of Path Parameter Flow**</span>

Suppose browser sends:

```text id="u6t8"
GET /users/25
```

---

# <span style="color:#dc2626">**Internal Execution Flow**</span>

---

## <span style="color:#16a34a">**Step 1 — Router Matches Pattern**</span>

FastAPI sees:

```python id="a7q4"
"/users/{id}"
```

Request path:

```text id="n3x1"
/users/25
```

Pattern matches.

---

## <span style="color:#16a34a">**Step 2 — Extract Dynamic Segment**</span>

Framework extracts:

```python id="f5v2"
id = "25"
```

Initially string.

---

## <span style="color:#16a34a">**Step 3 — Type Conversion Happens**</span>

Because:

```python id="c8m9"
id: int
```

FastAPI converts:

```python id="r1p7"
"25" → 25
```

---

## <span style="color:#16a34a">**Step 4 — Validation Happens**</span>

If conversion fails:

```text id="b6t4"
/users/abc
```

FastAPI returns validation error automatically.

---

## <span style="color:#16a34a">**Step 5 — Function Executes**</span>

```python id="x9k5"
get_user(25)
```

runs.

---

## <span style="color:#16a34a">**Step 6 — Response Returned**</span>

```json id="m4w1"
{
  "user_id": 25
}
```

---

# <span style="color:#2563eb">**Visual Mental Model**</span>

```text id="p8r3"
Incoming URL:
    /users/25

Route Pattern:
    /users/{id}

Extraction:
    id = 25

Function Call:
    get_user(id=25)
```

---

# <span style="color:#2563eb">**Complete Example**</span>

```python id="q5m8"
from fastapi import FastAPI

app = FastAPI()

@app.get("/products/{product_id}")
def get_product(product_id: int):

    return {
        "product_id": product_id
    }
```

---

# <span style="color:#2563eb">**Request Example**</span>

```text id="v2n4"
GET /products/100
```

---

# <span style="color:#2563eb">**Response**</span>

```json id="k7x1"
{
  "product_id": 100
}
```

---

# <span style="color:#2563eb">**What Happens Without Path Parameters?**</span>

Without them:

You would need:

```python id="y8m2"
@app.get("/products/1")
@app.get("/products/2")
@app.get("/products/3")
```

This breaks scalability completely.

---

# <span style="color:#2563eb">**Why Path Parameters are Fundamental in APIs**</span>

Modern APIs revolve around:

# <span style="color:#dc2626">**Resources**</span>

Examples:

| Resource  | Example        |
| --------- | -------------- |
| User      | `/users/10`    |
| Product   | `/products/50` |
| Order     | `/orders/99`   |
| Blog Post | `/posts/123`   |

Path parameters identify:

```text id="s4k7"
Which specific resource
```

client wants.

---

# <span style="color:#2563eb">**Path Parameters vs Query Parameters**</span>

Very important distinction.

---

## <span style="color:#16a34a">**Path Parameters**</span>

Identify:

# <span style="color:#dc2626">**Specific resource**</span>

Example:

```text id="w1v6"
/users/10
```

---

## <span style="color:#16a34a">**Query Parameters**</span>

Modify/filter request.

Example:

```text id="m8p3"
/users?active=true
```

---

# <span style="color:#2563eb">**Mental Difference**</span>

| Parameter Type  | Meaning               |
| --------------- | --------------------- |
| Path parameter  | WHAT resource         |
| Query parameter | HOW to process/filter |

---

# <span style="color:#2563eb">**Multiple Path Parameters**</span>

```python id="g7x2"
@app.get("/users/{user_id}/posts/{post_id}")
def get_post(user_id: int, post_id: int):

    return {
        "user_id": user_id,
        "post_id": post_id
    }
```

---

# <span style="color:#2563eb">**Request Example**</span>

```text id="d4m9"
/users/5/posts/20
```

---

# <span style="color:#2563eb">**Extraction**</span>

```python id="h1v8"
user_id = 5
post_id = 20
```

---

# <span style="color:#2563eb">**How Routing Internally Works**</span>

FastAPI internally builds route patterns.

Conceptually:

```python id="x6k4"
[
   {
      "pattern": "/users/{id}",
      "handler": get_user
   }
]
```

---

## <span style="color:#16a34a">**Pattern Matching Mechanism**</span>

Framework splits path:

```text id="n7w5"
/users/25
```

into segments:

```python id="j9p2"
["users", "25"]
```

Pattern:

```text id="r3v1"
/users/{id}
```

becomes:

```python id="k5m7"
["users", "{id}"]
```

Framework compares segment-by-segment.

Static parts must match:

```text id="a2x6"
users == users
```

Dynamic part captured:

```text id="c8t4"
{id} → 25
```

---

# <span style="color:#2563eb">**Type Validation in FastAPI**</span>

One powerful FastAPI feature.

---

## <span style="color:#16a34a">**Example**</span>

```python id="f4q1"
@app.get("/users/{id}")
def get_user(id: int):
```

FastAPI automatically:

- converts string to int
- validates input
- returns errors automatically

---

# <span style="color:#2563eb">**Validation Error Example**</span>

Request:

```text id="p7m9"
/users/hello
```

Error:

```json id="z2v5"
{
  "detail": [
    {
      "msg": "Input should be a valid integer"
    }
  ]
}
```

---

# <span style="color:#2563eb">**Important Design Principles**</span>

---

## <span style="color:#16a34a">**1. Use Path Parameters for Identity**</span>

Good:

```text id="w3k7"
/users/10
```

Because:

```text id="v1m4"
10 identifies resource
```

---

## <span style="color:#16a34a">**2. Keep URLs Hierarchical**</span>

Good:

```text id="b8x1"
/users/5/posts/20
```

Shows relationship.

---

## <span style="color:#16a34a">**3. Avoid Verb-Based URLs**</span>

Bad:

```text id="d5n2"
/getUser/10
```

Good:

```text id="j7v4"
/users/10
```

HTTP methods already describe action.

---

# <span style="color:#2563eb">**Real-World Analogy**</span>

Imagine library shelves.

```text id="f9k3"
/books/101
```

means:

```text id="m2x7"
Go to books collection
and retrieve book 101
```

Path parameter acts like:

# <span style="color:#dc2626">**Dynamic address locator**</span>

---

# <span style="color:#2563eb">**Coding Exercise to Strengthen Learning**</span>

# <span style="color:#dc2626">**Mini Student API Project**</span>

Build a FastAPI application.

---

# <span style="color:#2563eb">**Requirements**</span>

---

## <span style="color:#16a34a">**1. Create Student Route**</span>

```text id="q4v2"
/students/{student_id}
```

Return:

```json id="r8k5"
{
  "student_id": 1
}
```

---

## <span style="color:#16a34a">**2. Create Subject Route**</span>

```text id="m6x1"
/students/{student_id}/subjects/{subject_id}
```

Return both IDs.

---

## <span style="color:#16a34a">**3. Add Type Validation**</span>

Ensure IDs are integers.

Test invalid requests:

```text id="w2p9"
/students/abc
```

Observe validation errors.

---

## <span style="color:#16a34a">**4. Add Dynamic Data**</span>

Create dictionary:

```python id="n5v7"
students = {
    1: "Arjun",
    2: "Rahul"
}
```

Return actual names.

---

## <span style="color:#16a34a">**5. Add Conditional Logic**</span>

If student ID not found:

Return:

```json id="t7m4"
{
  "error": "Student not found"
}
```

---

# <span style="color:#2563eb">**Advanced Challenge**</span>

Build:

```text id="x1k6"
Mini Blog API
```

Routes:

```text id="f3v9"
/posts/{post_id}
/users/{user_id}/posts/{post_id}
/products/{category}/{product_id}
```

This exercise will deeply strengthen your understanding of:

- dynamic routing
- parameter extraction
- validation
- REST API design
- route hierarchy
- FastAPI routing internals
