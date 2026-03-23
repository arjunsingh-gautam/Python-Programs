# <span style="color:#ff1744">**Python `os` Module — Complete Guide (Concept, Methods, Use Cases)**</span>

---

# <span style="color:#ff6f00">**1. What is the `os` Module?**</span>

The `os` module in Python provides:

> **A way to interact with the Operating System (OS)**

It allows you to:

- Work with files and directories
- Handle environment variables
- Execute system commands
- Get system-level information

Think of it as:

```text
Python ↔ OS Bridge
```

---

# <span style="color:#d500f9">**2. Why Do We Need the `os` Module?**</span>

Without `os`, Python would be limited to:

- pure computation
- memory-based operations

With `os`, Python can:

- interact with file system
- automate system tasks
- build backend services
- manage processes

---

# <span style="color:#ff1744">**3. Core Functionalities of `os` Module**</span>

---

## <span style="color:#3a86ff">**A. Working with Directories**</span>

### Get Current Directory

```python
import os
print(os.getcwd())
```

---

### Change Directory

```python
os.chdir("path/to/folder")
```

---

### List Files

```python
os.listdir()
os.listdir("folder_name")
```

---

### Create Directory

```python
os.mkdir("new_folder")        # single folder
os.makedirs("a/b/c")         # nested folders
```

---

### Remove Directory

```python
os.rmdir("folder")           # empty folder
os.removedirs("a/b/c")       # nested
```

---

## <span style="color:#3a86ff">**B. Working with Files**</span>

### Rename File

```python
os.rename("old.txt", "new.txt")
```

---

### Delete File

```python
os.remove("file.txt")
```

---

### File Info

```python
os.stat("file.txt")
```

Returns metadata like:

- size
- last modified time

---

## <span style="color:#3a86ff">**C. Path Handling (`os.path`)**</span>

---

### Join Paths (Important)

```python
os.path.join("folder", "file.txt")
```

Prevents OS-specific issues.

---

### Check File Exists

```python
os.path.exists("file.txt")
```

---

### Check Type

```python
os.path.isfile("file.txt")
os.path.isdir("folder")
```

---

### Get Absolute Path

```python
os.path.abspath("file.txt")
```

---

### Split Path

```python
os.path.split("/home/user/file.txt")
```

---

## <span style="color:#3a86ff">**D. Environment Variables**</span>

---

### Get Environment Variable

```python
os.getenv("PATH")
```

---

### Set Environment Variable

```python
os.environ["MY_VAR"] = "123"
```

---

## <span style="color:#3a86ff">**E. Running System Commands**</span>

---

### Execute Command

```python
os.system("ls")     # Linux/Mac
os.system("dir")    # Windows
```

---

⚠️ Better alternative:

```python
import subprocess
subprocess.run(["ls"])
```

---

## <span style="color:#3a86ff">**F. Process and System Info**</span>

---

### Get Process ID

```python
os.getpid()
```

---

### Get User ID (Linux/Mac)

```python
os.getuid()
```

---

### System Name

```python
os.name
```

---

## <span style="color:#3a86ff">**G. Walking Through Directory Tree**</span>

---

### os.walk()

```python
for root, dirs, files in os.walk("folder"):
    print(root, dirs, files)
```

Used for:

- searching files
- indexing directories

---

# <span style="color:#ff1744">**4. Practical Example (Real Use Case)**</span>

### Task: Find all `.txt` files

```python
import os

for root, dirs, files in os.walk("."):
    for file in files:
        if file.endswith(".txt"):
            print(os.path.join(root, file))
```

---

# <span style="color:#ff1744">**5. Precautions While Using `os` Module**</span>

---

## <span style="color:#d500f9">**1. Avoid Hardcoding Paths**</span>

Bad:

```python
"/home/user/file.txt"
```

Good:

```python
os.path.join("home", "user", "file.txt")
```

---

## <span style="color:#d500f9">**2. Check Before Deleting**</span>

```python
if os.path.exists("file.txt"):
    os.remove("file.txt")
```

---

## <span style="color:#d500f9">**3. Be Careful with os.system()**</span>

Never use untrusted input:

```python
os.system(user_input)   # Dangerous
```

Use `subprocess` instead.

---

## <span style="color:#d500f9">**4. Handle Exceptions (EAFP)**</span>

```python
try:
    os.remove("file.txt")
except FileNotFoundError:
    pass
```

---

## <span style="color:#d500f9">**5. Permissions Issues**</span>

Some operations may fail due to:

- lack of permissions
- restricted directories

---

# <span style="color:#ff1744">**6. Real-World Use Cases**</span>

---

## <span style="color:#3a86ff">**1. File Management Systems**</span>

- organize files
- rename bulk files

---

## <span style="color:#3a86ff">**2. Backend Development**</span>

- handle uploads
- store logs

---

## <span style="color:#3a86ff">**3. Automation Scripts**</span>

- clean directories
- backup files

---

## <span style="color:#3a86ff">**4. DevOps / Scripting**</span>

- environment setup
- system monitoring

---

## <span style="color:#3a86ff">**5. Data Pipelines**</span>

- scan directories
- load datasets dynamically

---

# <span style="color:#ff1744">**7. Table of Important `os` Module Methods**</span>

---

## <span style="color:#7209b7">**Core Methods Summary**</span>

| Category  | Method              | Description           |
| --------- | ------------------- | --------------------- |
| Directory | `os.getcwd()`       | Get current directory |
| Directory | `os.chdir(path)`    | Change directory      |
| Directory | `os.listdir(path)`  | List files            |
| Directory | `os.mkdir()`        | Create folder         |
| Directory | `os.makedirs()`     | Create nested folders |
| Directory | `os.rmdir()`        | Remove folder         |
| File      | `os.remove()`       | Delete file           |
| File      | `os.rename()`       | Rename file           |
| File      | `os.stat()`         | File metadata         |
| Path      | `os.path.join()`    | Join paths            |
| Path      | `os.path.exists()`  | Check existence       |
| Path      | `os.path.isfile()`  | Check file            |
| Path      | `os.path.isdir()`   | Check directory       |
| Path      | `os.path.abspath()` | Absolute path         |
| Env       | `os.getenv()`       | Get env variable      |
| Env       | `os.environ`        | Set env variable      |
| System    | `os.system()`       | Run command           |
| Process   | `os.getpid()`       | Process ID            |
| Walk      | `os.walk()`         | Traverse directory    |

---

# <span style="color:#ff1744">**8. Advanced Insight (Important for You)**</span>

For modern Python:

- Prefer `pathlib` over `os.path` (more object-oriented)
- Use `subprocess` instead of `os.system`
- Use `shutil` for advanced file operations

---

# <span style="color:#ff1744">**Final Mental Model**</span>

`os` module gives Python:

```text
Access to file system
+
Access to environment
+
Access to system-level operations
```

It is essential for:

```text
Automation + Backend + System Programming
```

---
