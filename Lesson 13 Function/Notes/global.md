### 1. **What does `global` mean in Python?**

Normally, when you write a variable inside a function, Python treats it as **local** to that function.
But if you want to **modify** a variable that lives in the global scope (outside all functions), you need to declare it with `global`.

---

### 2. **When to use it**

- When you **need to assign** a new value to a global variable inside a function.
- Example: updating a global counter or config without passing it around.

---

### 3. **When NOT to use it**

- If you just need to **read** a global variable, no `global` needed.
- If you can avoid globals by using **function parameters and return values** → that’s cleaner (especially in larger projects).
- Overusing globals makes code **hard to debug** because any function can change the variable.

---

### 4. **Practical examples**

#### Example without `global` (fails)

```python
x = 10

def change():
    x = x + 1  # ❌ UnboundLocalError
    print(x)

change()
```

Why? → Python thinks `x` inside the function is a **new local variable**, so it complains.

---

#### Example with `global` (works)

```python
x = 10

def change():
    global x
    x = x + 1
    print(x)

change()   # 11
change()   # 12
print(x)   # 12
```

Here `global x` tells Python: “Don’t create a new local variable, use the one outside.”

---

#### Example where you don’t need `global`

```python
x = 10

def show():
    print(x)   # ✅ allowed, just reading

show()   # 10
```

---

#### Example of better alternative (returning value)

```python
x = 10

def change(val):
    return val + 1

x = change(x)   # 11
```

This avoids messy globals.

---

✅ **Summary:**

- Use `global` only when you _must_ assign to a global variable inside a function.
- Avoid it when possible → prefer function parameters & return values.

---
