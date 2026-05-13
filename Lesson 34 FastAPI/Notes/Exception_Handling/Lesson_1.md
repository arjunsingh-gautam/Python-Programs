# <span style="color:#2563eb">**Why Exception Handling is Important in APIs**</span>

APIs interact with:

- users
- databases
- external APIs
- files
- authentication systems
- networks

Many things can fail.

Without exception handling:

- server crashes
- bad user experience
- security leaks
- inconsistent responses
- debugging becomes hard

Exception handling ensures:

```text id="m1x7"
Failures are controlled,
predictable,
and meaningful
```

instead of chaotic.

---

# <span style="color:#2563eb">**What is an Exception?**</span>

An exception means:

> An abnormal event/error occurring during program execution.

Example:

```python id="t7v2"
10 / 0
```

raises:

```text id="k3m9"
ZeroDivisionError
```

In APIs, exceptions happen during:

- request parsing
- validation
- business logic
- database operations
- response generation

---

# <span style="color:#2563eb">**Mental Model of API Exception Handling**</span>

```text id="q4n8"
Request
   ↓
Processing
   ↓
Something Fails
   ↓
Exception Raised
   ↓
Exception Handler Catches It
   ↓
Controlled HTTP Response Returned
```

---

# <span style="color:#2563eb">**Types of Exceptions in APIs**</span>

# <span style="color:#dc2626">**1. Validation Exceptions**</span>

Client sends invalid data.

Example:

```text id="x2m5"
/users/abc
```

Expected:

```python id="v9k3"
id: int
```

Fails validation.

---

# <span style="color:#dc2626">**2. Authentication Exceptions**</span>

Example:

- invalid token
- missing login
- expired JWT

---

# <span style="color:#dc2626">**3. Authorization Exceptions**</span>

User authenticated but lacks permission.

Example:

```text id="n4t7"
Normal user trying to delete admin data
```

---

# <span style="color:#dc2626">**4. Database Exceptions**</span>

Examples:

- connection failure
- duplicate keys
- constraint violations
- transaction failures

---

# <span style="color:#dc2626">**5. File Handling Exceptions**</span>

Examples:

- missing file
- permission denied
- invalid upload

---

# <span style="color:#dc2626">**6. External API Exceptions**</span>

Examples:

- timeout
- API unavailable
- invalid response

---

# <span style="color:#dc2626">**7. Business Logic Exceptions**</span>

Application-specific failures.

Example:

```text id="u7x2"
Insufficient account balance
```

---

# <span style="color:#dc2626">**8. Server/Internal Exceptions**</span>

Unexpected bugs.

Examples:

- NoneType errors
- attribute errors
- logic bugs

---

# <span style="color:#2563eb">**How Exceptions Depend on Request Type**</span>

Different HTTP requests create different failure patterns.

---

# <span style="color:#dc2626">**GET Requests**</span>

Mostly fail due to:

- invalid path parameter
- missing resource
- DB lookup failures

Example:

```text id="f8m1"
/users/999
```

User not found.

---

# <span style="color:#dc2626">**POST Requests**</span>

Usually fail due to:

- invalid body data
- validation errors
- duplicate entries
- auth failures

Example:

```json id="v3t9"
{
  "email": "invalid-email"
}
```

---

# <span style="color:#dc2626">**PUT/PATCH Requests**</span>

Can fail due to:

- partial invalid data
- version conflicts
- update constraints

---

# <span style="color:#dc2626">**DELETE Requests**</span>

Can fail due to:

- permissions
- missing resource
- dependency constraints

---

# <span style="color:#2563eb">**Exception Handling Philosophy**</span>

Good APIs should:

| Principle               | Meaning                  |
| ----------------------- | ------------------------ |
| Fail predictably        | Controlled errors        |
| Return useful errors    | Informative responses    |
| Hide internal bugs      | No stack traces to users |
| Log failures            | For debugging            |
| Use proper status codes | Semantic correctness     |

---

# <span style="color:#2563eb">**Exception Handling Constructs in FastAPI**</span>

We will go from:

```text id="j5n4"
Simple → Advanced
```

---

# <span style="color:#2563eb">**1. Simple Python try-except**</span>

# <span style="color:#dc2626">**Basic Construct**</span>

```python id="p2v7"
try:
    risky_operation()

except Exception:
    handle_error()
```

---

# <span style="color:#2563eb">**FastAPI Example**</span>

```python id="z7x1"
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def divide():

    try:
        result = 10 / 0
        return {"result": result}

    except ZeroDivisionError:
        return {"error": "Cannot divide by zero"}
```

---

# <span style="color:#2563eb">**Problem with This Approach**</span>

Issues:

- inconsistent responses
- wrong status codes
- repeated code
- poor scalability

Not ideal for large APIs.

---

# <span style="color:#2563eb">**2. HTTPException (Recommended Basic Approach)**</span>

FastAPI provides:

```python id="m9t4"
HTTPException
```

---

# <span style="color:#dc2626">**Purpose**</span>

Allows returning:

- proper HTTP status codes
- structured errors

---

# <span style="color:#2563eb">**Syntax**</span>

```python id="f4x8"
from fastapi import HTTPException

raise HTTPException(
    status_code=404,
    detail="User not found"
)
```

---

# <span style="color:#2563eb">**Example**</span>

```python id="r1v6"
from fastapi import FastAPI, HTTPException

app = FastAPI()

users = {
    1: "Arjun",
    2: "Rahul"
}

@app.get("/users/{id}")
def get_user(id: int):

    if id not in users:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return {
        "name": users[id]
    }
```

---

# <span style="color:#2563eb">**Dry Run**</span>

Request:

```text id="k8m3"
/users/10
```

---

## <span style="color:#16a34a">**Execution**</span>

Condition fails:

```python id="t5v9"
id not in users
```

Raises:

```python id="n7x2"
HTTPException
```

FastAPI catches it internally.

Returns:

```json id="b4m1"
{
  "detail": "User not found"
}
```

with status:

```text id="y2t7"
404 Not Found
```

---

# <span style="color:#2563eb">**3. Custom Exceptions**</span>

Useful for business logic.

---

# <span style="color:#dc2626">**Example**</span>

```python id="q7n5"
class InsufficientBalance(Exception):
    pass
```

---

# <span style="color:#2563eb">**Why Custom Exceptions?**</span>

Makes code:

- cleaner
- semantic
- reusable

Instead of:

```python id="m2v1"
raise Exception("Balance low")
```

you write:

```python id="x4k8"
raise InsufficientBalance()
```

Much clearer.

---

# <span style="color:#2563eb">**4. Exception Handlers**</span>

# <span style="color:#dc2626">**What is an Exception Handler?**</span>

An exception handler is:

> Centralized logic that catches exceptions and converts them into HTTP responses.

Instead of handling errors everywhere.

---

# <span style="color:#2563eb">**Mental Model**</span>

```text id="w8t3"
Exception Raised
      ↓
FastAPI Searches Handler
      ↓
Matching Handler Executes
      ↓
Structured Response Returned
```

---

# <span style="color:#2563eb">**Syntax of Exception Handler**</span>

```python id="a9m4"
@app.exception_handler(ExceptionType)
async def handler(request, exc):
    ...
```

---

# <span style="color:#2563eb">**Custom Exception Handler Example**</span>

```python id="j4v7"
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI()

class InsufficientBalance(Exception):
    pass

@app.exception_handler(InsufficientBalance)
async def balance_handler(
    request: Request,
    exc: InsufficientBalance
):

    return JSONResponse(
        status_code=400,
        content={
            "error": "Insufficient balance"
        }
    )

@app.get("/")
def home():

    raise InsufficientBalance()
```

---

# <span style="color:#2563eb">**How It Works Internally**</span>

---

## <span style="color:#16a34a">**Step 1 — Exception Raised**</span>

```python id="z3n8"
raise InsufficientBalance()
```

---

## <span style="color:#16a34a">**Step 2 — FastAPI Intercepts Exception**</span>

Framework catches exception.

---

## <span style="color:#16a34a">**Step 3 — Searches Registered Handlers**</span>

Finds:

```python id="k7v2"
@app.exception_handler(InsufficientBalance)
```

---

## <span style="color:#16a34a">**Step 4 — Handler Executes**</span>

```python id="m5x9"
balance_handler()
```

runs.

---

## <span style="color:#16a34a">**Step 5 — JSON Response Returned**</span>

```json id="f1t6"
{
  "error": "Insufficient balance"
}
```

---

# <span style="color:#2563eb">**5. Global Exception Handler**</span>

Catch all unhandled exceptions.

---

# <span style="color:#dc2626">**Example**</span>

```python id="u6m3"
@app.exception_handler(Exception)
async def global_handler(request, exc):

    return JSONResponse(
        status_code=500,
        content={
            "error": "Internal server error"
        }
    )
```

---

# <span style="color:#2563eb">**Why Important?**</span>

Prevents:

- raw stack traces
- server crashes
- security leaks

---

# <span style="color:#2563eb">**Best Exception Handling Constructs in FastAPI**</span>

# <span style="color:#dc2626">**Simple → Advanced Progression**</span>

| Level | Construct          | Usage                |
| ----- | ------------------ | -------------------- |
| 1     | try-except         | Local handling       |
| 2     | HTTPException      | Basic API errors     |
| 3     | Custom exceptions  | Business logic       |
| 4     | Exception handlers | Centralized handling |
| 5     | Global handlers    | Fallback protection  |
| 6     | Middleware logging | Advanced systems     |

---

# <span style="color:#2563eb">**Best Practices for Exception Handling**</span>

---

## <span style="color:#16a34a">**1. Use Proper HTTP Status Codes**</span>

| Status | Meaning        |
| ------ | -------------- |
| 400    | Bad request    |
| 401    | Unauthorized   |
| 403    | Forbidden      |
| 404    | Not found      |
| 409    | Conflict       |
| 500    | Internal error |

---

## <span style="color:#16a34a">**2. Never Expose Internal Errors to Users**</span>

Bad:

```json id="x7v4"
{
  "error": "AttributeError line 92"
}
```

Good:

```json id="n1m8"
{
  "error": "Internal server error"
}
```

---

## <span style="color:#16a34a">**3. Use Structured Error Responses**</span>

Good:

```json id="p3t7"
{
  "error": {
    "code": "USER_NOT_FOUND",
    "message": "User not found"
  }
}
```

---

## <span style="color:#16a34a">**4. Log Exceptions Internally**</span>

Users should see safe message.

Developers should see real logs.

---

## <span style="color:#16a34a">**5. Separate Business Errors from System Errors**</span>

Business:

```text id="g5m2"
Insufficient balance
```

System:

```text id="k8x1"
Database crashed
```

Handle differently.

---

# <span style="color:#2563eb">**FastAPI Validation Exceptions**</span>

FastAPI automatically handles validation errors.

Example:

```python id="y2n6"
@app.get("/users/{id}")
def get_user(id: int):
```

Request:

```text id="m7v9"
/users/abc
```

FastAPI auto returns:

```json id="q1t4"
{
  "detail": [
    {
      "msg": "Input should be a valid integer"
    }
  ]
}
```

No manual handling required.

---

# <span style="color:#2563eb">**Advanced Architecture Pattern**</span>

Large systems often use:

```text id="r4x7"
Route Layer
    ↓
Service Layer
    ↓
Repository Layer
```

Exceptions raised in deeper layers.

Global handlers convert them to API responses.

Very scalable design.

---

# <span style="color:#2563eb">**Coding Exercise to Strengthen Learning**</span>

# <span style="color:#dc2626">**Mini Banking API**</span>

Build a FastAPI project.

---

# <span style="color:#2563eb">**Requirements**</span>

---

## <span style="color:#16a34a">**1. Create Account Route**</span>

```text id="x8t2"
/account/{id}
```

Return account balance.

---

## <span style="color:#16a34a">**2. Add Validation**</span>

If invalid account ID:

Raise:

```python id="v3m5"
HTTPException(404)
```

---

## <span style="color:#16a34a">**3. Create Custom Exception**</span>

```python id="n7x1"
class InsufficientBalance(Exception):
```

---

## <span style="color:#16a34a">**4. Create Exception Handler**</span>

Return:

```json id="f2t8"
{
  "error": "Insufficient balance"
}
```

---

## <span style="color:#16a34a">**5. Create Withdraw Route**</span>

```text id="k9m4"
/withdraw/{amount}
```

If amount > balance:

Raise custom exception.

---

## <span style="color:#16a34a">**6. Add Global Exception Handler**</span>

Catch unexpected failures.

---

# <span style="color:#2563eb">**Advanced Challenge**</span>

Implement:

- database exceptions
- JWT auth exceptions
- logging middleware
- standardized error schema
- error codes
- request tracing IDs

This exercise will deeply strengthen understanding of:

- exception propagation
- API robustness
- FastAPI error architecture
- centralized exception handling
- production-grade backend design
