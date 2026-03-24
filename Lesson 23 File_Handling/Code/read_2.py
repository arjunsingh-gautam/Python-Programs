# Reading file but upto a certain number of characters
import os   
os.chdir("d:/Desktop/Python_Programs/Lesson 23 File_Handling/Code/files")
f=open(os.path.abspath('demo4.txt'),'r')  
print(f.read(20))  # read first 20 characters
f.close()