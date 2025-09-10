# <span style="color:orange">Type Conversion & Number System </span>

## <span style="color:pink">Type-Conversion </span>

- In Python, type conversion (or typecasting) refers to the process of changing the data type of a variable from one type to another. - This is often necessary when performing operations that involve different data types or when you need a variable to be of a specific type.

1. **Implicit Type Conversion** (Automatic):

Python automatically performs certain type conversions when required, especially in situations where the operation is well-defined and there is no loss of information. This is also known as **_coercion_**.

```python
# Implicit type conversion
a = 5        # integer
b = 2.0      # floating-point

c = a + b     # The integer 'a' is implicitly converted to a float for the addition
print(c)      # Output: 7.0
```

2. **Explicit Type Conversion (Manual)**:

- Developers can explicitly convert one data type to another using built-in functions like **int(), float(), str(), etc.**

```python
# Explicit type conversion
x = 10.5      # floating-point
y = int(x)     # Explicitly converting float to integer
print(y)      # Output: 10
```

```python
# Example of converting a string to an integer
number_string = "123"
number_int = int(number_string)
print(number_int)  # Output: 123
```

```python
# Example of converting an integer to a string
integer_value = 42
string_value = str(integer_value)
print(string_value)  # Output: "42"
```

3. **Conversion Between Numeric Types:**

- Explicit conversion can be used to convert between numeric types, such as from int to float or vice versa.

```python
# Converting from int to float
integer_value = 42
float_value = float(integer_value)
print(float_value)  # Output: 42.0
```

4. **Conversion Between Sequence Types:**

- You can convert between different sequence types, like lists, tuples, and strings, using explicit conversion.

```python
# Converting a list to a tuple
my_list = [1, 2, 3]
my_tuple = tuple(my_list)
print(my_tuple)  # Output: (1, 2, 3)


# Converting a string to a list of characters
my_string = "hello"
char_list = list(my_string)
print(char_list)  # Output: ['h', 'e', 'l', 'l', 'o']
```

5. **Conversion Between Boolean and Numeric Types:**

- In Python, True is equivalent to 1, and False is equivalent to 0. You can explicitly convert between boolean and numeric types.

```python
# Converting boolean to integer
bool_value = True
int_value = int(bool_value)
print(int_value)  # Output: 1
```

## <span style="color:yellow">bin() :</span>

- converts an integer into a binary value
- Always return a string beginning with "0b"

## <span style="color:yellow">oct() :</span>

- converts an integer into a octal value
- Always return a string beginning with "0o"

## <span style="color:yellow">hex() :</span>

- converts an integer into a hexadecimal value
- Always return a string beginning with "0x"

## <span style="color:yellow">ord() :</span>

- Predefined function which takes character as argument and return it's unicode

## <span style="color:yellow">chr() :</span>

- Predefined function which takes unicode as argument and return it's character

## <span style="color:yellow">input() function :</span>

- It is a built-in function used to receive input from the user through the console.
- Can take at most one argument of string type
- input() always **return string type value**

---

## **<span style="color:green">Type Conversion parameters</span>**

Each type conversion function in Python can take various parameters. Here's a breakdown of what each function can take:

### `bool()`

The `bool()` function converts a value to a Boolean (True or False). It can take:

- `None`
- Numbers (`int`, `float`, `complex`) — non-zero values are `True`, zero values are `False`
- Strings — non-empty strings are `True`, empty strings are `False`
- Lists, tuples, sets, dictionaries — non-empty collections are `True`, empty collections are `False`
- Any object that implements `__bool__` or `__len__` — objects with `__bool__` returning `True` or `__len__` returning a non-zero value are `True`, otherwise `False`

**Example:**

```python
bool(None)       # False
bool(0)          # False
bool(42)         # True
bool('')         # False
bool('Hello')    # True
bool([])         # False
bool([1, 2, 3])  # True
```

### str()

The `str()` function converts a value to a string. It can take:

- Numbers (int, float, complex)
- Strings
- Lists, tuples, sets, dictionaries
- Any object that implements **str** or **repr**
  Example:

```python
str(42)          # '42'
str(3.14)        # '3.14'
str([1, 2, 3])   # '[1, 2, 3]'
str({'a': 1})    # "{'a': 1}"
```

### `float()`

The `float() `function converts a value to a floating-point number. It can take:

- Numbers (int, float)
- Strings representing floating-point numbers or integers
- Strings representing special floating-point values ('inf', '-inf', 'nan')
  Example:

```python
float(42)           # 42.0
float('3.14')       # 3.14
float('inf')        # inf
float('-inf')       # -inf
float('nan')        # nan
```

### `complex()`

The `complex()` function converts a value to a complex number. It can take:

- Two numbers (int, float) representing the real and imaginary parts
- A single string representing a complex number
- A single number (int, float)
  Example:

```python
complex(1, 2)       # (1+2j)
complex(3.14)       # (3.14+0j)
complex('1+2j')     # (1+2j)
```

### `int()`

The `int()` function converts a value to an integer. It can take:

- Numbers (int, float) — note that float is truncated towards zero
- Strings representing integers (optionally in a specified base)
  Example:

```python
int(3.14)           # 3
int('42')           # 42
int('101', 2)       # 5  (binary to decimal)
int('A', 16)        # 10 (hexadecimal to decimal)
```
