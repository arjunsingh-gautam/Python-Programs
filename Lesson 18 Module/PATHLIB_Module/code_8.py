# Searching files 
from pathlib import Path
p=Path(r"D:\Desktop\Python_Programs\Lesson 18 Module\PATHLIB_Module")
for file in p.glob("*.txt"):
    print(file)