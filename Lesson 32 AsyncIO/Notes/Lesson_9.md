# **<span style="color:#ff1744">Running Blocking Code Asynchronously — Deep Internal Mechanics</span>**

You’re now touching **real-world async systems**, where we mix:

- Async event loop
- Threads
- Processes

Let’s break this into **first principles → mechanism → full dry run of your code**.

---

# **<span style="color:#ff6f00">1. Core Problem</span>**

```text id="prob"
Blocking code (time.sleep, CPU work) freezes the event loop
```

Why?

```text id="prob2"
Event loop is single-threaded → cannot switch tasks unless control is yielded
```

---

# **<span style="color:#ff6f00">2. Core Solution</span>**

We **offload blocking work** to:

```text id="sol"
1. Threads → asyncio.to_thread()
2. Processes → run_in_executor()
```

So:

```text id="sol2"
Event loop remains free → continues scheduling coroutines
```

---

# **<span style="color:#ff1744">3. Mechanism (First Principle)</span>**

---

## **<span style="color:#8338ec">General Flow</span>**

```text id="flow"
Coroutine → delegates blocking work → external worker (thread/process)
↓
Worker executes blocking code
↓
Result returned via Future
↓
Event loop resumes coroutine
```

---

# **<span style="color:#ff1744">4. How `asyncio.to_thread()` Works Internally</span>**

---

## **<span style="color:#3a86ff">Code</span>**

```python id="code1"
asyncio.to_thread(fetch_data, 1)
```

---

## **<span style="color:#8338ec">Internal Steps</span>**

```text id="steps1"
1. Wrap function call into a Future
2. Submit to ThreadPoolExecutor (default one)
3. Thread executes fetch_data()
4. Result stored in Future
5. Event loop awaits that Future
6. When done → coroutine resumes
```

---

## **<span style="color:#3a86ff">Key Insight</span>**

```text id="ins1"
Blocking code runs OUTSIDE event loop thread
```

---

# **<span style="color:#ff1744">5. How `run_in_executor()` Works (Process Version)</span>**

---

## **<span style="color:#3a86ff">Code</span>**

```python id="code2"
loop.run_in_executor(executor, fetch_data, 1)
```

---

## **<span style="color:#8338ec">Internal Steps</span>**

```text id="steps2"
1. Serialize function + arguments
2. Send to process pool
3. Worker process executes fetch_data()
4. Result serialized back
5. Stored in Future
6. Event loop resumes coroutine
```

---

## **<span style="color:#3a86ff">Key Insight</span>**

```text id="ins2"
Runs in separate process → bypasses GIL
```

---

# **<span style="color:#ff1744">6. Now Full Dry Run of YOUR CODE</span>**

---

# **<span style="color:#8338ec">STEP 1 — Program Start</span>**

```python id="s1"
asyncio.run(main())
```

---

## **Internal**

```text id="s1int"
Create event loop
Wrap main() into Task
Start execution
```

---

# **<span style="color:#8338ec">STEP 2 — Thread Section Begins</span>**

```python id="s2"
task1 = asyncio.create_task(asyncio.to_thread(fetch_data, 1))
task2 = asyncio.create_task(asyncio.to_thread(fetch_data, 2))
```

---

## **What happens internally**

```text id="s2int"
1. to_thread creates coroutine
2. create_task schedules it
3. Both tasks submitted to ThreadPoolExecutor
4. Threads start executing fetch_data()
```

---

## **Thread Execution**

```text id="s2thread"
Thread1 → fetch_data(1)
Thread2 → fetch_data(2)
```

---

# **<span style="color:#8338ec">STEP 3 — Parallel Execution (Threads)</span>**

```text id="s3"
Both threads run simultaneously:

Thread1 → sleep(1)
Thread2 → sleep(2)
```

---

# **<span style="color:#8338ec">STEP 4 — Await task1</span>**

```python id="s4"
result1 = await task1
```

---

## **Internal**

```text id="s4int"
main pauses
Event loop waits for task1 Future
```

---

## **After 1 sec**

```text id="s4done"
Thread1 finishes → Future completed
Event loop resumes main
```

---

## **Output**

```text id="s4out"
Thread 1 fully completed
```

---

# **<span style="color:#8338ec">STEP 5 — Await task2</span>**

```python id="s5"
result2 = await task2
```

---

## **Internal**

```text id="s5int"
Task2 already running
Wait for completion
```

---

## **After 2 sec**

```text id="s5done"
Thread2 finishes
```

---

## **Output**

```text id="s5out"
Thread 2 fully completed
```

---

# **<span style="color:#8338ec">STEP 6 — Process Pool Section</span>**

```python id="s6"
loop = asyncio.get_running_loop()
```

---

## **Internal**

```text id="s6int"
Get current event loop reference
```

---

# **<span style="color:#8338ec">STEP 7 — ProcessPoolExecutor</span>**

```python id="s7"
with ProcessPoolExecutor() as executor:
```

---

## **Internal**

```text id="s7int"
Create worker processes
Initialize IPC channels
```

---

# **<span style="color:#8338ec">STEP 8 — Submit Tasks to Processes</span>**

```python id="s8"
task1 = loop.run_in_executor(executor, fetch_data, 1)
task2 = loop.run_in_executor(executor, fetch_data, 2)
```

---

## **Internal**

```text id="s8int"
Serialize fetch_data + args
Send to worker processes
Processes execute independently
```

---

# **<span style="color:#8338ec">STEP 9 — Process Execution</span>**

```text id="s9"
Process1 → sleep(1)
Process2 → sleep(2)
```

---

# **<span style="color:#8338ec">STEP 10 — Await Results</span>**

Same flow as threads:

```text id="s10"
await task1 → resume after 1 sec
await task2 → resume after 2 sec
```

---

# **<span style="color:#8338ec">STEP 11 — Final Output</span>**

```python id="s11"
return [result1, result2]
```

---

# **<span style="color:#ff1744">7. Timeline Summary</span>**

---

## **Threads Section**

```text id="timeline1"
Start both threads at same time
Task1 finishes at 1 sec
Task2 finishes at 2 sec
Total ≈ 2 sec
```

---

## **Process Section**

```text id="timeline2"
Same behavior but separate processes
True parallel execution
```

---

# **<span style="color:#ff1744">8. Key Differences (Thread vs Process in This Code)</span>**

| Feature  | Thread (`to_thread`) | Process (`run_in_executor`) |
| -------- | -------------------- | --------------------------- |
| Memory   | Shared               | Separate                    |
| GIL      | Affected             | Not affected                |
| Overhead | Low                  | High                        |
| Best for | I/O tasks            | CPU tasks                   |

---

# **<span style="color:#ff1744">9. Mental Model</span>**

---

```text id="mental"
Async loop = manager

Blocking work:
→ send to worker (thread/process)
→ wait for result (non-blocking)
```

---

# **<span style="color:#ff1744">10. Ultimate Insight</span>**

```text id="ultimate"
Async itself does NOT solve blocking
It only orchestrates execution

Actual blocking work must be moved OUTSIDE the event loop
```

---

# **<span style="color:#ff1744">Final Summary</span>**

- `asyncio.to_thread()` → runs blocking code in thread
- `run_in_executor()` → runs in thread/process pool
- Event loop stays free
- Results come back via Future

---

If you want to go even deeper, next step is:

**How asyncio integrates with OS-level thread pool and how Future bridges between threads/processes and event loop (this is the deepest layer).**
