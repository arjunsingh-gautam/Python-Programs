# <span style="color:#2563eb">**Is Naming Routes Like `/get_users`, `/post_users`, `/patch_users` Allowed?**</span>

# <span style="color:#16a34a">**YES — It is technically allowed**

FastAPI will work perfectly fine.

Example:

```python id="m1x7"
@app.get("/get_users")
def get_users():
    pass


@app.post("/post_users")
def create_user():
    pass
```

This is valid.

---

# <span style="color:#2563eb">**But Is It Good API Design?**</span>

# <span style="color:#dc2626">**Usually NO**

According to modern REST API design principles, this is generally considered:

- redundant
- non-standard
- less clean
- less scalable

---

# <span style="color:#2563eb">**Why It is Considered Poor REST Design**</span>

Because:

# <span style="color:#dc2626">**HTTP method already expresses the action**

So adding verbs inside path duplicates meaning.

---

# <span style="color:#2563eb">**Example**</span>

Suppose:

```python id="q4v2"
@app.get("/get_users")
```

Request already contains:

```http id="p8m5"
GET
```

So internally meaning becomes:

```text id="t7x1"
GET get_users
```

which is semantically repetitive.

---

# <span style="color:#2563eb">**REST Philosophy**</span>

REST separates:

| Part        | Responsibility       |
| ----------- | -------------------- |
| URL path    | identifies resource  |
| HTTP method | identifies operation |

---

# <span style="color:#2563eb">**Good REST Design**</span>

```http id="x2m8"
GET /users
POST /users
PATCH /users/{id}
DELETE /users/{id}
```

---

# <span style="color:#2563eb">**Bad/Non-RESTful Design**</span>

```http id="n9v3"
GET /get_users
POST /create_user
PATCH /update_user
DELETE /delete_user
```

Now operation encoded TWICE:

- in HTTP method
- in URL

---

# <span style="color:#2563eb">**Mental Model**</span>

---

# <span style="color:#dc2626">**RESTful URL**</span>

```text id="a5m2"
/users
```

means:

# <span style="color:#dc2626">**resource**

---

# <span style="color:#dc2626">**HTTP Method**</span>

```text id="r8x4"
GET
POST
PATCH
DELETE
```

means:

# <span style="color:#dc2626">**operation on resource**

---

# <span style="color:#2563eb">**Why REST APIs Prefer Nouns Instead of Verbs**</span>

REST models system as:

# <span style="color:#dc2626">**Resources**

not function calls.

---

# <span style="color:#2563eb">**Resource-Oriented Thinking**</span>

Good REST API thinks:

```text id="k3v7"
/users
/posts
/orders
```

NOT:

```text id="p6m1"
/getUsers
/createOrder
/updatePost
```

---

# <span style="color:#2563eb">**Feynman Analogy**</span>

Imagine library.

RESTful thinking:

```text id="u4x9"
"Books exist"
```

HTTP method specifies action:

| Method          | Meaning     |
| --------------- | ----------- |
| GET /books      | view books  |
| POST /books     | add book    |
| DELETE /books/1 | remove book |

---

Non-RESTful thinking:

```text id="f1m8"
/getBooks
/createBook
/deleteBook
```

This treats API more like:

# <span style="color:#dc2626">**remote function calls**

instead of resource system.

---

# <span style="color:#2563eb">**Why Beginners Often Prefer Verb-Based Routes**</span>

Because it feels intuitive initially.

Example:

```text id="w2m5"
"/get_users"
```

looks descriptive.

But as systems grow:

it becomes inconsistent and messy.

---

# <span style="color:#2563eb">**Scalability Problem with Verb-Based APIs**</span>

Suppose system grows.

Now routes become:

```text id="z8x1"
/get_users
/create_user
/update_user_email
/update_user_password
/delete_user
/activate_user
/deactivate_user
```

Very procedural.

Harder to standardize.

---

# <span style="color:#2563eb">**RESTful Alternative**</span>

```text id="n4v7"
/users
/users/{id}
/users/{id}/activate
```

Cleaner resource hierarchy.

---

# <span style="color:#2563eb">**Important Nuance — Sometimes Verb Routes ARE Acceptable**</span>

Very important.

Some operations are NOT simple CRUD resources.

Example:

```text id="t1m9"
transfer_money
send_email
generate_report
checkout_order
```

These are:

# <span style="color:#dc2626">**actions/workflows**

not merely resource manipulation.

In such cases verb/action routes are reasonable.

---

# <span style="color:#2563eb">**Example**</span>

```http id="q5x7"
POST /payments/transfer
POST /reports/generate
POST /auth/login
```

These are acceptable because:

# <span style="color:#dc2626">**they represent business actions**

not plain CRUD.

---

# <span style="color:#2563eb">**Good Rule of Thumb**</span>

---

# <span style="color:#dc2626">**For CRUD Resources → Use Nouns**</span>

Good:

```http id="m8v4"
GET /users
POST /users
DELETE /users/1
```

---

# <span style="color:#dc2626">**For Business Actions → Verbs May Be Fine**</span>

Good:

```http id="c7m1"
POST /auth/login
POST /orders/checkout
POST /payments/refund
```

---

# <span style="color:#2563eb">**Why RESTful Naming Matters in Industry**</span>

Because consistency improves:

- API readability
- onboarding
- maintainability
- predictability
- tooling compatibility

Large systems NEED standardization.

---

# <span style="color:#2563eb">**FastAPI Does NOT Enforce REST**</span>

FastAPI allows:

```python id="j2v9"
@app.get("/dance_with_users")
```

if you want.

Framework only provides routing mechanism.

RESTfulness is:

# <span style="color:#dc2626">**architectural design discipline**

not syntax restriction.

---

# <span style="color:#2563eb">**Comparison Table**</span>

| Style           | Example          | Recommended? |
| --------------- | ---------------- | ------------ |
| RESTful         | GET /users       | Yes          |
| Verb-based CRUD | GET /get_users   | Usually No   |
| Business action | POST /login      | Yes          |
| RPC-style       | POST /createUser | Sometimes    |

---

# <span style="color:#2563eb">**What Large Companies Typically Use**</span>

Most modern APIs from companies like:

- [GitHub API](https://docs.github.com/en/rest?utm_source=chatgpt.com)
- [Stripe API](https://docs.stripe.com/api?utm_source=chatgpt.com)
- [Spotify API](https://developer.spotify.com/documentation/web-api?utm_source=chatgpt.com)

primarily use:

# <span style="color:#dc2626">**resource-oriented REST naming**

---

# <span style="color:#2563eb">**Deepest Mental Model**</span>

---

# <span style="color:#dc2626">**REST APIs Think in Terms of Resources**

```text id="v3m8"
/users
/posts
/orders
```

---

# <span style="color:#dc2626">**HTTP Methods Encode Operations**

```text id="b8x2"
GET
POST
PATCH
DELETE
```

Therefore:

```text id="r4m7"
GET /users
```

already completely describes:

```text id="d7x1"
Retrieve users resource
```

No need for:

```text id="x9m3"
/get_users
```

---

# <span style="color:#2563eb">**Final Recommendation**</span>

For learning and professional backend engineering:

# <span style="color:#16a34a">**Prefer RESTful resource-oriented routes**

Use:

```http id="u3v8"
GET /users
POST /users
PATCH /users/{id}
DELETE /users/{id}
```

Reserve verb/action routes ONLY for:

# <span style="color:#dc2626">**true business operations/workflows**

like:

```http id="m9x4"
POST /login
POST /checkout
POST /transfer-money
```
