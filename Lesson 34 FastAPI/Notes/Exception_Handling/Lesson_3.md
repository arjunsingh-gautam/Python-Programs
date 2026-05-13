# <span style="color:#2563eb">**What Do We Need to Pass While Handling Custom Exceptions?**</span>

When working with custom exceptions in FastAPI, there are usually **3 major places** where values are passed:

| Place                  | What You Pass               |
| ---------------------- | --------------------------- |
| Custom Exception Class | Error-related data          |
| `raise` Statement      | Values for exception object |
| Exception Handler      | `request` and `exc`         |

---

# <span style="color:#2563eb">**Mental Model**</span>

Think of exception handling like this:

```text id="m1x7"
Something fails
      ↓
Create Exception Object
      ↓
Raise Exception
      ↓
FastAPI catches it
      ↓
Handler receives Exception Object
      ↓
Handler creates HTTP response
```

---

# <span style="color:#2563eb">**1. What We Pass Inside Custom Exception Class**</span>

Example:

```python id="x2v4"
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

# <span style="color:#2563eb">**Why We Pass These Values**</span>

These values store:

```text id="q7m2"
Context about failure
```

Without them:

Handler has no details.

---

# <span style="color:#2563eb">**What Gets Stored Internally**</span>

When this runs:

```python id="r8t5"
InsufficientBalance(
    balance=1000,
    amount=5000
)
```

Python internally creates object:

```python id="v3x9"
{
   "balance": 1000,
   "amount": 5000
}
```

attached to exception instance.

---

# <span style="color:#2563eb">**2. What We Pass During raise**</span>

Example:

```python id="p5m1"
raise InsufficientBalance(
    balance=1000,
    amount=5000
)
```

---

# <span style="color:#2563eb">**What Happens Here Internally**</span>

Python does:

---

## <span style="color:#16a34a">**Step 1**</span>

Creates exception object:

```python id="f2x8"
exc = InsufficientBalance(
    balance=1000,
    amount=5000
)
```

---

## <span style="color:#16a34a">**Step 2**</span>

Calls constructor:

```python id="n9v3"
__init__()
```

---

## <span style="color:#16a34a">**Step 3**</span>

Stores values:

```python id="y6m4"
exc.balance = 1000
exc.amount = 5000
```

---

## <span style="color:#16a34a">**Step 4**</span>

Raises exception object into runtime system.

---

# <span style="color:#2563eb">**3. What We Pass in Exception Handler**</span>

Example:

```python id="u4t7"
@app.exception_handler(InsufficientBalance)
async def balance_handler(
    request: Request,
    exc: InsufficientBalance
):
```

---

# <span style="color:#2563eb">**Understanding the Parameters**</span>

| Parameter | Purpose                 |
| --------- | ----------------------- |
| `request` | Incoming HTTP request   |
| `exc`     | Actual exception object |

---

# <span style="color:#2563eb">**What is exc?**</span>

`exc` contains:

```python id="w7x2"
balance
amount
```

because you stored them earlier.

---

# <span style="color:#2563eb">**How Handler Accesses Exception Data**</span>

```python id="j1m5"
exc.balance
exc.amount
```

Example:

```python id="k8v4"
return JSONResponse(
    status_code=400,
    content={
        "balance": exc.balance,
        "amount": exc.amount
    }
)
```

---

# <span style="color:#2563eb">**Complete Correct Example**</span>

```python id="a9m2"
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI()

class InsufficientBalance(Exception):

    def __init__(
        self,
        balance: int,
        amount: int
    ):

        self.balance = balance
        self.amount = amount

@app.exception_handler(InsufficientBalance)
async def balance_handler(
    request: Request,
    exc: InsufficientBalance
):

    return JSONResponse(
        status_code=400,
        content={
            "error": {
                "message": "Insufficient balance",
                "available_balance": exc.balance,
                "requested_amount": exc.amount
            }
        }
    )

@app.get("/withdraw/{amount}")
def withdraw(amount: int):

    balance = 1000

    if amount > balance:

        raise InsufficientBalance(
            balance=balance,
            amount=amount
        )

    return {
        "message": "Success"
    }
```

---

# <span style="color:#2563eb">**Most Common Syntax Errors Beginners Make**</span>

# <span style="color:#dc2626">**1. Forgetting self**</span>

Wrong:

```python id="x5m7"
class InsufficientBalance(Exception):

    def __init__(balance, amount):
```

Correct:

```python id="r2v8"
def __init__(self, balance, amount):
```

---

# <span style="color:#2563eb">**Why?**</span>

`self` represents:

```text id="f9x1"
Current object instance
```

Without it, Python cannot attach data to object.

---

# <span style="color:#dc2626">**2. Forgetting self.variable Assignment**</span>

Wrong:

```python id="n7m3"
def __init__(self, balance):
    balance = balance
```

Correct:

```python id="u1v9"
self.balance = balance
```

---

# <span style="color:#2563eb">**Why Wrong?**</span>

This:

```python id="t4x6"
balance = balance
```

only reassigns local variable.

Nothing stored inside object.

---

# <span style="color:#dc2626">**3. Raising Class Instead of Object with Required Arguments**</span>

Wrong:

```python id="m2v7"
raise InsufficientBalance
```

when constructor needs arguments.

Correct:

```python id="g8x1"
raise InsufficientBalance(
    balance=1000,
    amount=5000
)
```

---

# <span style="color:#2563eb">**Why Wrong?**</span>

Python needs actual object instance.

---

# <span style="color:#dc2626">**4. Using Wrong Exception Handler Decorator**</span>

Wrong:

```python id="q5m9"
@app.exception_handler()
```

Correct:

```python id="z1v4"
@app.exception_handler(InsufficientBalance)
```

---

# <span style="color:#2563eb">**Why?**</span>

FastAPI must know:

```text id="w3x8"
Which exception type this handler catches
```

---

# <span style="color:#dc2626">**5. Forgetting Request Parameter**</span>

Wrong:

```python id="p7m1"
async def balance_handler(exc):
```

Correct:

```python id="v2x5"
async def balance_handler(
    request: Request,
    exc: InsufficientBalance
):
```

---

# <span style="color:#2563eb">**Why?**</span>

FastAPI internally passes:

```python id="n6v3"
(request, exc)
```

Handler signature must match.

---

# <span style="color:#dc2626">**6. Returning Dictionary Instead of Response Object**</span>

Sometimes beginners do:

```python id="y8m4"
return {
    "error": "Insufficient balance"
}
```

Better:

```python id="x4v7"
return JSONResponse(
    status_code=400,
    content={...}
)
```

---

# <span style="color:#2563eb">**Why Better?**</span>

Allows:

- status codes
- headers
- structured HTTP responses

---

# <span style="color:#dc2626">**7. Using raise Instead of return Inside Handler**</span>

Wrong:

```python id="m1x8"
raise JSONResponse(...)
```

Correct:

```python id="r5v2"
return JSONResponse(...)
```

---

# <span style="color:#2563eb">**Why?**</span>

Handler's job:

```text id="t9m3"
Return HTTP response
```

not raise more exceptions.

---

# <span style="color:#dc2626">**8. Accessing Nonexistent Exception Attributes**</span>

Wrong:

```python id="q2v6"
exc.money
```

when only:

```python id="w7m4"
self.balance
```

exists.

---

# <span style="color:#2563eb">**Why?**</span>

Exception object only contains explicitly stored attributes.

---

# <span style="color:#2563eb">**Important Concept: Exception Object Lifecycle**</span>

---

## <span style="color:#16a34a">**Step 1 — Object Creation**</span>

```python id="a8x2"
InsufficientBalance(
    balance=1000,
    amount=5000
)
```

---

## <span style="color:#16a34a">**Step 2 — Attributes Stored**</span>

```python id="k4m9"
self.balance
self.amount
```

---

## <span style="color:#16a34a">**Step 3 — Exception Raised**</span>

```python id="p1v7"
raise ...
```

---

## <span style="color:#16a34a">**Step 4 — FastAPI Catches Exception**</span>

---

## <span style="color:#16a34a">**Step 5 — Handler Receives Same Object**</span>

```python id="x6m3"
exc
```

contains stored values.

---

## <span style="color:#16a34a">**Step 6 — Handler Creates HTTP Response**</span>

---

# <span style="color:#2563eb">**Best Practice Implementation Pattern**</span>

---

# <span style="color:#dc2626">**Good Pattern**</span>

```python id="f5x1"
class BusinessException(Exception):

    def __init__(
        self,
        code: str,
        message: str
    ):

        self.code = code
        self.message = message
```

Very scalable.

---

# <span style="color:#2563eb">**Why This Pattern is Powerful**</span>

Allows:

- reusable handlers
- standardized APIs
- structured error schemas
- scalable architecture

---

# <span style="color:#2563eb">**Mental Model to Remember Forever**</span>

```text id="u3v8"
Custom Exception
      =
Data Container for Failure Information
```

and:

```text id="m9x4"
Exception Handler
      =
Translator from Python Error
to HTTP Response
```
