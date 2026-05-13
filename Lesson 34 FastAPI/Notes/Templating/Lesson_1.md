# <span style="color:#2563eb">**What is Templating?**</span>

Templating is the process of:

> Dynamically generating text or HTML by combining:
>
> - static structure
> - dynamic data

A template acts like:

```text id="a3t1"
Blueprint + Placeholders
```

Then runtime data fills those placeholders.

---

# <span style="color:#2563eb">**Simple Idea of Templating**</span>

Suppose you want to generate:

```html id="u12x"
<h1>Hello Arjun</h1>
```

Instead of hardcoding:

```html id="q8m1"
<h1>Hello Arjun</h1>
```

you create a template:

```html id="k91p"
<h1>Hello {{ name }}</h1>
```

Then pass:

```python id="w4za"
name = "Arjun"
```

Result becomes:

```html id="n7bc"
<h1>Hello Arjun</h1>
```

---

# <span style="color:#2563eb">**Core Philosophy of Templating**</span>

Templating separates:

| Concern      | Responsibility |
| ------------ | -------------- |
| Structure/UI | Template       |
| Dynamic Data | Backend Logic  |

This separation is extremely important in software engineering.

---

# <span style="color:#2563eb">**Causality of Templating**</span>

# <span style="color:#dc2626">**Why Did Templating Become Necessary?**</span>

To understand templating deeply, we must understand the historical problem.

---

## <span style="color:#16a34a">**Problem Before Templating**</span>

Early web applications generated HTML manually.

Example:

```python id="b7fd"
html = "<h1>Hello " + username + "</h1>"
```

As applications grew:

```python id="m1zc"
html = (
    "<html>"
    "<body>"
    "<h1>Hello " + username + "</h1>"
    "<ul>"
)
```

Problems exploded.

---

# <span style="color:#2563eb">**What Problems Happened Without Templating?**</span>

---

## <span style="color:#16a34a">**1. Extremely Messy Code**</span>

Backend logic mixed with HTML.

Example:

```python id="x3vz"
if is_admin:
    html += "<button>Delete</button>"
```

Now code contains:

- Python logic
- HTML
- CSS
- UI logic

Everything mixed together.

This becomes unreadable.

---

## <span style="color:#16a34a">**2. Impossible Maintainability**</span>

Changing UI required changing backend code.

Even small HTML changes became painful.

---

## <span style="color:#16a34a">**3. No Separation of Concerns**</span>

Frontend developers and backend developers could not work independently.

---

## <span style="color:#16a34a">**4. Duplicate Code Everywhere**</span>

Headers, footers, navigation bars repeated.

Huge redundancy.

---

## <span style="color:#16a34a">**5. Security Problems**</span>

Manual string concatenation caused:

- XSS vulnerabilities
- broken HTML
- injection issues

---

# <span style="color:#2563eb">**Templating Solves These Problems**</span>

Templating introduces:

```text id="g8tr"
Template File + Dynamic Data
```

instead of:

```text id="m4rt"
Manual String Construction
```

---

# <span style="color:#2563eb">**Real-World Analogy**</span>

Imagine printing student report cards.

Without templating:

- write every report card manually

With templating:

```text id="r2pt"
Student Name: {{ name }}
Marks: {{ marks }}
Grade: {{ grade }}
```

Then software fills data automatically.

Much cleaner.

---

# <span style="color:#2563eb">**What Happens Internally in Templating?**</span>

Template engine performs:

```text id="j7yt"
Template
   +
Data Context
   ↓
Template Parsing
   ↓
Placeholder Replacement
   ↓
Final Output Generation
```

---

# <span style="color:#2563eb">**What is a Template Engine?**</span>

A template engine is software that:

- reads template files
- parses placeholders
- executes template logic
- injects data
- generates final output

Examples:

| Language   | Template Engine |
| ---------- | --------------- |
| Python     | Jinja2          |
| JavaScript | Handlebars, EJS |
| PHP        | Blade, Twig     |
| Java       | Thymeleaf       |
| Go         | html/template   |

---

# <span style="color:#2563eb">**What is Jinja2?**</span>

[Jinja2 Official Documentation](https://jinja.palletsprojects.com/?utm_source=chatgpt.com)

Jinja2 is:

> A powerful Python templating engine.

Created for:

- Flask
- web applications
- dynamic HTML generation

But usable anywhere.

---

# <span style="color:#2563eb">**Why Jinja2 Became Popular**</span>

Because it provides:

- clean syntax
- template inheritance
- loops
- conditions
- filters
- escaping/security
- separation of UI and logic

---

# <span style="color:#2563eb">**Basic Jinja2 Example**</span>

## <span style="color:#16a34a">**Template File**</span>

```html id="m9xr"
<h1>Hello {{ name }}</h1>
```

---

## <span style="color:#16a34a">**Python Code**</span>

```python id="n8wl"
from jinja2 import Template

template = Template("<h1>Hello {{ name }}</h1>")

output = template.render(name="Arjun")

print(output)
```

---

## <span style="color:#16a34a">**Output**</span>

```html id="x5op"
<h1>Hello Arjun</h1>
```

---

# <span style="color:#2563eb">**How Jinja2 Works Internally**</span>

# <span style="color:#dc2626">**Step-by-Step Internal Mechanics**</span>

---

## <span style="color:#16a34a">**Step 1 — Read Template**</span>

Jinja2 reads:

```html id="z7ke"
<h1>Hello {{ name }}</h1>
```

as plain text.

---

## <span style="color:#16a34a">**Step 2 — Parse Template Syntax**</span>

Jinja2 scans for special syntax:

| Syntax  | Meaning            |
| ------- | ------------------ |
| `{{ }}` | expression/output  |
| `{% %}` | logic/control flow |
| `{# #}` | comments           |

---

## <span style="color:#16a34a">**Step 3 — Build Internal Template Tree**</span>

Jinja2 converts template into internal representation.

Conceptually:

```text id="r7py"
HTML Node
   └── Variable Node(name)
```

Like a mini compiler.

---

## <span style="color:#16a34a">**Step 4 — Inject Context Data**</span>

You pass:

```python id="k8vq"
{
   "name": "Arjun"
}
```

called:

# <span style="color:#dc2626">**Context**</span>

Context = variables available inside template.

---

## <span style="color:#16a34a">**Step 5 — Render Final Output**</span>

Jinja2 replaces:

```html id="t2gh"
{{ name }}
```

with:

```text id="q9we"
Arjun
```

Final result:

```html id="y6tr"
<h1>Hello Arjun</h1>
```

---

# <span style="color:#2563eb">**Dry Run of Rendering Process**</span>

---

## <span style="color:#16a34a">**Input Template**</span>

```html id="c3pq"
<h1>Hello {{ name }}</h1>
```

---

## <span style="color:#16a34a">**Context**</span>

```python id="l7mn"
{
   "name": "Alice"
}
```

---

## <span style="color:#16a34a">**Execution**</span>

Jinja2 scans:

```text id="w2xc"
{{ name }}
```

Looks up variable:

```python id="a5vf"
context["name"]
```

Finds:

```python id="f8jh"
"Alice"
```

Replaces it.

---

## <span style="color:#16a34a">**Final HTML**</span>

```html id="d1ko"
<h1>Hello Alice</h1>
```

---

# <span style="color:#2563eb">**Jinja2 Syntax**</span>

---

# <span style="color:#dc2626">**1. Variable Output**</span>

```html id="g4ed"
{{ username }}
```

Prints variable.

---

# <span style="color:#dc2626">**2. Conditions**</span>

```html id="o7pw"
{% if is_admin %}
<button>Delete</button>
{% endif %}
```

---

# <span style="color:#dc2626">**3. Loops**</span>

```html id="m2qa"
<ul>
  {% for item in items %}
  <li>{{ item }}</li>
  {% endfor %}
</ul>
```

---

# <span style="color:#dc2626">**4. Comments**</span>

```html id="n9ts"
{# hidden comment #}
```

---

# <span style="color:#2563eb">**Example with Loop and Condition**</span>

## <span style="color:#16a34a">**Template**</span>

```html id="p7kr"
<h1>User List</h1>

<ul>
  {% for user in users %}
  <li>{{ user }} {% if user == "admin" %} (Administrator) {% endif %}</li>
  {% endfor %}
</ul>
```

---

## <span style="color:#16a34a">**Python Code**</span>

```python id="w8yc"
from jinja2 import Template

template = Template(open("template.html").read())

html = template.render(
    users=["alice", "bob", "admin"]
)

print(html)
```

---

## <span style="color:#16a34a">**Generated Output**</span>

```html id="f3jw"
<h1>User List</h1>

<ul>
  <li>alice</li>
  <li>bob</li>
  <li>admin (Administrator)</li>
</ul>
```

---

# <span style="color:#2563eb">**How Jinja2 Works Like a Compiler**</span>

Jinja2 internally behaves similarly to:

- tokenizer
- parser
- interpreter/compiler

---

## <span style="color:#16a34a">**Internal Stages**</span>

```text id="u1xv"
Template Text
    ↓
Lexer (tokenization)
    ↓
Parser
    ↓
AST Creation
    ↓
Code Generation
    ↓
Rendering
```

---

# <span style="color:#2563eb">**What is AST Here?**</span>

AST:

# <span style="color:#dc2626">**Abstract Syntax Tree**</span>

Template converted into structured nodes.

Example:

```html id="m5lp"
Hello {{ name }}
```

becomes conceptually:

```text id="q4re"
TextNode("Hello ")
VariableNode("name")
```

---

# <span style="color:#2563eb">**Why Templating is Powerful**</span>

Because it enables:

| Capability             | Benefit              |
| ---------------------- | -------------------- |
| Dynamic HTML           | Personalized pages   |
| Reusable layouts       | Less duplication     |
| Logic in templates     | Flexible UI          |
| Separation of concerns | Cleaner architecture |
| Context injection      | Dynamic rendering    |

---

# <span style="color:#2563eb">**Template Inheritance in Jinja2**</span>

One of the most powerful features.

---

## <span style="color:#16a34a">**Base Template**</span>

```html id="j9vr"
<html>
  <body>
    {% block content %} {% endblock %}
  </body>
</html>
```

---

## <span style="color:#16a34a">**Child Template**</span>

```html id="x8zn"
{% extends "base.html" %} {% block content %}
<h1>Home Page</h1>
{% endblock %}
```

---

## <span style="color:#16a34a">**Why Important?**</span>

Avoids repeating:

- navbar
- footer
- layout
- CSS includes

Huge maintainability advantage.

---

# <span style="color:#2563eb">**Autoescaping and Security**</span>

Jinja2 automatically escapes dangerous HTML.

Example:

Input:

```html id="b4xt"
<script>
  alert(1);
</script>
```

Escaped output:

```html id="y7mn"
&lt;script&gt;alert(1)&lt;/script&gt;
```

Prevents:

# <span style="color:#dc2626">**XSS (Cross Site Scripting)**</span>

---

# <span style="color:#2563eb">**How FastAPI Uses Jinja2**</span>

FastAPI integrates Jinja2 through:

```python id="o2fw"
from fastapi.templating import Jinja2Templates
```

---

## <span style="color:#16a34a">**Example**</span>

```python id="v1zk"
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="templates")

@app.get("/")
def home(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "name": "Arjun"
        }
    )
```

---

# <span style="color:#2563eb">**Flow in FastAPI + Jinja2**</span>

```text id="s5dw"
Browser Request
      ↓
FastAPI Route
      ↓
Load Jinja2 Template
      ↓
Pass Context Data
      ↓
Jinja2 Rendering
      ↓
Generated HTML
      ↓
Browser Response
```

---

# <span style="color:#2563eb">**Without Templating vs With Templating**</span>

| Without Templating          | With Templating        |
| --------------------------- | ---------------------- |
| Manual string concatenation | Structured templates   |
| Messy backend code          | Clean separation       |
| Hard maintenance            | Reusable layouts       |
| Repeated HTML               | Inheritance            |
| Unsafe output               | Autoescaping           |
| Poor scalability            | Scalable UI generation |

---

# <span style="color:#2563eb">**Limitations of Templating**</span>

---

## <span style="color:#16a34a">**1. Business Logic Should Not Be Heavy**</span>

Templates should not contain:

- complex algorithms
- database logic
- heavy computation

Templates should focus on presentation.

---

## <span style="color:#16a34a">**2. Large Frontends Prefer SPA Frameworks**</span>

Modern systems often use:

- React
- Vue
- Angular

instead of server-side templating.

---

# <span style="color:#2563eb">**Server-Side Rendering vs Client-Side Rendering**</span>

| Type   | Rendering Happens |
| ------ | ----------------- |
| Jinja2 | Server            |
| React  | Browser/client    |

---

# <span style="color:#2563eb">**Mental Model of Templating**</span>

Think of templating as:

```text id="d8ur"
HTML Blueprint
     +
Dynamic Data
     +
Rendering Engine
     =
Final Web Page
```

Jinja2 is the engine that performs this transformation.
