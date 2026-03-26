# Testing methods of code2.py using unittest
import unittest
from code2 import Employee
class TestEmployee(unittest.TestCase):
    @classmethod
    def setUpClass(cls): # helper method to set up the test environment for the entire class
        print("setUpClass called")
    @classmethod
    def tearDownClass(cls): # helper method to clean up the test environment for the entireclass
        print("tearDownClass called")
    
    def setUp(self): # helper method to set up the test environment
        print("setUp called")
        self.emp1 = Employee('John', 'Doe', 50000)
        self.emp2 = Employee('Jane', 'Smith', 60000)

    def tearDown(self): # helper method to clean up the test environment
        print("tearDown called")
        del self.emp1
        del self.emp2

    def test_email(self):
        print("test_email called")
        self.assertEqual(self.emp1.email, 'john.doe@company.com')
        self.assertEqual(self.emp2.email, 'jane.smith@company.com')
    def test_full_name(self):
        print("test_full_name called")
        self.assertEqual(self.emp1.full_name, 'John Doe')
        self.assertEqual(self.emp2.full_name, 'Jane Smith')
    def test_apply_raise(self):
        print("test_apply_raise called")
        self.emp1.apply_raise()
        self.emp2.apply_raise()
        self.assertEqual(self.emp1.salary, 52500)
        self.assertEqual(self.emp2.salary, 63000)

if __name__ == '__main__':
    unittest.main()