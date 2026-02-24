""" Open same file in append mode

Add today’s date and time

Add 3 log messages """
from datetime import datetime
logs=["Learning Data Persistency in Python\n",f"Log time:{datetime.now()}"]
f=open(r"Lesson 23 File_Handling\Code\log.txt",'w')
f.writelines(logs)
f.close()