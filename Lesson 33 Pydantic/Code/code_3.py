# Implementing type alias vs NewType to demonstrate the differences and use cases for each in Python type hinting.
from typing import NewType
# Using type alias to create a new type for better readability.
UserID = int
# Using NewType to create a distinct type that is not interchangeable with its underlying type.
UserName = NewType('UserName', str)
def get_user_info(user_id: UserID, user_name: UserName) -> str:
    return f"User ID: {user_id}, User Name: {user_name}"

user_id: UserID = 123
user_name: UserName = UserName("Alice")
info = get_user_info(user_id, user_name)
print(info)