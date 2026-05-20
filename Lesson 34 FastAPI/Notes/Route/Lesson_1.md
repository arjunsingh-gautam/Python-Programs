# <span style="color:#2563eb">**What is the Modular Approach to Define Routes in FastAPI?**</span>

The modular approach means:

# <span style="color:#dc2626">**Separating routes into independent modules/files based on functionality**

Instead of:

```text id="m1x7"
putting everything inside main.py
```

you organize routes into:

- routers
- directories
- feature modules

---

# <span style="color:#2563eb">**Simple Example**</span>

Instead of:

```text id="q4v2"
main.py
   ├── user routes
   ├── auth routes
   ├── product routes
   ├── comment routes
   ├── admin routes
```

you create:

```text id="p8m5"
routers/
    ├── users.py
    ├── auth.py
    ├── products.py
    ├── comments.py
```

This is modular routing.

---

# <span style="color:#2563eb">**Why We Need Modular Routing**</span>

This emerges from a fundamental software engineering problem:

# <span style="color:#dc2626">**Codebase complexity growth**

---

# <span style="color:#2563eb">**What Happens Without Modularization?**</span>

Suppose application grows.

Eventually:

```text id="t7x1"
main.py
=
5000+ lines
```

containing:

- all routes
- all dependencies
- all logic
- all imports

Now system becomes:

- hard to navigate
- hard to debug
- hard to scale
- hard to collaborate on

---

# <span style="color:#2563eb">**The Real Problem is Cognitive Complexity**</span>

Humans cannot efficiently reason about:

```text id="x2m8"
massive monolithic files
```

Modularization reduces:

# <span style="color:#dc2626">**mental load**

---

# <span style="color:#2563eb">**Feynman Analogy**</span>

Imagine hospital.

---

# <span style="color:#dc2626">**Bad Design**</span>

One giant room:

- surgery
- pharmacy
- reception
- ICU
- diagnostics

Everything mixed together.

Chaos.

---

# <span style="color:#dc2626">**Good Design**</span>

Separate departments:

- cardiology
- radiology
- emergency
- pharmacy

Each handles specific concern.

FastAPI routers work similarly.

---

# <span style="color:#2563eb">**Mental Model of Routers**</span>

```text id="n9v3"
Router
   =
Mini FastAPI application
focused on one feature/domain
```

---

# <span style="color:#2563eb">**What is APIRouter?**</span>

FastAPI provides:

```python id="a5m2"
APIRouter
```

It behaves like:

```text id="r8x4"
smaller isolated route registry
```

Later attached into main application.

---

# <span style="color:#2563eb">**Core Architecture**</span>

```text id="k3v7"
FastAPI App
      ↓
Includes multiple routers
      ↓
Each router contains related endpoints
```

---

# <span style="color:#2563eb">**Basic Folder Structure**</span>

Good beginner structure:

```text id="p6m1"
project/

│
├── main.py
├── database.py
├── models.py
├── schemas.py
│
├── routers/
│     ├── users.py
│     ├── posts.py
│     └── auth.py
```

---

# <span style="color:#2563eb">**STEP-BY-STEP Implementation**</span>

Now let us build complete modular routing system.

---

# <span style="color:#2563eb">**STEP 1 — Create Router File**</span>

Create:

```text id="u4x9"
routers/users.py
```

---

# <span style="color:#2563eb">**users.py**</span>

```python id="f1m8"
from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def get_users():

    return {
        "message": "all users"
    }


@router.get("/{user_id}")
def get_user(user_id: int):

    return {
        "user_id": user_id
    }
```

---

# <span style="color:#2563eb">**Important Components**</span>

---

# <span style="color:#dc2626">**1. APIRouter()**</span>

```python id="w2m5"
router = APIRouter()
```

Creates isolated router object.

This router internally stores:

- routes
- metadata
- dependencies
- tags

---

# <span style="color:#dc2626">**2. @router.get() Instead of @app.get()**</span>

```python id="z8x1"
@router.get("/")
```

means:

```text id="n4v7"
Register route INSIDE router
```

NOT directly into global app yet.

---

# <span style="color:#2563eb">**Internal Mental Model**</span>

```text id="t1m9"
Router collects routes locally
```

---

# <span style="color:#2563eb">**STEP 2 — Include Router in Main App**</span>

Now:

```text id="q5x7"
main.py
```

---

# <span style="color:#2563eb">**main.py**</span>

```python id="m8v4"
from fastapi import FastAPI

from routers.users import router as users_router

app = FastAPI()


app.include_router(
    users_router,
    prefix="/users",
    tags=["Users"]
)
```

---

# <span style="color:#2563eb">**How include_router Works Internally**</span>

This is VERY important.

---

# <span style="color:#dc2626">**Router Before Inclusion**</span>

Router contains:

```text id="c7m1"
"/"
"/{user_id}"
```

locally.

---

# <span style="color:#dc2626">**After Inclusion with Prefix**</span>

```python id="j2v9"
prefix="/users"
```

FastAPI transforms routes into:

```text id="v3m8"
/users/
/users/{user_id}
```

---

# <span style="color:#2563eb">**Mental Model**</span>

```text id="b8x2"
include_router()
    =
Attach mini app into main app
```

---

# <span style="color:#2563eb">**Deep Internal Working**</span>

Internally:

```text id="r4m7"
APIRouter stores route definitions
```

Then:

```python id="d7x1"
app.include_router(...)
```

copies/merges router routes into main application's routing table.

---

# <span style="color:#2563eb">**Internal Routing Table After Inclusion**</span>

```text id="x9m3"
GET /users/
GET /users/{user_id}
```

Now app can dispatch requests correctly.

---

# <span style="color:#2563eb">**Dry Run — Complete Request Flow**</span>

Suppose client requests:

```http id="u3v8"
GET /users/5
```

---

# <span style="color:#dc2626">**STEP 1 — Uvicorn Receives Request**</span>

ASGI server receives HTTP request.

---

# <span style="color:#dc2626">**STEP 2 — FastAPI Checks Routing Table**</span>

Routing table contains:

```text id="m9x4"
/users/{user_id}
```

Route matches.

---

# <span style="color:#dc2626">**STEP 3 — Path Parameter Extracted**</span>

```python id="a2v7"
user_id = 5
```

---

# <span style="color:#dc2626">**STEP 4 — Route Function Called**</span>

```python id="f5x1"
get_user(user_id=5)
```

---

# <span style="color:#dc2626">**STEP 5 — Response Serialized**</span>

```json id="m1k8"
{
  "user_id": 5
}
```

returned.

---

# <span style="color:#2563eb">**Why Separate Routers by Feature?**</span>

This follows:

# <span style="color:#dc2626">**Separation of Concerns**

---

# <span style="color:#2563eb">**Bad Architecture**</span>

```text id="q4v6"
main.py contains:
- users
- products
- auth
- comments
- admin
- payments
```

Huge coupling.

---

# <span style="color:#2563eb">**Good Architecture**</span>

```text id="t7x2"
users router
    handles user domain

posts router
    handles post domain
```

Each module isolated logically.

---

# <span style="color:#2563eb">**Why This Matters in Real Teams**</span>

In production:

different developers often own:

- auth service
- payments
- users
- analytics

Modular routing enables parallel development.

---

# <span style="color:#2563eb">**Advanced Router Features**</span>

Routers can also contain:

- dependencies
- middleware-like behavior
- tags
- prefixes
- response models

---

# <span style="color:#2563eb">**Example with Prefix and Tags**</span>

```python id="q8m1"
router = APIRouter(
    prefix="/posts",
    tags=["Posts"]
)
```

Now every route automatically prefixed.

---

# <span style="color:#2563eb">**Better Modular Syntax**</span>

## <span style="color:#16a34a">**posts.py**</span>

```python id="m3x8"
from fastapi import APIRouter

router = APIRouter(
    prefix="/posts",
    tags=["Posts"]
)


@router.get("/")
def get_posts():

    return {"posts": []}
```

---

# <span style="color:#2563eb">**Then main.py Simplifies**</span>

```python id="r5v2"
from fastapi import FastAPI

from routers.posts import router as posts_router

app = FastAPI()

app.include_router(posts_router)
```

Cleaner.

---

# <span style="color:#2563eb">**Best Practices for Routers in FastAPI**</span>

---

# <span style="color:#dc2626">**1. Group Routes by Domain/Feature**</span>

Good:

```text id="n7m4"
users.py
posts.py
auth.py
```

Bad:

```text id="k2x9"
misc.py
everything.py
```

---

# <span style="color:#dc2626">**2. Keep main.py Thin**</span>

main.py should mainly:

- create app
- include routers
- configure middleware
- startup/shutdown

NOT contain business logic.

---

# <span style="color:#dc2626">**3. Use Separate Layers**</span>

Avoid putting:

- DB logic
- business logic
- validation logic

directly inside routes.

Later separate:

```text id="v8m6"
routes
services
repositories
schemas
models
```

---

# <span style="color:#dc2626">**4. Use Prefixes Consistently**</span>

Example:

```text id="b4x1"
/users
/posts
/comments
```

Improves API clarity.

---

# <span style="color:#dc2626">**5. Use Tags for Documentation**</span>

```python id="d2v7"
tags=["Users"]
```

Organizes Swagger/OpenAPI docs nicely.

---

# <span style="color:#2563eb">**Production-Level Folder Structure**</span>

Good scalable structure:

```text id="h6m3"
app/

├── main.py
│
├── routers/
│     ├── users.py
│     ├── posts.py
│     └── auth.py
│
├── services/
│
├── repositories/
│
├── schemas/
│
├── models/
│
├── database/
│
└── core/
```

This scales MUCH better.

---

# <span style="color:#2563eb">**Deepest Mental Model**</span>

```text id="y1x5"
APIRouter
    =
Feature-specific route container
```

and:

```text id="u1v9"
include_router()
    =
Attach modular route subsystem
into global application
```

The modular routing approach fundamentally exists to solve:

# <span style="color:#dc2626">**growing software complexity**

through:

- isolation
- separation of concerns
- maintainability
- scalability
- team collaboration
