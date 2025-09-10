# Here we see how Python stores a string:
str_var = "(1,2,3),[1,243,294,\"arj\"],5+6j"

# Print the id of the entire string
print("String Object ID:", id(str_var))

# Print the ids of individual characters
for i, char in enumerate(str_var):
    print(f"Character: {char} | ID: {id(char)}")
