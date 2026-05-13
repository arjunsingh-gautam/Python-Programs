# <span style="color:#2563eb">**Why Do We Pass `request` in Exception Handlers?**</span>

When an exception occurs in an API, FastAPI passes:

```python id="m1x7"
request
```

because the exception handler may need:

- information about the HTTP request
- request metadata
- client details
- URL path
- headers
- method type
- logging/tracing information

The exception alone tells:

```text id="q4v2"
WHAT failed
```

The request tells:

```text id="p8m5"
WHERE and HOW it failed
```

---

# <span style="color:#2563eb">**Simple Analogy**</span>

Imagine:

A customer visits a bank counter.

---

## <span style="color:#16a34a">**Customer Request**</span>

```text id="t7x1"
Withdraw ₹5000
```

---

## <span style="color:#16a34a">**Problem Happens**</span>

Insufficient balance.

Now bank manager needs TWO things:

| Needed Information               | Equivalent |
| -------------------------------- | ---------- |
| What problem occurred            | Exception  |
| Which customer/request caused it | Request    |

Without request information:

Manager only knows:

```text id="x2m8"
Some withdrawal failed
```

But not:

- which account
- which branch
- which customer
- which operation
- which request path

---

# <span style="color:#2563eb">**Mental Model**</span>

```text id="n9v3"
Exception
   =
Failure Information

Request
   =
Context of Failure
```

Together they form complete error handling.

---

# <span style="color:#2563eb">**What Information Exists Inside request?**</span>

FastAPI `Request` object contains:

| Data         | Example          |
| ------------ | ---------------- |
| URL path     | `/withdraw/5000` |
| HTTP method  | `GET`            |
| Headers      | Auth token       |
| Client IP    | `192.168.x.x`    |
| Query params | `?page=2`        |
| Cookies      | session data     |

---

# <span style="color:#2563eb">**Example Exception Handler**</span>

```python id="a5m2"
@app.exception_handler(InsufficientBalance)
async def balance_handler(
    request: Request,
    exc: InsufficientBalance
):

    return JSONResponse(
        status_code=400,
        content={
            "path": request.url.path,
            "error": "Insufficient balance"
        }
    )
```

---

# <span style="color:#2563eb">**What Happens Internally?**</span>

Suppose request:

```text id="r8x4"
/withdraw/5000
```

---

## <span style="color:#16a34a">**Step 1 — Request Object Created**</span>

FastAPI internally creates:

```python id="k3v7"
request
```

containing request metadata.

---

## <span style="color:#16a34a">**Step 2 — Exception Raised**</span>

```python id="p6m1"
raise InsufficientBalance()
```

---

## <span style="color:#16a34a">**Step 3 — FastAPI Calls Handler**</span>

Conceptually:

```python id="u4x9"
balance_handler(
    request=request,
    exc=exception_object
)
```

---

## <span style="color:#16a34a">**Step 4 — Handler Uses Request Context**</span>

```python id="f1m8"
request.url.path
```

gives:

```text id="y7v3"
/withdraw/5000
```

---

# <span style="color:#2563eb">**Why This is Useful in Real Systems**</span>

---

# <span style="color:#dc2626">**1. Logging**</span>

Very important in production.

Example:

```python id="w2m5"
print(request.url.path)
```

Logs:

```text id="z8x1"
Failure occurred on /withdraw/5000
```

---

# <span style="color:#dc2626">**2. Security Monitoring**</span>

Can inspect:

- suspicious IPs
- invalid tokens
- attack patterns

Example:

```python id="n4v7"
request.client.host
```

---

# <span style="color:#dc2626">**3. Better Debugging**</span>

Without request:

```text id="t1m9"
Balance error happened
```

With request:

```text id="x6v2"
Balance error happened on:
POST /withdraw/5000
from user 42
```

Huge difference.

---

# <span style="color:#dc2626">**4. Request Tracing**</span>

Large distributed systems track requests using:

- request IDs
- correlation IDs
- tracing headers

All accessed through request object.

---

# <span style="color:#2563eb">**Important Internal Mechanic**</span>

FastAPI exception handler signature:

```python id="q5x7"
async def handler(
    request: Request,
    exc: ExceptionType
)
```

exists because internally FastAPI does:

```python id="m8v4"
handler(request, exception)
```

So handler must accept both parameters.

---

# <span style="color:#2563eb">**Can We Ignore request?**</span>

Yes technically.

Example:

```python id="c7m1"
@app.exception_handler(MyException)
async def handler(request, exc):

    return JSONResponse(...)
```

You may not use `request`.

But parameter still needed because FastAPI passes it.

---

# <span style="color:#2563eb">**Analogy from Hospital System**</span>

Imagine:

Doctor receives emergency alert:

```text id="j2v9"
Patient critical
```

This is like exception.

But doctor also needs:

- patient identity
- room number
- medical history
- current treatment

This is like request context.

Without context:

Doctor cannot respond intelligently.

---

# <span style="color:#2563eb">**Why request is Architecturally Important**</span>

Modern APIs are:

# <span style="color:#dc2626">**Context-Driven Systems**</span>

The same exception may need different handling depending on:

- route
- user
- authentication
- request type
- headers
- API version

Request object provides that context.

---

# <span style="color:#2563eb">**Production-Level Example**</span>

```python id="v3m8"
@app.exception_handler(Exception)
async def global_handler(
    request: Request,
    exc: Exception
):

    print("Path:", request.url.path)
    print("Method:", request.method)
    print("Client:", request.client.host)

    return JSONResponse(
        status_code=500,
        content={
            "error": "Internal server error"
        }
    )
```

---

# <span style="color:#2563eb">**Final Mental Model**</span>

```text id="b8x2"
Exception
   =
What failed

Request
   =
Where, how, and for whom it failed
```

Both together enable:

```text id="r4m7"
Intelligent API error handling
```
