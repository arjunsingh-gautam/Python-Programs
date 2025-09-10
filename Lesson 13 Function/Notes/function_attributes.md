Perfect, let’s make a **clear set of notes** for your study. I’ll keep it structured and deep, so you can revise later like a mini-handbook.

---

# 📘 Function Attributes in Python

---

## 1. **Syntax**

Since functions are objects in Python, we can attach attributes to them using dot notation:

```python
function_name.attribute_name = value
```

Examples:

```python
def greet():
    print("Hello")

greet.language = "English"   # create attribute
print(greet.language)        # access attribute
```

---

## 2. **How to Create Function Attributes**

There are **two common ways**:

### (a) Outside the function

```python
def my_func():
    pass

my_func.counter = 0   # attach attribute
```

### (b) Inside the function (self-initializing)

```python
def my_func():
    if not hasattr(my_func, "counter"):
        my_func.counter = 0   # initialize once
    my_func.counter += 1
    print("Called", my_func.counter, "times")
```

---

## 3. **Use Cases**

Function attributes are useful when you need a function to “remember” or carry data across calls:

- **Counters** → track how many times a function was called.
- **Toggles** → alternate between states (`ON`/`OFF`, `Flip`/`Flop`).
- **Caching / Memoization (simple)** → store previous results without a separate dictionary.
- **Configuration** → attach small pieces of metadata (e.g., `my_func.version = "1.0"`).

---

## 4. **Working of Function Attributes**

- In Python, **functions are first-class objects**.
- Just like objects of a class, they have a namespace (`__dict__`) where attributes can be stored.
- Example:

  ```python
  def hello(): pass
  hello.a = 10
  print(hello.__dict__)  # {'a': 10}
  ```

- Attributes “stick” to the function object until you delete them or program ends.

---

## 5. **Precautions**

- **Don’t confuse with local variables**:
  Attributes are tied to the _function object_, not the _function body_.

  ```python
  def f():
      x = 0  # local, recreated each call
  f.count = 0  # attribute, persists across calls
  ```

- **Not thread-safe**:
  If multiple threads call the function, attributes can be overwritten unpredictably.

- **Not for heavy state management**:
  Use classes if state gets complex. Function attributes are fine for small helpers.

- **Avoid clashing with built-ins**:
  Functions already have attributes like `__name__`, `__doc__`. Don’t overwrite these unless intentional.

---

## ✅ Quick Example: Toggle with Function Attribute

```python
def toggle():
    if not hasattr(toggle, "state"):
        toggle.state = "OFF"
    toggle.state = "ON" if toggle.state == "OFF" else "OFF"
    return toggle.state

print(toggle())  # ON
print(toggle())  # OFF
print(toggle())  # ON
```

---

# ✨ Summary

- **Syntax:** `function.attr = value`
- **Create:** inside or outside the function.
- **Use cases:** counters, toggles, memoization, metadata.
- **Working:** attributes live in the function’s object dictionary.
- **Precautions:** don’t overuse; for complex state use classes.

---

🔎 Check-in for you:
If I run this code:

```python
def adder(x, y):
    return x + y

adder.calls = 0
print(adder.calls)
adder.calls += 1
print(adder.calls)
```

---

---

Perfect — let’s dive into those built-in functions. These are **general Python functions** (not just for functions) that let you work with attributes of **any object**.

Since functions are also objects, you can use them with functions too.

---

# 🔑 Attribute Management Functions in Python

---

## 1. **`hasattr(object, name)`**

- Checks if an object has an attribute with the given name.
- Returns `True` / `False`.

```python
def greet(): pass
greet.lang = "English"

print(hasattr(greet, "lang"))   # True
print(hasattr(greet, "count"))  # False
```

---

## 2. **`getattr(object, name[, default])`**

- Gets the value of an attribute.
- If attribute doesn’t exist:

  - raises `AttributeError` (if `default` not given),
  - or returns `default` (if provided).

```python
def greet(): pass
greet.lang = "English"

print(getattr(greet, "lang"))        # English
print(getattr(greet, "count", 0))    # 0 (returns default instead of error)
```

---

## 3. **`setattr(object, name, value)`**

- Sets (creates/updates) an attribute.
- Equivalent to `object.name = value`.

```python
def greet(): pass
setattr(greet, "lang", "English")   # same as greet.lang = "English"
print(greet.lang)  # English
```

---

## 4. **`delattr(object, name)`**

- Deletes an attribute.
- Equivalent to `del object.name`.

```python
def greet(): pass
greet.lang = "English"

delattr(greet, "lang")    # same as: del greet.lang
print(hasattr(greet, "lang"))  # False
```

---

# ⚡ Putting it all together

```python
def counter():
    if not hasattr(counter, "calls"):   # check if attribute exists
        setattr(counter, "calls", 0)    # create attribute
    counter.calls += 1                  # update
    return getattr(counter, "calls")    # fetch safely

print(counter())  # 1
print(counter())  # 2
delattr(counter, "calls")               # delete attribute
print(hasattr(counter, "calls"))        # False
```

---

# ✅ Summary

- **`hasattr(obj, "attr")`** → check if attribute exists
- **`getattr(obj, "attr", default)`** → get attribute value
- **`setattr(obj, "attr", value")`** → set/create attribute
- **`delattr(obj, "attr")`** → remove attribute

These four are the “Swiss-army knife” for dealing with attributes dynamically.

---

📝 **Mini Task for you:**
Write a function `bookmark()` that remembers the **last string** it received.

- On each call, it should print:
  `"Previous: <last>, Current: <new>"`
- Use `hasattr`, `setattr`, and `getattr` to manage the memory.

Would you like me to sketch the **skeleton code** with placeholders, or do you want to attempt it fully on your own first?
