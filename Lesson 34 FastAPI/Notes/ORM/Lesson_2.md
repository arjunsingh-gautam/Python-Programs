# <span style="color:#2563eb">**Setting Up Database in FastAPI using SQLAlchemy + SQLite**</span>

We will deeply cover:

1. Why database setup is needed
2. SQLAlchemy architecture
3. Boilerplate setup
4. Important components
5. Session concept
6. Dependency Injection concept
7. Internal mechanics
8. Best practices
9. Mental models
10. Analogies

---

# <span style="color:#2563eb">**Big Picture Architecture**</span>

```text id="m1x7"
FastAPI Route
      ↓
Dependency Injection
      ↓
Database Session
      ↓
SQLAlchemy ORM
      ↓
SQLite Database
```

---

# <span style="color:#2563eb">**What Problem Are We Solving?**</span>

Applications need persistent storage.

Without database:

```python id="q4v2"
users = []
```

Data disappears when server restarts.

Database provides:

- persistence
- querying
- relationships
- transactions
- scalability

---

# <span style="color:#2563eb">**Why SQLAlchemy?**</span>

[SQLAlchemy](https://www.sqlalchemy.org/?utm_source=chatgpt.com) is the most popular Python ORM.

It provides:

- ORM layer
- SQL abstraction
- connection management
- transaction handling
- query building

---

# <span style="color:#2563eb">**Why SQLite?**</span>

SQLite is lightweight and file-based.

Good for:

- learning
- prototypes
- local apps
- small systems

No separate DB server required.

---

# <span style="color:#2563eb">**Mental Model of SQLAlchemy + FastAPI**</span>

Think of:

| Component            | Analogy                     |
| -------------------- | --------------------------- |
| FastAPI              | Restaurant front desk       |
| SQLAlchemy           | Waiter/translator           |
| Session              | Conversation/order ticket   |
| SQLite               | Kitchen/database            |
| Dependency Injection | Automatic waiter assignment |

---

# <span style="color:#2563eb">**Project Structure Best Practice**</span>

```text id="t7x1"
project/
│
├── main.py
├── database.py
├── models/
│   └── user.py
├── schemas/
│   └── user.py
├── routes/
│   └── user.py
└── services/
```

---

# <span style="color:#2563eb">**Step 1 — Install Dependencies**</span>

```bash id="x2m8"
pip install fastapi sqlalchemy uvicorn
```

SQLite already included in Python.

---

# <span style="color:#2563eb">**Step 2 — Create Database Setup File**</span>

## <span style="color:#16a34a">**database.py**</span>

```python id="n9v3"
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base

DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()
```

---

# <span style="color:#2563eb">**Understanding Important Components**</span>

---

# <span style="color:#dc2626">**1. DATABASE_URL**</span>

```python id="a5m2"
DATABASE_URL = "sqlite:///./test.db"
```

Defines database location.

---

## <span style="color:#16a34a">**SQLite URL Breakdown**</span>

```text id="r8x4"
sqlite:///./test.db
```

means:

| Part      | Meaning         |
| --------- | --------------- |
| sqlite    | database type   |
| ///       | local file path |
| ./test.db | DB file         |

---

# <span style="color:#dc2626">**2. create_engine()**</span>

```python id="k3v7"
engine = create_engine(...)
```

---

## <span style="color:#16a34a">**What is Engine?**</span>

Engine is:

# <span style="color:#dc2626">**Database communication manager**</span>

It manages:

- DB connections
- SQL execution
- connection pooling

---

## <span style="color:#16a34a">**Mental Model**</span>

```text id="p6m1"
Engine
   =
Bridge between application and database
```

---

# <span style="color:#dc2626">**3. connect_args**</span>

```python id="u4x9"
connect_args={"check_same_thread": False}
```

SQLite restriction workaround.

SQLite normally allows one thread only.

FastAPI uses multiple threads.

This setting prevents thread issues.

---

# <span style="color:#dc2626">**4. sessionmaker()**</span>

```python id="f1m8"
SessionLocal = sessionmaker(...)
```

Creates:

# <span style="color:#dc2626">**Session factory**</span>

Not actual session.

It creates session objects later.

---

# <span style="color:#2563eb">**What is a Session?**</span>

# <span style="color:#dc2626">**Most Important ORM Concept**</span>

A session represents:

> A temporary conversation/workspace with database.

---

# <span style="color:#2563eb">**Feynman Analogy of Session**</span>

Imagine bank visit.

---

## <span style="color:#16a34a">**Without Session**</span>

Every action:

```text id="w2m5"
Open account
Deposit
Withdraw
```

requires new conversation from scratch.

Very inefficient.

---

## <span style="color:#16a34a">**With Session**</span>

You get:

```text id="z8x1"
One active banking session
```

All operations happen inside that interaction.

Then finalized.

---

# <span style="color:#2563eb">**Technical Meaning of Session**</span>

Session tracks:

- object changes
- queries
- transactions
- DB state

Session is:

```text id="n4v7"
ORM transaction workspace
```

---

# <span style="color:#2563eb">**What Session Internally Does**</span>

Session manages:

| Task            | Description             |
| --------------- | ----------------------- |
| Query execution | Runs SQL                |
| Change tracking | Detect modified objects |
| Transactions    | Commit/rollback         |
| Identity map    | Cache loaded objects    |

---

# <span style="color:#2563eb">**Session Lifecycle**</span>

```text id="t1m9"
Open Session
      ↓
Run Queries
      ↓
Track Changes
      ↓
Commit/Rollback
      ↓
Close Session
```

---

# <span style="color:#2563eb">**What is declarative_base()?**</span>

```python id="q5x7"
Base = declarative_base()
```

Creates:

# <span style="color:#dc2626">**Base ORM class**</span>

All ORM models inherit from it.

---

# <span style="color:#2563eb">**Why Needed?**</span>

Allows SQLAlchemy to:

- detect models
- map tables
- generate metadata

---

# <span style="color:#2563eb">**Step 3 — Create ORM Model**</span>

## <span style="color:#16a34a">**models/user.py**</span>

```python id="m8v4"
from sqlalchemy import Column, Integer, String
from database import Base

class User(Base):

    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
```

---

# <span style="color:#2563eb">**Understanding ORM Model Components**</span>

---

# <span style="color:#dc2626">**1. tablename**</span>

```python id="c7m1"
__tablename__ = "users"
```

Maps model to DB table.

---

# <span style="color:#dc2626">**2. Column()**</span>

Defines DB column.

Example:

```python id="j2v9"
name = Column(String)
```

maps to:

```sql id="v3m8"
name VARCHAR
```

---

# <span style="color:#dc2626">**3. primary_key=True**</span>

Marks unique identifier.

---

# <span style="color:#2563eb">**Mental Mapping**</span>

| Python    | Database |
| --------- | -------- |
| Class     | Table    |
| Object    | Row      |
| Attribute | Column   |

---

# <span style="color:#2563eb">**Step 4 — Create Tables**</span>

## <span style="color:#16a34a">**main.py**</span>

```python id="b8x2"
from fastapi import FastAPI
from database import engine, Base
from models.user import User

app = FastAPI()

Base.metadata.create_all(bind=engine)
```

---

# <span style="color:#2563eb">**What Happens Internally?**</span>

SQLAlchemy scans models:

```python id="r4m7"
class User(Base)
```

Generates SQL:

```sql id="d7x1"
CREATE TABLE users (...)
```

Executes against SQLite.

---

# <span style="color:#2563eb">**Step 5 — Dependency Injection for DB Session**</span>

# <span style="color:#dc2626">**What is Dependency Injection?**</span>

Dependency Injection means:

> Automatically providing required resources to functions.

---

# <span style="color:#2563eb">**Simple Analogy**</span>

Imagine restaurant.

Customer orders food.

Chef automatically receives:

- utensils
- ingredients
- gas stove

without manually creating them every time.

Dependency injection similarly provides:

```text id="x9m3"
Database session
Authentication
Config
Services
```

automatically.

---

# <span style="color:#2563eb">**Database Dependency Function**</span>

```python id="u3v8"
from database import SessionLocal

def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()
```

---

# <span style="color:#2563eb">**Understanding Important Components**</span>

---

# <span style="color:#dc2626">**1. SessionLocal()**</span>

```python id="m9x4"
db = SessionLocal()
```

Creates actual database session.

---

# <span style="color:#dc2626">**2. yield**</span>

```python id="a2v7"
yield db
```

Temporarily gives session to route.

---

# <span style="color:#2563eb">**Why yield Instead of return?**</span>

Because FastAPI needs:

```text id="f5x1"
Setup
↓
Use
↓
Cleanup
```

yield allows cleanup after request completes.

---

# <span style="color:#dc2626">**3. finally**</span>

```python id="m1k8"
db.close()
```

Ensures session closes even if error occurs.

Very important.

---

# <span style="color:#2563eb">**Why Closing Sessions Matters**</span>

Without closing:

- memory leaks
- connection exhaustion
- locked DB resources

occur.

---

# <span style="color:#2563eb">**Step 6 — Using Dependency Injection in Route**</span>

```python id="q4v6"
from fastapi import Depends
from sqlalchemy.orm import Session

@app.get("/users")
def get_users(
    db: Session = Depends(get_db)
):

    return db.query(User).all()
```

---

# <span style="color:#2563eb">**What Happens Internally?**</span>

---

## <span style="color:#16a34a">**Step 1 — Request Comes**</span>

```text id="t7x2"
GET /users
```

---

## <span style="color:#16a34a">**Step 2 — FastAPI Detects Dependency**</span>

```python id="z7m3"
Depends(get_db)
```

---

## <span style="color:#16a34a">**Step 3 — Executes get_db()**</span>

Creates session:

```python id="p3v7"
db = SessionLocal()
```

---

## <span style="color:#16a34a">**Step 4 — Injects Session into Route**</span>

```python id="w6x2"
db
```

passed automatically.

---

## <span style="color:#16a34a">**Step 5 — Route Uses Session**</span>

```python id="n8v1"
db.query(User).all()
```

---

## <span style="color:#16a34a">**Step 6 — Request Ends**</span>

finally block runs:

```python id="r2m5"
db.close()
```

---

# <span style="color:#2563eb">**Why Dependency Injection is Powerful**</span>

Without DI:

```python id="k5v7"
db = SessionLocal()
```

inside every route.

Huge duplication.

DI centralizes resource management.

---

# <span style="color:#2563eb">**Best Practices**</span>

---

# <span style="color:#dc2626">**1. One Session Per Request**</span>

Very important.

Avoid global sessions.

---

# <span style="color:#dc2626">**2. Always Close Sessions**</span>

Use:

```python id="m4x1"
try/finally
```

or dependency injection.

---

# <span style="color:#dc2626">**3. Separate Models and Schemas**</span>

ORM models ≠ Pydantic schemas.

---

# <span style="color:#dc2626">**4. Use Dependency Injection for DB Access**</span>

Cleaner architecture.

---

# <span style="color:#dc2626">**5. Keep DB Logic in Services/Repositories**</span>

Avoid large route functions.

---

# <span style="color:#2563eb">**Common Beginner Mistakes**</span>

---

# <span style="color:#dc2626">**1. Not Closing Sessions**</span>

Causes connection leaks.

---

# <span style="color:#dc2626">**2. Using Global Session**</span>

Very dangerous.

Sessions are not thread-safe.

---

# <span style="color:#dc2626">**3. Mixing ORM Models with API Responses**</span>

Can expose hidden fields.

---

# <span style="color:#dc2626">**4. Using SQLite in Production**</span>

SQLite is not ideal for high concurrency.

---

# <span style="color:#2563eb">**Final Mental Models**</span>

---

# <span style="color:#dc2626">**ORM Mental Model**</span>

```text id="y1v6"
ORM
=
Translator between Python objects and SQL
```

---

# <span style="color:#dc2626">**Session Mental Model**</span>

```text id="m8p3"
Session
=
Temporary conversation workspace with database
```

---

# <span style="color:#dc2626">**Dependency Injection Mental Model**</span>

```text id="g7x2"
Dependency Injection
=
Automatic resource provider
```

---

# <span style="color:#dc2626">**Engine Mental Model**</span>

```text id="d4m9"
Engine
=
Database communication bridge
```
