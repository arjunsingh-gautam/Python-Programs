# Writing multiple lines to a file using write

import os
os.chdir("d:/Desktop/Python_Programs/Lesson 23 File_Handling/Code/files")
with open(os.path.abspath('demo4.txt'),'w') as f:   # automatically closes file
    f.write("Line 1: Hello, World!\n")
    f.write("Line 2: Welcome to file handling in Python.\n")
    f.write("Line 3: This is a demo file.\n")
    f.write("Line 4: We are writing multiple lines.\n")
    f.write("Line 5: Goodbye!\n")