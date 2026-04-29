# **<span style="color:#ff1744">Multiprocessing in Python (Using `multiprocessing` Library)</span>**

---

# **<span style="color:#ff6f00">1. What is Multiprocessing (Quick Recall)</span>**

Multiprocessing means:

```text
Running multiple independent processes in parallel,
each with its own memory and Python interpreter
```

Unlike threads:

```text
Processes do NOT share memory
Each process runs truly in parallel
```

---

# **<span style="color:#ff1744">2. How to Create Processes</span>**

We use:

```python
from multiprocessing import Process
```

---

## **<span style="color:#3a86ff">Basic Syntax</span>**

```python
p = Process(target=function_name, args=(arg1, arg2))
p.start()
p.join()
```

---

## **<span style="color:#8338ec">Simple Example</span>**

```python
from multiprocessing import Process
import time

def task(name):
    print(f"Process {name} starting")
    time.sleep(2)
    print(f"Process {name} finished")

p1 = Process(target=task, args=("A",))
p2 = Process(target=task, args=("B",))

p1.start()
p2.start()

p1.join()
p2.join()

print("Main process finished")
```

---

# **<span style="color:#ff1744">3. What Does `.start()` Do Internally?</span>**

When you call:

```python
p.start()
```

Python does:

```text
1. Ask OS to create new process
2. Copy (or initialize) Python interpreter
3. Pass target function to child process
4. Start execution in parallel
```

So:

```text
Main process → continues execution
Child process → runs task()
```

---

# **<span style="color:#ff1744">4. What Does `.join()` Do?</span>**

```python
p.join()
```

Means:

```text
"Wait until this process finishes"
```

---

## **<span style="color:#3a86ff">Without join()</span>**

```text
Main process may finish before child processes
```

---

## **<span style="color:#3a86ff">With join()</span>**

```text
Main process waits for all child processes
```

---

# **<span style="color:#ff1744">5. Execution Flow (Step-by-Step)</span>**

Let’s dry run the earlier example.

---

## **<span style="color:#8338ec">Step 1 — Main Process Starts</span>**

```text
Main process begins execution
```

---

## **<span style="color:#8338ec">Step 2 — Create Process Objects</span>**

```python
p1 = Process(...)
p2 = Process(...)
```

Internally:

```text
Process objects created
BUT no OS process yet
```

---

## **<span style="color:#8338ec">Step 3 — Start Processes</span>**

```python
p1.start()
p2.start()
```

Now:

```text
OS creates two new processes
Each process starts executing task()
```

Execution becomes:

```text
Main Process continues
Process A runs task("A")
Process B runs task("B")
```

---

## **<span style="color:#8338ec">Step 4 — Parallel Execution</span>**

Timeline:

```text
Time 0:
Process A → starts
Process B → starts

Time 1:
Both sleeping

Time 2:
Process A finishes
Process B finishes
```

---

## **<span style="color:#8338ec">Step 5 — join()</span>**

```python
p1.join()
p2.join()
```

Main process:

```text
Waits for p1 and p2 to finish
```

---

## **<span style="color:#8338ec">Step 6 — Main Process Continues</span>**

```python
print("Main process finished")
```

Runs only after both processes finish.

---

# **<span style="color:#ff1744">6. Dry Run with Timeline</span>**

Example:

```python
from multiprocessing import Process
import time

def task():
    print("Child process running")
    time.sleep(2)
    print("Child process done")

p = Process(target=task)

p.start()
p.join()

print("Main done")
```

---

## **<span style="color:#8338ec">Execution Timeline</span>**

```text
Time 0:
Main → start()
Child → begins task()

Time 1:
Child → sleeping
Main → waiting (join)

Time 2:
Child → done
Main → resumes

Time 2+:
Main → prints "Main done"
```

---

# **<span style="color:#ff1744">7. What Happens Without join()</span>**

```python
p.start()

print("Main done")
```

Possible output:

```text
Main done
Child process running
Child process done
```

Problem:

```text
Main finishes early
```

---

# **<span style="color:#ff1744">8. Important Rules</span>**

---

## **<span style="color:#3a86ff">Always Use if **name** == "**main**"</span>**

Especially on Windows:

```python
if __name__ == "__main__":
    # multiprocessing code
```

Reason:

```text
Prevents infinite process spawning
```

---

# **<span style="color:#ff1744">9. Multiple Processes Example</span>**

```python
from multiprocessing import Process
import time

def task(n):
    print(f"Process {n} running")
    time.sleep(1)
    print(f"Process {n} done")

if __name__ == "__main__":
    processes = []

    for i in range(5):
        p = Process(target=task, args=(i,))
        p.start()
        processes.append(p)

    for p in processes:
        p.join()

    print("All processes completed")
```

---

## **<span style="color:#8338ec">Execution Flow</span>**

```text
5 processes created
All run in parallel
Main waits using join()
After all finish → print final message
```

---

# **<span style="color:#ff1744">10. Key Mental Model</span>**

```text
start() → launches process
join() → waits for process
```

---

Think like:

```text
start() → "Go do your work"
join() → "I will wait until you finish"
```

---

# **<span style="color:#ff1744">Summary</span>**

- `Process()` → defines a new process
- `start()` → creates and starts process
- `join()` → waits for process to finish
- Processes run in parallel with separate memory

---

If you want next level understanding, I can explain:

**Multiprocessing Pool (like ThreadPoolExecutor but for processes) — very important for real-world CPU parallelism.**
