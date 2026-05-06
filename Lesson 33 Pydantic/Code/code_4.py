# TypeDict in Python to implement type checking for dictionaries with specific keys and value types.
from typing import TypedDict

class User(TypedDict):
    id: int
    name: str
    email: str

u:User={
    "id": 123,"name": "Alice","email": "alice@example.com"}


def get_user_info(user: User) -> str:
    return f"User ID: {user['id']}, User Name: {user['name']}, User Email: {user['email']}"

print(get_user_info(u))