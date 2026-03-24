# How to append to a file in Python
import os
os.chdir("d:/Desktop/Python_Programs/Lesson 23 File_Handling/Code/files")
with open(os.path.abspath('demo3'),'a') as f:   # 'a'ppend mode, automatically closes file
    f.write("\nThis line is appended to the file.")