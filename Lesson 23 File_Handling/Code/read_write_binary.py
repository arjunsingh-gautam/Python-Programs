# Reading and writin a binary file in Python
import os
os.chdir("d:/Desktop/Python_Programs/Lesson 23 File_Handling/Code/files")
with open(os.path.abspath('DT.png'),'rb') as f:  # 'wb' for writing binary, automatically closes file
    content=f.read()  # read entire file as bytes
    with open(os.path.abspath('DT_copy.png'),'wb') as f2:  # 'wb' for writing binary, automatically closes file
        f2.write(content)  # write bytes to new file