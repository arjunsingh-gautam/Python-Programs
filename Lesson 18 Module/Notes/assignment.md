---
# 🧠 15-Minute Python Modules Revision Assignment

⏱ **Time limit:** 15 minutes
🛠 **Tools:** Terminal + editor (no notebook)
---

## PART A — Module Creation & Import Basics (4 min)

### Task A1: Create a module

Create a file named:

📄 `math_ops.py`

```python
print("math_ops module loaded")

PI = 3.14

def add(a, b):
    return a + b
```

---

### Task A2: Import it

Create another file:

📄 `main.py`

```python
import math_ops

print(math_ops.PI)
print(math_ops.add(2, 3))
```

#### Expected Observation

- When does `"math_ops module loaded"` print?
- How many times does it print if you run `main.py` twice?

✍️ **Write down your answer**

---

## PART B — Module Cache (`sys.modules`) (3 min)

### Task B1: Inspect module cache

Add this to `main.py`:

```python
import sys
print("math_ops" in sys.modules)
```

---

### Task B2: Import again

Add:

```python
import math_ops
import math_ops
```

#### Questions:

1. Does the print statement run again?
2. Why not?

✍️ **Answer in 1–2 lines**

---

## PART C — `__name__ == "__main__"` (4 min)

### Task C1: Modify module

Update `math_ops.py`:

```python
def add(a, b):
    return a + b

def test():
    print("Testing add:", add(2, 3))

if __name__ == "__main__":
    test()
```

---

### Task C2: Run directly

```bash
python math_ops.py
```

#### Observation:

- What prints?
- Why?

---

### Task C3: Import it

```bash
python main.py
```

#### Observation:

- Does `test()` run?
- Why not?

✍️ **Explain in simple language**

---

## PART D — Reloading Modules (4 min)

### Task D1: Start Python REPL

```bash
python
```

---

### Task D2: Import module

```python
import math_ops
math_ops.add(2, 3)
```

---

### Task D3: Modify module

Change `math_ops.py`:

```python
def add(a, b):
    return a * b
```

---

### Task D4: Use again (no reload)

```python
math_ops.add(2, 3)
```

#### Observation:

- Old result or new result?
- Why?

---

### Task D5: Reload

```python
from importlib import reload
reload(math_ops)
math_ops.add(2, 3)
```

✔️ Note the change

---

## BONUS (Optional, 2 min if time allows)

### Task E — Dangerous Reload Behavior

In REPL:

```python
from math_ops import add
reload(math_ops)
add(2, 3)
```

❓ Why didn’t it change?

✍️ Write a one-line reason.

---

# 📌 Final Reflection (Must Answer)

Answer these **without looking up**:

1. Why does Python import a module only once?
2. Where is the module cached?
3. When is `reload()` required?
4. Why is `__name__ == "__main__"` important?
5. Why does reload not update `from module import name`?

---

# ✅ If You Can Answer These…

You **fully understand Python modules** at an implementation level.

---
