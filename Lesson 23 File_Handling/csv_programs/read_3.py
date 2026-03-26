# Reading using a different delimiter
import csv  
import os
os.chdir("d:/Desktop/Python_Programs/Lesson 23 File_Handling/csv_programs")
with open('names_copy_pipe.csv','r') as file:
    reader = csv.reader(file, delimiter='|') # create a non-materialized reader object with pipe delimiter
    for row in reader:
        print(row)