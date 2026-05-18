# <span style="color:#2563eb">**What are CRUD APIs?**</span>

CRUD stands for:

| Letter | Meaning |
| ------ | ------- |
| C      | Create  |
| R      | Read    |
| U      | Update  |
| D      | Delete  |

CRUD APIs are APIs that perform these four fundamental operations on data.

---

# <span style="color:#2563eb">**Simple Example**</span>

Suppose you have a Notes application.

CRUD operations would be:

| Operation | Meaning     |
| --------- | ----------- |
| Create    | Add note    |
| Read      | Fetch note  |
| Update    | Edit note   |
| Delete    | Remove note |

---

# <span style="color:#2563eb">**Why Most Systems are CRUD APIs**</span>

This is a very important systems insight.

Most software systems fundamentally revolve around:

# <span style="color:#dc2626">**Managing state/data over time**</span>

Almost every application stores and manipulates information.

Examples:

| System          | Managed Data          |
| --------------- | --------------------- |
| Instagram       | posts/users/comments  |
| Banking app     | accounts/transactions |
| E-commerce      | products/orders       |
| Hospital system | patients/reports      |
| School portal   | students/courses      |

At core, all these systems mainly:

- create data
- retrieve data
- modify data
- remove data

which is exactly CRUD.

---

# <span style="color:#2563eb">**Causality of CRUD APIs**</span>

# <span style="color:#dc2626">**Why Did CRUD APIs Naturally Emerge?**</span>

Because databases themselves fundamentally support CRUD operations.

Databases store:

```text id="m1x7"
Persistent state
```

The most fundamental operations on state are:

```text id="q4v2"
Create
Read
Update
Delete
```

Therefore backend APIs naturally evolved to expose those same operations over HTTP.

---

# <span style="color:#2563eb">**Mental Model of CRUD APIs**</span>

```text id="p8m5"
CRUD APIs
    =
Remote interface for manipulating persistent state
```

---

# <span style="color:#2563eb">**Feynman Analogy**</span>

Imagine library management system.

Books can only fundamentally be:

| Action         | CRUD Mapping |
| -------------- | ------------ |
| Add book       | Create       |
| View book      | Read         |
| Edit book info | Update       |
| Remove book    | Delete       |

Most information systems behave similarly.

---

# <span style="color:#2563eb">**Why CRUD Became Dominant in Web Systems**</span>

Because most business software is essentially:

# <span style="color:#dc2626">**State management systems**

Examples:

- inventory systems
- HR systems
- CMS
- blogs
- admin dashboards
- finance apps

Most backend work is:

```text id="t7x1"
moving structured data between:
clients ↔ databases
```

CRUD maps perfectly to this.

---

# <span style="color:#2563eb">**Constraints of CRUD APIs**</span>

CRUD APIs are extremely useful but have limitations.

---

# <span style="color:#dc2626">**1. Too Data-Centric**</span>

CRUD focuses heavily on database tables.

But real business workflows are often more complex.

Example:

```text id="x2m8"
Transfer money
```

is NOT simple CRUD.

It involves:

- validation
- transactions
- auditing
- multi-step operations

---

# <span style="color:#dc2626">**2. Weak Business Modeling**</span>

CRUD APIs often expose tables directly.

This can create:

- poor abstractions
- tightly coupled frontend/backend
- weak domain modeling

---

# <span style="color:#dc2626">**3. Complex Workflows Become Awkward**</span>

Example:

```text id="n9v3"
Checkout process
```

may require:

- inventory checks
- payment validation
- shipping logic
- notifications

Pure CRUD becomes insufficient.

---

# <span style="color:#dc2626">**4. Can Encourage Anemic Architecture**</span>

Some CRUD systems become:

```text id="a5m2"
thin routes + direct DB operations
```

without real domain logic.

---

# <span style="color:#2563eb">**Despite Constraints, CRUD Remains Foundational**</span>

Even complex systems internally still use CRUD heavily.

Because:

# <span style="color:#dc2626">**persistent state manipulation is universal**

---

# <span style="color:#2563eb">**How CRUD Links with HTTP Request Model**</span>

This is extremely important.

HTTP itself naturally maps to CRUD semantics.

---

# <span style="color:#2563eb">**HTTP Method ↔ CRUD Mapping**</span>

| HTTP Method | CRUD Operation |
| ----------- | -------------- |
| POST        | Create         |
| GET         | Read           |
| PUT/PATCH   | Update         |
| DELETE      | Delete         |

This mapping became REST convention.

---

# <span style="color:#2563eb">**Why HTTP Methods Exist**</span>

HTTP methods describe:

# <span style="color:#dc2626">**Intent of request**

Example:

| Method | Meaning           |
| ------ | ----------------- |
| GET    | retrieve resource |
| POST   | create resource   |
| PUT    | replace resource  |
| PATCH  | partially modify  |
| DELETE | remove resource   |

---

# <span style="color:#2563eb">**Mental Model**</span>

```text id="r8x4"
HTTP Method
     =
Operation intent

CRUD
     =
Database action
```

REST APIs connect both worlds.

---

# <span style="color:#2563eb">**Detailed CRUD + HTTP Flow**</span>

Suppose:

```text id="k3v7"
/notes
```

represents note resources.

---

# <span style="color:#dc2626">**CREATE Operation**</span>

```http id="p6m1"
POST /notes
```

Request body:

```json id="u4x9"
{
  "title": "Learn FastAPI"
}
```

Meaning:

```text id="f1m8"
Create new note
```

---

# <span style="color:#dc2626">**READ Operation**</span>

```http id="w2m5"
GET /notes/1
```

Meaning:

```text id="z8x1"
Fetch note with ID 1
```

---

# <span style="color:#dc2626">**UPDATE Operation**</span>

```http id="n4v7"
PUT /notes/1
```

Meaning:

```text id="t1m9"
Modify note 1
```

---

# <span style="color:#dc2626">**DELETE Operation**</span>

```http id="q5x7"
DELETE /notes/1
```

Meaning:

```text id="m8v4"
Remove note 1
```

---

# <span style="color:#2563eb">**Complete Mental Model of CRUD APIs**</span>

```text id="c7m1"
HTTP Request
      ↓
FastAPI Route
      ↓
Pydantic Validation
      ↓
Session Injection
      ↓
ORM Operation
      ↓
SQL Query
      ↓
Database
      ↓
ORM Result
      ↓
Pydantic Serialization
      ↓
HTTP Response
```

This lifecycle repeats for almost all CRUD systems.

---

# <span style="color:#2563eb">**How to Write CRUD APIs in FastAPI**</span>

Now let us implement complete example.

---

# <span style="color:#dc2626">**Example — Student CRUD API**</span>

We will implement:

| Route                 | Purpose  |
| --------------------- | -------- |
| POST /students        | Create   |
| GET /students         | Read all |
| GET /students/{id}    | Read one |
| PUT /students/{id}    | Update   |
| DELETE /students/{id} | Delete   |

---

# <span style="color:#2563eb">**STEP 1 — Database Setup**</span>

## <span style="color:#16a34a">**database.py**</span>

```python id="j2v9"
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import DeclarativeBase

DATABASE_URL = "sqlite:///./students.db"

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(bind=engine)

class Base(DeclarativeBase):
    pass
```

---

# <span style="color:#2563eb">**STEP 2 — ORM Model**</span>

## <span style="color:#16a34a">**models.py**</span>

```python id="v3m8"
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from database import Base

class Student(Base):

    __tablename__ = "students"

    id: Mapped[int] = mapped_column(
        primary_key=True
    )

    name: Mapped[str]

    age: Mapped[int]
```

---

# <span style="color:#2563eb">**STEP 3 — Pydantic Schemas**</span>

## <span style="color:#16a34a">**schemas.py**</span>

```python id="b8x2"
from pydantic import BaseModel

class StudentCreate(BaseModel):

    name: str
    age: int

class StudentResponse(BaseModel):

    id: int
    name: str
    age: int
```

---

# <span style="color:#2563eb">**STEP 4 — Main FastAPI App**</span>

## <span style="color:#16a34a">**main.py**</span>

```python id="r4m7"
from fastapi import FastAPI
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session
from sqlalchemy import select

from database import engine
from database import Base
from database import SessionLocal

from models import Student
from schemas import StudentCreate

app = FastAPI()

Base.metadata.create_all(bind=engine)

def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()
```

---

# <span style="color:#2563eb">**CREATE API**</span>

```python id="d7x1"
@app.post("/students")
def create_student(
    student: StudentCreate,
    db: Session = Depends(get_db)
):

    db_student = Student(
        name=student.name,
        age=student.age
    )

    db.add(db_student)

    db.commit()

    db.refresh(db_student)

    return db_student
```

---

# <span style="color:#2563eb">**Mental Flow of CREATE**</span>

```text id="x9m3"
Request JSON
      ↓
Pydantic Validation
      ↓
ORM Object Creation
      ↓
Session Tracking
      ↓
INSERT SQL
      ↓
Database Commit
      ↓
Response Return
```

---

# <span style="color:#2563eb">**READ ALL API**</span>

```python id="u3v8"
@app.get("/students")
def get_students(
    db: Session = Depends(get_db)
):

    stmt = select(Student)

    result = db.execute(stmt)

    students = result.scalars().all()

    return students
```

---

# <span style="color:#2563eb">**READ ONE API**</span>

```python id="m9x4"
@app.get("/students/{id}")
def get_student(
    id: int,
    db: Session = Depends(get_db)
):

    student = db.get(Student, id)

    if not student:

        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return student
```

---

# <span style="color:#2563eb">**UPDATE API**</span>

```python id="a2v7"
@app.put("/students/{id}")
def update_student(
    id: int,
    student_data: StudentCreate,
    db: Session = Depends(get_db)
):

    student = db.get(Student, id)

    if not student:

        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    student.name = student_data.name
    student.age = student_data.age

    db.commit()

    db.refresh(student)

    return student
```

---

# <span style="color:#2563eb">**DELETE API**</span>

```python id="f5x1"
@app.delete("/students/{id}")
def delete_student(
    id: int,
    db: Session = Depends(get_db)
):

    student = db.get(Student, id)

    if not student:

        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    db.delete(student)

    db.commit()

    return {
        "message": "Deleted successfully"
    }
```

---

# <span style="color:#2563eb">**Most Important CRUD API Mental Model**</span>

Every CRUD API fundamentally follows:

```text id="m1k8"
Receive Request
      ↓
Validate Input
      ↓
Acquire Session
      ↓
Perform ORM Operation
      ↓
Commit Transaction
      ↓
Serialize Response
      ↓
Return HTTP Response
```

This pattern repeats almost everywhere.

---

# <span style="color:#2563eb">**Important SQLAlchemy CRUD Constructs**</span>

| Construct      | Purpose              |
| -------------- | -------------------- |
| `db.add()`     | insert object        |
| `db.get()`     | fetch by primary key |
| `select()`     | build query          |
| `db.execute()` | execute query        |
| `scalars()`    | extract ORM objects  |
| `db.commit()`  | persist transaction  |
| `db.refresh()` | reload DB state      |
| `db.delete()`  | remove object        |

---

# <span style="color:#2563eb">**Best Practices for CRUD APIs**</span>

---

# <span style="color:#dc2626">**1. Separate Models and Schemas**</span>

ORM models ≠ API schemas.

---

# <span style="color:#dc2626">**2. Use Dependency Injection for Sessions**</span>

Never create sessions manually everywhere.

---

# <span style="color:#dc2626">**3. Validate Input with Pydantic**</span>

Never trust raw request data.

---

# <span style="color:#dc2626">**4. Handle Missing Resources Properly**</span>

Use:

```python id="q4x8"
HTTPException(404)
```

---

# <span style="color:#dc2626">**5. Keep Routes Thin**</span>

Business logic should later move into service layer.

---

# <span style="color:#2563eb">**Final Mental Model**</span>

CRUD APIs are fundamentally:

# <span style="color:#dc2626">**HTTP interfaces for manipulating persistent database state**

They connect:

```text id="t8m2"
HTTP semantics
       ↔
Business operations
       ↔
Database state transitions
```

using:

- routes
- schemas
- sessions
- ORM models
- transactions
- serialization

as the core architectural building blocks.
