# Parsing a file in Python 
import os
os.chdir("d:/Desktop/Python_Programs/Lesson 23 File_Handling/Code/files")
with open(os.path.abspath('demo4.txt'),'r') as f:  # automatically closes file
    while True:
        line=f.read(5)  # read 20 characters at a time
        if line=='':  # EOF
            break
        print(line)  # print line without adding extra newline