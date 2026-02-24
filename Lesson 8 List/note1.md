# 1️⃣ What Is Slicing?

General form:

```python
sequence[start : stop : step]
```

It does **NOT** mutate.
It returns a **new sequence** of the same type (for built-ins like list, tuple, str).

---

# 2️⃣ Core Semantic Rules

### Rule 1 — Start is INCLUDED

### Rule 2 — Stop is EXCLUDED

### Rule 3 — Step decides direction

- `step > 0` → move right
- `step < 0` → move left
- `step = 0` → ❌ ValueError

### Rule 4 — Traversal must be logically reachable

If:

- `step > 0` → `start < stop`
- `step < 0` → `start > stop`

Otherwise → empty slice.

---

# 3️⃣ Internal Mental Model

Slicing behaves like:

```python
for i in range(start, stop, step):
    result.append(sequence[i])
```

But BEFORE this, Python:

1. Fills missing defaults
2. Normalizes indices
3. Clips to bounds
4. Computes slice length mathematically

Then copies elements.

It does NOT dynamically walk and stop.

---

# 4️⃣ Default Values (Critical Section)

Defaults depend ONLY on step sign.

## Case A — step > 0

| Parameter | Default  |
| --------- | -------- |
| start     | 0        |
| stop      | len(seq) |

Equivalent to:

```python
range(0, len(seq), step)
```

Example:

```python
l[:]
```

Becomes:

```python
l[0:len(l):1]
```

---

## Case B — step < 0

| Parameter | Default              |
| --------- | -------------------- |
| start     | len(seq) - 1         |
| stop      | -1 (boundary marker) |

Equivalent to:

```python
range(len(seq)-1, -1, step)
```

Example:

```python
l[::-1]
```

Becomes:

```python
range(len(l)-1, -1, -1)
```

---

⚠ Important:

That `-1` stop is a boundary, not the actual last element.

Because stop is excluded.

---

# 5️⃣ Index Normalization

Negative indices are converted BEFORE slicing logic.

Rule:

```python
real_index = len(seq) + index
```

Example:

```python
l = [1,2,3,4,5,6]
```

Length = 6

| Given | Normalized |
| ----- | ---------- |
| -1    | 5          |
| -2    | 4          |
| -6    | 0          |

So:

```python
l[1:-2]
```

Becomes:

```python
l[1:4]
```

---

# 6️⃣ Why Your Examples Did Not Work

## Example 1

```python
l[1:4:-1]
```

Given:

- start = 1
- stop = 4
- step = -1

Step is negative → must move left.

Check:

```python
1 > 4 ❌
```

Impossible traversal.

Equivalent to:

```python
list(range(1,4,-1))
```

Which is empty.

---

## Example 2

```python
l[1:-2:-1]
```

Normalize -2:

```python
-2 → 4
```

Now:

```python
l[1:4:-1]
```

Same as above.

Again:

```python
1 > 4 ❌
```

Empty.

---

You were comparing raw values:

```python
1 > -2
```

But slicing compares normalized values:

```python
1 > 4
```

---

# 7️⃣ Complete Order of Internal Processing

When Python sees:

```python
l[start:stop:step]
```

It does:

### Step 1 — If step is None → set to 1

### Step 2 — If step == 0 → error

### Step 3 — Fill defaults based on step sign

### Step 4 — Normalize negative indices

### Step 5 — Clip out-of-range indices

### Step 6 — Evaluate `range(start, stop, step)`

### Step 7 — Allocate result list

### Step 8 — Copy elements

---

# 8️⃣ Clipping Rules (Important)

Python clips indices silently.

Example:

```python
l[100:200]
```

Becomes:

```python
l[6:6]
```

Result:

```python
[]
```

No error.

Same for negative overflow:

```python
l[-100:2]
```

Becomes:

```python
l[0:2]
```

Result:

```python
[1,2]
```

Slicing never raises IndexError.

Indexing does.

---

# 9️⃣ Precautions While Using Slicing

## ⚠ 1 — Always Think in Terms of range()

Translate mentally:

```python
list(range(start, stop, step))
```

After normalization.

---

## ⚠ 2 — Remember Direction Rule

- step positive → start must be left of stop
- step negative → start must be right of stop

---

## ⚠ 3 — Stop Is Exclusive

Common mistake:

```python
l[0:3]
```

Gives indices 0,1,2

Never includes 3.

---

## ⚠ 4 — Negative Indices Don’t Change Direction

They only map to positive index.

Direction depends only on step.

---

## ⚠ 5 — Default Stop Changes with Step

This causes confusion:

```python
l[:3:-1]
```

Defaults:

- start = 5
- stop = 3
- step = -1

Equivalent to:

```python
range(5,3,-1)
```

Result:

```python
[6,5]
```

---

## ⚠ 6 — Slice Creates Copy (For Lists)

```python
l2 = l[:]
```

Creates shallow copy.

Modifying l2 doesn’t change l.

---

## ⚠ 7 — Step Larger Than Length Is Valid

```python
l[::100]
```

Returns first element only.

---

# 🔟 Advanced Concept — Slice Object

When you write:

```python
l[1:4:-1]
```

Python internally creates:

```python
slice(1,4,-1)
```

You can do:

```python
s = slice(1,4,-1)
l[s]
```

Same result.

---

# 1️⃣1️⃣ Final Golden Mental Model

When slicing:

### 1. Determine step

### 2. Fill missing start/stop based on step sign

### 3. Convert negative indices

### 4. Clip to valid bounds

### 5. Evaluate:

```python
range(start, stop, step)
```

That’s it.

---

# 1️⃣2️⃣ One-Line Summary

Slicing is not dynamic traversal.

It is:

> Precomputed index generation using normalized range logic.

---
