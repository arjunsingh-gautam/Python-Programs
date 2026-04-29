# **<span style="color:#ff1744">Dry Run and Execution Flow of the Threading Code</span>**

We will analyze the program step-by-step and understand:

- What happens in each line
- How threads are created
- How scheduling occurs
- Why `join()` is required
- Why total execution time ≈ **1 second instead of 10 seconds**

---

# **<span style="color:#ff6f00">1. Code Overview</span>**

The program creates **10 threads**, each performing:

```
sleep for 1 second
```

Since sleeping is an **I/O wait**, threads can run concurrently.

Goal of the program:

```
Run multiple sleeping tasks simultaneously
Measure total execution time
```

---

# **<span style="color:#8338ec">2. Step 1 — Import Modules</span>**

```python
import threading
import time
```

Two modules are used:

| Module      | Purpose                         |
| ----------- | ------------------------------- |
| `threading` | Create and manage threads       |
| `time`      | Measure time and simulate delay |

---

# **<span style="color:#8338ec">3. Step 2 — Start Timer</span>**

```python
start = time.perf_counter()
```

`perf_counter()`:

```
High-precision timer
```

Used to measure **execution duration**.

Example:

```
start = 10.25 seconds
```

---

# **<span style="color:#8338ec">4. Step 3 — Define Thread Task</span>**

```python
def do_something(name):
```

Each thread runs this function.

---

### **<span style="color:#3a86ff">Inside Function</span>**

```python
print(f"Thread-{name} is sleeping for 1 second...")
```

Thread prints a message.

---

```python
time.sleep(1)
```

Thread **sleeps for 1 second**.

Important:

```
During sleep → thread releases CPU
Other threads can run
```

---

```python
print(f"Thread-{name} Done Sleeping!")
```

Thread wakes and prints completion message.

---

# **<span style="color:#8338ec">5. Step 4 — Create Thread List</span>**

```python
threads = []
```

This list stores all thread objects.

Why?

```
So we can later call join() on them
```

---

# **<span style="color:#8338ec">6. Step 5 — Create Threads</span>**

```python
for i in range(10):
```

Loop runs **10 times**.

---

## **<span style="color:#3a86ff">Iteration 1</span>**

```
i = 0
```

Thread creation:

```python
t = threading.Thread(target=do_something, args=i)
```

This creates a thread object.

Important:

Thread is **not yet running**.

Thread metadata contains:

```
Target function → do_something
Arguments → i
Thread state → NEW
```

---

### **<span style="color:#3a86ff">Start Thread</span>**

```python
t.start()
```

Now Python:

```
Creates OS thread
Schedules thread execution
Calls do_something(i)
```

Thread begins executing concurrently.

---

### **<span style="color:#3a86ff">Store Thread</span>**

```python
threads.append(t)
```

We save thread reference for later synchronization.

---

### **<span style="color:#3a86ff">Loop Continues</span>**

The loop repeats.

Result:

```
10 threads created
10 threads started
```

---

# **<span style="color:#8338ec">7. What Happens During Thread Execution</span>**

Timeline example:

```
Thread-0 → sleeping
Thread-1 → sleeping
Thread-2 → sleeping
Thread-3 → sleeping
Thread-4 → sleeping
Thread-5 → sleeping
Thread-6 → sleeping
Thread-7 → sleeping
Thread-8 → sleeping
Thread-9 → sleeping
```

All threads reach:

```
time.sleep(1)
```

Since sleeping releases CPU:

```
Threads overlap execution
```

---

# **<span style="color:#8338ec">8. Step 6 — Join Threads</span>**

```python
for thread in threads:
    thread.join()
```

This loop ensures:

```
Main thread waits for all worker threads
```

Workflow:

```
Wait thread-0
Wait thread-1
Wait thread-2
...
Wait thread-9
```

Main thread resumes **only after all threads finish**.

---

# **<span style="color:#8338ec">9. Thread Completion Timeline</span>**

Approximate timeline:

```
0s → all threads start
0s → all threads begin sleep
1s → all threads wake
1s → print "Done Sleeping"
```

Total time:

```
≈ 1 second
```

Instead of:

```
10 seconds
```

---

# **<span style="color:#8338ec">10. Step 7 — Stop Timer</span>**

```python
finish = time.perf_counter()
```

Example:

```
finish = 11.25 seconds
```

---

# **<span style="color:#8338ec">11. Calculate Execution Time</span>**

```python
print(f"Finished in {finish-start} second(s)")
```

Example output:

```
Finished in 1.02 second(s)
```

---

# **<span style="color:#ff1744">Why Execution Time Is ~1 Second</span>**

Without threading:

```
sleep 1 sec
sleep 1 sec
sleep 1 sec
...
sleep 1 sec
```

Total:

```
10 seconds
```

With threading:

```
10 threads sleeping simultaneously
```

Total:

```
≈1 second
```

Because sleep is **I/O wait**.

---

# **<span style="color:#ff1744">Important Issue in the Code</span>**

You wrote:

```python
args=i
```

But `args` must be a **tuple**.

Correct form:

```python
args=(i,)
```

Otherwise Python may treat it incorrectly.

Correct thread creation:

```python
t = threading.Thread(target=do_something, args=(i,))
```

---

# **<span style="color:#ff1744">Final Execution Flow Summary</span>**

```
Program start
↓
Start timer
↓
Define thread function
↓
Create thread list
↓
Loop creates 10 threads
↓
Each thread starts running do_something()
↓
Threads sleep for 1 second
↓
Main thread waits using join()
↓
Threads finish execution
↓
Main thread resumes
↓
Stop timer
↓
Print execution time
```

---

# **<span style="color:#ff1744">Mental Model</span>**

Imagine **10 workers** assigned a task:

```
Sleep for 1 minute
```

Without threading:

```
Worker 1 sleeps
Worker 2 sleeps
Worker 3 sleeps
...
```

Total time:

```
10 minutes
```

With threading:

```
All workers sleep simultaneously
```

Total time:

```
1 minute
```

---

If you want, I can also explain **two very important threading concepts that become crucial next**:

1. **Race conditions and thread safety (why shared variables break)**
2. **Why threading fails for CPU tasks and when multiprocessing is required**

These concepts complete the **deep understanding of Python concurrency.**
