# Making directories:
import os
os.chdir("D:\Desktop\Python_Programs\Lesson 18 Module\PATHLIB_Module")
from pathlib import Path
p=Path("demo_folder")
if p.exists():
    os.rmdir("D:\Desktop\Python_Programs\Lesson 18 Module\PATHLIB_Module\demo_folder")
p.mkdir()
Path("demo1/demo2/demo3").mkdir(parents=True)