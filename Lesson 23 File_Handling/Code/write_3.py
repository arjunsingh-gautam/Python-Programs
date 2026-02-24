# appending to existing file
from datetime import datetime
with open(r"Lesson 23 File_Handling\Code\note.txt",'a') as f:
    f.writelines(f"Log time:{datetime.now()}")