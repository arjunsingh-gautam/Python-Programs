# How to create a context manager in Python using a class with __enter__ and __exit__ methods:
import os
os.chdir("d:/Desktop/Python_Programs/Lesson 26 Context_Manager")
class MyContextManager:
    def __init__(self,filename,mode):
        self.filename=filename
        self.mode=mode
    def __enter__(self):
        self.file=open(self.filename,self.mode)
        return self.file  # return the file object to be used in the with block
    def __exit__(self,exc_type,exc_value,traceback):
        self.file.close()  # ensure the file is closed when exiting the with block, even if an error occurs

# Example usage of the custom context manager to read from a file
with MyContextManager(os.path.abspath('demo1.txt'),'w') as f:  # automatically opens file
    f.write("Testing")  # write to file
# The file will be automatically closed after the with block, even if an error occurs.

print(f.closed)  # check if file is closed (should be True)