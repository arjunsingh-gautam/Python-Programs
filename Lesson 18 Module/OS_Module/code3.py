import os
# Removing directories using :
# 1.rmdir: Remove directory but not recursively
# 2. removedirs: Remove directory recursively
os.chdir("d:/Desktop/Python_Programs/Lesson 18 Module/OS_Module")
os.rmdir("os-demo-dir1")
os.removedirs("os-demo-dir2/demo-dir3")