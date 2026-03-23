# Changing/Renaming file uisng os.rename
import os
os.chdir("d:/Desktop/Python_Programs/Lesson 18 Module/OS_Module")
os.rename('demo.txt','text.txt')

# Printing file metadata:
print(os.stat('text.txt'))