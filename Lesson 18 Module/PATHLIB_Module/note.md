# **<span style="color:#ff1744">Pathlib Library in Python — Complete Practical Guide</span>**

`pathlib` is the **modern standard way to work with filesystem paths in Python**.
It replaces older approaches like:

```
os
os.path
glob
```

with a **clean object-oriented interface**.

---

# **<span style="color:#ff6f00">1. Why Use `pathlib` Instead of `os` / `os.path`</span>**

Before Python 3.4, path handling looked like this:

```python
import os

path = os.path.join("folder", "file.txt")

if os.path.exists(path):
    print("File exists")
```

Problems:

```
Paths treated as plain strings
Functions spread across multiple modules
Harder to read
Platform differences
```

---

### **Pathlib Solution**

```python
from pathlib import Path

path = Path("folder") / "file.txt"

if path.exists():
    print("File exists")
```

Advantages:

```
Paths are objects
Readable syntax
Cross-platform compatibility
Built-in file operations
Cleaner code
```

---

# **<span style="color:#8338ec">2. Core Concept of `pathlib`</span>**

Everything revolves around the **Path object**.

```python
from pathlib import Path
```

Create path:

```python
p = Path("data/file.txt")
```

Now `p` is an object with methods like:

```
p.exists()
p.is_file()
p.read_text()
p.parent
```

---

### **Internal Representation**

Example path:

```
data/file.txt
```

Path object stores:

```
directory parts
file name
file extension
root
```

---

# **<span style="color:#3a86ff">3. Important Features of Pathlib</span>**

Major features:

```
Object oriented path manipulation
Cross-platform compatibility
File system operations
Directory iteration
File reading/writing
Pattern based searching
```

---

# **<span style="color:#ff1744">4. Most Important Pathlib Methods</span>**

Below are the most commonly used methods.

---

# **<span style="color:#3a86ff">1. Creating Path Objects</span>**

```python
from pathlib import Path

p = Path("data/file.txt")
print(p)
```

Output:

```
data/file.txt
```

---

# **<span style="color:#3a86ff">2. Joining Paths</span>**

```python
from pathlib import Path

p = Path("folder") / "subfolder" / "file.txt"
print(p)
```

Output:

```
folder/subfolder/file.txt
```

The `/` operator is overloaded.

---

# **<span style="color:#3a86ff">3. Checking Path Existence</span>**

```python
p.exists()
```

Example:

```python
from pathlib import Path

p = Path("data.txt")

print(p.exists())
```

Output:

```
True / False
```

---

# **<span style="color:#3a86ff">4. Checking File or Directory</span>**

```python
p.is_file()
p.is_dir()
```

Example:

```python
from pathlib import Path

p = Path("data.txt")

print(p.is_file())
```

---

# **<span style="color:#3a86ff">5. Getting File Information</span>**

Example:

```python
from pathlib import Path

p = Path("data/file.txt")

print(p.name)
print(p.stem)
print(p.suffix)
print(p.parent)
```

Output example:

```
file.txt
file
.txt
data
```

Meaning:

| Property | Meaning                |
| -------- | ---------------------- |
| name     | file name              |
| stem     | name without extension |
| suffix   | file extension         |
| parent   | parent directory       |

---

# **<span style="color:#3a86ff">6. Creating Directories</span>**

Create folder:

```python
Path("new_folder").mkdir()
```

Create nested folders:

```python
Path("a/b/c").mkdir(parents=True)
```

Important arguments:

```
parents=True
exist_ok=True
```

---

# **<span style="color:#3a86ff">7. Reading and Writing Files</span>**

Write file:

```python
p.write_text("Hello World")
```

Read file:

```python
content = p.read_text()
print(content)
```

---

# **<span style="color:#3a86ff">8. Iterating Through Directory</span>**

Example:

```python
from pathlib import Path

folder = Path("data")

for item in folder.iterdir():
    print(item)
```

This lists all files and folders.

---

# **<span style="color:#3a86ff">9. Searching Files (glob)</span>**

Find all `.txt` files:

```python
from pathlib import Path

p = Path("data")

for file in p.glob("*.txt"):
    print(file)
```

Recursive search:

```python
p.rglob("*.py")
```

---

# **<span style="color:#ff1744">5. Demo Program to Practice Pathlib</span>**

Try this mini project.

### **Directory Analyzer**

This script:

```
Lists files
Shows file size
Filters by extension
```

Code:

```python
from pathlib import Path

folder = Path(".")

print("Python files in this folder:\n")

for file in folder.glob("*.py"):
    size = file.stat().st_size
    print(file.name, "->", size, "bytes")
```

What you will learn:

```
Path creation
Directory scanning
File metadata
Pattern search
```

---

# **<span style="color:#ff1744">6. Real Use Cases of Pathlib</span>**

---

### **1. Dataset Processing**

Machine learning projects often load files dynamically.

Example:

```
Load all images in dataset folder
```

---

### **2. Log File Analysis**

Scan directories for logs.

Example:

```
Find all .log files recursively
```

---

### **3. Automation Scripts**

Examples:

```
Rename files
Organize folders
Backup scripts
```

---

### **4. Backend Development**

Used in frameworks like:

```
Django
FastAPI
Flask
```

Example:

```
handling uploaded files
```

---

### **5. DevOps Scripts**

Examples:

```
deployment scripts
log management
file cleanup
```

---

# **<span style="color:#ff1744">7. Comparison: pathlib vs os.path</span>**

| Task              | os.path              | pathlib          |
| ----------------- | -------------------- | ---------------- |
| Join paths        | `os.path.join()`     | `/` operator     |
| File exists       | `os.path.exists()`   | `Path.exists()`  |
| File name         | `os.path.basename()` | `Path.name`      |
| Directory listing | `os.listdir()`       | `Path.iterdir()` |
| File extension    | manual parsing       | `Path.suffix`    |

---

# **<span style="color:#ff1744">8. Best Practices When Using Pathlib</span>**

Recommended:

```
Always use Path objects instead of raw strings
Use "/" operator for joining paths
Prefer pathlib over os.path in new projects
```

Convert to string when required:

```python
str(path)
```

Some libraries still expect string paths.

---

# **<span style="color:#ff1744">9. Mental Model</span>**

Old approach:

```
Paths = strings
Operations = separate functions
```

New approach:

```
Paths = objects
Operations = methods
```

Example:

```
"data/file.txt" → string
Path("data/file.txt") → object
```

Objects provide methods like:

```
exists()
is_file()
read_text()
glob()
```

---

# **<span style="color:#ff1744">Summary</span>**

`pathlib` provides:

```
Cleaner path manipulation
Object-oriented design
Cross-platform support
Powerful file system utilities
```

Most important methods:

```
Path()
exists()
is_file()
is_dir()
mkdir()
read_text()
write_text()
iterdir()
glob()
rglob()
```

---

If you want, I can also teach a **very practical mini project**:

**Build a Python File Organizer using pathlib that automatically sorts files into folders (images, docs, code).**

This project will make you **fully comfortable with pathlib in real-world usage**.
