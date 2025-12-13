# <span style="color:orange">Operators </span>

## <span style="color:pink">Arithmatic Operator </span>

1. **Addition +:**

   - Special Behavior: Adds two values.
   - Constraints: Suitable for numbers, strings (concatenation).

2. **Subtraction -:**

   - Special Behavior: Subtracts the right operand from the left operand.
   - Constraints: Suitable for numbers.

3. **Multiplication &#9728;:**

   - Special Behavior: Multiplies two values.
   - Constraints: Suitable for numbers, strings (replication).

4. **Division /:**

   - Special Behavior: Divides the left operand by the right operand.

   - Constraints:

     - Results in a floating-point number, even if the operands are integers.

     - Division by zero is not allowed and raises a ZeroDivisionError.

5. **Floor Division //:**

   - Special Behavior: Divides the left operand by the right operand, rounding down to the nearest integer.
   - Constraints:

     - Results in an integer.

     - Division by zero is not allowed and raises a ZeroDivisionError.

6. **Modulus %:**

   - Special Behavior: Returns the remainder of the division of the left operand by the right operand.
   - Constraints:

     - Results in an integer.

     - Division by zero is not allowed and raises a ZeroDivisionError.

7. **Exponentiation &#9728;&#9728; or pow():**

   - Special Behavior: Raises the left operand to the power of the right operand.
   - Constraints: Suitable for numbers. Large exponentiation results may be subject to memory limitations.

#### pow()

- The pow() function in Python is used to calculate the power of a number.
- It takes two arguments, the base, and the exponent, and returns the result of raising the base to the power of the exponent.

The syntax is as follows:

```python

pow(base, exponent, modulus)
```

- base: The base value.
- exponent: The exponent to which the base is raised.
- modulus (optional): If specified, the result will be the remainder when divided by the modulus.

Here's an example:

```python
result = pow(2, 3)
print(result)
```

- In this example, 2 is the base, and 3 is the exponent. The result will be 2 raised to the power of 3, which is 8.

## <span style="color:pink">Relational Operator </span>

- Relational operators are used to compare two values
- Always producing a Boolean result (True or False).

1. ### Equal to `==`

- **Special Behavior:** Tests if two values are equal.
- **Constraints:** Suitable for various types (integers, floats, strings, etc.).

  ```python
  result = 5 == 5
  print(result)  # Output: True

  string_comparison = "hello" == "world"
  print(string_comparison)  # Output: False
  ```

2. ### Not equal to `!=`

- **Special Behavior:** Tests if two values are not equal.
- **Constraints:** Suitable for various types.

  ```python
  result = 5 != 3
  print(result)  # Output: True
  ```

3. ### Greater than `>`

- **Special Behavior:** Tests if the left operand is greater than the right operand.
- **Constraints:** Suitable for numbers (integers, floats).

  ```python
  result = 8 > 5
  print(result)  # Output: True
  ```

4. ### Less than `<`

- **Special Behavior:** Tests if the left operand is less than the right operand.
- **Constraints:** Suitable for numbers.

  ```python
  result = 3 < 7
  print(result)  # Output: True
  ```

5. ### Greater than or equal to `>=`

- **Special Behavior:** Tests if the left operand is greater than or equal to the right operand.
- **Constraints:** Suitable for numbers.

  ```python
  result = 10 >= 10
  print(result)  # Output: True
  ```

6. ### Less than or equal to `<=`

- **Special Behavior:** Tests if the left operand is less than or equal to the right operand.
- **Constraints:** Suitable for numbers.

  ```python
  result = 5 <= 8
  print(result)  # Output: True
  ```

Relational operators play a crucial role in making logical comparisons in Python programming.

> **Note:**

> - (10>8<7) Python Evaluation:
> - In Python, chained comparisons are allowed and they are interpreted as logical ANDs. The expression 10 > 8 < 7 is equivalent to (10 > 8) and (8 < 7).
> - 10 > 8 evaluates to True
> - 8 < 7 evaluates to False
> - So, 10 > 8 < 7 is evaluated as True and False, which results in False.

> - C Evaluation:
> - In C, chained comparisons are not interpreted the same way as in Python. Instead, each comparison is evaluated independently and in sequence, based on the precedence of operators.
> - The expression 10 > 8 < 7 in C is evaluated as follows:
> - First, 10 > 8 is evaluated, resulting in 1 (since True is represented as 1 in C).
> - Then, 1 < 7 is evaluated, resulting in 1 (since 1 is indeed less than 7).
>   So, the entire expression 10 > 8 < 7 in C evaluates to 1.

> **Strings** are compared **lexicographically/alphabetically**

## <span style="color:pink">Logical Operator </span>

In Python, there are three main logical operators: `and`, `or`, and `not`. These operators are used to perform logical operations on boolean values (True or False).

### `and` Operator:

- Returns True if both operands are true.
- Returns False if at least one operand is false.

  ```python
  result = True and False  # Result is False
  ```

### `or` Operator:

- Returns True if at least one operand is true.
- Returns False if both operands are false.

  ```python
  result = True or False  # Result is True
  ```

### `not` Operator:

- Returns True if the operand is false.
- Returns False if the operand is true.

  ```python
  result = not True  # Result is False
  ```

### Special Behaviors:

**Short-Circuit Evaluation:**

- Python uses short-circuit evaluation for logical operators.
- In `x and y`, if `x` is False, `y` is not evaluated because the result will always be False.
- In `x or y`, if `x` is True, `y` is not evaluated because the result will always be True.

  ```python
  result = False and some_function()  # some_function() is not called due to short-circuiting
  ```

### Important Points:

**Chaining:**

- Logical operators can be chained together to express more complex conditions.

  ```python
  result = (x > 5) and (y < 10) or (z == 0)
  ```

**Order of Precedence:**

- Logical operators have a specific order of precedence.
- Use parentheses to clarify the order of evaluation if needed.

  ```python
  result = (x > 5) and (y < 10)  # Explicitly defining the order
  ```

### Constraints:

**Non-Boolean Operands:**

- Python allows non-boolean operands in logical expressions.
- For `and`, the result is the first false operand; for `or`, it is the first true operand.

  ```python
  result = 0 and 'Hello'  # Result is 0
  ```

**Truthiness and Falsiness:**

- Objects have a truthiness or falsiness associated with them.
- For example, empty lists, strings, and numeric zero are considered falsy.

  ```python
  result = [] or 'Default'  # Result is 'Default'
  ```

## <span style="color:pink">Bitwise Operator </span>

Bitwise operators in Python perform operations at the bit level. They work on integers by manipulating individual bits. The main bitwise operators are `&` (AND), `|` (OR), `^` (XOR), `~` (NOT), `<<` (left shift), and `>>` (right shift).

### Important Points:

**Binary Representation:**

- Bitwise operators work on the binary representation of integers.

**AND (`&`) Operator:**

- Sets each bit to 1 if both bits are 1.

  ```python
  result = 5 & 3  # Result is 1 (binary: 101 & 011 = 001)
  ```

**OR (`|`) Operator:**

- Sets each bit to 1 if at least one of the corresponding bits is 1.

  ```python
  result = 5 | 3  # Result is 7 (binary: 101 | 011 = 111)
  ```

**XOR (`^`) Operator:**

- Sets each bit to 1 if exactly one of the corresponding bits is 1.

  ```python
  result = 5 ^ 3  # Result is 6 (binary: 101 ^ 011 = 110)
  ```

**NOT (`~`) Operator:**

- Inverts the bits (0 becomes 1, and 1 becomes 0).

  ```python
  result = ~5  # Result is -6 (binary: ~0101 = 1010, in two's complement representation)
  ```

**Left Shift (`<<`) Operator:**

- Shifts the bits to the left by a specified number of positions, filling in with zeros.

  ```python
  result = 5 << 1  # Result is 10 (binary: 101 << 1 = 1010)
  ```

- `a<<n`==> a\*(2^n)

**Right Shift (`>>`) Operator:**

- Shifts the bits to the right by a specified number of positions, filling in with the sign bit.

  ```python
  result = 5 >> 1  # Result is 2 (binary: 101 >> 1 = 10)
  ```

- `a>>n`==> a/(2^n)

### Constraints:

**Bitwise Operators and Booleans:**

- Bitwise operators can be used with integers but not with boolean values.

  ```python
  # This will raise a TypeError
  result = True & False
  ```

**Bitwise Operators and Floating-Point Numbers:**

- Bitwise operators are not applicable to floating-point numbers.

  ```python
  # This will raise a TypeError
  result = 5.0 & 3.0
  ```

### Important Use Cases:

**Bit Manipulation:**

- Bitwise operators are commonly used for low-level programming tasks, such as manipulating hardware registers or encoding/decoding data.

**Flags and Masks:**

- Flags in computer systems are often implemented using bitwise operators. Each flag corresponds to a specific bit, and bitwise operations are used to manipulate these flags.

**Efficient Arithmetic Operations:**

- Some bitwise operations can be more efficient than their arithmetic counterparts in specific scenarios, especially for certain types of optimization.

## <span style="color:pink">Identity Operator </span>

Identity operators in Python are used to compare the memory locations of two objects. The two main identity operators are `is` and `is not`.

### Important Points:

**`is` Operator:**

- The `is` operator returns True if both operands refer to the same object (share the same memory address).

  ```python
  a = [1, 2, 3]
  b = a
  result = a is b  # Result is True
  ```

**`is not` Operator:**

- The `is not` operator returns True if the operands do not refer to the same object.

  ```python
  a = [1, 2, 3]
  b = [1, 2, 3]
  result = a is not b  # Result is True (different objects)
  ```

**Object Identity vs. Equality:**

- Identity (`is`) checks if two variables refer to the same object, while equality (`==`) checks if the values of two objects are the same.

  ```python
  a = [1, 2, 3]
  b = [1, 2, 3]
  result_identity = a is b  # Result is False (different objects)
  result_equality = a == b  # Result is True (values are the same)
  ```

**None and Identity:**

- The `is` operator is commonly used to check if a variable is `None`.

  ```python
  x = None
  result = x is None  # Result is True
  ```

### Constraints:

**Immutability and Identity:**

- For immutable objects (like numbers and strings), the `is` operator may behave differently due to Python's optimization. Always use `==` for comparing immutable objects.

  ```python
  a = 5
  b = 5
  result = a is b  # May be True due to optimization, but not guaranteed
  ```

**Identity Operators and Booleans:**

- Identity operators can be used with boolean values.

  ```python
  result = True is True  # Result is True
  ```

### Important Use Cases:

**Checking for None:**

- Identity operators are commonly used to check if a variable is `None`.

  ```python
  x = some_function()
  if x is None:
      print("Variable x is None")
  ```

**Optimizing Code:**

- In some cases, identity operators can be used for optimization, especially when dealing with mutable objects.

  ```python
  # Example: Only update if the object is not already the desired one
  if obj is not desired_obj:
      obj = desired_obj
  ```

**Avoiding Unintended Side Effects:**

- Identity operators can be useful in avoiding unintended side effects by ensuring that two variables do not reference the same object when it's not desired.

## <span style="color:pink">Membership Operator </span>

Membership operators in Python are used to test whether a value is a member of a sequence, such as a string, list, or tuple. The two main membership operators are `in` and `not in`.

### Important Points:

**`in` Operator:**

- The `in` operator returns True if a specified value is found in the sequence.

  ```python
  my_list = [1, 2, 3, 4]
  result = 3 in my_list  # Result is True
  ```

**`not in` Operator:**

- The `not in` operator returns True if a specified value is not found in the sequence.

  ```python
  my_list = [1, 2, 3, 4]
  result = 5 not in my_list  # Result is True
  ```

**String Membership:**

- Membership operators can be used with strings to check if a substring is present.

  ```python
  my_string = "Hello, World!"
  result = "Hello" in my_string  # Result is True
  ```

**Tuple Membership:**

- Membership operators work with tuples as well.

  ```python
  my_tuple = (1, 2, 3, 4)
  result = 2 in my_tuple  # Result is True
  ```

### Constraints:

**Case Sensitivity:**

- Membership operators are case-sensitive. For strings, "Hello" and "hello" are considered different.

  ```python
  my_string = "Hello, World!"
  result = "hello" in my_string  # Result is False
  ```

**Membership Operators and Sets:**

- Membership operators can be used with sets. However, sets are inherently unordered, so the order of elements doesn't matter.

  ```python
  my_set = {1, 2, 3, 4}
  result = 3 in my_set  # Result is True
  ```

### Important Use Cases:

**Checking for Presence in a Collection:**

- Membership operators are commonly used to check if a value is present in a list, tuple, string, or other iterable.

  ```python
  if user_input in valid_options:
      print("Valid option selected.")
  ```

**Filtering Data:**

- Membership operators can be used to filter data based on certain conditions.

  ```python
  numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
  even_numbers = [num for num in numbers if num % 2 == 0]
  ```

**Testing for Substrings:**

- Membership operators are useful for checking if a substring is present in a larger string.

  ```python
  if "error" in log_message:
      print("Error found in log.")
  ```

## <span style="color:pink">Assignment Operator </span>

Assignment operators in Python are used to assign values to variables. They are shortcuts for performing operations on variables and updating their values. The basic assignment operator is `=`.

### Important Points:

**Basic Assignment:**

- The `=` operator is used for basic assignment.

  ```python
  x = 10  # Assigns the value 10 to the variable x
  ```

**Arithmetic Assignment:**

- Arithmetic assignment operators combine arithmetic operations with assignment.

  ```python
  y = 5
  y += 3  # Equivalent to y = y + 3
  ```

**Multiple Assignment:**

- Multiple assignment allows assigning multiple variables in a single line.

  ```python
  a, b, c = 1, 2, 3
  ```

**Chained Assignment:**

- Chained assignment allows assigning the same value to multiple variables in a single line.

  ```python
  m = n = 7  # Both m and n are assigned the value 7
  ```

### Constraints:

**Immutable Objects:**

- Assignment operators work differently for mutable and immutable objects. For immutable objects (e.g., numbers, strings), a new object is created.

  ```python
  a = 5
  b = a  # b refers to a new object with the value 5
  ```

**Undefined Variables:**

- Variables must be defined before they can be assigned.

  ```python
  # This will raise a NameError
  z = undefined_variable
  ```

### Important Use Cases:

**Updating Variables:**

- Assignment operators are commonly used to update the values of variables.

  ```python
  counter = 0
  counter += 1  # Increment counter by 1
  ```

**Swapping Values:**

- Assignment operators can be used to swap the values of two variables.

  ```python
  x = 5
  y = 10
  x, y = y, x  # Swaps the values of x and y
  ```

**Concise Iteration:**

- Assignment operators are useful for concise iteration over data structures.

  ```python
  for item in data:
      total += item  # Adds each item to the total
  ```

Feel free to copy and use this Markdown code as needed.

## [Precedence and Asscociativity of Operators](https://www.geeksforgeeks.org/precedence-and-associativity-of-operators-in-python/)

# Python Operator Precedence and Associativity

---

| **Precedence**  | **Operators**                                   | **Description**                                                          | **Associativity** |
| --------------- | ----------------------------------------------- | ------------------------------------------------------------------------ | ----------------- |
| **1 (highest)** | `()`                                            | Parentheses (grouping)                                                   | N/A               |
|                 | `f(args...)`                                    | Function call                                                            | Left-to-right     |
|                 | `x[index:index]`                                | Slicing                                                                  | Left-to-right     |
|                 | `x[index]`                                      | Indexing                                                                 | Left-to-right     |
|                 | `x.attribute`                                   | Attribute reference                                                      | Left-to-right     |
|                 | `await x`                                       | Await expression                                                         | N/A               |
|                 | `**`                                            | Exponentiation                                                           | Right-to-left     |
| **2**           | `+x, -x, ~x`                                    | Unary plus, Unary minus, Bitwise NOT                                     | Right-to-left     |
| **3**           | `*, @, /, //, %`                                | Multiplication, Matrix multiplication, Division, Floor division, Modulus | Left-to-right     |
| **4**           | `+, -`                                          | Addition, Subtraction                                                    | Left-to-right     |
| **5**           | `<<, >>`                                        | Bitwise shift operators                                                  | Left-to-right     |
| **6**           | `&`                                             | Bitwise AND                                                              | Left-to-right     |
| **7**           | `^`                                             | Bitwise XOR                                                              | Left-to-right     |
| **8**           | `                                             ` | Bitwise OR                                                               | Left-to-right     |
| **9**           | `in, not in, is, is not, <, <=, >, >=, !=, ==`  | Membership, Identity, Comparison operators                               | Left-to-right     |
| **10**          | `not x`                                         | Boolean NOT                                                              | Right-to-left     |
| **11**          | `and`                                           | Boolean AND                                                              | Left-to-right     |
| **12**          | `or`                                            | Boolean OR                                                               | Left-to-right     |
| **13**          | `if - else`                                     | Conditional expression (ternary operator)                                | Right-to-left     |
| **14**          | `lambda`                                        | Lambda expression                                                        | Right-to-left     |
| **15**          | `:=`                                            | Assignment expression (walrus operator)                                  | Right-to-left     |
| **16 (lowest)** | `=`                                             | Assignment                                                               | Right-to-left     |
|                 | `+=, -=,, /=, //=, %=, @=, &=,^=, >>=, <<=`     | Augmented assignment operators                                           | Right-to-left     |

### 🔹 **Key Points:**

1. **Parentheses `()` have the highest precedence**—used for function calls, indexing, and grouping expressions.
2. **Exponentiation `**`is right-to-left associative**—meaning`2 ** 3 ** 2`is evaluated as`2 ** (3 ** 2)`.
3. **Multiplication `*`, division `/`, floor division `//`, and modulus `%` come before addition/subtraction**.
4. **Bitwise operators (`&`, `^`, `|`) have lower precedence than arithmetic operators**.
5. **Comparison operators like `==`, `<`, `>`, and `in` have lower precedence than bitwise operators**.
6. **Logical `not`, `and`, and `or` have lower precedence than comparison operators**.
7. **Ternary operator `if-else` and lambda expressions have low precedence**.
8. **Assignment (`=`) and augmented assignment (`+=`, `-=`, etc.) have the lowest precedence**.
