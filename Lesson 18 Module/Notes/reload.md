# 1️⃣ Short Answer (Intuition First)

> We need to **reload a module** because **Python imports a module only once per process**.
> After that, **changes in the `.py` file are ignored**, unless we explicitly reload it.

---

# 2️⃣ What Really Happens During `import` (Internals)

Let’s break Python’s behavior step-by-step.

---

## Step 1: Python sees `import mymodule`

Python does **NOT** immediately read the file.

Instead, it checks:

```python
sys.modules
```

This is a **global dictionary**:

```python
{ module_name : module_object }
```

---

## Step 2: Module already in `sys.modules`?

### Case A: ❌ Not present

Python will:

1. Read `mymodule.py`
2. Compile to bytecode
3. Create a **module object**
4. Execute top-level code
5. Store module object in `sys.modules`

✔️ Import finished

---

### Case B: ✅ Already present

Python will:

1. **SKIP the file**
2. **SKIP execution**
3. Return the existing module object

❌ No recompilation
❌ No re-execution
❌ No change picked up

---

### ⚠️ THIS IS THE KEY REASON FOR RELOAD

Python assumes:

> “If a module is already loaded, I trust it.”

---

## Step 3: Why Python does this?

### Performance reasons

- Avoid repeated disk I/O
- Avoid repeated compilation
- Ensure **single shared module state**

Imagine:

```python
import config
import config
import config
```

You don’t want:

- variables reset
- connections recreated
- memory duplicated

---

# 3️⃣ Where `.pyc` Fits (Clarifying a Common Confusion)

Important correction to your earlier understanding:

> Python **does NOT execute `.pyc` from `sys.modules`**

Correct model:

- `sys.modules` stores **module objects**
- `.pyc` is just **cached bytecode on disk**

### `.pyc` purpose:

- Faster future startup
- Skip recompilation if source unchanged

But:
❌ `.pyc` does NOT auto-reload on source change during runtime

---

# 4️⃣ Why Changes Are Ignored Without Reload

Example timeline:

```text
Python process starts
↓
import mymodule
↓
mymodule stored in sys.modules
↓
You modify mymodule.py
↓
import mymodule again ❌
```

Python says:

> “Already imported. Returning cached module.”

---

# 5️⃣ What `reload()` Actually Does Internally

```python
from importlib import reload
reload(mymodule)
```

### Internally:

1. Re-reads `.py` file
2. Recompiles to bytecode
3. Re-executes top-level code
4. Updates existing module object

⚠️ Same object, refreshed contents

---

# 6️⃣ Why Reload Is Rare in Production

Reload:

- Can break references
- Doesn’t reset everything safely
- Can cause inconsistent state

Used mainly in:

- REPL
- notebooks
- debugging
- hot development

---
