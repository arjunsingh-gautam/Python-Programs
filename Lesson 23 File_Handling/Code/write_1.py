""" Create a file notes.txt and:

Write 5 lines of text
Each line should contain a number and its squar """
import os
os.chdir("d:/Desktop/Python_Programs/Lesson 23 File_Handling/Code/files")

lines=["3:9\n","4:16\n","5:25\n","9:81\n","7:49\n"]
with open(os.path.abspath('demo2.txt'),'w') as f:   # automatically closes file
    f.writelines(lines)
