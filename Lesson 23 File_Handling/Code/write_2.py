""" Open same file in append mode

Add today’s date and time

Add 3 log messages """
from datetime import datetime
import os
os.chdir("d:/Desktop/Python_Programs/Lesson 23 File_Handling/Code/files")
logs=["Learning Data Persistency in Python\n",f"Log time:{datetime.now()}"]
f=open(os.path.abspath('demo3'),'w')
f.writelines(logs)
f.close()