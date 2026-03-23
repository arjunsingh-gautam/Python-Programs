# OS path module
import os

file_path=os.path.join(os.environ.get("HOME"),"test.txt")
print(file_path)
file_path2="temp/dir1/dir2"
print(os.path.basename(file_path2))
print(os.path.dirname(file_path2))
print(os.path.split(file_path2))
print(os.path.exists(file_path2))