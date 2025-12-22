#Lambda can take  any no. of args includign zero
# accept positional,keyword,variable length arg like a normal function

# Lambda with multiple arguments, including a keyword argument and *args
complex_lambda = lambda x, y, z=10, *args: (x + y + z) * sum(args)
print(complex_lambda(1, 2, 3, 4, 5))  # Output: 54

# Explanation:
# x = 1, y = 2, z = 3 (keyword argument), args = (4, 5)
# (1 + 2 + 3) * sum(4, 5) = 6 * 9 = 54
