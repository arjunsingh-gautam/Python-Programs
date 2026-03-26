# Reading a csv file using DictReader
import csv
import os
os.chdir("d:/Desktop/Python_Programs/Lesson 23 File_Handling/csv_programs")
with open('names.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)