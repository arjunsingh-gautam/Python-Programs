# In this module we will learn about the concepth of mocking and how to use it in unit testing. Mocking is a technique used in unit testing to replace real objects with mock objects that simulate the behavior of the real objects. This allows us to test our code in isolation without relying on external dependencies.
# We will use the unittest.mock module to create mock objects in our tests. The unittest.mock module provides a powerful and flexible way to create mock objects and define their behavior. We can use the Mock class to create mock objects and the patch function to replace real objects with mock objects in our tests.
# We will also learn about the different types of mock objects and how to use them in our tests. We will see how to use mock objects to test functions that interact with external APIs, databases, and other dependencies. By the end of this module, you will have a good understanding of how to use mocking in your unit tests to improve the reliability and maintainability of your code.

# simple module that interacts with an external API and then write unit tests for it using mocking.
import requests
def get_user_data(user_id):
    response = requests.get(f'https://jsonplaceholder.typicode.com/users/{user_id}')
    if response.status_code == 200:
        return response.json()
    else:
        return None
    


