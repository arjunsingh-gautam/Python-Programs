# Task A1 and A2:

- When does "math_ops module loaded" print?
- It is printed when run main.py in which when import line get executed

- How many times does it print if you run main.py twice?
- It is once per execution

# Task B1 and B2:

- When we import a module it object is created in memory and sys.module store it inside it's dictionary for referencing all active module objects in memory
- 2 import statement doesn't run the print statement since the when python see when executing it sees that module object is already present doesn't execute it
