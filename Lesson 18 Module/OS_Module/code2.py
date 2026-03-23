# Making directory using mkdir,mkdirs
import os
# Using mkdir("dir") # Precaution: Intermediate Paths/Directories should be present otherwise raise Error
os.chdir("d:/Desktop/Python_Programs/Lesson 18 Module/OS_Module")
print(os.getcwd())

print(os.listdir())

os.mkdir("os-demo-dir1")

os.makedirs('os-demo-dir2/demo-dir3')# Also create intermediate directories if not present

print(os.listdir())

# Removing directories using :
# 1.rmdir: Remove directory but not recursively
# 2. removedirs: Remove directory recursively

os.rmdir("os-demo-dir1")
os.removedirs("os-demo-dir2/demo-dir3")