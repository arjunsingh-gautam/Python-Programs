# <span style="color:#2563eb">**Understanding Jinja2 Syntax and FastAPI Templating**</span>

We will cover:

1. Jinja2 syntax
2. Writing UI templates
3. Template inheritance
4. Jinja2 + FastAPI data flow
5. Complete FastAPI templating code explanation
6. Internal mechanics
7. Full dry run
8. Coding exercise

---

# <span style="color:#2563eb">**1. Jinja2 Syntax Fundamentals**</span>

Jinja2 provides special syntax markers.

| Syntax  | Purpose            |
| ------- | ------------------ |
| `{{ }}` | Output variables   |
| `{% %}` | Logic/control flow |
| `{# #}` | Comments           |

---

# <span style="color:#dc2626">**1. Variable Output Syntax**</span>

Used to print data.

```html id="j2v1"
<h1>Hello {{ name }}</h1>
```

If:

```python id="a7m1"
name = "Arjun"
```

Result:

```html id="t4n8"
<h1>Hello Arjun</h1>
```

---

## <span style="color:#16a34a">**Internal Mechanics**</span>

Jinja2:

1. detects `{{ name }}`
2. searches variable in context dictionary
3. converts value to string
4. injects into HTML

Conceptually:

```python id="p8r2"
html = html.replace("{{ name }}", context["name"])
```

Real implementation is more advanced.

---

# <span style="color:#dc2626">**2. If Conditions**</span>

```html id="q7w2"
{% if age >= 18 %}
<p>Adult</p>
{% else %}
<p>Minor</p>
{% endif %}
```

---

## <span style="color:#16a34a">**How It Works**</span>

Jinja2 evaluates condition:

```python id="m9k4"
age >= 18
```

Then renders matching block only.

---

# <span style="color:#dc2626">**3. Loops**</span>

```html id="v5z1"
<ul>
  {% for item in items %}
  <li>{{ item }}</li>
  {% endfor %}
</ul>
```

---

## <span style="color:#16a34a">**Dry Run**</span>

Context:

```python id="u7c3"
items = ["Apple", "Banana", "Orange"]
```

Loop execution:

```text id="x2b7"
Iteration 1 → Apple
Iteration 2 → Banana
Iteration 3 → Orange
```

Generated HTML:

```html id="l3s9"
<ul>
  <li>Apple</li>
  <li>Banana</li>
  <li>Orange</li>
</ul>
```

---

# <span style="color:#dc2626">**4. Comments**</span>

```html id="r1m6"
{# hidden comment #}
```

Not rendered in final HTML.

---

# <span style="color:#dc2626">**5. Filters**</span>

Filters transform data.

```html id="e8h2"
{{ name|upper }}
```

If:

```python id="c7j1"
name = "arjun"
```

Result:

```html id="g4n9"
ARJUN
```

---

## <span style="color:#16a34a">**Common Filters**</span>

| Filter   | Purpose          |
| -------- | ---------------- |
| `upper`  | uppercase        |
| `lower`  | lowercase        |
| `length` | count length     |
| `title`  | title case       |
| `safe`   | disable escaping |

---

# <span style="color:#2563eb">**2. Writing UI Templates in Jinja2**</span>

Templates are usually HTML files.

Example:

```text id="t7v3"
templates/
   index.html
```

---

# <span style="color:#dc2626">**Example UI Template**</span>

```html id="y9x5"
<!DOCTYPE html>
<html>
  <head>
    <title>Users</title>
  </head>

  <body>
    <h1>User List</h1>

    <ul>
      {% for user in users %}
      <li>{{ user }}</li>
      {% endfor %}
    </ul>
  </body>
</html>
```

---

# <span style="color:#2563eb">**What Makes It Dynamic?**</span>

Dynamic part:

```html id="z4r7"
{% for user in users %}
```

Static part:

```html id="w6k2"
<h1>User List</h1>
```

Templating combines:

```text id="n5p1"
Static HTML
    +
Dynamic Data
```

---

# <span style="color:#2563eb">**3. Template Inheritance in Jinja2**</span>

# <span style="color:#dc2626">**Why Template Inheritance Exists**</span>

Without inheritance:

Every page repeats:

- navbar
- footer
- CSS links
- layout structure

Huge duplication.

---

# <span style="color:#2563eb">**Inheritance Concept**</span>

Create:

1. base template
2. child templates

Children reuse parent layout.

---

# <span style="color:#2563eb">**Base Template Example**</span>

## <span style="color:#16a34a">**base.html**</span>

```html id="p2m4"
<!DOCTYPE html>
<html>
  <head>
    <title>{% block title %}{% endblock %}</title>
  </head>

  <body>
    <nav>Home | About | Contact</nav>

    <hr />

    {% block content %} {% endblock %}

    <hr />

    <footer>My Website</footer>
  </body>
</html>
```

---

# <span style="color:#2563eb">**Understanding Blocks**</span>

```html id="u8v1"
{% block content %} {% endblock %}
```

means:

> Child templates can replace this section.

Think of it like placeholders for larger sections.

---

# <span style="color:#2563eb">**Child Template Example**</span>

## <span style="color:#16a34a">**home.html**</span>

```html id="g6s3"
{% extends "base.html" %} {% block title %} Home Page {% endblock %} {% block
content %}

<h1>Welcome User</h1>

<p>This is home page</p>

{% endblock %}
```

---

# <span style="color:#2563eb">**How Inheritance Works Internally**</span>

---

## <span style="color:#16a34a">**Step 1 — Child Detects Parent**</span>

```html id="j7q5"
{% extends "base.html" %}
```

Jinja2 loads parent template.

---

## <span style="color:#16a34a">**Step 2 — Parent Blocks Identified**</span>

Jinja2 finds:

```html id="v4c9"
{% block content %}
```

---

## <span style="color:#16a34a">**Step 3 — Child Overrides Blocks**</span>

Child content replaces parent block.

---

## <span style="color:#16a34a">**Step 4 — Final HTML Generated**</span>

Result:

```html id="f8d2"
<!DOCTYPE html>
<html>
  <head>
    <title>Home Page</title>
  </head>

  <body>
    <nav>Home | About | Contact</nav>

    <hr />

    <h1>Welcome User</h1>

    <p>This is home page</p>

    <hr />

    <footer>My Website</footer>
  </body>
</html>
```

---

# <span style="color:#2563eb">**Why Template Inheritance is Powerful**</span>

Benefits:

| Benefit         | Reason              |
| --------------- | ------------------- |
| Reusability     | Shared layouts      |
| Maintainability | Edit one base file  |
| Consistency     | Uniform UI          |
| Scalability     | Easy large projects |

---

# <span style="color:#2563eb">**4. Jinja2 + FastAPI Complete Data Flow**</span>

# <span style="color:#dc2626">**Full Lifecycle**</span>

```text id="h3v8"
Browser Request
      ↓
FastAPI Route
      ↓
TemplateResponse()
      ↓
Load Jinja2 Template
      ↓
Pass Context Data
      ↓
Jinja2 Rendering
      ↓
Generate HTML
      ↓
FastAPI Response
      ↓
Browser Displays Page
```

---

# <span style="color:#2563eb">**5. Complete FastAPI + Jinja2 Example**</span>

---

# <span style="color:#dc2626">**Project Structure**</span>

```text id="r5y2"
project/
│
├── main.py
│
└── templates/
    ├── base.html
    └── home.html
```

---

# <span style="color:#2563eb">**base.html**</span>

```html id="q9m7"
<!DOCTYPE html>
<html>
  <head>
    <title>{% block title %}{% endblock %}</title>
  </head>

  <body>
    <h2>My Website</h2>

    <hr />

    {% block content %} {% endblock %}
  </body>
</html>
```

---

# <span style="color:#2563eb">**home.html**</span>

```html id="m3t6"
{% extends "base.html" %} {% block title %} Home {% endblock %} {% block content
%}

<h1>Hello {{ name }}</h1>

<ul>
  {% for subject in subjects %}
  <li>{{ subject }}</li>
  {% endfor %}
</ul>

{% endblock %}
```

---

# <span style="color:#2563eb">**main.py**</span>

```python id="x7n2"
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="templates")

@app.get("/")
def home(request: Request):

    data = {
        "request": request,
        "name": "Arjun",
        "subjects": [
            "Math",
            "Physics",
            "Programming"
        ]
    }

    return templates.TemplateResponse(
        "home.html",
        data
    )
```

---

# <span style="color:#2563eb">**6. Explaining Each FastAPI Component**</span>

---

# <span style="color:#dc2626">**1. FastAPI Import**</span>

```python id="v2b4"
from fastapi import FastAPI, Request
```

---

## <span style="color:#16a34a">**Why Request is Needed**</span>

Jinja2 templates in FastAPI require request object.

Why?

Because templates may need:

- request info
- URL generation
- session access
- headers

---

# <span style="color:#dc2626">**2. Jinja2Templates**</span>

```python id="k6w1"
from fastapi.templating import Jinja2Templates
```

Wrapper around Jinja2 engine.

Helps FastAPI integrate with Jinja2.

---

# <span style="color:#dc2626">**3. Creating Template Loader**</span>

```python id="n4e7"
templates = Jinja2Templates(directory="templates")
```

This tells FastAPI:

```text id="p9t2"
Look for HTML templates inside templates/ folder
```

---

## <span style="color:#16a34a">**Internal Mechanism**</span>

Internally creates Jinja2 environment:

Conceptually:

```python id="u3x8"
Environment(
    loader=FileSystemLoader("templates")
)
```

---

# <span style="color:#dc2626">**4. Route Definition**</span>

```python id="a8r5"
@app.get("/")
```

Registers route.

Maps:

```text id="m2v9"
GET /
```

to:

```python id="g5y4"
home()
```

---

# <span style="color:#dc2626">**5. Context Dictionary**</span>

```python id="l1f7"
data = {
    "request": request,
    "name": "Arjun"
}
```

This dictionary becomes template variables.

Inside HTML:

```html id="h8k3"
{{ name }}
```

reads:

```python id="z4q1"
data["name"]
```

---

# <span style="color:#dc2626">**6. TemplateResponse**</span>

```python id="d7p2"
templates.TemplateResponse(
    "home.html",
    data
)
```

---

## <span style="color:#16a34a">**What It Does Internally**</span>

---

### <span style="color:#9333ea">**Step 1 — Load Template File**</span>

```text id="c6n5"
templates/home.html
```

---

### <span style="color:#9333ea">**Step 2 — Parse Jinja2 Syntax**</span>

Detects:

- variables
- loops
- conditions

---

### <span style="color:#9333ea">**Step 3 — Inject Context Data**</span>

```python id="f2v8"
{
   "name": "Arjun"
}
```

---

### <span style="color:#9333ea">**Step 4 — Render Final HTML**</span>

Produces plain HTML.

---

### <span style="color:#9333ea">**Step 5 — Return HTTP Response**</span>

Browser receives HTML page.

---

# <span style="color:#2563eb">**7. Full Dry Run of Request**</span>

Suppose browser visits:

```text id="s3x1"
http://127.0.0.1:8000/
```

---

## <span style="color:#16a34a">**Execution Flow**</span>

---

### <span style="color:#9333ea">**1. Uvicorn Receives Request**</span>

```text id="e4b7"
GET /
```

---

### <span style="color:#9333ea">**2. FastAPI Router Matches Route**</span>

Finds:

```python id="w5n2"
@app.get("/")
```

---

### <span style="color:#9333ea">**3. Executes home() Function**</span>

```python id="r8k4"
home(request)
```

---

### <span style="color:#9333ea">**4. Context Data Created**</span>

```python id="q7y9"
{
   "name": "Arjun"
}
```

---

### <span style="color:#9333ea">**5. Jinja2 Loads home.html**</span>

Template parsed.

---

### <span style="color:#9333ea">**6. Template Inheritance Process Happens**</span>

Jinja2 loads:

```text id="v9m3"
base.html
```

Then merges child blocks.

---

### <span style="color:#9333ea">**7. Variables Replaced**</span>

```html id="t4r1"
{{ name }}
```

becomes:

```html id="k3z6"
Arjun
```

---

### <span style="color:#9333ea">**8. Loop Executes**</span>

```html id="b7x2"
{% for subject in subjects %}
```

Generates list items.

---

### <span style="color:#9333ea">**9. Final HTML Returned**</span>

Browser renders page visually.

---

# <span style="color:#2563eb">**8. Important Design Principles**</span>

---

## <span style="color:#16a34a">**Keep Business Logic Out of Templates**</span>

Bad:

```html id="p8c5"
{% if calculate_salary(user) > 50000 %}
```

Good:

Backend computes first.

---

## <span style="color:#16a34a">**Templates Should Focus on Presentation**</span>

Templates should handle:

- UI
- formatting
- rendering

Not:

- database queries
- algorithms
- heavy logic

---

# <span style="color:#2563eb">**9. Coding Exercise to Solidify Learning**</span>

# <span style="color:#dc2626">**Mini Student Dashboard Project**</span>

Build:

```text id="u5r4"
Student Dashboard Website
```

---

# <span style="color:#2563eb">**Requirements**</span>

Create:

---

## <span style="color:#16a34a">**1. base.html**</span>

Include:

- navbar
- footer
- title block
- content block

---

## <span style="color:#16a34a">**2. home.html**</span>

Show:

- student name
- branch
- list of subjects

---

## <span style="color:#16a34a">**3. FastAPI Route**</span>

Pass dynamic data:

```python id="o2m7"
{
   "name": "Your Name",
   "branch": "EXTC",
   "subjects": [...]
}
```

---

## <span style="color:#16a34a">**4. Add Condition**</span>

If CGPA > 8:

Show:

```html id="f6x9"
Excellent Performance
```

Else:

```html id="z3v2"
Keep Improving
```

---

## <span style="color:#16a34a">**5. Add Loop**</span>

Render subjects dynamically.

---

# <span style="color:#2563eb">**Advanced Challenge**</span>

Add:

- multiple pages
- template inheritance
- CSS
- student profile card
- marks table
- dynamic route `/student/{id}`

---

# <span style="color:#2563eb">**Expected Learning Outcome**</span>

After this exercise you should deeply understand:

- Jinja2 syntax
- template rendering
- inheritance
- context passing
- FastAPI integration
- request-response lifecycle
- dynamic HTML generation
