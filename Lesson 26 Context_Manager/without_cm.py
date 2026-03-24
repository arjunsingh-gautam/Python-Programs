# In this module we will demonstrate code without context manager (with statement) and then we will see how to do the same thing with context manager in the next module 

import os
cwd=os.chdir("d:/Desktop/Python_Programs/Lesson 26 Context_Manager")    
os.chdir('sample-dir-one')
print(os.listdir())  # list files in sample-dir-one
cwd=os.chdir("d:/Desktop/Python_Programs/Lesson 26 Context_Manager") 

cwd=os.chdir("d:/Desktop/Python_Programs/Lesson 26 Context_Manager")
os.chdir('sample-dir-two')
print(os.listdir())  # list files in sample-dir-two     

# Here we have to manually change the directory and list files in each directory. This can be error-prone and cumbersome if we have to work with multiple directories. In the next module, we will see how to use context manager to handle this more elegantly.