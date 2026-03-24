# Reading from a file in Python and writing to a file in Python
import os
os.chdir("d:/Desktop/Python_Programs/Lesson 23 File_Handling/Code/files")
with open(os.path.abspath('demo4.txt'),'r') as f:  # automatically closes file
    content=f.read()
    with open(os.path.abspath('demo5.txt'),'w') as f2:  # automatically closes file
        f2.write(content)

