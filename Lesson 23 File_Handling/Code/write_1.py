""" Create a file notes.txt and:

Write 5 lines of text
Each line should contain a number and its squar """
lines=["3:9\n","4:16\n","5:25\n","9:81\n","7:49\n"]
with open(r"Lesson 23 File_Handling\Code\note.txt","w") as f: # automatically closes file
    f.writelines(lines)