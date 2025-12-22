## Step 1️⃣ Create a `.py` file (this _is_ your module)

Any Python file can be a module **if it can be imported**.

📁 Example file:

```text
math_utils.py
```

📄 Contents:

```python
# math_utils.py

PI = 3.14159

def add(a, b):
    return a + b

def square(x):
    return x * x
```

✔️ You have now **defined a user-defined module**.

---

## Step 2️⃣ Ensure the module is importable (VERY IMPORTANT)

Python must be able to **find** the module.

Python searches in `sys.path`, in this order:

1. Current working directory
2. Directories in `PYTHONPATH`
3. Standard library
4. site-packages

### Quick check:

```python
import sys
print(sys.path)
```

📌 Easiest approach:

- Keep your module in the **same directory** as the script that imports it

---

## Step 3️⃣ Import the module

### Option 1: Import entire module

```python
import math_utils

print(math_utils.add(2, 3))
print(math_utils.square(4))
```

✔️ Best for readability and avoiding name collisions.

---

### Option 2: Import specific members

```python
from math_utils import add, square

print(add(2, 3))
print(square(4))
```

✔️ Shorter names, but risk of conflicts.

---

### Option 3: Import with alias

```python
import math_utils as mu

print(mu.square(5))
```

✔️ Common in real projects.

---

## Step 4️⃣ Use `__name__ == "__main__"` (Best Practice)

Add this to your module:

```python
# math_utils.py

def add(a, b):
    return a + b

if __name__ == "__main__":
    print(add(2, 3))  # runs only when executed directly
```

### Why?

- Prevents test/debug code from running during import
- Makes module reusable and executable

---

## Step 5️⃣ (Optional) Create `__pycache__`

When imported:

```python
import math_utils
```

Python automatically:

- compiles to bytecode
- stores `.pyc` in `__pycache__`

You **do nothing manually**.

---

## Step 6️⃣ Verify module loading (debugging tip)

```python
import sys
print(sys.modules.keys())
```

If your module appears → import succeeded.

---

## Step 7️⃣ Modify and reload (during development)

Python will **not auto-reload** changed modules.

```python
import importlib
import math_utils

importlib.reload(math_utils)
```

---

## Step 8️⃣ (Optional) Organize into packages (preview)

```
project/
│── main.py
│── utils/
│   ├── __init__.py
│   └── math_utils.py
```

```python
from utils.math_utils import add
```

---

## Final Checklist (Interview-Ready)

✔️ Create `.py` file
✔️ Place it in importable path
✔️ Define functions/classes/variables
✔️ Import using `import` / `from`
✔️ Use `__name__ == "__main__"`
✔️ Reload explicitly if changed

---

## One-line Interview Answer

> To define a user-defined module in Python, create a `.py` file containing reusable code, place it in Python’s import path, and import it using the `import` statement. Python executes the module once, caches it in memory, and allows reuse across programs.

---
