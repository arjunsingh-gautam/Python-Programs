# In this module we will learn about seek and tell functions in Python file handling    

import os
os.chdir("d:/Desktop/Python_Programs/Lesson 23 File_Handling/Code/files")
with open(os.path.abspath('demo4.txt'),'r') as f:  # automatically closes file
    print(f.read(10))  # read first 10 characters
    print(f.tell())  # current position in file (number of characters from start)
    f.seek(0)  # move file pointer to the beginning of the file
    print(f.read(10))  # read first 10 characters again 