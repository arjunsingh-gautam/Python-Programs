# Typevar in Python to ensure type consistency and propagation of types across functions and classes.
from typing import TypeVar, Generic

T = TypeVar('T')



def first_element(lst: list[T]) -> T:
    return lst[0]

numbers = [1, 2, 3]
print(first_element(numbers))  # Output: 1
strings = ["a", "b", "c"]
print(first_element(strings))  # Output: "a"