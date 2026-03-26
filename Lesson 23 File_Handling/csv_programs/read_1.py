# Parsing a csv file using the csv module
import csv
import os
os.chdir("d:/Desktop/Python_Programs/Lesson 23 File_Handling/csv_programs")
with open('names.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)