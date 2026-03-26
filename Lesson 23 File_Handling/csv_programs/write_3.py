# Writing to a csv file using DictWriter
import csv
import os
os.chdir("d:/Desktop/Python_Programs/Lesson 23 File_Handling/csv_programs")
with open('names.csv','r') as file:
    reader = csv.DictReader(file) # create a non-materialized reader object
    with open('names_copy_dict.csv','w',newline='') as file: # open the file in append mode
        fieldnames = reader.fieldnames # get the fieldnames from the reader object
        writer = csv.DictWriter(file, fieldnames=fieldnames) # create a writer object with fieldnames
        writer.writeheader() # write the header to the file
        for row in reader:
            writer.writerow(row) # write the row to the file