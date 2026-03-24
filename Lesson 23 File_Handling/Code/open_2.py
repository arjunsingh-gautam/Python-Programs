# Opening file using context manager (with statement)
import os
os.chdir("d:/Desktop/Python_Programs/Lesson 23 File_Handling/Code/files")
with open(os.path.abspath('demo1.txt'),'r') as f:
    print(f.read())

# The file will be automatically closed after the with block, even if an error occurs.