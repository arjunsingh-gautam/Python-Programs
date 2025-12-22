# 1️⃣ Ways of Importing Modules in Python

Python provides **multiple import styles** to balance:

- readability
- namespace safety
- convenience

---

## 1. `import module_name`

### Syntax

```python
import math
```

### How it works

- Imports the **entire module**
- Module name becomes a **namespace**

### Usage

```python
print(math.sqrt(16))
print(math.pi)
```

### When to use

✔️ Most recommended
✔️ Avoids name collisions
✔️ Best for large projects

---

## 2. `import module_name as alias`

### Syntax

```python
import numpy as np
```

### How it works

- Same as normal import
- Shorter alias

### Usage

```python
np.array([1, 2, 3])
```

### When to use

✔️ Long module names
✔️ Industry standard (`np`, `pd`, `plt`)

---

## 3. `from module import name`

### Syntax

```python
from math import sqrt, pi
```

### How it works

- Imports **specific members**
- No module namespace

### Usage

```python
print(sqrt(16))
print(pi)
```

### Pros / Cons

✅ Cleaner syntax
❌ Risk of name conflict
❌ Harder to track origin

---

## 4. `from module import name as alias`

### Syntax

```python
from math import sqrt as s
```

### Usage

```python
print(s(25))
```

✔️ Useful when avoiding conflicts

---

## 5. `from module import *` (❌ NOT RECOMMENDED)

### Syntax

```python
from math import *
```

### Problems

❌ Pollutes namespace
❌ Unclear source of names
❌ Breaks readability
❌ Dangerous in large codebases

Only safe in:

- interactive shell
- controlled scripts

---

## 6. Importing User-Defined Modules

### Directory structure

```
project/
│── main.py
│── utils.py
```

### Code

```python
import utils
utils.helper()
```

---

## 7. Importing from Packages

### Structure

```
project/
│── main.py
│── helpers/
│   ├── __init__.py
│   └── math_utils.py
```

### Import

```python
from helpers.math_utils import add
```

---

## 8. Relative Imports (inside packages only)

```python
from .math_utils import add
from ..core import config
```

⚠️ Cannot be used in top-level scripts

---

# 2️⃣ What is `__name__ == "__main__"`?

This is **one of the most important Python concepts**.

---

## The Core Idea (Plain English)

> Python needs to know whether a file is being
> 🔹 **run directly**
> 🔹 **or imported by another file**

`__name__` tells Python that.

---

## How `__name__` works

| Situation         | `__name__` value |
| ----------------- | ---------------- |
| File run directly | `"__main__"`     |
| File imported     | module name      |

---

## Simple Example

### File: `math_utils.py`

```python
def add(a, b):
    return a + b

print("Math module loaded")
```

### Case 1: Run directly

```bash
python math_utils.py
```

Output:

```
Math module loaded
```

---

### Case 2: Import it

```python
import math_utils
```

Output:

```
Math module loaded
```

❌ Problem:

- Code runs even when imported

---

## Solution: `__name__ == "__main__"`

### Fixed version

```python
def add(a, b):
    return a + b

if __name__ == "__main__":
    print("Running directly")
```

---

### Behavior

#### Run directly

```bash
python math_utils.py
```

Output:

```
Running directly
```

---

#### Imported

```python
import math_utils
```

Output:

```
(no output)
```

---

## 🧠 Analogy (Very Important)

Think of a module as a **machine**.

- `import module` → _install the machine_
- `__main__` → _press the power button_

You don’t want the machine to start working **just because it was installed**.

---

## Why this is essential

✔️ Prevents unwanted execution
✔️ Enables testing inside modules
✔️ Allows reuse
✔️ Industry best practice

---

## Common Use Cases

### 1️⃣ Testing code

```python
if __name__ == "__main__":
    test_add()
```

---

### 2️⃣ Script + Library dual behavior

```python
if __name__ == "__main__":
    main()
```

---

### 3️⃣ Entry point definition

Used by:

- scripts
- CLIs
- libraries

---

## Interview-Ready One-Liner

> `__name__ == "__main__"` ensures that code runs only when a Python file is executed directly, and not when it is imported as a module.

---

## Summary Table

| Import Style              | Use           |
| ------------------------- | ------------- |
| `import module`           | Best practice |
| `import module as alias`  | Convenience   |
| `from module import name` | Specific use  |
| `from module import *`    | Avoid         |
| `relative imports`        | Packages only |

---
