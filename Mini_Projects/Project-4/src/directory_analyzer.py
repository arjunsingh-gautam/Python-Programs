"""
- This module will take a directory path as input and prints all files inside it
"""
from pathlib import Path
def listing_files(path):
    folder=Path(path)
    for item in folder.iterdir():
        print(item)
        
def searching_files(path,extension):
    p=Path(path)
    for file in p.rglob(f"*.{extension}"):
        print(file)
        

    
    