# 🔹 1️⃣ Libraries Used

---

## 🟣 `io.StringIO`

`StringIO` creates an **in-memory text stream**.

Normally, `tokenize.generate_tokens()` expects a `readline` function (like a file object).
But your code is a string.

So this:

```python
StringIO(code).readline
```

Makes your string behave like a file.

👉 Think of it as:

```
String → Fake File → Tokenizer
```

---

## 🟣 `tokenize`

This module converts Python source code into **tokens**.

Tokens are the smallest meaningful pieces of Python syntax:

Example:

```python
def calculate(x):
```

Becomes tokens like:

- NAME → def
- NAME → calculate
- OP → (
- NAME → x
- OP → )
- OP → :

The tokenizer does **lexical analysis**.

It does NOT understand program meaning — only structure.

---

## 🟣 `ast`

`ast` = Abstract Syntax Tree

This converts tokens into a **tree structure representing program meaning**.

Example:

```python
return x * 2
```

Becomes something like:

```
Return
 └── BinOp
     ├── Name(x)
     ├── Mult
     └── Constant(2)
```

Now Python understands the **semantics**.

---

## 🟣 `dis`

`dis` disassembles Python bytecode.

Python does NOT run source code directly.

It compiles to **bytecode instructions** for the Python Virtual Machine (PVM).

Example bytecode instruction:

```
LOAD_CONST 2
BINARY_MULTIPLY
RETURN_VALUE
```

This is the lowest-level Python-visible layer before execution.

---

## 🟣 `visast.visualise`

This is an external library (not built-in).

It graphically visualizes AST trees.

Internally it:

- Traverses AST
- Builds a graph
- Displays structure visually

It helps you see how Python structured your program.

---

# 🔹 2️⃣ The Code Itself

Your input:

```python
def calculate(x):
    return x * 2
calculate(5)
```

---

# 🔹 3️⃣ Stage 1 — Tokenization

### Function:

```python
def show_tokens(code):
    for tok in tokenize.generate_tokens(StringIO(code).readline):
        token_name = tokenize.tok_name[tok.type]
        if not (token_name == "NL" or token_name == "NEWLINE"):
            print(f"{token_name:<12} {tok.string:<12} {tok.start} {tok.end}")
```

### What Happens:

`generate_tokens()` produces a sequence of TokenInfo objects.

Each token has:

- `tok.type` → numeric token type
- `tok.string` → actual text
- `tok.start` → (line, column)
- `tok.end` → (line, column)

You filter out:

- NL
- NEWLINE

Because they’re not useful for structural understanding.

---

### Example Token Output (Simplified)

You’ll see something like:

```
NAME         def          (2,0)  (2,3)
NAME         calculate    (2,4)  (2,13)
OP           (            (2,13) (2,14)
NAME         x            (2,14) (2,15)
OP           )            (2,15) (2,16)
OP           :            (2,16) (2,17)
INDENT                    (3,0)  (3,4)
NAME         return       (3,4)  (3,10)
NAME         x            (3,11) (3,12)
OP           *            (3,13) (3,14)
NUMBER       2            (3,15) (3,16)
DEDENT
NAME         calculate
OP           (
NUMBER       5
OP           )
ENDMARKER
```

---

### What This Shows

Tokenizer only understands:

- Keywords
- Identifiers
- Operators
- Numbers
- Structure markers (INDENT/DEDENT)

It does NOT know:

- That `calculate` is a function
- That `x * 2` is multiplication logic

It only knows shapes.

---

# 🔹 4️⃣ Stage 2 — AST

```python
tree = ast.parse(code)
print(ast.dump(tree, indent=4))
```

Now Python builds meaning.

You’ll see something like:

```
Module(
    body=[
        FunctionDef(
            name='calculate',
            args=arguments(
                args=[arg(arg='x')]
            ),
            body=[
                Return(
                    value=BinOp(
                        left=Name(id='x'),
                        op=Mult(),
                        right=Constant(value=2)
                    )
                )
            ]
        ),
        Expr(
            value=Call(
                func=Name(id='calculate'),
                args=[Constant(value=5)]
            )
        )
    ]
)
```

---

### What This Means

Top Level → `Module`

Inside module body:

1️⃣ FunctionDef
2️⃣ Expression (function call)

Inside FunctionDef:

- name = calculate
- parameter = x
- body = Return node

Inside Return:

- BinOp (Binary Operation)
  - left = x
  - op = Mult
  - right = 2

Now Python understands:

```
This is a function
This is multiplication
This is a call
```

---

# 🔹 5️⃣ Stage 3 — Compilation to Bytecode

```python
bytecode = compile(tree, '<string>', 'exec')
print(dis.dis(bytecode))
```

`compile()` converts AST → Bytecode.

`dis.dis()` shows instructions.

---

### You’ll See Something Like:

```
  2           0 LOAD_CONST               0 (<code object calculate>)
              2 LOAD_CONST               1 ('calculate')
              4 MAKE_FUNCTION            0
              6 STORE_NAME               0 (calculate)

  4           8 LOAD_NAME                0 (calculate)
             10 LOAD_CONST               2 (5)
             12 CALL_FUNCTION            1
             14 POP_TOP
             16 LOAD_CONST               3 (None)
             18 RETURN_VALUE
```

And inside function:

```
  3           0 LOAD_FAST                0 (x)
              2 LOAD_CONST               1 (2)
              4 BINARY_MULTIPLY
              6 RETURN_VALUE
```

---

# 🔹 Understanding Bytecode Instructions

Inside function:

| Instruction     | Meaning                       |
| --------------- | ----------------------------- |
| LOAD_FAST x     | Load local variable x         |
| LOAD_CONST 2    | Load constant 2               |
| BINARY_MULTIPLY | Multiply top two stack values |
| RETURN_VALUE    | Return result                 |

Python is stack-based.

Execution is like:

```
Push x
Push 2
Multiply
Return result
```

---

# 🔥 Full Compilation Pipeline Summary

```
Source Code
    ↓
Tokenizer
    ↓
Tokens
    ↓
Parser
    ↓
AST
    ↓
Compiler
    ↓
Bytecode
    ↓
Python Virtual Machine
```

---

# 🧠 What This Teaches You

You are now seeing:

- How Python reads code
- How syntax becomes structure
- How structure becomes instructions
- How instructions execute

This is **compiler-level understanding**.

---

# 🔥 Deep Insight

Your code demonstrates that:

- Python is NOT interpreted line-by-line.
- Python compiles everything to bytecode first.
- The AST is the most powerful layer for analysis.
- Tools like linters, formatters, type checkers work on AST.

---

# 🏆 Why This Matters for You

Since you’re serious about deep CS and system-level understanding:

- Understanding AST = essential for building compilers
- Understanding bytecode = essential for performance tuning
- Understanding tokenization = essential for language design

This is how tools like:

- Black
- MyPy
- PyLint
- Code analyzers

are built.

---
