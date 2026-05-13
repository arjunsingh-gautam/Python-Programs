# <span style="color:#2563eb">**Why We Need Custom Exception Handlers**</span>

Suppose your API has business rules like:

- insufficient balance
- invalid coupon
- seat already booked
- stock unavailable
- order already shipped

These are:

# <span style="color:#dc2626">**Business Logic Exceptions**</span>

They are NOT server crashes.

They are expected failures.

You should return:

- meaningful HTTP status code
- clean JSON response
- structured error message

instead of:

```text id="x1m4"
500 Internal Server Error
```

---

# <span style="color:#2563eb">**Mental Model of Custom Exception Handling**</span>

```text id="r8v2"
Business Rule Fails
        ↓
Raise Custom Exception
        ↓
FastAPI Intercepts Exception
        ↓
Exception Handler Runs
        ↓
HTTP Response Returned
```

---

# <span style="color:#2563eb">**Simplest Implementation**</span>

# <span style="color:#dc2626">**Step 1 — Create Custom Exception**</span>

```python id="n4t7"
class InsufficientBalance(Exception):
    pass
```

---

## <span style="color:#16a34a">**What This Means**</span>

You are defining:

```text id="q7x1"
A special error type
```

for your application.

Instead of generic:

```python id="j5m3"
Exception
```

you now have semantic meaning:

```python id="u9v8"
InsufficientBalance
```

Much cleaner.

---

# <span style="color:#dc2626">**Step 2 — Create Exception Handler**</span>

```python id="p3k8"
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
```

---

# <span style="color:#2563eb">**Understanding Important Components**</span>

---

# <span style="color:#dc2626">**1. @app.exception_handler(...)**</span>

```python id="m8x2"
@app.exception_handler(InsufficientBalance)
```

Registers:

```text id="v1q5"
Which exception this handler catches
```

Think of it like:

```text id="c7t9"
Routing table for exceptions
```

---

# <span style="color:#dc2626">**2. request: Request**</span>

```python id="z4m7"
request: Request
```

Contains incoming HTTP request info.

Useful for:

- logging
- tracing
- debugging
- request metadata

---

# <span style="color:#dc2626">**3. exc: InsufficientBalance**</span>

```python id="x9v1"
exc
```

is the actual exception object.

Can contain:

- message
- metadata
- business details

---

# <span style="color:#dc2626">**4. JSONResponse**</span>

```python id="r2k6"
JSONResponse(...)
```

Creates proper HTTP JSON response.

---

# <span style="color:#dc2626">**5. status_code**</span>

```python id="g5x3"
status_code=400
```

Important because APIs communicate failures through HTTP semantics.

---

# <span style="color:#2563eb">**Step 3 — Raise Exception Inside Route**</span>

```python id="t8m4"
@app.get("/withdraw/{amount}")
def withdraw(amount: int):

    balance = 1000

    if amount > balance:
        raise InsufficientBalance()

    return {
        "message": "Withdrawal successful"
    }
```

---

# <span style="color:#2563eb">**Complete Execution Dry Run**</span>

Suppose request:

```text id="w7v9"
/withdraw/5000
```

---

## <span style="color:#16a34a">**Step 1 — Route Executes**</span>

```python id="h2k8"
withdraw(5000)
```

---

## <span style="color:#16a34a">**Step 2 — Condition Fails**</span>

```python id="f1x7"
5000 > 1000
```

True.

---

## <span style="color:#16a34a">**Step 3 — Exception Raised**</span>

```python id="y4m2"
raise InsufficientBalance()
```

Program execution immediately stops.

---

## <span style="color:#16a34a">**Step 4 — FastAPI Catches Exception**</span>

Framework searches:

```python id="v8q1"
@app.exception_handler(InsufficientBalance)
```

---

## <span style="color:#16a34a">**Step 5 — Handler Executes**</span>

```python id="b3t5"
balance_handler()
```

runs.

---

## <span style="color:#16a34a">**Step 6 — HTTP Response Sent**</span>

Client receives:

```json id="u6m4"
{
  "error": "Insufficient balance"
}
```

with:

```text id="k9x7"
400 Bad Request
```

---

# <span style="color:#2563eb">**Full Simple Example**</span>

```python id="d7p2"
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

@app.get("/withdraw/{amount}")
def withdraw(amount: int):

    balance = 1000

    if amount > balance:
        raise InsufficientBalance()

    return {
        "message": "Withdrawal successful"
    }
```

---

# <span style="color:#2563eb">**Problems in This Simple Implementation**</span>

Although functional, it has limitations.

---

# <span style="color:#dc2626">**Problem 1 — Hardcoded Error Message**</span>

Handler always returns:

```json id="q5x8"
{
  "error": "Insufficient balance"
}
```

No dynamic details.

---

# <span style="color:#dc2626">**Problem 2 — No Error Codes**</span>

Large APIs need machine-readable error identifiers.

---

# <span style="color:#dc2626">**Problem 3 — No Logging**</span>

No debugging visibility.

---

# <span style="color:#dc2626">**Problem 4 — Weak Structure**</span>

Error schema inconsistent.

---

# <span style="color:#2563eb">**Improved Implementation with Best Practices**</span>

# <span style="color:#dc2626">**Step 1 — Add Data to Exception**</span>

```python id="z2v6"
class InsufficientBalance(Exception):

    def __init__(
        self,
        balance: int,
        amount: int
    ):

        self.balance = balance
        self.amount = amount
```

---

## <span style="color:#16a34a">**Why Important?**</span>

Exception now carries business context.

---

# <span style="color:#dc2626">**Improved Handler**</span>

```python id="m4t1"
@app.exception_handler(InsufficientBalance)
async def balance_handler(
    request: Request,
    exc: InsufficientBalance
):

    return JSONResponse(
        status_code=400,
        content={
            "error": {
                "code": "INSUFFICIENT_BALANCE",
                "message": "Insufficient balance",
                "available_balance": exc.balance,
                "requested_amount": exc.amount
            }
        }
    )
```

---

# <span style="color:#dc2626">**Improved Route**</span>

```python id="p8v3"
@app.get("/withdraw/{amount}")
def withdraw(amount: int):

    balance = 1000

    if amount > balance:

        raise InsufficientBalance(
            balance=balance,
            amount=amount
        )

    return {
        "message": "Withdrawal successful"
    }
```

---

# <span style="color:#2563eb">**Response Now Becomes Much Better**</span>

```json id="g7m2"
{
  "error": {
    "code": "INSUFFICIENT_BALANCE",
    "message": "Insufficient balance",
    "available_balance": 1000,
    "requested_amount": 5000
  }
}
```

---

# <span style="color:#2563eb">**Why This Design is Better**</span>

| Improvement          | Benefit              |
| -------------------- | -------------------- |
| Structured errors    | Consistent API       |
| Error codes          | Frontend handling    |
| Metadata             | Better debugging     |
| Semantic exception   | Cleaner architecture |
| Centralized handling | Scalability          |

---

# <span style="color:#2563eb">**Best Practices for Custom Exception Handling**</span>

---

# <span style="color:#dc2626">**1. Create Semantic Exceptions**</span>

Good:

```python id="n1k4"
InsufficientBalance
UserNotFound
InvalidCoupon
```

Bad:

```python id="v7x9"
Exception("something failed")
```

---

# <span style="color:#dc2626">**2. Centralize Error Handling**</span>

Avoid:

```python id="j3m8"
return {"error": "..."}
```

everywhere.

Use exception handlers.

---

# <span style="color:#dc2626">**3. Return Proper HTTP Status Codes**</span>

| Situation        | Status |
| ---------------- | ------ |
| Invalid request  | 400    |
| Unauthorized     | 401    |
| Forbidden        | 403    |
| Missing resource | 404    |
| Conflict         | 409    |
| Internal error   | 500    |

---

# <span style="color:#dc2626">**4. Use Structured Error Responses**</span>

Good:

```json id="q2v5"
{
  "error": {
    "code": "USER_NOT_FOUND",
    "message": "User not found"
  }
}
```

Bad:

```json id="f8t1"
{
  "msg": "oops"
}
```

---

# <span style="color:#dc2626">**5. Never Leak Internal Errors**</span>

Bad:

```json id="u5m9"
{
  "error": "AttributeError line 72"
}
```

Security risk.

---

# <span style="color:#2563eb">**Common Mistakes Beginners Make**</span>

---

# <span style="color:#dc2626">**1. Returning Errors Instead of Raising Exceptions**</span>

Bad:

```python id="k4v2"
return {"error": "balance low"}
```

Why bad?

- wrong status code
- inconsistent handling
- route keeps responsibility

Better:

```python id="t9x3"
raise InsufficientBalance()
```

---

# <span style="color:#dc2626">**2. Catching Generic Exception Everywhere**</span>

Bad:

```python id="w7m1"
except Exception:
```

Hides real problems.

Catch specific exceptions when possible.

---

# <span style="color:#dc2626">**3. Putting Business Logic Inside Handler**</span>

Bad:

```python id="x3k8"
@app.exception_handler(...)
async def handler(...):

    if balance > amount:
```

Handlers should format responses only.

---

# <span style="color:#dc2626">**4. Using Wrong Status Codes**</span>

Example:

```text id="p6v4"
Returning 500 for business validation error
```

Incorrect semantics.

---

# <span style="color:#2563eb">**Production-Level Architecture Pattern**</span>

Large systems usually follow:

```text id="z1t5"
Route Layer
     ↓
Service Layer
     ↓
Business Exceptions Raised
     ↓
Global Exception Handlers
     ↓
Standardized API Response
```

Very scalable architecture.

---

# <span style="color:#2563eb">**Mental Model to Remember**</span>

Think of custom exceptions as:

```text id="c8m6"
Business Failure Signals
```

And exception handlers as:

```text id="r4v1"
HTTP Translators
```

They translate:

```text id="y9x2"
Python Exception
      ↓
HTTP API Response
```

cleanly and centrally.
