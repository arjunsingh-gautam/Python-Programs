# In this module we will learn about seek and tell while writing to a file in Python file handling
import os
import time
os.chdir("d:/Desktop/Python_Programs/Lesson 23 File_Handling/Code/files")
with open(os.path.abspath('demo6.txt'),'w') as f:   # automatically closes      
    f.write("Hello, World!\n")
    print(f.tell())  # current position in file (number of characters from start)
    time.sleep(10)  # sleep for 30 second to see the effect of time on file pointer
    f.write("Welcome to file handling in Python.\n")
    print(f.tell())  # current position in file (number of characters from start)
    time.sleep(10)  # sleep for 30 second to see the effect of time on file pointer
    f.seek(0)  # move file pointer to the beginning of the file
    f.write("Hi, Universe!\n")  # overwrite first line