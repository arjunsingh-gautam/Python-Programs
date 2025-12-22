# Expression Condition

# 1.Single Expression: A lambda function can only contain a single expression. This means it cannot have multiple lines of code or statements like return, if, for, while, etc.
# Valid lambda function
lambda x: x + 1

# Invalid lambda function (cannot contain multiple expressions or statements)
# lambda x: x + 1; x - 2


#############################
# 2. Immediate Evaluation: The expression in a lambda function is evaluated when the lambda function is called, not when it is defined.
func = lambda x: x * 2
print(func(5))  # Output: 10

##############################
#3.Limited Scope: The expression can use variables from the enclosing scope but cannot modify them.
y = 10
func = lambda x: x + y
print(func(5))  # Output: 15

# Modifying y within the lambda is not allowed
# func = lambda x: (y := x + 5)  # SyntaxError in Python versions before 3.8

