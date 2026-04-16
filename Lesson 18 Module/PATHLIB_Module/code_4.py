# Checking file or Directory
from pathlib import Path
p=Path(r"D:/Desktop/MVP_Finezza")
print(p.is_dir())
p=Path(r"D:\Desktop\Python_Programs\Lesson 18 Module\PATHLIB_Module\file.txt")
print(p.is_file())
print(p.name)
print(p.stem)
print(p.suffix)
print(p.parent)