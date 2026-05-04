# Applying basic type hinting to variables and function parameters and return types.

def create_user(name: str, age: int|None=None) -> dict[str, int | str|None]:
    return {"name": name, "age": age}

user: dict = create_user("Alice", 30)
print(user)

