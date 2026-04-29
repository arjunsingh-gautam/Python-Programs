# **<span style="color:#ff1744">Multiprocessing in Python — Complete Deep-Dive</span>**

---

# **<span style="color:#ff6f00">1. What is Multiprocessing?</span>**

Multiprocessing means:

```text
Running multiple processes in parallel,
each with its own memory space and Python interpreter
```

Structure:

```text
Main Process
 ├── Process 1
 ├── Process 2
 ├── Process 3
```

Each process:

- Runs independently
- Has its own memory
- Has its own GIL

---

# **<span style="color:#ff1744">2. Multiprocessing vs Multithreading</span>**

| Feature        | Multithreading       | Multiprocessing          |
| -------------- | -------------------- | ------------------------ |
| Execution unit | Threads              | Processes                |
| Memory         | Shared               | Separate                 |
| GIL            | Shared               | Each process has its own |
| CPU usage      | Limited by GIL       | True parallelism         |
| Communication  | Easy (shared memory) | Hard (IPC needed)        |
| Overhead       | Low                  | High                     |

---

## **<span style="color:#8338ec">Analogy</span>**

### Threading:

```text
Multiple workers in one room sharing tools
```

### Multiprocessing:

```text
Multiple workers in different rooms with their own tools
```

---

# **<span style="color:#ff1744">3. Causality — Why Multiprocessing Exists</span>**

The core problem:

```text
GIL prevents true parallel execution of CPU-bound tasks
```

So even with multiple threads:

```text
Only one thread executes Python code at a time
```

Solution:

```text
Use multiple processes → each has its own GIL
```

This enables:

```text
True parallel execution on multiple CPU cores
```

---

# **<span style="color:#ff1744">4. Where Multiprocessing is Useful</span>**

---

## **<span style="color:#3a86ff">Best Use Cases</span>**

```text
CPU-bound tasks
Heavy computations
Data processing
Image processing
Machine learning
Scientific simulations
```

---

## **<span style="color:#3a86ff">Where It Is NOT Useful</span>**

```text
I/O-bound tasks
Network calls
File reading/writing
```

Reason:

```text
Overhead > benefit
```

---

# **<span style="color:#ff1744">5. How Python Enables Multiprocessing (Internal Mechanics)</span>**

---

## **<span style="color:#8338ec">Step-by-Step Internal Flow</span>**

---

### **Step 1 — Main Process Starts**

```text
Python program starts → main process created
```

---

### **Step 2 — New Process Creation**

```python
from multiprocessing import Process
p = Process(target=task)
p.start()
```

Internally:

```text
1. OS creates new process
2. Python interpreter starts inside new process
3. Memory space is duplicated (or forked)
```

---

### **Step 3 — Code Execution in Child Process**

```text
Child process runs task() independently
```

---

### **Step 4 — Parent Continues Execution**

```text
Main process continues unless join() is called
```

---

### **Step 5 — Process Completion**

```text
Child process finishes execution → terminates
```

---

## **<span style="color:#3a86ff">Example</span>**

```python
from multiprocessing import Process
import time

def task():
    print("Running task")
    time.sleep(2)

p = Process(target=task)

p.start()
p.join()

print("Main done")
```

---

# **<span style="color:#ff1744">6. Why Multiprocessing Improves CPU Performance</span>**

---

## **<span style="color:#8338ec">Problem with Threads</span>**

```text
Thread A → gets GIL → runs
Thread B → waits
Thread C → waits
```

---

## **<span style="color:#8338ec">Solution with Processes</span>**

```text
Process A → CPU Core 1
Process B → CPU Core 2
Process C → CPU Core 3
```

Each process has:

```text
Own Python interpreter
Own GIL
```

Result:

```text
True parallel execution
```

---

# **<span style="color:#ff1744">7. Why Multiprocessing is NOT Good for I/O Tasks</span>**

I/O tasks:

```text
Wait for external resource
```

Example:

```text
Network call → waiting
File read → waiting
```

Multiprocessing adds overhead:

```text
Process creation
Memory duplication
Communication overhead
```

So:

```text
Threading is better for I/O tasks
```

---

# **<span style="color:#ff1744">8. How Multiprocessing Works Around GIL</span>**

GIL is:

```text
Global Interpreter Lock → per process
```

So:

```text
Process 1 → GIL 1
Process 2 → GIL 2
Process 3 → GIL 3
```

Each process executes independently.

Thus:

```text
Multiple processes → multiple GILs → parallel execution
```

---

# **<span style="color:#ff1744">9. Constraints of Multiprocessing</span>**

---

## **<span style="color:#3a86ff">1. Memory Isolation</span>**

Processes do NOT share memory.

```text
Variables cannot be shared directly
```

Solution:

```text
Queues
Pipes
Shared memory
```

---

## **<span style="color:#3a86ff">2. Data Serialization (Pickling)</span>**

Arguments passed between processes must be:

```text
Pickle-able
```

Example problem:

```python
Cannot pass open file handles
Cannot pass lambda functions
```

---

## **<span style="color:#3a86ff">3. Platform Differences</span>**

Windows uses:

```text
spawn()
```

Linux uses:

```text
fork()
```

Behavior differs.

---

## **<span style="color:#3a86ff">4. Complex Debugging</span>**

Harder to debug than threads.

---

# **<span style="color:#ff1744">10. Overheads of Multiprocessing</span>**

---

## **<span style="color:#8338ec">1. Process Creation Cost</span>**

Creating process is expensive:

```text
Memory allocation
Interpreter startup
```

---

## **<span style="color:#8338ec">2. Memory Duplication</span>**

Each process has its own memory:

```text
High RAM usage
```

---

## **<span style="color:#8338ec">3. Inter-Process Communication (IPC)</span>**

Communication requires:

```text
Serialization + transfer
```

This is slow.

---

## **<span style="color:#8338ec">4. Context Switching</span>**

Switching between processes is heavier than threads.

---

# **<span style="color:#ff1744">11. Example — CPU Bound Task</span>**

---

## **Without Multiprocessing**

```python
def compute():
    for _ in range(10**7):
        pass

compute()
compute()
```

Runs sequentially.

---

## **With Multiprocessing**

```python
from multiprocessing import Process

def compute():
    for _ in range(10**7):
        pass

p1 = Process(target=compute)
p2 = Process(target=compute)

p1.start()
p2.start()

p1.join()
p2.join()
```

Runs in parallel.

---

# **<span style="color:#ff1744">12. Use Cases of Multiprocessing</span>**

---

## **<span style="color:#3a86ff">1. Data Processing</span>**

```text
Large dataset transformations
```

---

## **<span style="color:#3a86ff">2. Image/Video Processing</span>**

```text
Parallel pixel operations
```

---

## **<span style="color:#3a86ff">3. Machine Learning</span>**

```text
Training models
Feature extraction
```

---

## **<span style="color:#3a86ff">4. Scientific Computing</span>**

```text
Simulations
Matrix operations
```

---

## **<span style="color:#3a86ff">5. Backend Systems</span>**

```text
Parallel request handling
```

---

# **<span style="color:#ff1744">13. Mental Model</span>**

Multiprocessing:

```text
Multiple independent Python programs
running in parallel
```

Threading:

```text
Multiple execution paths inside one Python program
```

---

# **<span style="color:#ff1744">Final Summary</span>**

Multiprocessing:

```text
Bypasses GIL
Uses multiple CPU cores
Provides true parallelism
```

But comes with:

```text
High overhead
Memory isolation
Communication complexity
```

---

# **<span style="color:#ff1744">Key Insight</span>**

Use:

```text
Threading → I/O-bound tasks
Multiprocessing → CPU-bound tasks
```

---

If you want next step, I can explain:

**Multiprocessing Pool vs Process vs ThreadPoolExecutor — which one to use in real systems and why most high-performance systems use process pools.**
