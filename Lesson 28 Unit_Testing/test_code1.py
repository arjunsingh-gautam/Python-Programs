# Unit test code for the code1.py file 
import unittest
import code1

class TestCode1(unittest.TestCase): # Test class that inherits from unittest.TestCase
    def test_add(self): # Test method for the add function and must start with 'test_'
        self.assertEqual(code1.add(2, 3), 5) # Assert that the result of add(2, 3) is equal to 5
        self.assertEqual(code1.add(-1, 1), 0) # Assert that the result of add(-1, 1) is equal to 0
        self.assertEqual(code1.add(0, 0), 0) # Assert that the result of add(0, 0) is equal to 0
    def test_subtract(self): # Test method for the subtract function
        self.assertEqual(code1.subtract(5, 2), 3) # Assert that the result of subtract(5, 2) is equal to 3
        self.assertEqual(code1.subtract(0, 1), -1) # Assert that the result of subtract(0, 1) is equal to -1
        self.assertEqual(code1.subtract(-1, -1), 0) # Assert that the result of subtract(-1, -1) is equal to 0
    def test_multiply(self): # Test method for the multiply function
        self.assertEqual(code1.multiply(2, 3), 6) # Assert that the result of multiply(2, 3) is equal to 6
        self.assertEqual(code1.multiply(-1, 1), -1) # Assert that the result of multiply(-1, 1) is equal to -1
        self.assertEqual(code1.multiply(0, 5), 0) # Assert that the result of multiply(0, 5) is equal to 0  
    def test_divide(self): # Test method for the divide function
        self.assertEqual(code1.divide(6, 3), 2) # Assert that the result of divide(6, 3) is equal to 2
        self.assertEqual(code1.divide(-4, 2), -2) # Assert that the result of divide(-4, 2) is equal to -2
        self.assertEqual(code1.divide(0, 5), 0) # Assert that the result of divide(0, 5) is equal to 0
        with self.assertRaises(ValueError): # Assert that a ValueError is raised when dividing by zero
            code1.divide(5, 0)
        

if __name__ == '__main__':
    unittest.main() # Run the unit tests