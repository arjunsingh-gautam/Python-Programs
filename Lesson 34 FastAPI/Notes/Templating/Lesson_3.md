# <span style="color:#2563eb">**What is Server-Side Rendering (SSR)?**</span>

Server-Side Rendering means:

> The HTML page is generated on the server before being sent to the browser.

The server:

1. receives request
2. processes data
3. renders HTML
4. sends fully generated page to browser

---

# <span style="color:#2563eb">**Simple Mental Model**</span>

```text id="n1q2"
Browser asks for page
        ↓
Server builds HTML page
        ↓
Server sends completed HTML
        ↓
Browser displays page
```

---

# <span style="color:#2563eb">**Example of SSR with Jinja2**</span>

Suppose template:

```html id="j7w1"
<h1>Hello {{ name }}</h1>
```

Server receives:

```python id="a4k8"
name = "Arjun"
```

Server renders:

```html id="m9z2"
<h1>Hello Arjun</h1>
```

Browser receives already-completed HTML.

Browser does NOT generate the UI.

Server generates it.

---

# <span style="color:#2563eb">**Why It is Called "Server-Side" Rendering**</span>

Because rendering happens:

```text id="x3r7"
Inside backend server
```

instead of:

```text id="u8m5"
Inside browser/client
```

---

# <span style="color:#2563eb">**What Does “Rendering” Mean?**</span>

Rendering means:

> Converting templates + data into final visual HTML.

Example:

```html id="w2n9"
<h1>Hello {{ name }}</h1>
```

-

```python id="f6y3"
name = "Alice"
```

↓

```html id="v5t1"
<h1>Hello Alice</h1>
```

That transformation process is rendering.

---

# <span style="color:#2563eb">**SSR Request Lifecycle**</span>

# <span style="color:#dc2626">**Complete Flow**</span>

```text id="q7b2"
Browser Request
      ↓
Web Server (Uvicorn/Gunicorn)
      ↓
FastAPI Route
      ↓
Database/API Calls
      ↓
Jinja2 Template Rendering
      ↓
HTML Generated
      ↓
Response Sent
      ↓
Browser Displays Page
```

---

# <span style="color:#2563eb">**Example of SSR in FastAPI + Jinja2**</span>

---

## <span style="color:#16a34a">**FastAPI Code**</span>

```python id="e3x7"
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

## <span style="color:#16a34a">**Template**</span>

```html id="c4z1"
<h1>Hello {{ name }}</h1>
```

---

## <span style="color:#16a34a">**Generated HTML**</span>

Server sends:

```html id="n8r5"
<h1>Hello Arjun</h1>
```

Browser simply displays it.

---

# <span style="color:#2563eb">**What Happens Without SSR?**</span>

Without SSR:

Server sends mostly empty HTML:

```html id="d2m6"
<div id="app"></div>
```

Then browser JavaScript:

- fetches data
- builds UI
- renders page

This is:

# <span style="color:#dc2626">**Client-Side Rendering (CSR)**</span>

---

# <span style="color:#2563eb">**Server-Side Rendering vs Client-Side Rendering**</span>

| Feature            | SSR             | CSR                |
| ------------------ | --------------- | ------------------ |
| Rendering Location | Server          | Browser            |
| HTML Sent          | Fully rendered  | Mostly empty shell |
| Initial Load       | Faster visually | Slower initially   |
| SEO                | Excellent       | Can be harder      |
| Browser Work       | Less            | More               |
| Server Work        | More            | Less               |

---

# <span style="color:#2563eb">**Why SSR Was Created**</span>

Originally browsers were weak.

JavaScript capabilities limited.

Servers handled rendering because:

- browsers were slow
- internet was slower
- SEO required HTML
- JS frameworks didn't exist

Traditional web systems used SSR heavily.

Examples:

- Django templates
- Jinja2
- PHP
- Ruby on Rails
- JSP

---

# <span style="color:#2563eb">**What Problems Does SSR Solve?**</span>

# <span style="color:#dc2626">**Advantages of SSR**</span>

---

## <span style="color:#16a34a">**1. Faster Initial Page Display**</span>

Browser immediately receives usable HTML.

No need to wait for heavy JavaScript.

---

## <span style="color:#16a34a">**2. Better SEO**</span>

Search engines can directly read HTML.

Important for:

- blogs
- news websites
- documentation
- e-commerce

---

## <span style="color:#16a34a">**3. Works Better on Weak Devices**</span>

Since browser does less work.

Good for:

- low-end phones
- older devices

---

## <span style="color:#16a34a">**4. Simpler Frontend Architecture**</span>

No huge frontend frameworks required.

---

## <span style="color:#16a34a">**5. Better First Contentful Paint (FCP)**</span>

Users see content quickly.

---

# <span style="color:#2563eb">**What Problems Exist with Server-Side Rendering?**</span>

# <span style="color:#dc2626">**Core Problems of SSR**</span>

---

## <span style="color:#16a34a">**1. Every Request Requires Full Rendering**</span>

Suppose 10,000 users open page.

Server must:

```text id="u4w8"
Render HTML
10,000 times
```

Huge CPU overhead.

---

## <span style="color:#16a34a">**2. Higher Server Load**</span>

Server performs:

- database queries
- rendering
- template parsing
- HTML generation

for every request.

---

## <span style="color:#16a34a">**3. Slower Interactivity**</span>

Traditional SSR pages reload completely.

Example:

```text id="z7x1"
Click button
    ↓
Full page refresh
```

Feels slower compared to SPA frameworks.

---

## <span style="color:#16a34a">**4. Poor Real-Time UX**</span>

Complex interactive apps become harder.

Example:

- chat apps
- dashboards
- drag-drop systems
- real-time editors

---

## <span style="color:#16a34a">**5. Tight Coupling of Frontend and Backend**</span>

UI and backend often strongly connected.

Harder for frontend/backend teams to scale independently.

---

# <span style="color:#2563eb">**Overheads of Server-Side Rendering**</span>

# <span style="color:#dc2626">**What Extra Work SSR Creates**</span>

---

## <span style="color:#16a34a">**1. CPU Overhead**</span>

Rendering templates repeatedly costs CPU.

Example:

```text id="r3n6"
Template parsing
Loop execution
String generation
HTML creation
```

for every request.

---

## <span style="color:#16a34a">**2. Memory Overhead**</span>

Each request may allocate:

- template context
- rendered strings
- response buffers

---

## <span style="color:#16a34a">**3. Network Overhead**</span>

SSR often sends larger HTML pages repeatedly.

---

## <span style="color:#16a34a">**4. Blocking Request Time**</span>

User waits until:

```text id="w8y2"
Data Fetching
   +
Rendering
```

completes.

---

## <span style="color:#16a34a">**5. Scaling Complexity**</span>

More users →

More rendering →

More CPU servers needed.

---

# <span style="color:#2563eb">**Example of SSR Overhead**</span>

Suppose page contains:

- user info
- posts
- comments
- notifications

For every request:

```text id="v6t3"
Database Queries
      ↓
Data Aggregation
      ↓
Jinja2 Rendering
      ↓
HTML Generation
      ↓
HTTP Response
```

Thousands of users multiply this cost heavily.

---

# <span style="color:#2563eb">**Constraints of Server-Side Rendering**</span>

# <span style="color:#dc2626">**Fundamental Architectural Constraints**</span>

---

## <span style="color:#16a34a">**1. Limited Rich Interactivity**</span>

SSR struggles with highly interactive UIs.

Example:

- Google Docs
- Figma
- advanced dashboards

These prefer CSR/SPA.

---

## <span style="color:#16a34a">**2. Page Reload Model**</span>

Traditional SSR apps often reload pages.

This creates slower UX.

---

## <span style="color:#16a34a">**3. Stateful UI is Harder**</span>

Managing:

- live updates
- client state
- transitions

becomes harder.

---

## <span style="color:#16a34a">**4. Rendering Bottleneck**</span>

Server becomes rendering bottleneck.

All users depend on server rendering capacity.

---

## <span style="color:#16a34a">**5. Harder Offline Support**</span>

SSR heavily depends on server availability.

---

# <span style="color:#2563eb">**What is Client-Side Rendering (CSR)?**</span>

CSR means:

> Browser JavaScript generates UI.

Server mainly provides:

- JSON APIs
- data endpoints

Frontend framework handles rendering.

Examples:

- React
- Vue
- Angular

---

# <span style="color:#2563eb">**CSR Flow**</span>

```text id="m2q7"
Browser Loads JS
      ↓
JS Fetches API Data
      ↓
React/Vue Builds UI
      ↓
Browser Updates DOM
```

---

# <span style="color:#2563eb">**Advantages of CSR**</span>

---

## <span style="color:#16a34a">**1. Highly Interactive UI**</span>

Excellent for:

- dashboards
- real-time apps
- rich UX

---

## <span style="color:#16a34a">**2. Faster Navigation After Initial Load**</span>

SPA apps update parts of page only.

No full reloads.

---

## <span style="color:#16a34a">**3. Better Separation of Frontend/Backend**</span>

Backend becomes pure API provider.

---

## <span style="color:#16a34a">**4. Reduced Server Rendering Cost**</span>

Browser handles rendering workload.

---

# <span style="color:#2563eb">**Problems of CSR**</span>

---

## <span style="color:#16a34a">**1. Slower Initial Load**</span>

Browser must:

- download JS
- execute JS
- fetch data
- render UI

before content appears.

---

## <span style="color:#16a34a">**2. SEO Challenges**</span>

Search engines may struggle.

---

## <span style="color:#16a34a">**3. Heavy Browser CPU Usage**</span>

Low-end devices may struggle.

---

# <span style="color:#2563eb">**When to Use Server-Side Rendering**</span>

Use SSR when:

| Good SSR Use Cases       |
| ------------------------ |
| Blogs                    |
| News websites            |
| Documentation sites      |
| SEO-heavy sites          |
| Simple dashboards        |
| Content-focused websites |
| E-commerce product pages |
| Admin panels             |

---

# <span style="color:#2563eb">**When to Use Client-Side Rendering**</span>

Use CSR when:

| Good CSR Use Cases          |
| --------------------------- |
| Chat apps                   |
| Real-time dashboards        |
| Social media apps           |
| Drag-drop systems           |
| Rich UI applications        |
| Highly interactive apps     |
| Complex state-heavy systems |

---

# <span style="color:#2563eb">**Modern Hybrid Approaches**</span>

Modern frameworks combine SSR + CSR.

Examples:

- [Next.js](https://nextjs.org/?utm_source=chatgpt.com)
- [Nuxt.js](https://nuxt.com/?utm_source=chatgpt.com)
- [SvelteKit](https://svelte.dev/docs/kit/introduction?utm_source=chatgpt.com)

They use:

```text id="t5w4"
SSR for initial load
+
CSR for interactivity
```

Best of both worlds.

---

# <span style="color:#2563eb">**Mental Model**</span>

---

## <span style="color:#16a34a">**SSR Philosophy**</span>

```text id="k9r1"
Server builds UI
Browser displays it
```

---

## <span style="color:#16a34a">**CSR Philosophy**</span>

```text id="u3m8"
Server provides data
Browser builds UI
```

---

# <span style="color:#2563eb">**Final Comparison Summary**</span>

| Feature            | SSR                  | CSR              |
| ------------------ | -------------------- | ---------------- |
| Rendering Location | Server               | Browser          |
| Initial Load Speed | Faster visually      | Slower           |
| Interactivity      | Moderate             | Excellent        |
| SEO                | Excellent            | Harder           |
| Server CPU Usage   | Higher               | Lower            |
| Browser CPU Usage  | Lower                | Higher           |
| Scalability        | Rendering bottleneck | Better scaling   |
| Rich UI Support    | Limited              | Excellent        |
| Architecture       | Simpler              | More complex     |
| Best For           | Content sites        | Interactive apps |
