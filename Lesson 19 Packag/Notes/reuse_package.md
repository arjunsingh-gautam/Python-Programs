# **<span style="color:#c1121f">Ways of Reusing Packages</span>**

## 1️⃣ What “reusing a package” means

> You **write a package once** and **use it in many places** by importing it.

Instead of:

```text
copy-paste code ❌
```

You do:

```python
import my_package  ✅
```

---

## 2️⃣ Method 1: Reuse Inside the Same Project (Most Common)

#### Folder structure

```
project/
├── mypkg/
│   ├── __init__.py
│   └── math_utils.py
└── main.py
```

---

#### `math_utils.py`

```python
def add(a, b):
    return a + b
```

---

#### `__init__.py`

```python
from .math_utils import add
```

---

#### `main.py`

```python
from mypkg import add
print(add(2, 3))
```

✔️ Works because:

- Python searches current project directory
- Package is on `sys.path`

📌 **Best for:**

- small to medium projects
- internal reuse

---

## 3️⃣ Method 2: Reuse Using Absolute Path (`sys.path`)

Python only imports from paths listed in:

```python
sys.path
```

You can **add your package path manually**.

---

#### Example

```
shared_lib/
└── mypkg/
    ├── __init__.py
    └── utils.py
```

---

#### In any script

```python
import sys
sys.path.append("/full/path/to/shared_lib")

from mypkg.utils import helper
```

✔️ Quick & dirty
❌ Not recommended for production

📌 **Use only for experiments**

---

## 4️⃣ Method 3: Reuse via Environment Variable (`PYTHONPATH`)

Set path once, reuse everywhere.

#### Linux / macOS

```bash
export PYTHONPATH="/home/user/shared_lib"
```

#### Windows

```cmd
set PYTHONPATH=C:\shared_lib
```

Then:

```python
import mypkg
```

✔️ Cleaner than `sys.path.append`
❌ Environment-dependent

📌 **Good for personal setups**

---

## 5️⃣ Method 4: Reuse by Installing Package (BEST PRACTICE)

This is how **real libraries** work.

---

### Step 1: Create package structure

```
mypkg/
├── mypkg/
│   ├── __init__.py
│   └── math_utils.py
├── pyproject.toml
```

---

### Step 2: Minimal `pyproject.toml`

```toml
[project]
name = "mypkg"
version = "0.1.0"
```

---

### Step 3: Install locally

```bash
pip install -e .
```

Now you can use it **from anywhere**:

```python
import mypkg
```

✔️ Professional
✔️ Versioned
✔️ Reusable across projects

---

## 6️⃣ Method 5: Reuse via Git Repository

```bash
pip install git+https://github.com/you/mypkg.git
```

✔️ Ideal for:

- teams
- private libraries
- open source

---

## 7️⃣ Method 6: Reuse via PyPI (Industry Level)

```bash
pip install requests
```

This is:

- package reuse at scale
- version controlled
- dependency managed

📌 **Same mechanism as Method 4**

---

## 8️⃣ How Python Actually Finds Reused Packages

Order Python checks:

1. Current directory
2. PYTHONPATH
3. Standard library
4. site-packages (pip installed)

If found → imported
Else → `ModuleNotFoundError`

---

## 9️⃣ Very Simple Analogy (Remember This)

Think of a package as a **toolbox**:

| Method       | Analogy                 |
| ------------ | ----------------------- |
| Same project | Toolbox in same room    |
| sys.path     | You carried it manually |
| PYTHONPATH   | Fixed shelf             |
| pip install  | Installed in workshop   |
| PyPI         | Bought from market      |

---

## 🔟 Common Mistakes to Avoid

❌ Copy-pasting package folders
❌ Editing installed packages directly
❌ Using relative imports outside packages
❌ Forgetting `__init__.py`

---

## 1️⃣1️⃣ Interview-Ready Summary

> A Python package can be reused by placing it on Python’s import path or installing it via pip. Installing packages is the recommended approach for scalable, reusable, and maintainable code.

---

## 1️⃣2️⃣ Which Method Should _You_ Use?

| Situation                | Best Method        |
| ------------------------ | ------------------ |
| Learning / small project | Same project       |
| Experiments              | `sys.path`         |
| Personal reuse           | PYTHONPATH         |
| Serious project          | `pip install -e .` |
| Team / production        | PyPI / Git         |

---
