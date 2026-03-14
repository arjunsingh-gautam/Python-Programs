# <span style="color:#ff1744">**EAFP Principle in Python (Easier to Ask Forgiveness than Permission)**</span>

---

## <span style="color:#8338ec">**1. What is the EAFP Principle?**</span>

EAFP means:

> **Try the operation first. If it fails, handle the exception.**

Instead of checking conditions beforehand, you **assume the operation will work** and catch errors if they occur.

General pattern:

```python
try:
    risky_operation()
except SomeError:
    handle_error()
```

Python’s philosophy prefers **EAFP** because Python is dynamically typed and uses **duck typing**.

---

## <span style="color:#3a86ff">**2. Simple Analogy for EAFP**</span>

Imagine opening a door.

EAFP approach:

1. Try to open the door.
2. If it is locked, handle the situation.

You **don’t first check if the door is locked**.

---

## <span style="color:#06d6a0">**3. Simple Code Example**</span>

Suppose we want to access a dictionary key.

### EAFP Approach

```python
data = {"name": "Alice", "age": 25}

try:
    print(data["salary"])
except KeyError:
    print("Salary not found")
```

Execution:

1. Python tries to access `"salary"`
2. Key not found
3. `KeyError` raised
4. Exception handled

Output:

```
Salary not found
```

---

## <span style="color:#8338ec">**4. Why EAFP Is Used**</span>

EAFP exists because Python emphasizes:

```
Behavior over strict type checking
```

Reasons:

1. Dynamic typing
2. Duck typing
3. Faster code in many cases
4. Cleaner logic

Instead of writing many checks, Python encourages **attempt first, handle failure later**.

---

## <span style="color:#3a86ff">**5. Practical Example (File Handling)**</span>

### EAFP way

```python
try:
    file = open("data.txt")
    content = file.read()
except FileNotFoundError:
    print("File does not exist")
```

Here we **directly attempt the operation**.

---

## <span style="color:#06d6a0">**6. Benefits of EAFP**</span>

### 1. Cleaner code

No unnecessary checks.

Example:

```
try operation → handle failure
```

instead of:

```
check condition → then operation
```

---

### 2. Pythonic style

Most Python libraries follow EAFP.

Examples:

- file handling
- dictionary access
- attribute access

---

### 3. Better performance in many cases

If failures are rare, checking beforehand wastes time.

Example:

```
checking condition + operation
```

vs

```
operation only
```

---

### 4. Avoids race conditions

Example:

Checking file existence before opening it:

```
File may disappear between check and use
```

EAFP avoids this issue.

---

## <span style="color:#8338ec">**7. Constraints / Limitations of EAFP**</span>

### 1. Exceptions are expensive

Exception handling has overhead.

If errors happen frequently, performance may drop.

---

### 2. Harder debugging if exceptions are overused

Catching very broad exceptions can hide bugs.

Bad practice:

```python
try:
    do_something()
except:
    pass
```

---

### 3. Code flow may become less obvious

Too many try-except blocks may reduce readability.

---

# <span style="color:#ff1744">**LBYL Principle (Look Before You Leap)**</span>

---

## <span style="color:#8338ec">**1. What is LBYL?**</span>

LBYL means:

> **Check conditions before performing the operation.**

General pattern:

```
if condition:
    perform operation
else:
    handle case
```

This approach is common in **statically typed languages**.

---

## <span style="color:#3a86ff">**2. Simple Analogy for LBYL**</span>

Before opening a door:

1. Check if the door is locked
2. If unlocked → open it

You verify before acting.

---

## <span style="color:#06d6a0">**3. Simple Code Example**</span>

Dictionary example again.

### LBYL Approach

```python
data = {"name": "Alice", "age": 25}

if "salary" in data:
    print(data["salary"])
else:
    print("Salary not found")
```

Python checks first.

---

## <span style="color:#8338ec">**4. Why LBYL Is Used**</span>

LBYL is useful when:

1. Errors are expected frequently
2. Exceptions would be costly
3. Program logic requires explicit checks

Example:

```
division by zero
```

Better to check first.

---

## <span style="color:#3a86ff">**5. Example: Division**</span>

LBYL:

```python
x = 10
y = 0

if y != 0:
    print(x / y)
else:
    print("Cannot divide by zero")
```

---

## <span style="color:#06d6a0">**6. Benefits of LBYL**</span>

### 1. Clear logical flow

Conditions are explicit.

---

### 2. Avoids exception overhead

If failure cases are frequent, this can be faster.

---

### 3. Easier reasoning in critical systems

For safety-critical code (finance, embedded), explicit checks help.

---

## <span style="color:#8338ec">**7. Constraints / Limitations of LBYL**</span>

### 1. Code becomes verbose

Many condition checks.

---

### 2. Duplicate work

Example:

```
check condition
then perform operation
```

Operation may internally perform the same check.

---

### 3. Race conditions

Example:

```python
if os.path.exists("file.txt"):
    open("file.txt")
```

Between check and open:

```
File may be deleted
```

Program fails.

---

# <span style="color:#ff1744">**Comparison: EAFP vs LBYL**</span>

| Feature         | EAFP                      | LBYL                      |
| --------------- | ------------------------- | ------------------------- |
| Philosophy      | Try first, handle errors  | Check first, then act     |
| Python style    | Preferred                 | Less Pythonic             |
| Code size       | Usually shorter           | Often longer              |
| Error detection | Runtime exception         | Conditional logic         |
| Performance     | Faster if errors are rare | Better if errors frequent |
| Race conditions | Avoids many cases         | More prone                |
| Readability     | Sometimes harder          | Often clearer             |

---

# <span style="color:#ff1744">**Example Comparing Both Approaches**</span>

## <span style="color:#8338ec">**Task: Access Object Attribute**</span>

### EAFP

```python
try:
    print(obj.name)
except AttributeError:
    print("Object has no name")
```

---

### LBYL

```python
if hasattr(obj, "name"):
    print(obj.name)
else:
    print("Object has no name")
```

Both work, but Python developers usually prefer **EAFP**.

---

# <span style="color:#ff1744">**When to Use Each Approach**</span>

### Use EAFP when:

```
Failure is rare
Operation is safe to attempt
Working with duck typing
```

Examples:

- file operations
- dictionary access
- attribute access

---

### Use LBYL when:

```
Failure is common
Exceptions would be expensive
Explicit logic is required
```

Examples:

- user input validation
- division checks
- numeric boundaries

---

# <span style="color:#ff1744">**Final Mental Model**</span>

EAFP mindset:

```
Try doing it
If it fails → recover
```

LBYL mindset:

```
Check everything
Then perform operation
```

Python generally prefers:

```
EAFP + Duck Typing
```

because it produces **flexible and expressive code**.

---
