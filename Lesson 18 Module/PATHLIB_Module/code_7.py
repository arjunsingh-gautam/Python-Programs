# Iterating through directory:
from pathlib import Path
folder=Path(r"D:\Desktop\Python_Programs\Lesson 18 Module\PATHLIB_Module")

for item in folder.iterdir():
    print(item)
    