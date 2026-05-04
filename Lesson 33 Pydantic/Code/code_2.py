# Using type aliases to simplify complex type hints and improve code readability.

from typing import NewType
RGB=NewType('RGB', tuple[int, int, int])
HSL=NewType('HSL', tuple[int, int, int])

type User=dict[str, str|int|RGB|HSL|None]

def create_user(first_name:str,last_name:str,age:int|None=None,fav_color:RGB|HSL|None=None) -> User:
    email=f"{first_name.lower()}.{last_name.lower()}@example.com"
    return {
        "first_name": first_name,
        "last_name": last_name,
        "age": age,
        "fav_color": fav_color,
        "email": email
    }
    
user1: User = create_user("Alice", "Smith", 30, RGB((255, 0, 0)))
print(user1) 
user2: User = create_user("Bob", "Johnson", fav_color=HSL((120, 100, 50)))
print(user2)

# Here we defined two type aliases, RGB and HSL, to represent color values. We also created a User type alias for a dictionary that can hold various user attributes. The create_user function uses these type aliases in its parameters and return type, making the code more readable and easier to understand.