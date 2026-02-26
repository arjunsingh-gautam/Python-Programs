# <span style="color:#2E86C1"><b>`send()` in Generators — Deep Mechanics & Step-by-Step Execution</b></span>

We’ll cover:

1. What `send()` actually does
2. How it changes generator behavior
3. Exact execution flow step-by-step
4. Simple analogy
5. Internal mechanics (frame & yield expression)
6. When `send()` is useful
7. Common mistakes

---

## <span style="color:#AF7AC5"><b>1️⃣ What Is `send()`?</b></span>

Normally:

```python
next(generator)
```

→ resumes generator
→ runs until next `yield`
→ returns yielded value

But `send(value)`:

> Resumes generator AND sends a value into the paused `yield` expression.

So `yield` becomes a two-way communication channel.

---

## <span style="color:#48C9B0"><b>2️⃣ Basic Example</b></span>

```python
def echo():
    value = yield
    print("Received:", value)
```

Now:

```python
g = echo()
next(g)        # Prime generator
g.send(10)
```

Output:

```
Received: 10
```

Why?

Let’s break it down.

---

## <span style="color:#E74C3C"><b>3️⃣ Step-by-Step Execution</b></span>

### Step 1 — Create generator

```python
g = echo()
```

Nothing runs yet.

Generator state: **Created**

---

### Step 2 — Prime generator

```python
next(g)
```

Execution begins:

```python
value = yield
```

It reaches `yield` and pauses.

Important:

- `yield` has not yet received any value.
- It yields `None` (since no value specified).

Generator state: **Suspended at yield**

---

### Step 3 — Send value

```python
g.send(10)
```

Mechanism:

- Generator resumes.
- The `yield` expression returns 10.
- So:

```python
value = 10
```

Now:

```python
print("Received:", value)
```

Executes.

Then function ends → raises `StopIteration`.

---

## <span style="color:#5DADE2"><b>4️⃣ Important Rule</b></span>

You cannot send a non-None value before first `yield`.

This fails:

```python
g = echo()
g.send(10)   # ERROR
```

Because generator has not started.

You must first move it to first `yield`:

```python
next(g)
```

This is called **priming** the generator.

---

# <span style="color:#BB8FCE"><b>5️⃣ More Practical Example</b></span>

```python
def running_total():
    total = 0
    while True:
        number = yield total
        total += number
```

Use it:

```python
g = running_total()

print(next(g))      # 0
print(g.send(5))    # 5
print(g.send(3))    # 8
print(g.send(10))   # 18
```

---

## Step-by-Step Flow

### First next(g)

- Starts function
- `total = 0`
- Hits `yield total`
- Returns 0
- Pauses

---

### g.send(5)

- Resumes generator
- `yield total` becomes 5
- So:

```python
number = 5
```

- total += 5 → total = 5
- Loop continues
- Hits `yield total`
- Returns 5
- Pauses

---

### g.send(3)

- number = 3
- total = 8
- yield 8

---

This is full duplex communication.

---

# <span style="color:#F5B041"><b>6️⃣ Analogy — Walkie Talkie</b></span>

Normal `yield`:

- Generator talks.
- Caller listens.

With `send()`:

- Caller talks back.
- Generator listens.

Walkie-talkie conversation:

```
Generator: "Current total is 0"
Caller: "Add 5"
Generator: "Now total is 5"
Caller: "Add 3"
Generator: "Now total is 8"
```

Two-way channel.

---

# <span style="color:#58D68D"><b>7️⃣ Internal Mechanism</b></span>

Inside generator object:

- Frame stored on heap
- Instruction pointer saved
- Local variables preserved

When paused at:

```python
number = yield total
```

The generator:

- Sends `total` to caller
- Suspends execution

When `send(x)` is called:

- Generator resumes
- `yield total` evaluates to x
- Assignment happens

So `yield` behaves like:

```python
number = (value sent by caller)
```

---

# <span style="color:#F39C12"><b>8️⃣ Advanced — Coroutine Behavior</b></span>

Generators with `send()` are called **coroutines**.

Before async/await existed, this was used to:

- Build event loops
- Cooperative multitasking
- Pipeline processing

Example pattern:

```python
def consumer():
    while True:
        item = yield
        print("Consumed:", item)
```

Producer sends values:

```python
c = consumer()
next(c)
c.send("A")
c.send("B")
```

---

# <span style="color:#EC7063"><b>9️⃣ When Is `send()` Useful?</b></span>

✔ Stateful pipelines
✔ Coroutine-based designs
✔ Event-driven systems
✔ Streaming processors
✔ Custom state machines
✔ Interactive data processing

Used heavily before async/await.

---

# <span style="color:#3498DB"><b>🔟 Common Mistakes</b></span>

❌ Forgetting to prime generator
❌ Confusing `yield` and `return`
❌ Sending values after generator finished
❌ Not handling StopIteration

---

# <span style="color:#8E44AD"><b>1️⃣1️⃣ Generator Lifecycle with send()</b></span>

States:

```
Created
  ↓ next()
Running
  ↓ yield
Suspended
  ↓ send(value)
Running
  ↓ yield
Suspended
  ↓ StopIteration
Finished
```

---

# <span style="color:#1ABC9C"><b>1️⃣2️⃣ Key Concept</b></span>

`yield` is not just “produce value”.

It is:

> A suspension point that can receive values when resumed.

That’s the real power.

---

# <span style="color:#2E4053"><b>Final Summary</b></span>

- `next()` resumes generator without sending value.
- `send(value)` resumes and injects value into paused `yield`.
- `yield` becomes a bidirectional communication point.
- Generator frame is suspended and resumed.
- Useful for coroutines and stateful pipelines.

---
