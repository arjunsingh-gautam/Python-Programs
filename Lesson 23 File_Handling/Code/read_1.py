# Reading from a file in Python
import os
os.chdir("d:/Desktop/Python_Programs/Lesson 23 File_Handling/Code/files")
f=open(os.path.abspath('demo4.txt'),'r')
print(f.read())
f.close()