# Reading contents of a file line by line using readline()
import os   
os.chdir("d:/Desktop/Python_Programs/Lesson 23 File_Handling/Code/files")
f=open(os.path.abspath('demo4.txt'),'r')        
print(f.readline(),end='')  # read first line
print(f.readline(),end='')  # read second line 
f.close()