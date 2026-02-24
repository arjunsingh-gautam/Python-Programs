# **<span style="color:orange">Introduction to Python </span>**

## <span style="color:pink">History of Python </span>

Python was conceived in late 1980s by **Guido Van Rossum** at _Centrum Wiskunde & Informatica in Netherlands_

## <span style="color:pink">Version history of Python </span>

- Python 1.0 ---> 1994
- Python 2.0 --->2000
- Python 3.0 --->2008
  > Python 3.0 <u>**does not support backward compability**</u> i.e code written Python 2.0 cannot run by Python 3.0

## <span style="color:pink">Why we should learn Pyton? </span>

1. Presence of third-party modules
2. Extensive support libraries(NumPy for numerical calculations, Pandas for data analytics etc)
3. Open source and community development
4. Versatile, Easy to read, learn and write
5. User-friendly data structures
6. High-level language
7. **Dynamically typed language**(No need to mention data type based on the value assigned, it takes data type)
8. **Object-oriented language**
9. Portable and Interactive
10. Ideal for prototypes – provide more functionality with less coding
11. Highly Efficient(Python’s clean object-oriented design provides enhanced process control, and the language is equipped with excellent text processing and integration capabilities, as well as its own unit testing framework, which makes it more efficient.)
12. (IoT)Internet of Things Opportunities
13. **Interpreted Language**
14. Portable across Operating systems
15. **Dynamic Binding**
16. Emphasis on **readability**
17. **Automatic Memory Management**

> **Indentation based block of code**

## <span style="color:pink">Where Python can be used?</span>

- Webdevelopment
- AI,ML,IoT
- Data Science and Analytics
- Automation

## <span style="color:pink">How to develop Python Software?</span>

![Build](https://www.c-sharpcorner.com/article/why-learn-python-an-introduction-to-python/Images/last2.png)

> Pyton uses **Just Intime Compiler**

---

# <span style="color:#33ff00"> Python Code: Build and Execution Process </span>

- When you write Python code, it goes through several steps to be executed. Here's a detailed overview of the process:

## <span style="color:pink"> 1. Writing the Code </span>

You write Python code in a file with a `.py` extension. This code consists of various statements and instructions for the Python interpreter to execute.

## <span style="color:pink">2. The Python Interpreter

Python is an interpreted language, which means the code is executed line-by-line by an interpreter rather than being compiled into machine code beforehand. The most commonly used Python interpreter is CPython, which is written in C.

## <span style="color:pink">3. Lexical Analysis

When you run a Python script, the first step the interpreter performs is lexical analysis. The source code is converted into a series of tokens. Tokens are the basic building blocks of the code, such as keywords, operators, identifiers, literals, etc.

## <span style="color:pink">4. Parsing

The stream of tokens is then passed to a parser. The parser analyzes the syntax of the tokens to ensure that they form a valid structure according to the rules of the Python language. The output of this stage is an Abstract Syntax Tree (AST), which represents the hierarchical structure of the code.

## <span style="color:pink">5. Semantic Analysis

The AST is further processed for semantic analysis. This step involves checking the meaning of the code, such as type checking, variable scope resolution, and ensuring that all operations are valid.

## <span style="color:pink">6. Bytecode Compilation

Once the AST passes semantic analysis, it is converted into bytecode. Bytecode is a low-level representation of the code that is more abstract than machine code but can be efficiently executed by the interpreter. The bytecode is stored in `.pyc` files (Python Compiled files) in the `__pycache__` directory.

## <span style="color:pink">7. Execution

The Python Virtual Machine (PVM) executes the bytecode. The PVM is a stack-based machine that executes the bytecode instructions one at a time. The PVM is responsible for managing the runtime environment, including memory management, garbage collection, and executing built-in functions and libraries.

![Python Interpreter](img/Interpreter.png)

## <span style="color:pink">Detailed Process Flow

1. **Source Code (`.py` file)**
   - Written by the programmer.

2. **Lexical Analysis**
   - Tokenizer splits the code into tokens.
   - Example: `print("Hello, World!")` -> `['print', '(', '"Hello, World!"', ')']`

3. **Parsing**
   - Tokens are parsed into an Abstract Syntax Tree (AST).
   - Example: `print("Hello, World!")` -> AST node representing a function call.

4. **Semantic Analysis**
   - Checks for meaningful and valid constructs.
   - Example: Ensures `print` is a valid function call.

5. **Bytecode Compilation**
   - AST is converted to bytecode.
   - Example: Bytecode instruction for `print("Hello, World!")`.

6. **Execution (PVM)**
   - PVM executes the bytecode.
   - Example: `print` function is called, and "Hello, World!" is printed to the console.

## <span style="color:pink">Summary

In summary, the process of building and executing Python code involves writing the source code, lexical analysis to convert the code into tokens, parsing the tokens into an AST, performing semantic analysis, compiling the AST into bytecode, and finally executing the bytecode on the Python Virtual Machine (PVM). This process allows Python to be a highly dynamic and flexible language, capable of running on various platforms with minimal changes to the code.

---

When a Python source code file is executed, the process can be broken down into several steps, from parsing the code to executing it. Here’s a comprehensive breakdown:

---

### **1. Writing the Code**

- The programmer writes the Python code in a `.py` file. For example:

  ```python
  def greet(name):
      return f"Hello, {name}!"

  print(greet("Alice"))
  ```

---

### **2. Python Interpreter Reads the File**

- When the file is executed (`python file.py`), the **Python interpreter** starts the process.
- The interpreter includes:
  - **Parser**: Converts source code into a structured form.
  - **Compiler**: Translates the structured form into bytecode.
  - **Virtual Machine (VM)**: Executes the bytecode.

---

### **3. Parsing**

- The interpreter reads the file and parses the source code.
- Syntax and lexical checks are performed. For example:
  - Ensures proper indentation.
  - Verifies correct use of keywords.
- If syntax errors are detected, the interpreter raises an error (e.g., `SyntaxError`).

---

### **4. Compilation**

- After parsing, the interpreter compiles the source code into **bytecode**.
  - Bytecode is a low-level, platform-independent representation of the code.
  - Stored in `.pyc` files in the `__pycache__` directory for reuse.
  - Example: `file.pyc` contains the compiled bytecode of `file.py`.

#### Why compile?

- Compilation allows for efficient execution since the bytecode is optimized for the Python Virtual Machine (PVM).

---

### **5. Execution by the Python Virtual Machine (PVM)**

- The PVM executes the bytecode instructions line by line.
- The PVM is a stack-based virtual machine that handles:
  - **Memory management** (allocation, deallocation).
  - **Function calls and returns**.
  - **Operations and evaluations** (e.g., arithmetic, logic).

#### Key Mechanisms:

1. **Global Interpreter Lock (GIL)**:
   - In CPython (the standard Python implementation), the GIL ensures that only one thread executes Python bytecode at a time.
   - This simplifies memory management but can limit performance in multi-threaded programs.

2. **Garbage Collection**:
   - Python uses automatic memory management with garbage collection.
   - Unreferenced objects are cleaned up to free memory.
   - Uses reference counting and cycle-detection algorithms.

3. **Execution Flow**:
   - Executes top-level statements in the order they appear.
   - Handles function calls by pushing arguments and local variables onto a call stack.
   - Returns results by popping values off the stack.

---

### **6. Interaction with the Operating System**

- During execution, the interpreter interacts with the operating system for tasks like:
  - File I/O (reading/writing files).
  - Network communication.
  - Managing system resources.

---

### **7. Output**

- Results of execution are displayed in the terminal or written to files.
- Example: The output `Hello, Alice!` is printed on the console.

---

### **Additional Details**

#### **Error Handling**

- During execution, the interpreter monitors for runtime errors (e.g., `ZeroDivisionError`, `NameError`).
- If an exception is raised and not handled, the program halts and displays a traceback.

#### **Performance Optimization**

- Tools like Just-In-Time (JIT) compilers (e.g., PyPy) can further optimize bytecode execution by compiling it into machine code.

#### **Interactive Mode**

- In interactive mode (`python` or `ipython`), the interpreter compiles and executes code immediately, providing feedback.

---

This sequence—from parsing to output—illustrates how Python transforms human-readable code into actionable operations on a computer.

---

---

Great question! Let's break this down step-by-step and make it simple with analogies and practical perspectives.

---

## 🧠 What is CPython and the GIL?

### 1. **CPython**

- CPython is the **default implementation** of Python.
- When you write Python code (`.py`), CPython compiles it into **bytecode** (`.pyc`), and then it **interprets** and executes that bytecode.

---

### 2. **What is the GIL (Global Interpreter Lock)?**

The **GIL** is a mutex (mutual exclusion lock) in CPython that **only allows one thread to execute Python bytecode at a time**, **even on multi-core CPUs**.

> 🧠 Think of it like a **single-lane bridge** over a river. Even if you have 100 cars (threads) wanting to cross, only **one car can go at a time**. Others have to wait, even if you have multiple lanes on the road elsewhere (multi-core CPUs).

---

## 🧬 Internal Details: Why Does the GIL Exist?

CPython uses reference counting to manage memory. For example:

```python
a = []
b = a
```

Now both `a` and `b` point to the same object in memory.

If two threads modify the reference count of an object **at the same time**, and CPython isn't careful, the memory could get **corrupted** (e.g., think of one thread deleting it while another is using it).

So, GIL ensures that **one thread executes at a time**, keeping everything safe.

---

## ⚙️ Does the GIL block everything?

- ✅ **Yes, for CPU-bound Python code**.
- ❌ **No, for I/O-bound tasks (like reading a file or requesting a URL)** — CPython **releases** the GIL during blocking I/O, so **other threads can run**.

---

## 🤯 Why is this important for developers?

### 1. **You can't achieve true parallelism in Python using threads for CPU-bound tasks**

- Example:

```python
import threading

def cpu_task():
    for _ in range(10**7):
        pass

t1 = threading.Thread(target=cpu_task)
t2 = threading.Thread(target=cpu_task)

t1.start()
t2.start()
t1.join()
t2.join()
```

Even on an 8-core CPU, the two threads will **run one after another**, not in parallel — **because of the GIL**.

---

### 2. **Use multiprocessing instead**

If you're doing CPU-heavy tasks, use the `multiprocessing` module — it **creates separate processes**, each with its own GIL.

> 🛠 Think of this like hiring two chefs in two **separate kitchens** — they don’t fight for tools and can work at the same time.

---

## 👨‍💻 When is this knowledge useful?

| Scenario                                        | Importance of GIL Knowledge                                  |
| ----------------------------------------------- | ------------------------------------------------------------ |
| Writing CPU-intensive code                      | ✅ Very important — use multiprocessing instead of threading |
| Writing I/O-bound apps (e.g. web crawlers)      | ✅ Use threads or async — GIL won’t block                    |
| General scripting or automation                 | ❌ Not much impact                                           |
| Debugging concurrency issues                    | ✅ GIL understanding helps                                   |
| Understanding Python performance vs C++/Go/Java | ✅ Important — those languages don’t have a GIL              |

---

## 📝 Summary

- The **GIL** ensures thread safety in CPython by allowing only **one thread to execute bytecode** at a time.
- It’s like a **single-lane bridge** for threads.
- It affects **CPU-bound multithreaded performance**, not I/O-bound.
- Developers should use:
  - `multiprocessing` for CPU-bound
  - `threading` or `asyncio` for I/O-bound

---

Absolutely! Let's walk through what the **GIL (Global Interpreter Lock)** does internally using a **very simple multithreaded Python example**, and then explain what **actually happens under the hood in CPython** — with analogy and code comments.

---

## 🧪 Example Python Code: CPU-bound with Threads

```python
import threading

count = 0

def increment():
    global count
    for _ in range(1000000):
        count += 1

t1 = threading.Thread(target=increment)
t2 = threading.Thread(target=increment)

t1.start()
t2.start()
t1.join()
t2.join()

print("Final count:", count)
```

---

## 🚀 What You Expect

You might think:

- Each thread does `count += 1` a million times.
- So the final count should be **2 million**.

But in reality, you may get:

```
Final count: 1489123   # (varies each run)
```

---

## 🤖 What Actually Happens Under the Hood (GIL in Action)

Let’s break down `count += 1`:

> Under the hood, `count += 1` is **not atomic**. It breaks into:

1. Load `count`
2. Add `1`
3. Store result in `count`

Now imagine both threads are **interrupting each other mid-operation** because CPython **releases and re-acquires the GIL every few bytecode instructions**.

### 🔍 Here's a Simplified View of What Happens

```text
Thread A               | Thread B
-----------------------|--------------------------
Loads count = 100      |
                       | Loads count = 100
Adds 1 → 101           |
                       | Adds 1 → 101
Stores 101             |
                       | Stores 101
```

➡️ Final `count` = 101 instead of 102 — **increment lost due to race condition**.

### 🔒 What GIL Does:

The GIL ensures that **only one thread runs Python bytecode at a time**:

```text
THREAD A: acquires GIL
    does 100 bytecode ops (some increments)
THREAD A: releases GIL
THREAD B: acquires GIL
    does 100 bytecode ops
THREAD B: releases GIL
...
```

So, even though `threading` is used, they run **one after another**, rapidly switching.

---

## 🏗️ Simple Analogy

> You have **one pen** (GIL) shared between **two students** (threads). Only the student holding the pen can write. Even if both are fast and smart, only one can write at any moment.

---

## 🧠 Why This Matters to Developers

- **Wrong output due to race conditions** like above.
- Performance doesn't improve using threads for **CPU-bound** work.
- **Solution**: Use `multiprocessing`:

```python
from multiprocessing import Process

# Same increment function...

# Replace Thread with Process
p1 = Process(target=increment)
p2 = Process(target=increment)
```

This spawns **separate Python interpreters**, each with its **own GIL and memory space**, and achieves true parallelism.

---

## 🧪 Optional: View GIL Switching

You can actually **see GIL behavior** by using Python's `sys.setswitchinterval()`:

```python
import sys
sys.setswitchinterval(0.0001)  # Increase switching frequency
```

It changes how often the GIL is released — like adjusting how long a student keeps the pen before passing it.

---
