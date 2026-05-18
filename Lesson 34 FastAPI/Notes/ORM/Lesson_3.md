# <span style="color:#2563eb">**Modern SQLAlchemy 2.x Style in Python 3.14**</span>

Modern [SQLAlchemy](https://www.sqlalchemy.org/?utm_source=chatgpt.com) (especially 2.x style) changed significantly from old SQLAlchemy syntax.

Modern SQLAlchemy focuses on:

- type-safe ORM
- Python typing
- declarative mapping
- explicit sessions
- cleaner querying
- modern async support

The modern style is:

# <span style="color:#dc2626">**Typed Declarative ORM Style**</span>

---

# <span style="color:#2563eb">**Mental Model of SQLAlchemy Constructs**</span>

| SQL World   | SQLAlchemy World |
| ----------- | ---------------- |
| Table       | ORM class        |
| Row         | Object           |
| SELECT      | `select()`       |
| INSERT      | `add()`          |
| UPDATE      | modify object    |
| DELETE      | `delete()`       |
| Transaction | Session          |
| Connection  | Engine           |

---

# <span style="color:#2563eb">**Modern SQLAlchemy Core Architecture**</span>

```text id="m1x7"
Application
     ↓
Session
     ↓
ORM Models
     ↓
SQLAlchemy Query Builder
     ↓
Generated SQL
     ↓
Database
```

---

# <span style="color:#2563eb">**1. Modern Table Schema Generation Syntax**</span>

# <span style="color:#dc2626">**Modern Declarative Base Syntax**</span>

```python id="q4v2"
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass
```

---

# <span style="color:#2563eb">**Why Modern Syntax Exists**</span>

Older style:

```python id="p8m5"
Base = declarative_base()
```

Modern SQLAlchemy prefers:

```python id="t7x1"
class Base(DeclarativeBase)
```

because:

- better typing
- better IDE support
- cleaner inheritance model

---

# <span style="color:#2563eb">**Modern ORM Model Syntax**</span>

```python id="x2m8"
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

class User(Base):

    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)

    name: Mapped[str]

    age: Mapped[int]
```

---

# <span style="color:#2563eb">**Understanding Important Modern Constructs**</span>

---

# <span style="color:#dc2626">**1. Mapped[T]**</span>

```python id="n9v3"
Mapped[int]
```

means:

```text id="a5m2"
ORM-managed mapped field of type int
```

---

## <span style="color:#16a34a">**Why Important?**</span>

Enables:

- type safety
- IDE autocomplete
- static analysis
- better ORM integration

---

# <span style="color:#dc2626">**2. mapped_column()**</span>

```python id="r8x4"
mapped_column(primary_key=True)
```

Defines database column metadata.

Equivalent SQL:

```sql id="k3v7"
PRIMARY KEY
```

---

# <span style="color:#2563eb">**Modern vs Old Syntax**</span>

| Old                  | Modern            |
| -------------------- | ----------------- |
| `Column(Integer)`    | `Mapped[int]`     |
| `Column(String)`     | `Mapped[str]`     |
| `declarative_base()` | `DeclarativeBase` |

---

# <span style="color:#2563eb">**Modern Full Schema Example**</span>

```python id="p6m1"
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

class Base(DeclarativeBase):
    pass

class User(Base):

    __tablename__ = "users"

    id: Mapped[int] = mapped_column(
        primary_key=True
    )

    name: Mapped[str]

    email: Mapped[str]

    age: Mapped[int]
```

---

# <span style="color:#2563eb">**DDL Concepts in SQLAlchemy**</span>

# <span style="color:#dc2626">**What is DDL?**</span>

DDL means:

# <span style="color:#dc2626">**Data Definition Language**</span>

Operations that define database structure.

Examples:

| SQL          | Meaning          |
| ------------ | ---------------- |
| CREATE TABLE | create structure |
| ALTER TABLE  | modify structure |
| DROP TABLE   | remove structure |

---

# <span style="color:#2563eb">**SQLAlchemy DDL Generation**</span>

```python id="u4x9"
Base.metadata.create_all(engine)
```

---

# <span style="color:#2563eb">**What Happens Internally?**</span>

SQLAlchemy scans ORM models.

Generates SQL automatically:

```sql id="f1m8"
CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    name VARCHAR,
    email VARCHAR,
    age INTEGER
);
```

---

# <span style="color:#2563eb">**Mental Model**</span>

```text id="w2m5"
Python ORM Models
        ↓
SQLAlchemy Metadata System
        ↓
DDL SQL Generation
        ↓
Database Schema
```

---

# <span style="color:#2563eb">**Important Table Constraints Syntax**</span>

---

# <span style="color:#dc2626">**1. Primary Key**</span>

```python id="z8x1"
id: Mapped[int] = mapped_column(
    primary_key=True
)
```

---

# <span style="color:#dc2626">**2. Unique Constraint**</span>

```python id="n4v7"
email: Mapped[str] = mapped_column(
    unique=True
)
```

---

# <span style="color:#dc2626">**3. Nullable Constraint**</span>

```python id="t1m9"
name: Mapped[str] = mapped_column(
    nullable=False
)
```

---

# <span style="color:#dc2626">**4. Default Values**</span>

```python id="q5x7"
age: Mapped[int] = mapped_column(
    default=18
)
```

---

# <span style="color:#dc2626">**5. Foreign Keys**</span>

```python id="m8v4"
from sqlalchemy import ForeignKey

user_id: Mapped[int] = mapped_column(
    ForeignKey("users.id")
)
```

---

# <span style="color:#2563eb">**Relationships in Modern SQLAlchemy**</span>

```python id="c7m1"
from sqlalchemy.orm import relationship

class User(Base):

    __tablename__ = "users"

    id: Mapped[int] = mapped_column(
        primary_key=True
    )

    posts: Mapped[list["Post"]] = relationship(
        back_populates="user"
    )
```

---

# <span style="color:#2563eb">**Mental Model of Relationships**</span>

```text id="j2v9"
Foreign Key
      +
ORM Relationship Mapping
```

creates object-level relationships.

---

# <span style="color:#2563eb">**Modern Querying Syntax (DML Operations)**</span>

# <span style="color:#dc2626">**What is DML?**</span>

DML means:

# <span style="color:#dc2626">**Data Manipulation Language**</span>

Operations that manipulate rows.

Examples:

| SQL    | Meaning |
| ------ | ------- |
| SELECT | read    |
| INSERT | create  |
| UPDATE | modify  |
| DELETE | remove  |

---

# <span style="color:#2563eb">**Modern Session Setup**</span>

```python id="v3m8"
from sqlalchemy.orm import Session
```

Session is central for DML operations.

---

# <span style="color:#2563eb">**1. INSERT Operation**</span>

# <span style="color:#dc2626">**Modern Syntax**</span>

```python id="b8x2"
with Session(engine) as session:

    user = User(
        name="Arjun",
        email="a@gmail.com",
        age=22
    )

    session.add(user)

    session.commit()
```

---

# <span style="color:#2563eb">**Internal Flow**</span>

```text id="r4m7"
Python Object
      ↓
Session Tracking
      ↓
INSERT SQL Generated
      ↓
Database Insert
```

---

# <span style="color:#2563eb">**Generated SQL Internally**</span>

```sql id="d7x1"
INSERT INTO users (
    name,
    email,
    age
)
VALUES (
    'Arjun',
    'a@gmail.com',
    22
);
```

---

# <span style="color:#2563eb">**Important Constructs**</span>

| Construct       | Purpose             |
| --------------- | ------------------- |
| `session.add()` | track object        |
| `commit()`      | persist transaction |

---

# <span style="color:#2563eb">**2. SELECT Query Syntax**</span>

Modern SQLAlchemy uses:

# <span style="color:#dc2626">**select() construct**</span>

---

## <span style="color:#16a34a">**Basic Query**</span>

```python id="x9m3"
from sqlalchemy import select

stmt = select(User)
```

---

# <span style="color:#2563eb">**Executing Query**</span>

```python id="u3v8"
with Session(engine) as session:

    stmt = select(User)

    result = session.execute(stmt)

    users = result.scalars().all()
```

---

# <span style="color:#2563eb">**Understanding Important Constructs**</span>

---

# <span style="color:#dc2626">**1. select(User)**</span>

Creates SQL query object.

Equivalent SQL:

```sql id="m9x4"
SELECT * FROM users;
```

---

# <span style="color:#dc2626">**2. session.execute()**</span>

Sends SQL to database.

---

# <span style="color:#dc2626">**3. scalars()**</span>

Extracts ORM objects from result rows.

---

# <span style="color:#dc2626">**4. all()**</span>

Returns all rows as list.

---

# <span style="color:#2563eb">**Filtering Queries**</span>

```python id="a2v7"
stmt = select(User).where(
    User.age > 18
)
```

Equivalent SQL:

```sql id="f5x1"
SELECT *
FROM users
WHERE age > 18;
```

---

# <span style="color:#2563eb">**Multiple Conditions**</span>

```python id="m1k8"
stmt = select(User).where(
    User.age > 18,
    User.name == "Arjun"
)
```

---

# <span style="color:#2563eb">**Ordering Results**</span>

```python id="q4v6"
stmt = select(User).order_by(
    User.age.desc()
)
```

---

# <span style="color:#2563eb">**Limit Results**</span>

```python id="t7x2"
stmt = select(User).limit(5)
```

---

# <span style="color:#2563eb">**3. UPDATE Operation**</span>

---

## <span style="color:#16a34a">**Object-Oriented Style**</span>

```python id="z7m3"
with Session(engine) as session:

    user = session.get(User, 1)

    user.name = "Rahul"

    session.commit()
```

---

# <span style="color:#2563eb">**Internal Mechanism**</span>

Session tracks:

```python id="p3v7"
user.name changed
```

Automatically generates:

```sql id="w6x2"
UPDATE users
SET name = 'Rahul'
WHERE id = 1;
```

---

# <span style="color:#2563eb">**Why This is Powerful**</span>

You modify objects naturally.

ORM handles SQL generation.

---

# <span style="color:#2563eb">**4. DELETE Operation**</span>

```python id="n8v1"
with Session(engine) as session:

    user = session.get(User, 1)

    session.delete(user)

    session.commit()
```

---

# <span style="color:#2563eb">**Generated SQL**</span>

```sql id="r2m5"
DELETE FROM users
WHERE id = 1;
```

---

# <span style="color:#2563eb">**Modern Querying Philosophy**</span>

Modern SQLAlchemy encourages:

```text id="k5v7"
Explicit SQL construction
```

instead of old implicit query chains.

---

# <span style="color:#2563eb">**Old vs Modern Query Syntax**</span>

| Old Style             | Modern Style           |
| --------------------- | ---------------------- |
| `session.query(User)` | `select(User)`         |
| implicit querying     | explicit query objects |
| less typed            | fully typed            |

---

# <span style="color:#2563eb">**Session Context Manager Syntax**</span>

Modern best practice:

```python id="m4x1"
with Session(engine) as session:
```

---

# <span style="color:#2563eb">**Why Important?**</span>

Automatically handles:

- session closing
- cleanup
- resource management

---

# <span style="color:#2563eb">**Transaction Concepts**</span>

# <span style="color:#dc2626">**commit()**</span>

```python id="y1v6"
session.commit()
```

Permanently saves changes.

---

# <span style="color:#dc2626">**rollback()**</span>

```python id="m8p3"
session.rollback()
```

Undoes failed transaction.

---

# <span style="color:#2563eb">**Feynman Analogy for Transactions**</span>

Imagine online shopping.

Until payment confirmed:

```text id="g7x2"
Cart changes are temporary
```

commit() means:

```text id="d4m9"
Finalize order permanently
```

rollback() means:

```text id="h1v7"
Cancel operation safely
```

---

# <span style="color:#2563eb">**Important Modern SQLAlchemy Constructs**</span>

| Construct         | Purpose              |
| ----------------- | -------------------- |
| `Mapped[T]`       | typed ORM field      |
| `mapped_column()` | DB column definition |
| `select()`        | query builder        |
| `Session()`       | transaction/session  |
| `relationship()`  | ORM relationships    |
| `ForeignKey()`    | table relationships  |
| `commit()`        | save changes         |
| `rollback()`      | undo changes         |
| `scalars()`       | extract ORM objects  |
| `where()`         | filtering            |
| `order_by()`      | sorting              |
| `limit()`         | pagination           |

---

# <span style="color:#2563eb">**Best Practices**</span>

---

# <span style="color:#dc2626">**1. Use Modern Typed Syntax**</span>

Prefer:

```python id="j9m2"
Mapped[str]
```

over old `Column(String)` style.

---

# <span style="color:#dc2626">**2. Use Session Context Managers**</span>

Always:

```python id="u5v8"
with Session(engine)
```

---

# <span style="color:#dc2626">**3. Keep ORM Models Focused**</span>

Avoid huge god-models.

---

# <span style="color:#dc2626">**4. Separate ORM Models and Pydantic Schemas**</span>

Very important architecture principle.

---

# <span style="color:#dc2626">**5. Learn Underlying SQL**</span>

ORM does NOT replace SQL knowledge.

Critical best practice.

---

# <span style="color:#2563eb">**Common Beginner Mistakes**</span>

---

# <span style="color:#dc2626">**1. Forgetting commit()**</span>

Changes not saved.

---

# <span style="color:#dc2626">**2. Confusing ORM Object with Pydantic Schema**</span>

Different purposes.

---

# <span style="color:#dc2626">**3. Keeping Sessions Open Too Long**</span>

Can leak resources.

---

# <span style="color:#dc2626">**4. Using Old Query Syntax in New Projects**</span>

Modern style preferred.

---

# <span style="color:#2563eb">**Final Mental Models**</span>

---

# <span style="color:#dc2626">**Mapped[T]**</span>

```text id="v2m5"
Typed ORM-managed database field
```

---

# <span style="color:#dc2626">**Session**</span>

```text id="q7x9"
Temporary transaction workspace
```

---

# <span style="color:#dc2626">**select()**</span>

```text id="n4v1"
Python representation of SQL query
```

---

# <span style="color:#dc2626">**ORM Model**</span>

```text id="x8m3"
Python blueprint mapped to database table
```
