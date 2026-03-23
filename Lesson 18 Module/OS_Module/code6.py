# To print the entire directory tree
import os
for dirpath,dirnames,filenames in os.walk(os.getcwd()):
    print("Current Path:",dirpath)
    print("Directories:",dirnames)
    print("Files:",filenames)