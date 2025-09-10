# <span style="color:orange">Control Statenents in Python </span>

# Explanation of if Statements in Python

In Python, if statements are used to conditionally execute a block of code based on a specified condition. There are various forms of if statements, including single-line if statements and if...else statements. Here's an explanation of these types along with some important points:

## 1. Single Line if Statement

A single-line if statement is a concise way to write conditional code when there is only one statement to be executed based on the condition.

**Syntax:**

```python
result = value_if_true if condition else value_if_false
```

## Example:

```python
x = 10
message = "Positive" if x > 0 else "Non-positive"
print(message)
```

## Important Points:

1. It provides a compact way to express a simple conditional assignment.
2. Ensure that the expression is clear and not overly complex for readability.

## 2. if...else Statement

An `if...else` statement allows for two different blocks of code to be executed based on whether a condition is True or False.

**Syntax:**

```python
if condition:
    # code to be executed if the condition is True
else:
    # code to be executed if the condition is False
```

## Example:

```python
x = 10
if x > 0:
    print("Positive")
else:
    print("Non-positive")
```

## Important Points:

- The `else` block is optional. If omitted, the code block under `if` is executed when the condition is True, and nothing happens when it's False.
- Ensure proper indentation for readability.

## 3. if...elif...else Statement

An `if...elif...else` statement allows for multiple conditions to be checked sequentially, and the corresponding block of code is executed for the first true condition.

**Syntax:**

```python
if condition1:
    # code to be executed if condition1 is True
elif condition2:
    # code to be executed if condition2 is True
else:
    # code to be executed if none of the conditions are True
```

## Example:

```python
x = 0
if x > 0:
    print("Positive")
elif x < 0:
    print("Negative")
else:
    print("Zero")
```

## Important Points:

- Multiple `elif` blocks can be used to handle various conditions in a cascading manner.
- The `else` block is optional.

## 4. Nested if Statements in Python

Nested if statements in Python allow you to include one or more if statements inside another if statement. This means that the inner if statement is evaluated only when the outer if statement's condition is true. Nested if statements provide a way to handle more complex conditional logic by allowing you to check multiple conditions in a structured manner.

## Detailed Explanation of Nested if Statements:

### Nested if Statements in Python

In Python, a nested if statement is formed when one or more if statements are placed inside another if statement. The structure of a nested if statement looks like this:

```python
if outer_condition:
    # Outer if block
    if inner_condition:
        # Inner if block
        # Code to be executed if both outer and inner conditions are true
    else:
        # Code to be executed if outer condition is true but inner condition is false
else:
    # Code to be executed if outer condition is false
```

## Important Points:

- Nested if statements can be extended to include multiple levels of conditions.
- Proper indentation is crucial for readability and to define the scope of each block.
- Avoid excessive nesting as it can make the code harder to understand.

## 5. Match Statement in Python (PEP 634)

As of my last knowledge update in January 2022, Python does not have a `match` statement. However, starting from Python 3.10, a new `match` statement has been proposed as part of PEP 634 (Structural Pattern Matching). This feature introduces a more powerful and flexible way to perform pattern matching in Python.

### Syntax:

```python
match expression:
    pattern1:
        # Code to be executed if expression matches pattern1
    pattern2:
        # Code to be executed if expression matches pattern2
    ...
    patternN:
        # Code to be executed if expression matches patternN
    case _:
        # Code to be executed if expression does not match any pattern
```

## Example:

```python
def weekday_name(day):
    match day:
        case "Mon":
            return "Monday"
        case "Tue":
            return "Tuesday"
        case "Wed":
            return "Wednesday"
        case "Thu":
            return "Thursday"
        case "Fri":
            return "Friday"
        case _:
            return "Invalid day"
```

## Key Concepts:

- **Patterns:** Patterns allow you to destructure and match complex data structures. Patterns can include literals, variables, wildcards, sequences, and more.

- **Match Expressions:** The `match` statement operates on a specified expression, and based on its value, the corresponding pattern is selected and executed.

- **Case Blocks:** Each pattern is associated with a case block that contains the code to be executed if the pattern matches the expression.

- **Wildcard (`_`):** The underscore `_` can be used as a wildcard pattern to match anything. It is often used in the final `case _:` block to handle unmatched cases.

## Important Points:

- Pattern matching simplifies complex conditional structures by providing a more declarative and readable syntax.

- It enhances the expressiveness of code when dealing with data structures like lists, tuples, and custom objects.

- The proposed `match` statement is expected to be a more flexible and intuitive alternative to the existing `if...elif...else` constructs for certain use cases.

# Python `match` Statement - Detailed Notes

## **Introduction**

The `match` statement in Python (introduced in Python 3.10) is used for **pattern matching**, similar to switch-case in other languages but more powerful. It allows for checking values and structures in a more readable way.

## **Syntax**

```python
match variable:
    case pattern1:
        # Code block
    case pattern2:
        # Code block
    case _:
        # Default case (similar to 'else')
```

### **Example:**

```python
num = 3

match num:
    case 1:
        print("One")
    case 2:
        print("Two")
    case 3:
        print("Three")
    case _:
        print("Other number")
```

### **Key Features of `match` Statement:**

- It checks patterns **sequentially** from top to bottom.
- The **first matching case executes**; remaining cases are ignored.
- The **underscore (`_`) is the default case**, like `else` in an `if-else` structure.

## **Types of Patterns in Match Statements**

### **1. Literal Pattern (Direct Matching)**

Matches specific values (like integers, strings, or booleans).

```python
match value:
    case 10:
        print("Value is 10")
    case "hello":
        print("Value is 'hello'")
```

### **2. Multiple Patterns Using `|` (OR Operator)**

Used when a case should match multiple values.

```python
num = 5

match num:
    case 1 | 2 | 3:
        print("Number is small")
    case 4 | 5 | 6:
        print("Number is medium")
    case _:
        print("Number is large")
```

### **3. Using `if` Conditions (Guarding a Case)**

For adding additional conditions inside a case.

```python
num = 7

match num:
    case x if 1 <= x <= 9:
        print("Number is between 1 and 9")
    case _:
        print("Number is out of range")
```

### **4. Matching Lists and Tuples**

You can match structures like lists or tuples.

```python
match [x, y]:
    case [1, 2]:
        print("Matched [1, 2]")
    case [a, b]:
        print(f"Matched a list with values: {a} and {b}")
```

### **5. Matching Dictionary Keys**

You can match based on dictionary contents.

```python
data = {"name": "Alice", "age": 25}

match data:
    case {"name": "Alice", "age": age}:
        print(f"Alice is {age} years old")
    case _:
        print("No match")
```

### **6. Matching Variable Names**

Extract values from a structure by assigning them to variables.

```python
match (10, 20):
    case (a, b):
        print(f"Matched: a={a}, b={b}")
```

### **7. Ignoring Unused Variables**

Use `_` for unused values.

```python
match (1, 2, 3):
    case (x, _, z):
        print(f"First: {x}, Last: {z}")
```

### **8. Class Matching (Advanced Feature)**

Objects can also be matched.

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

p = Point(2, 3)

match p:
    case Point(x, y):
        print(f"Point coordinates: {x}, {y}")
```

## **Best Practices for Writing Match Statements**

1. **Avoid duplicate patterns** – Only the first matching case executes.
2. **Use `|` for multiple patterns in one case.**
3. **Use `if` guards for conditions inside cases.**
4. **Always include a `_` case to handle unexpected values.**
5. **Use pattern unpacking for lists, tuples, and dictionaries.**

## **Common Pitfalls & How to Avoid Them**

### **1. Overlapping Patterns (Ambiguous Behavior)**

```python
num = 3
match num:
    case 1 | 2 | 3:
        print("Matched small numbers")
    case 3:
        print("Matched exactly 3")  # This will never run!
```

**✅ Fix:** Put more specific cases first.

```python
match num:
    case 3:
        print("Matched exactly 3")
    case 1 | 2:
        print("Matched small numbers")
```

### **2. Using `case x if x in range(1, 10):` for Large Ranges**

For large ranges, **use `if` guards** instead of listing all values.

```python
match num:
    case x if 1 <= x <= 100:
        print("Matched range 1-100")
```

## **Conclusion**

- Python’s `match` is more **powerful than switch-case** in other languages.
- It can handle **numbers, strings, lists, dictionaries, and even objects**.
- Use **`|` for multiple patterns**, **`if` for conditions**, and **structured patterns for complex data**.
