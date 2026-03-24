# Reading from a file in Python using context manager (with statement)
import os   
os.chdir("d:/Desktop/Python_Programs/Lesson 23 File_Handling/Code/files")
with open(os.path.abspath('demo4.txt'),'r') as f:  # automatically closes file
    while True:
        line=f.readline()
        if not line:  # EOF
            break
        print(line,end='')  # print line without adding extra newline