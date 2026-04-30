# **<span style="color:#ff1744">Modern `asyncio` — How to Schedule & Run Async Tasks Properly</span>**

This is the **practical toolkit** you’ll use in real systems. We’ll cover:

- Modern entry points
- How to schedule tasks
- Key `asyncio` APIs (what / how / when)
- Examples + internal behavior
- Clear decision rules

---

# **<span style="color:#ff6f00">1. Modern Entry Point</span>**

## **Use `asyncio.run()` (always for top-level)**

```python
import asyncio

async def main():
    print("Hello async")

asyncio.run(main())
```

### **Internals (high-level)**

```text
create event loop
wrap main() into a Task
run loop until complete
shutdown loop cleanly
```

### **When to use**

```text
Always at program entry (scripts, CLI tools)
```

---

# **<span style="color:#ff1744">2. Creating Work — Coroutines vs Tasks</span>**

## **Coroutine (definition only)**

```python
async def fetch():
    ...
```

```text
Lazy: does nothing until awaited or scheduled
```

## **Task (scheduled work)**

```python
task = asyncio.create_task(fetch())
```

```text
Immediately scheduled in the event loop
```

---

# **<span style="color:#ff1744">3. Core Scheduling Methods</span>**

---

# **<span style="color:#8338ec">A. `await` (sequential dependency)</span>**

```python
r = await fetch()
```

### **Use when**

```text
You need the result before continuing
Order matters
```

### **Behavior**

```text
Pause current coroutine → run fetch → resume
```

---

# **<span style="color:#8338ec">B. `asyncio.create_task()` (concurrency)</span>**

```python
t1 = asyncio.create_task(fetch1())
t2 = asyncio.create_task(fetch2())

r1 = await t1
r2 = await t2
```

### **Use when**

```text
Independent tasks
Want overlap (I/O concurrency)
```

### **Behavior**

```text
Schedule immediately → run in background → await later
```

---

# **<span style="color:#8338ec">C. `asyncio.gather()` (group + ordered results)</span>**

```python
results = await asyncio.gather(fetch1(), fetch2(), fetch3())
```

### **Use when**

```text
Run many coroutines together
Collect all results
Preserve input order
```

### **Behavior**

```text
Schedules all → waits for all → returns list
```

---

## **Example**

```python
import asyncio

async def task(n):
    await asyncio.sleep(n)
    return n

async def main():
    results = await asyncio.gather(task(2), task(1), task(3))
    print(results)

asyncio.run(main())
```

```text
Output: [2, 1, 3]
(order preserved, not completion order)
```

---

# **<span style="color:#8338ec">D. `asyncio.as_completed()` (process as finished)</span>**

```python
tasks = [asyncio.create_task(task(i)) for i in [3,1,2]]

for t in asyncio.as_completed(tasks):
    print(await t)
```

### **Use when**

```text
You want results ASAP (streaming)
Order doesn’t matter
```

### **Behavior**

```text
Yields tasks as they finish
```

---

# **<span style="color:#8338ec">E. `asyncio.wait()` (low-level control)</span>**

```python
done, pending = await asyncio.wait(tasks)
```

### **Use when**

```text
Need fine-grained control
Timeouts / partial completion
```

---

# **<span style="color:#8338ec">F. `asyncio.TaskGroup` (Modern Structured Concurrency)</span>**

Python 3.11+ recommended way.

```python
import asyncio

async def main():
    async with asyncio.TaskGroup() as tg:
        t1 = tg.create_task(task(1))
        t2 = tg.create_task(task(2))
```

### **Why important**

```text
Safer than create_task
Automatic cancellation on failure
Structured lifecycle
```

### **Use when**

```text
Modern production code
Managing related tasks together
```

---

# **<span style="color:#ff1744">4. Running Blocking Code (Modern Way)</span>**

---

## **<span style="color:#8338ec">A. `asyncio.to_thread()` (I/O blocking)</span>**

```python
result = await asyncio.to_thread(blocking_func, arg)
```

### **Use when**

```text
File I/O, legacy blocking APIs
```

---

## **<span style="color:#8338ec">B. `run_in_executor()` (CPU or custom pool)</span>**

```python
loop = asyncio.get_running_loop()
result = await loop.run_in_executor(None, blocking_func)
```

### **Use when**

```text
CPU-bound or custom executors
```

---

# **<span style="color:#ff1744">5. Time & Coordination Utilities</span>**

---

## **<span style="color:#8338ec">A. `asyncio.sleep()`</span>**

```python
await asyncio.sleep(2)
```

```text
Non-blocking delay (yields control)
```

---

## **<span style="color:#8338ec">B. `asyncio.wait_for()` (timeout)</span>**

```python
await asyncio.wait_for(task(), timeout=2)
```

```text
Cancels if exceeds time
```

---

## **<span style="color:#8338ec">C. `asyncio.shield()`</span>**

```python
await asyncio.shield(task)
```

```text
Protect task from cancellation
```

---

# **<span style="color:#ff1744">6. Cancellation & Error Handling</span>**

---

## **Cancel a task**

```python
task.cancel()
```

---

## **Handle cancellation**

```python
try:
    await task
except asyncio.CancelledError:
    print("Cancelled")
```

---

# **<span style="color:#ff1744">7. Example — Putting It All Together</span>**

```python
import asyncio

async def fetch(n):
    print(f"Start {n}")
    await asyncio.sleep(n)
    print(f"End {n}")
    return n

async def main():
    async with asyncio.TaskGroup() as tg:
        t1 = tg.create_task(fetch(2))
        t2 = tg.create_task(fetch(1))

    print("Results:", t1.result(), t2.result())

asyncio.run(main())
```

---

## **Execution Flow**

```text
TaskGroup schedules both
↓
Task2 finishes first
↓
Task1 finishes later
↓
Results collected safely
```

---

# **<span style="color:#ff1744">8. When to Use What (Decision Table)</span>**

| Situation              | Use                 |
| ---------------------- | ------------------- |
| Program entry          | `asyncio.run()`     |
| Sequential dependency  | `await`             |
| Fire concurrent tasks  | `create_task()`     |
| Run many + collect all | `gather()`          |
| Process as finished    | `as_completed()`    |
| Structured concurrency | `TaskGroup`         |
| Blocking I/O           | `to_thread()`       |
| CPU work               | `run_in_executor()` |
| Timeout control        | `wait_for()`        |

---

# **<span style="color:#ff1744">9. Mental Model</span>**

```text
Coroutine → "what to do"
Task → "do it now"
await → "pause until ready"
Event loop → "scheduler"
```

---

# **<span style="color:#ff1744">10. Ultimate Insight</span>**

```text
Async performance comes from:
Scheduling multiple tasks + yielding control correctly
```

Not from:

```text
Just using async/await
```

---

If you want, next I can show:

**Real-world async patterns (web scraping, API batching, rate limiting) that combine all these primitives into production-grade code.**
