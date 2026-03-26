# Writing to a csv file using a different delimiter
import csv  
import os
os.chdir("d:/Desktop/Python_Programs/Lesson 23 File_Handling/csv_programs")
with open('names.csv','r') as file:
    reader = csv.reader(file) # create a non-materialized reader object
    with open('names_copy_pipe.csv','w',newline='') as file: # open the file in append mode
        writer = csv.writer(file, delimiter='|') # create a writer object with pipe delimiter
        for row in reader:
            writer.writerow(row) # write the row to the file