# Here we see the real use of context manager in Python. We will implement a custom context manager.
import os
os.chdir("d:/Desktop/Python_Programs/Lesson 26 Context_Manager")
class change_dir:
    def __init__(self, new_path):
        self.new_path = new_path
        self.original_path = None

    def __enter__(self):
        self.original_path = os.getcwd()# save original directory
        os.chdir(self.new_path)  # change to new directory


    def __exit__(self, exc_type, exc_value, traceback):
        os.chdir(self.original_path)  # change back to original directory

# Example usage of the custom context manager to change directories
with change_dir(os.path.abspath('sample-dir-one')):  # automatically changes to sample-dir-one
    print(os.listdir())  # list files in sample-dir-one

with change_dir(os.path.abspath('sample-dir-two')):  # automatically changes to sample-dir-two
    print(os.listdir())  # list files in sample-dir-two

# Here we have used a custom context manager to change directories. The __enter__ method changes to the new directory and the __exit__ method changes back to the original directory. This ensures that we always return to the original directory after the with block, even if an error occurs.