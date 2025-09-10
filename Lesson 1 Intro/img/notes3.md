Great question — and it cuts to the heart of how Python is **executed** and why it's labeled an **interpreted language**, even though compilation is involved.

---

## ✅ Short Answer:

> Python is called an **interpreted language** because its source code is **not compiled into native machine code** ahead of time. Instead, it is **executed line-by-line (instruction-by-instruction) by an interpreter**, specifically the **Python Virtual Machine (PVM)**.

---

## 🔍 But Wait — Python _Does_ Compile to Bytecode?

Yes! Internally:

1. Python source code (`.py`) is **compiled to bytecode** (`.pyc`).
2. This bytecode is then **interpreted by the PVM**.

➡️ This compilation step is **internal**, and the output (`.pyc` files) is **not machine code**, but **platform-independent bytecode**.

---

## 🧠 So Why Isn’t Python Called a Compiled Language?

Because:

| Feature                | Python                           | Compiled Languages (like C/C++)      |
| ---------------------- | -------------------------------- | ------------------------------------ |
| **Compilation Output** | Bytecode (`.pyc`)                | Machine code (binary `.exe`, `.out`) |
| **Execution Engine**   | Python Virtual Machine (PVM)     | CPU directly                         |
| **Distribution**       | Source code often required       | Binary executable                    |
| **Runtime Errors**     | Detected during execution        | Many caught at compile time          |
| **Flexibility**        | Dynamic typing, eval, reflection | Mostly static                        |

✅ The key difference is that **Python bytecode is not executable by your CPU**. It still requires an interpreter (PVM) at runtime.

---

## 📦 Analogy:

- **C** → Source → Compiler → Machine Code → Executed by CPU ✅
- **Python** → Source → Bytecode → PVM Interpreter → Executed ✅

So Python is:

> **Interpreted language with internal compilation** to bytecode

---

## 🔁 Examples of True Compiled Languages:

- C, C++, Rust, Go — produce **native machine binaries**
- These **do not need an interpreter at runtime**

## 🔁 Examples of Interpreted (or hybrid) Languages:

| Language       | Compiled to             | Execution                   |
| -------------- | ----------------------- | --------------------------- |
| **Python**     | Bytecode (`.pyc`)       | Interpreted by PVM          |
| **Java**       | Bytecode (`.class`)     | Interpreted by JVM          |
| **JavaScript** | AST/bytecode in browser | Interpreted or JIT compiled |
| **PHP, Ruby**  | Internal VM bytecode    | Interpreted                 |

---

## 🧾 Final Answer:

> Python is **called an interpreted language** because the final bytecode it generates is **not executed directly by hardware**, but by the **Python Virtual Machine (PVM)**, which interprets the bytecode **at runtime**.

Even though it includes a compilation step, it’s **not compiled to native code**, so Python is **not a compiled language** in the traditional sense.

---
