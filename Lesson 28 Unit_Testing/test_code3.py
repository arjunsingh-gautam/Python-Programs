# Writing unit test for the code3.py module using mocking
import unittest
from unittest.mock import patch
from code3 import get_user_data
class TestGetUserData(unittest.TestCase):
    @patch('code3.requests.get') # patch the requests.get method to replace it with a mock object
    def test_get_user_data_success(self, mock_get):
        # Define the behavior of the mock object for a successful response
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {
            'id': 1,
            'name': 'John Doe',
            'username': 'johndoe',
            'email': 'johndoe@email.com'
        }
        user_data = get_user_data(1) # Call the function to test
        mock_get.assert_called_with('https://jsonplaceholder.typicode.com/users/1') # Assert that the requests.get method was called with the correct URL
        self.assertEqual(user_data['id'], 1) # Assert that the id is correct
        self.assertEqual(user_data['name'], 'John Doe') # Assert that the name is correct
        self.assertEqual(user_data['username'], 'johndoe') # Assert that the username is correct
        self.assertEqual(user_data['email'], 'johndoe@email.com') # Assert that the email is correct
    @patch('code3.requests.get') # patch the requests.get method to replace it with a mock object
    def test_get_user_data_failure(self, mock_get):
        # Define the behavior of the mock object for a failed response
        mock_get.return_value.status_code = 404
        user_data = get_user_data(999) # Call the function to test with a non-existent user id
        self.assertIsNone(user_data) # Assert that the result is None for a failed response
if __name__ == '__main__':
    unittest.main() # Run the unit tests