# Implementing context manager in Python using contextlib module and the @contextmanager decorator:

import os
from contextlib import contextmanager
os.chdir("d:/Desktop/Python_Programs/Lesson 26 Context_Manager")
@contextmanager
def open_file(file_path, mode):
    f=open(file_path,mode)
    try:
        yield f  # yield the file object to the caller
    finally:
        f.close()  # ensure file is closed after use

# Example usage of the custom context manager to read from a file
with open_file(os.path.abspath('demo1.txt'),'r') as f:  # automatically opens file
    print(f.read())  # read and print file contents

print(f.closed)  # check if file is closed (should be True)