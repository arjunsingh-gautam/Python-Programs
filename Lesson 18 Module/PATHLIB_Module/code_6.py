# Reading and Writing Files
from pathlib import Path
p=Path(r'D:\Desktop\Python_Programs\Lesson 18 Module\PATHLIB_Module\file.txt')
p.write_text("Hello World!")
content=p.read_text()
print(content)