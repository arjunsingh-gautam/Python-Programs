# <span style="color:#2563eb">**What is a Relationship in Database Models?**</span>

A relationship represents:

> A connection between two database tables.

Real-world data is connected.

Examples:

| Entity    | Connected To |
| --------- | ------------ |
| User      | Posts        |
| Student   | Courses      |
| Customer  | Orders       |
| Blog Post | Comments     |

Databases model these connections using:

# <span style="color:#dc2626">**Relationships**</span>

---

# <span style="color:#2563eb">**Why Relationships Exist**</span>

Without relationships, data becomes:

* duplicated
* inconsistent
* hard to maintain
* difficult to query

Relationships solve:

# <span style="color:#dc2626">**Data association problem**</span>

---

# <span style="color:#2563eb">**Feynman Analogy**</span>

Imagine school.

Students and classrooms.

Without relationships:

Every classroom stores full student information repeatedly.

Huge duplication.

Instead:

```text id="m1x7"
Student ID references student
```

Efficient and structured.

That reference connection is relationship.

---

# <span style="color:#2563eb">**Mental Model of Relationships**</span>

```text id="q4v2"
One table points to another table
using identifiers
```

Usually through:

# <span style="color:#dc2626">**Foreign Keys**</span>

---

# <span style="color:#2563eb">**Types of Relationships**</span>

| Type         | Example            |
| ------------ | ------------------ |
| One-to-One   | User ↔ Profile     |
| One-to-Many  | User ↔ Posts       |
| Many-to-Many | Students ↔ Courses |

---

# <span style="color:#2563eb">**1. One-to-Many Relationship**</span>

Most common relationship.

Example:

```text id="p8m5"
One user can have many posts
```

---

# <span style="color:#2563eb">**Database Structure**</span>

## <span style="color:#16a34a">**users table**</span>

| id | name  |
| -- | ----- |
| 1  | Arjun |

---

## <span style="color:#16a34a">**posts table**</span>

| id | title | user_id |
| -- | ----- | ------- |
| 1  | Hello | 1       |
| 2  | SQL   | 1       |

---

# <span style="color:#2563eb">**What is user_id?**</span>

```text id="t7x1"
user_id
```

references:

```text id="x2m8"
users.id
```

This creates relationship.

---

# <span style="color:#2563eb">**Foreign Key Concept**</span>

A foreign key means:

> A column pointing to primary key of another table.

---

# <span style="color:#2563eb">**Modern SQLAlchemy Relationship Syntax**</span>

---

## <span style="color:#16a34a">**User Model**</span>

```python id="n9v3"
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import relationship
from sqlalchemy.orm import mapped_column

class User(Base):

    __tablename__ = "users"

    id: Mapped[int] = mapped_column(
        primary_key=True
    )

    name: Mapped[str]

    posts: Mapped[list["Post"]] = relationship(
        back_populates="user"
    )
```

---

## <span style="color:#16a34a">**Post Model**</span>

```python id="a5m2"
from sqlalchemy import ForeignKey

class Post(Base):

    __tablename__ = "posts"

    id: Mapped[int] = mapped_column(
        primary_key=True
    )

    title: Mapped[str]

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id")
    )

    user: Mapped["User"] = relationship(
        back_populates="posts"
    )
```

---

# <span style="color:#2563eb">**Understanding Important Components**</span>

---

# <span style="color:#dc2626">**1. ForeignKey("users.id")**</span>

```python id="r8x4"
ForeignKey("users.id")
```

means:

```text id="k3v7"
user_id references users table primary key
```

Database-level relationship.

---

# <span style="color:#dc2626">**2. relationship()**</span>

```python id="p6m1"
relationship(...)
```

creates:

# <span style="color:#dc2626">**Object-level relationship access**</span>

---

# <span style="color:#2563eb">**Difference Between ForeignKey and relationship()**</span>

| Construct      | Purpose                  |
| -------------- | ------------------------ |
| ForeignKey     | DB-level constraint      |
| relationship() | Python object navigation |

---

# <span style="color:#2563eb">**Mental Model**</span>

```text id="u4x9"
ForeignKey
    =
Database relationship

relationship()
    =
Python object connection
```

---

# <span style="color:#2563eb">**What relationship() Enables**</span>

Without relationship:

```python id="f1m8"
post.user_id
```

Only numeric ID available.

With relationship:

```python id="w2m5"
post.user.name
```

ORM automatically fetches related object.

---

# <span style="color:#2563eb">**How ORM Relationships Work Internally**</span>

Suppose:

```python id="z8x1"
post.user
```

---

# <span style="color:#dc2626">**Internal Mechanism**</span>

---

## <span style="color:#16a34a">**Step 1 — ORM Sees Relationship Access**</span>

```python id="n4v7"
post.user
```

---

## <span style="color:#16a34a">**Step 2 — ORM Reads Foreign Key**</span>

```python id="t1m9"
post.user_id
```

Suppose:

```python id="q5x7"
user_id = 1
```

---

## <span style="color:#16a34a">**Step 3 — ORM Generates SQL**</span>

```sql id="m8v4"
SELECT *
FROM users
WHERE id = 1;
```

---

## <span style="color:#16a34a">**Step 4 — ORM Creates User Object**</span>

```python id="c7m1"
User(...)
```

---

## <span style="color:#16a34a">**Step 5 — Returns Related Object**</span>

```python id="j2v9"
post.user.name
```

works naturally.

---

# <span style="color:#2563eb">**What is back_populates?**</span>

```python id="v3m8"
back_populates="posts"
```

links both sides of relationship.

---

# <span style="color:#2563eb">**Meaning**</span>

```text id="b8x2"
User.posts
      ↔
Post.user
```

ORM synchronizes both directions.

---

# <span style="color:#2563eb">**Why Relationships are Powerful**</span>

They allow:

* natural object navigation
* automatic JOIN handling
* easier querying
* cleaner architecture

---

# <span style="color:#2563eb">**Relationship Types in SQLAlchemy**</span>

---

# <span style="color:#dc2626">**One-to-One**</span>

Example:

```text id="r4m7"
User ↔ Profile
```

One user has one profile.

---

# <span style="color:#dc2626">**One-to-Many**</span>

Example:

```text id="d7x1"
User ↔ Posts
```

One user has many posts.

---

# <span style="color:#dc2626">**Many-to-Many**</span>

Example:

```text id="x9m3"
Students ↔ Courses
```

Requires association table.

---

# <span style="color:#2563eb">**What is @property in Model Classes?**</span>

Now moving to Python class concept.

---

# <span style="color:#dc2626">**What is @property?**</span>

`@property` converts a method into:

# <span style="color:#dc2626">**Read-only computed attribute**</span>

---

# <span style="color:#2563eb">**Basic Example**</span>

```python id="u3v8"
class User:

    def __init__(self, first, last):

        self.first = first
        self.last = last

    @property
    def full_name(self):

        return f"{self.first} {self.last}"
```

Usage:

```python id="m9x4"
user.full_name
```

NOT:

```python id="a2v7"
user.full_name()
```

---

# <span style="color:#2563eb">**Mental Model of @property**</span>

```text id="f5x1"
Method behaving like attribute
```

---

# <span style="color:#2563eb">**Why @property Exists**</span>

Suppose full name is:

```text id="m1k8"
Derived/computed value
```

not stored in DB.

Instead of:

```python id="q4v6"
user.get_full_name()
```

you expose it naturally:

```python id="t7x2"
user.full_name
```

Cleaner API design.

---

# <span style="color:#2563eb">**Feynman Analogy**</span>

Imagine employee file.

Stored data:

* first name
* last name

Computed data:

```text id="z7m3"
Full display name
```

No need to physically store it.

Can compute dynamically when requested.

That is what `@property` does.

---

# <span style="color:#2563eb">**Using @property in SQLAlchemy Models**</span>

---

## <span style="color:#16a34a">**Example**</span>

```python id="p3v7"
class User(Base):

    __tablename__ = "users"

    id: Mapped[int] = mapped_column(
        primary_key=True
    )

    first_name: Mapped[str]

    last_name: Mapped[str]

    @property
    def full_name(self):

        return f"{self.first_name} {self.last_name}"
```

---

# <span style="color:#2563eb">**Usage**</span>

```python id="w6x2"
user.full_name
```

returns:

```text id="n8v1"
Arjun Sharma
```

---

# <span style="color:#2563eb">**Why Useful in Models**</span>

Useful for:

| Use Case             | Example         |
| -------------------- | --------------- |
| Computed values      | full name       |
| Formatting           | formatted price |
| Derived calculations | age from DOB    |
| Convenience fields   | profile URL     |

---

# <span style="color:#2563eb">**Important Distinction**</span>

@property values are:

# <span style="color:#dc2626">**NOT database columns**</span>

They are computed dynamically in Python.

---

# <span style="color:#2563eb">**Example**</span>

This:

```python id="r2m5"
@property
def full_name(self):
```

does NOT create:

```sql id="k5v7"
full_name column
```

in database.

---

# <span style="color:#2563eb">**When to Use @property**</span>

Use when:

* value derived from existing fields
* computation lightweight
* convenience access needed
* no DB storage required

---

# <span style="color:#2563eb">**When NOT to Use @property**</span>

Avoid when:

* heavy DB queries required
* expensive computations
* value should persist permanently

---

# <span style="color:#2563eb">**Common Mistakes with @property**</span>

---

# <span style="color:#dc2626">**1. Thinking Property Creates DB Column**</span>

False.

@property is pure Python behavior.

---

# <span style="color:#dc2626">**2. Performing Heavy Queries Inside Property**</span>

Bad:

```python id="m4x1"
@property
def expensive_data(self):
```

that triggers many DB queries.

Can create hidden performance issues.

---

# <span style="color:#dc2626">**3. Using Property for Business Workflows**</span>

@property should compute values, not execute workflows.

---

# <span style="color:#2563eb">**Final Mental Models**</span>

---

# <span style="color:#dc2626">**Relationship**</span>

```text id="y1v6"
Connection between database entities
```

---

# <span style="color:#dc2626">**ForeignKey**</span>

```text id="m8p3"
Database-level table reference
```

---

# <span style="color:#dc2626">**relationship()**</span>

```text id="g7x2"
Object-level navigation between related models
```

---

# <span style="color:#dc2626">**@property**</span>

```text id="d4m9"
Computed dynamic attribute behaving like field
```
