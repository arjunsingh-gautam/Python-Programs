# Writing to a csv file using the csv module
import csv
import os
os.chdir("d:/Desktop/Python_Programs/Lesson 23 File_Handling/csv_programs")
with open('names.csv','r') as file:
    reader = csv.reader(file) # create a non-materialized reader object
    with open('names_copy.csv','w',newline='') as file: # open the file in append mode
        writer = csv.writer(file) # create a writer object
        for row in reader:
            writer.writerow(row) # write the row to the file