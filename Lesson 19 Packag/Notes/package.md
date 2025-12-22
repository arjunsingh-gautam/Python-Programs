# **<span style="color:#c1121f">Packages in Python</span>**

## 1️⃣ What is a Package in Python?

#### Definition

> A **package** is a **directory** that groups related **modules** together under a common namespace.

In short:

```
module  = single .py file
package = folder of modules
```

---

## 2️⃣ Why Packages Exist (Problem They Solve)

Imagine a large project **without packages**:

```text
add.py
subtract.py
multiply.py
divide.py
user.py
auth.py
payment.py
```

Problems:
❌ Name conflicts
❌ No logical grouping
❌ Hard to scale
❌ Messy imports

---

#### Packages solve this by:

- Organizing code logically
- Avoiding name collisions
- Making large systems manageable
- Enabling reusable libraries

---

## 3️⃣ Basic Package Structure

#### Example

```text
myapp/
│
├── math_utils/
│   ├── add.py
│   ├── subtract.py
│
├── auth/
│   ├── login.py
│   ├── signup.py
│
└── main.py
```

Here:

- `math_utils` → package
- `add.py`, `subtract.py` → modules

---

## 4️⃣ What Makes a Directory a Package?

### Old Python (≤ 3.2)

A directory was a package **only if** it contained:

```text
__init__.py
```

---

### Modern Python (≥ 3.3)

Two types of packages exist:

#### 1️⃣ Regular package

```text
mypkg/
├── __init__.py
├── mod1.py
```

#### 2️⃣ Namespace package (advanced)

```text
mypkg/
├── mod1.py
```

✔️ No `__init__.py` needed
✔️ Used by large frameworks
✔️ Rare in day-to-day work

⚠️ For learning and interviews:

> **Always use `__init__.py`**

---

## 5️⃣ Role of `__init__.py`

`__init__.py` runs **when the package is imported**.

#### Example

```text
math_utils/
├── __init__.py
├── add.py
```

```python
## __init__.py
print("math_utils loaded")
```

```python
import math_utils
```

Output:

```
math_utils loaded
```

---

#### Common uses of `__init__.py`

✔️ Package initialization
✔️ Exposing selected APIs
✔️ Setting up imports

---

### Exposing APIs (Important)

```python
## math_utils/__init__.py
from .add import add
```

Now:

```python
from math_utils import add
```

Instead of:

```python
from math_utils.add import add
```

---

## 6️⃣ How Python Finds Packages (Import System)

When you write:

```python
import math_utils.add
```

Python searches directories in:

```python
sys.path
```

Order:

1. Current script directory
2. PYTHONPATH
3. Standard library
4. Site-packages

---

## 7️⃣ Importing from Packages (All Ways)

#### 1. Absolute import (recommended)

```python
from math_utils.add import add
```

---

#### 2. Package import

```python
import math_utils.add
math_utils.add.add(2, 3)
```

---

#### 3. Import via `__init__.py`

```python
from math_utils import add
```

---

#### 4. Relative imports (inside package only)

```python
from .add import add
from ..auth.login import login
```

⚠️ Cannot be used in scripts

---

## 8️⃣ Packages vs Modules (Clear Difference)

| Feature     | Module      | Package          |
| ----------- | ----------- | ---------------- |
| Structure   | `.py` file  | directory        |
| Purpose     | Single unit | Group of modules |
| Namespace   | Flat        | Hierarchical     |
| Scalability | Low         | High             |

---

## 9️⃣ Real-World Example (How Frameworks Use Packages)

Django:

```text
django/
├── db/
├── http/
├── urls/
├── forms/
```

NumPy:

```text
numpy/
├── linalg/
├── fft/
├── random/
```

---

## 1️⃣0️⃣ Common Mistakes (Very Important)

❌ Forgetting `__init__.py`
❌ Using relative imports in scripts
❌ Circular imports between packages
❌ Importing everything (`*`)

---

## 1️⃣1️⃣ Interview-Ready Explanation

> A package is a directory that organizes related modules under a common namespace, improving structure, scalability, and reuse. Python loads packages using the import system and executes `__init__.py` during initialization.

---

## 1️⃣2️⃣ Mental Model (Remember This)

📦 **Package = Folder**
📄 **Module = File**
🚪 **`__init__.py` = Entry gate**

---
